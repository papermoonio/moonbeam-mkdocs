#!/usr/bin/env python3
import argparse
import json
import re
import hashlib
from pathlib import Path

import yaml
JINJA_TAG_RE = re.compile(r"({{.*?}}|{%-?.*?%}|{#.*?#})", re.S)
TEXT_NODE_RE = re.compile(r">([^<]+)<")
ATTR_RE = re.compile(
    r"\b(alt|title|placeholder|aria-label|aria-labelledby|value)\s*=\s*(\"[^\"]*\"|'[^']*')",
    re.I,
)
HTML_COMMENT_RE = re.compile(r"<!--.*?-->", re.S)
DISCLAIMER_BLOCK_RE = re.compile(
    r"<(?P<tag>[a-z0-9]+)\b(?P<attrs>[^>]*)>(?P<content>.*?)</(?P=tag)>",
    re.I | re.S,
)
TRANSLATION_CALL_RE = re.compile(
    r"\{\{\s*(?:lang\.)?(?:t|trans)\(\s*['\"]([^'\"]+)['\"]\s*\)\s*\}\}"
)
MAX_KEY_WORDS = 4


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


def _load_docs_dir(root):
    mkdocs_path = root / "mkdocs.yml"
    if not mkdocs_path.exists():
        return "docs"
    contents = mkdocs_path.read_text(encoding="utf-8")
    try:
        config = yaml.safe_load(contents) or {}
    except Exception:
        config = None
    if isinstance(config, dict):
        docs_dir = config.get("docs_dir")
        if isinstance(docs_dir, str) and docs_dir.strip():
            return docs_dir
    for line in contents.splitlines():
        if line.lstrip().startswith("#"):
            continue
        match = re.match(r"^\s*docs_dir:\s*(.+?)\s*$", line)
        if not match:
            continue
        raw = match.group(1).split("#", 1)[0].strip()
        if not raw:
            continue
        if raw[0] in "\"'" and raw[-1:] in "\"'":
            raw = raw[1:-1]
        return raw
    return "docs"


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


def _short_key_slug(value, max_words):
    full_slug = _slugify(value)
    words = [w for w in full_slug.split("_") if w]
    if len(words) <= max_words:
        return full_slug
    truncated = "_".join(words[:max_words]) or "text"
    digest = hashlib.sha1(full_slug.encode("utf-8")).hexdigest()[:6]
    return f"{truncated}__{digest}"


def _humanize_key(key):
    tail = key.split(".")[-1]
    if "__" in tail:
        tail = tail.split("__", 1)[0]
    text = tail.replace("_", " ").strip()
    if not text:
        return key
    return text[:1].upper() + text[1:]


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
    for match in HTML_COMMENT_RE.finditer(content):
        blocked_ranges.append(match.span())

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
        slug = _short_key_slug(value, MAX_KEY_WORDS)
        base = f"{prefix}.{slug}" if prefix else slug
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
        if "{{" in value or "{%" in value or "}}" in value or "{#" in value or "#}" in value:
            continue
        if JINJA_TAG_RE.search(value):
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
        if "{{" in value or "{%" in value or "}}" in value or "{#" in value or "#}" in value:
            continue
        if JINJA_TAG_RE.search(value):
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


def _extract_translation_keys(content):
    stripped = HTML_COMMENT_RE.sub("", content)
    stripped = re.sub(r"{#.*?#}", "", stripped, flags=re.S)
    return {match.group(1) for match in TRANSLATION_CALL_RE.finditer(stripped)}


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


def _normalize_translation_calls(text):
    return TRANSLATION_CALL_RE.sub(r"{{ t('\1') }}", text)


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


def _ensure_trailing_newline(text):
    if not text.endswith("\n"):
        return text + "\n"
    return text


def _strip_common_prefix(stem, prefix):
    prefix = prefix.strip().lower()
    stem_lower = stem.lower()
    for sep in ("-", "_"):
        needle = f"{prefix}{sep}"
        if stem_lower.startswith(needle):
            return stem[len(needle) :]
    return stem


def _derive_snippet_key(parts, path):
    if not parts:
        return None
    top = parts[0]
    if top not in {"_common", "_disclaimer", "_disclaimers"}:
        return None

    if top == "_common":
        base = ["common"]
    else:
        base = ["disclaimer"]

    rel_dirs = list(parts[1:-1])
    if rel_dirs:
        base.extend(_slugify(d.replace("-", "_")) for d in rel_dirs if d)

    stem = path.stem
    if rel_dirs:
        stem = _strip_common_prefix(stem, rel_dirs[-1])
    leaf = _slugify(stem.replace("-", "_"))
    if leaf:
        base.append(leaf)
    return ".".join(base)


def _wrap_snippet_content_with_call(original, key):
    call = f"{{{{ t('{key}') }}}}"
    text = original.replace("\r\n", "\n")
    # If this snippet is exactly a translation call already, just normalize it.
    if TRANSLATION_CALL_RE.fullmatch(text.strip()):
        return _ensure_trailing_newline(_normalize_translation_calls(text).strip())

    # If it is a single wrapper tag, replace its inner content while preserving the wrapper.
    m = re.match(
        r"^(?P<open>\s*<(?P<tag>[a-z0-9]+)\b[^>]*>\s*)"
        r"(?P<body>[\s\S]*?)"
        r"(?P<close>\s*</(?P=tag)>\s*)$",
        text,
        flags=re.I,
    )
    if m:
        open_part = m.group("open")
        close_part = m.group("close")
        # Try to keep indentation similar to existing content.
        body = m.group("body") or ""
        indent_match = re.search(r"\n([ \t]+)\S", body)
        indent = indent_match.group(1) if indent_match else "  "
        wrapped = f"{open_part}\n{indent}{call}\n{close_part}".strip()
        return _ensure_trailing_newline(wrapped)

    return _ensure_trailing_newline(call)


def _ingest_snippet_locale(
    snippet_root,
    root,
    min_length,
    locale_data,
    used_keys,
    value_to_key,
    dry_run=False,
):
    added = []
    if not snippet_root.exists():
        return added
    allowed = {"_common", "_disclaimer", "_disclaimers"}
    for path in snippet_root.rglob("*"):
        if not path.is_file():
            continue
        parts = path.relative_to(snippet_root).parts
        if not parts:
            continue
        if parts[0] not in allowed:
            continue
        try:
            raw = path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            continue

        # If snippet already contains a translation call, normalize it and ensure the key exists.
        existing_keys = list(TRANSLATION_CALL_RE.findall(raw))
        if existing_keys:
            updated = _normalize_translation_calls(_apply_transforms(raw, do_standardize=True))
            updated = _ensure_trailing_newline(updated.strip())
            if not dry_run and updated != raw:
                path.write_text(updated, encoding="utf-8")
            for key in existing_keys:
                if key not in used_keys:
                    _ensure_key(locale_data, key, _humanize_key(key))
                    used_keys.add(key)
                    added.append(key)
            continue

        # Otherwise, derive a stable key from snippet path and replace the file with a translation call.
        derived = _derive_snippet_key(parts, path)
        if not derived:
            continue

        updated = _wrap_snippet_content_with_call(raw, derived)
        if not dry_run and updated != raw:
            path.write_text(updated, encoding="utf-8")

        value = raw.strip()
        if len(value) >= min_length and derived not in used_keys:
            _ensure_key(locale_data, derived, value)
            used_keys.add(derived)
            value_to_key.setdefault(value, derived)
            added.append(derived)
    return added


def _inject_feedback_from_config(root, locale_data, used_keys):
    mkdocs_path = root / "mkdocs.yml"
    if not mkdocs_path.exists():
        return []
    try:
        cfg = yaml.safe_load(mkdocs_path.read_text(encoding="utf-8")) or {}
    except Exception:
        return []
    extra = cfg.get("extra") or {}
    analytics = extra.get("analytics") or {}
    feedback = analytics.get("feedback") or {}
    if not isinstance(feedback, dict):
        return []

    def set_if_absent(key, value):
        if key not in used_keys and value:
            _ensure_key(locale_data, key, value)
            used_keys.add(key)

    added = []
    set_if_absent("partials.feedback.title", feedback.get("title"))
    ratings = feedback.get("ratings") or []
    if isinstance(ratings, list):
        for item in ratings:
            if not isinstance(item, dict):
                continue
            data_val = item.get("data")
            if data_val == 1:
                set_if_absent("partials.feedback.rating_up_name", item.get("name"))
                set_if_absent("partials.feedback.rating_up_note", item.get("note"))
                added.extend(
                    [
                        k
                        for k in [
                            "partials.feedback.rating_up_name",
                            "partials.feedback.rating_up_note",
                        ]
                        if k in used_keys
                    ]
                )
            elif data_val == 0:
                set_if_absent("partials.feedback.rating_down_name", item.get("name"))
                set_if_absent("partials.feedback.rating_down_note", item.get("note"))
                added.extend(
                    [
                        k
                        for k in [
                            "partials.feedback.rating_down_name",
                            "partials.feedback.rating_down_note",
                        ]
                        if k in used_keys
                    ]
                )
    return added


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
        default=None,
        help="Path to the repo root (defaults to cwd if mkdocs.yml exists).",
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
        "--skip-snippets",
        action="store_true",
        help="Skip ingesting .snippets/text content into the locale file.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show files that would change without writing.",
    )
    args = parser.parse_args()

    if args.root:
        root = args.root
    else:
        cwd = Path.cwd()
        root = cwd if (cwd / "mkdocs.yml").exists() else Path(__file__).resolve().parents[1]
    docs_dir = _load_docs_dir(root)
    if args.locale_file:
        locale_path = args.locale_file
    else:
        docs_path = Path(docs_dir)
        if not docs_path.is_absolute():
            docs_path = root / docs_path
        if str(docs_dir).strip() in {"", "."}:
            locale_path = root / "locale" / "en.yml"
        else:
            locale_path = docs_path / "locale" / "en.yml"

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
    tagged_keys = set()
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
        tagged_keys.update(_extract_translation_keys(updated))
        if updated != original:
            changed_files.append(path)
            if not args.dry_run:
                path.write_text(updated, encoding="utf-8")

    for key in sorted(tagged_keys):
        if key not in used_keys:
            _ensure_key(locale_data, key, _humanize_key(key))
            used_keys.add(key)

    snippet_msg = ""
    if args.skip_snippets:
        snippet_msg = "Skipped .snippets/text ingestion."
        snippet_added = []
    else:
        snippet_root = (root / docs_dir) / ".snippets" / "text"
        snippet_added = _ingest_snippet_locale(
            snippet_root,
            root,
            args.min_length,
            locale_data,
            used_keys,
            value_to_key,
            dry_run=args.dry_run,
        )
        snippet_msg = f"Snippet keys added: {len(snippet_added)}" if snippet_added else "No snippet keys added."

    feedback_added = _inject_feedback_from_config(root, locale_data, used_keys)

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
        "Scanned {scanned} file(s). Updated {updated}. Locale written: {written}. {snippet}".format(
            scanned=scanned_files,
            updated=len(changed_files),
            written="yes" if locale_written else "no",
            snippet=f"{snippet_msg} Feedback keys added: {len(feedback_added)}",
        )
    )


if __name__ == "__main__":
    main()
