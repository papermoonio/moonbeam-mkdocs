#!/usr/bin/env python3
import argparse
import json
import re
from pathlib import Path

import yaml
JINJA_TAG_RE = re.compile(r"({{.*?}}|{%-?.*?%}|{#.*?#})", re.S)
TEXT_NODE_RE = re.compile(r">([^<]+)<")
ATTR_RE = re.compile(
    r"\b(alt|title|placeholder|aria-label|aria-labelledby|value)\s*=\s*(\"[^\"]*\"|'[^']*')",
    re.I,
)
DISCLAIMER_BLOCK_RE = re.compile(
    r"<(?P<tag>[a-z0-9]+)\b(?P<attrs>[^>]*)>(?P<content>.*?)</(?P=tag)>",
    re.I | re.S,
)


class _Dumper(yaml.SafeDumper):
    pass


def _str_representer(dumper, data):
    style = "|" if "\n" in data else None
    return dumper.represent_scalar("tag:yaml.org,2002:str", data, style=style)


_Dumper.add_representer(str, _str_representer)


def _flatten(prefix, value, dest):
    if isinstance(value, dict):
        for key, val in value.items():
            next_prefix = f"{prefix}.{key}" if prefix else key
            _flatten(next_prefix, val, dest)
    else:
        dest[prefix] = value


def _load_locale_data(locale_path):
    data = yaml.safe_load(locale_path.read_text(encoding="utf-8")) or {}
    flat = {}
    _flatten("", data, flat)
    return data, flat


def _load_flat_json(json_path):
    payload = json.loads(json_path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        return {}
    return {
        str(key): value
        for key, value in payload.items()
        if isinstance(key, str) and isinstance(value, str)
    }


def _ensure_key(data, key, value):
    parts = key.split(".")
    current = data
    for part in parts[:-1]:
        if part not in current:
            current[part] = {}
        elif not isinstance(current[part], dict):
            return
        current = current[part]
    current.setdefault(parts[-1], value)


def _find_block_ranges(text, tag):
    ranges = []
    for match in re.finditer(rf"<{tag}\b[^>]*>.*?</{tag}>", text, flags=re.I | re.S):
        ranges.append((match.start(), match.end()))
    return ranges


def _in_ranges(span, ranges):
    for start, end in ranges:
        if span[0] >= start and span[1] <= end:
            return True
    return False


def _slugify(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "_", text)
    text = text.strip("_")
    return text or "text"


def _clean_text(text):
    text = re.sub(JINJA_TAG_RE, "", text)
    text = re.sub(r"<[^>]+>", "", text)
    return " ".join(text.split())


def _path_prefix(path, root):
    try:
        relative = path.relative_to(root)
    except ValueError:
        relative = path
    parts = list(relative.parts)
    if parts:
        parts[-1] = path.stem
    prefix_parts = [_slugify(part.replace("-", "_")) for part in parts]
    return ".".join(p for p in prefix_parts if p)


def _collect_template_replacements(
    path,
    content,
    prefix,
    min_length,
    allow_duplicates,
    value_to_key,
    used_keys,
):
    replacements = []
    script_ranges = _find_block_ranges(content, "script")
    style_ranges = _find_block_ranges(content, "style")
    blocked_ranges = script_ranges + style_ranges

    for match in DISCLAIMER_BLOCK_RE.finditer(content):
        attrs = match.group("attrs") or ""
        if not re.search(r"\bclass\s*=\s*['\"][^'\"]*\bdisclaimer\b", attrs, re.I):
            continue
        span = match.span("content")
        if _in_ranges(span, blocked_ranges):
            continue
        raw_content = match.group("content")
        if "{{" in raw_content or "{%" in raw_content or "}}" in raw_content:
            continue
        value = _clean_text(raw_content)
        if not value or len(value) < min_length:
            continue
        key = "disclaimer.third_party"
        used_keys.add(key)
        value_to_key.setdefault(value, key)
        leading = raw_content[: len(raw_content) - len(raw_content.lstrip())]
        trailing = raw_content[len(raw_content.rstrip()) :]
        replacement = f"{leading}{{{{ t('{key}') }}}}{trailing}"
        replacements.append((span, replacement, key, value))
        blocked_ranges.append(span)

    def get_key(value):
        if not allow_duplicates and value in value_to_key:
            return value_to_key[value]
        base = f"{prefix}.{_slugify(value)}" if prefix else _slugify(value)
        key = base
        counter = 2
        while key in used_keys:
            key = f"{base}_{counter}"
            counter += 1
        used_keys.add(key)
        value_to_key[value] = key
        return key

    for match in ATTR_RE.finditer(content):
        value = match.group(2)[1:-1]
        span = match.span(2)
        if _in_ranges(span, blocked_ranges):
            continue
        if "{{" in value or "{%" in value or "}}" in value:
            continue
        if len(value.strip()) < min_length:
            continue
        key = get_key(value)
        replacement = f"\"{{{{ t('{key}') }}}}\""
        replacements.append((span, replacement, key, value))

    for match in TEXT_NODE_RE.finditer(content):
        value = match.group(1)
        span = match.span(1)
        if _in_ranges(span, blocked_ranges):
            continue
        if "{{" in value or "{%" in value or "}}" in value:
            continue
        stripped = value.strip()
        if len(stripped) < min_length:
            continue
        key = get_key(stripped)
        leading = value[: len(value) - len(value.lstrip())]
        trailing = value[len(value.rstrip()) :]
        replacement = f"{leading}{{{{ t('{key}') }}}}{trailing}"
        replacements.append((span, replacement, key, stripped))

    replacements.sort(key=lambda item: item[0][0], reverse=True)
    return replacements


def _standardize_calls(text):
    text = re.sub(r"\blang\.t\(", "t(", text)
    text = re.sub(r"\btrans\(", "t(", text)
    return text


def _apply_transforms(text, do_standardize):
    parts = []
    cursor = 0
    for match in JINJA_TAG_RE.finditer(text):
        segment = text[cursor:match.start()]
        parts.append(segment)

        tag = match.group(0)
        if do_standardize:
            tag = _standardize_calls(tag)
        parts.append(tag)
        cursor = match.end()

    tail = text[cursor:]
    parts.append(tail)
    return "".join(parts)


def _iter_template_files(targets, extensions):
    for target in targets:
        if target.is_file():
            yield target
            continue
        if not target.is_dir():
            continue
        for path in target.rglob("*"):
            if path.is_file() and path.suffix in extensions:
                yield path


def main():
    parser = argparse.ArgumentParser(
        description="Apply translation tags to templates and write a locale file."
    )
    parser.add_argument(
        "paths",
        nargs="*",
        help="Files or directories to process (defaults to material-overrides).",
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="Path to the tanssi-mkdocs repo root.",
    )
    parser.add_argument(
        "--locale-file",
        type=Path,
        default=None,
        help="Locale YAML to create/update (defaults to tanssi-docs/locale/en.yml).",
    )
    parser.add_argument(
        "--restore-from-json",
        type=Path,
        default=None,
        help="Optional flat key/value JSON to seed the locale file.",
    )
    parser.add_argument(
        "--extensions",
        default="html,jinja,j2",
        help="Comma-separated list of file extensions to process.",
    )
    parser.add_argument(
        "--min-length",
        type=int,
        default=6,
        help="Minimum string length to replace (default: 6).",
    )
    parser.add_argument(
        "--allow-duplicates",
        action="store_true",
        help="Allow duplicate keys for identical values.",
    )
    parser.add_argument(
        "--skip-key-replacements",
        action="store_true",
        help="Skip replacing literal strings with t('key') tags.",
    )
    parser.add_argument(
        "--skip-locale-write",
        action="store_true",
        help="Skip writing the locale YAML file.",
    )
    parser.add_argument(
        "--skip-standardize",
        action="store_true",
        help="Skip standardizing lang.t()/trans() to t().",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show files that would change without writing.",
    )
    args = parser.parse_args()

    root = args.root
    locale_path = args.locale_file or root / "tanssi-docs" / "locale" / "en.yml"

    targets = [Path(path) for path in args.paths] or [root / "material-overrides"]
    extensions = {
        f".{ext.lstrip('.')}" for ext in args.extensions.split(",") if ext.strip()
    }

    locale_data = {}
    value_to_key = {}
    used_keys = set()
    if locale_path.exists():
        locale_data, flat = _load_locale_data(locale_path)
        used_keys.update(flat.keys())
        for key, value in flat.items():
            if isinstance(value, str) and value and value not in value_to_key:
                value_to_key[value] = key

    if args.restore_from_json and args.restore_from_json.exists():
        for key, value in _load_flat_json(args.restore_from_json).items():
            _ensure_key(locale_data, key, value)
        flat = {}
        _flatten("", locale_data, flat)
        used_keys.update(flat.keys())
        for key, value in flat.items():
            if isinstance(value, str) and value and value not in value_to_key:
                value_to_key[value] = key

    changed_files = []
    scanned_files = 0
    for path in _iter_template_files(targets, extensions):
        scanned_files += 1
        original = path.read_text(encoding="utf-8")
        updated = original
        if not args.skip_key_replacements:
            prefix = _path_prefix(path, root)
            generated = _collect_template_replacements(
                path,
                original,
                prefix,
                args.min_length,
                args.allow_duplicates,
                value_to_key,
                used_keys,
            )
            for _, _, key, value in generated:
                _ensure_key(locale_data, key, value)
            if generated:
                updated = original
                for span, replacement, _, _ in generated:
                    updated = updated[: span[0]] + replacement + updated[span[1] :]

        updated = _apply_transforms(updated, do_standardize=not args.skip_standardize)
        if updated != original:
            changed_files.append(path)
            if not args.dry_run:
                path.write_text(updated, encoding="utf-8")

    locale_written = False
    if not args.skip_locale_write and locale_data and not args.dry_run:
        locale_path.parent.mkdir(parents=True, exist_ok=True)
        locale_path.write_text(
            yaml.dump(
                locale_data,
                allow_unicode=True,
                sort_keys=False,
                width=120,
                Dumper=_Dumper,
            ),
            encoding="utf-8",
        )
        locale_written = True

    if args.dry_run:
        for path in changed_files:
            print(f"Would update {path}")
    else:
        for path in changed_files:
            print(f"Updated {path}")
    print(
        "Scanned {scanned} file(s). Updated {updated}. Locale written: {written}.".format(
            scanned=scanned_files,
            updated=len(changed_files),
            written="yes" if locale_written else "no",
        )
    )


if __name__ == "__main__":
    main()
