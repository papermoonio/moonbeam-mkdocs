import io
from pathlib import Path

import yaml
import json
import re
from jinja2 import pass_context
from babel.messages.catalog import Catalog
from babel.messages.pofile import read_po, write_po
from babel.messages.mofile import write_mo
from babel.support import Translations
from mkdocs.plugins import event_priority


def _flatten(prefix, value, dest):
    if isinstance(value, dict):
        for k, v in value.items():
            key = f"{prefix}.{k}" if prefix else k
            _flatten(key, v, dest)
    else:
        dest[prefix] = value


def _load_yaml_translations(locale_dir):
    translations = {}
    if not locale_dir.exists():
        return translations
    for path in locale_dir.glob("*.yml"):
        data = yaml.safe_load(path.read_text()) or {}
        flat = {}
        _flatten("", data, flat)
        translations[path.stem] = flat
    return translations


def _load_gettext_translations(i18n_dir):
    translations = {}
    if not i18n_dir.exists():
        return translations
    for lang_dir in i18n_dir.iterdir():
        if not lang_dir.is_dir():
            continue
        lc_dir = lang_dir / "LC_MESSAGES"
        if not lc_dir.exists():
            continue
        po_path = lc_dir / "messages.po"
        mo_path = lc_dir / "messages.mo"
        translator = None
        if po_path.exists():
            with po_path.open("r", encoding="utf-8") as po_file:
                catalog = read_po(po_file)
            buffer = io.BytesIO()
            write_mo(buffer, catalog)
            buffer.seek(0)
            translator = Translations(fp=buffer)
        elif mo_path.exists():
            with mo_path.open("rb") as mo_file:
                translator = Translations(mo_file)
        if translator is not None:
            translations[lang_dir.name] = translator
    return translations


def _build_translator(config):
    docs_dir = Path(config.get("docs_dir", "docs"))
    yaml_translations = _load_yaml_translations(docs_dir / "locale")
    gettext_translations = _load_gettext_translations(docs_dir / "i18n")
    default_lang = config.get("theme", {}).get("language", "en")

    def translate(key, lang=None):
        current_lang = lang or default_lang
        translator = gettext_translations.get(current_lang)
        if translator:
            value = translator.gettext(key)
            if value and value != key:
                return value
        yaml_lang = yaml_translations.get(current_lang, {})
        if key in yaml_lang:
            return yaml_lang[key]
        fallback_translator = gettext_translations.get(default_lang)
        if fallback_translator:
            value = fallback_translator.gettext(key)
            if value and value != key:
                return value
        return yaml_translations.get(default_lang, {}).get(key, key)

    return translate


def _has_custom_translation(yaml_translations, gettext_translations, key, lang, default_lang):
    if key in yaml_translations.get(lang, {}):
        return True
    if key in yaml_translations.get(default_lang, {}):
        return True
    translator = gettext_translations.get(lang)
    if translator:
        value = translator.gettext(key)
        if value and value != key:
            return True
    fallback_translator = gettext_translations.get(default_lang)
    if fallback_translator:
        value = fallback_translator.gettext(key)
        if value and value != key:
            return True
    return False


def _sync_theme_translations(config):
    docs_dir = Path(config.get("docs_dir", "docs"))
    yaml_translations = _load_yaml_translations(docs_dir / "locale")
    if not yaml_translations:
        return

    theme = config.get("theme", {})
    custom_dir = getattr(theme, "custom_dir", None)
    if not custom_dir and hasattr(theme, "get"):
        custom_dir = theme.get("custom_dir")
    if not custom_dir:
        return

    base_dir = Path(__file__).resolve().parent
    custom_path = Path(custom_dir)
    if not custom_path.is_absolute():
        custom_path = base_dir / custom_path

    translations_dir = custom_path / ".translations"
    translations_dir.mkdir(parents=True, exist_ok=True)

    project_name = config.get("site_name", "Tanssi Docs")
    for locale, data in yaml_translations.items():
        target = translations_dir / f"{locale}.json"
        target.write_text(
            json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
        _write_po_translations(docs_dir, locale, data, project_name)


def _get_catalog_metadata(catalog):
    metadata = getattr(catalog, "metadata", None)
    if metadata is not None:
        return dict(metadata)
    headers = getattr(catalog, "mime_headers", None)
    if headers is None:
        return {}
    return {key: value for key, value in headers}


def _set_catalog_metadata(catalog, metadata):
    if hasattr(catalog, "metadata"):
        catalog.metadata.update(metadata)
        return
    headers = list(getattr(catalog, "mime_headers", []) or [])
    if not headers:
        catalog.mime_headers = list(metadata.items())
        return
    index = {key: idx for idx, (key, _value) in enumerate(headers)}
    for key, value in metadata.items():
        if key in index:
            headers[index[key]] = (key, value)
        else:
            headers.append((key, value))
    catalog.mime_headers = headers


def _write_po_translations(docs_dir, locale, data, project_name):
    i18n_dir = docs_dir / "i18n" / locale / "LC_MESSAGES"
    i18n_dir.mkdir(parents=True, exist_ok=True)
    po_path = i18n_dir / "messages.po"

    existing_metadata = {}
    if po_path.exists():
        with po_path.open("r", encoding="utf-8") as po_file:
            existing_catalog = read_po(po_file)
        existing_metadata = _get_catalog_metadata(existing_catalog)

    catalog = Catalog(
        locale=locale,
        project=existing_metadata.get("Project-Id-Version", project_name),
    )
    metadata = dict(existing_metadata)
    metadata.setdefault("Project-Id-Version", project_name)
    metadata.setdefault("POT-Creation-Date", "2025-01-01 00:00+0000")
    metadata.setdefault("Language", locale)
    metadata.setdefault("Content-Type", "text/plain; charset=UTF-8")
    metadata.setdefault("Content-Transfer-Encoding", "8bit")
    _set_catalog_metadata(catalog, metadata)

    for key in sorted(data):
        catalog.add(key, data[key] if data[key] is not None else "")

    with po_path.open("wb") as po_file:
        write_po(po_file, catalog, width=0)


def on_config(config):
    _sync_theme_translations(config)
    return config


def on_env(env, config, files):
    translator = _build_translator(config)
    docs_dir = Path(config.get("docs_dir", "docs"))
    yaml_translations = _load_yaml_translations(docs_dir / "locale")
    gettext_translations = _load_gettext_translations(docs_dir / "i18n")
    default_lang = config.get("theme", {}).get("language", "en")

    @pass_context
    def t(context, key):
        lang_code = None
        page = context.get("page")
        if page is not None:
            lang_code = getattr(page, "lang", None)
            if not lang_code:
                lang_code = getattr(getattr(page, "file", None), "locale", None)
        if not lang_code:
            cfg = context.get("config", {}) or {}
            lang_code = cfg.get("theme", {}).get("language")
        lang_code = lang_code or default_lang

        if _has_custom_translation(
            yaml_translations, gettext_translations, key, lang_code, default_lang
        ):
            return translator(key, lang=lang_code)

        lang_obj = context.get("lang")
        if lang_obj is not None and hasattr(lang_obj, "t"):
            return lang_obj.t(key)

        return translator(key, lang=lang_code)

    env.globals["trans"] = translator
    env.globals["t"] = t
    env.filters["trans"] = translator
    return env


def on_page_context(context, page, config, nav):
    """
    Keep locale pages rooted at their own base so assets/search resolve inside the locale.
    """
    i18n = config.plugins.get("i18n")
    if not i18n or not page or not hasattr(page.file, "locale"):
        return context

    default_lang = next(
        (lang.locale for lang in i18n.config.languages if getattr(lang, "default", False)),
        config.get("theme", {}).get("language", "en"),
    )
    page_locale = page.file.locale or default_lang
    if page_locale == default_lang:
        return context

    base = getattr(page, "base_url", context.get("base", ""))
    if base.startswith("../"):
        base = base[3:] or "."
        page.base_url = base
        context["base"] = base
    return context


def on_post_page(output, page, config):
    """
    Adjust Material's base path so locale pages resolve assets/search inside their locale,
    and render simple trans() placeholders left in snippets.
    """
    i18n = config.plugins.get("i18n")
    if i18n and page:
        default_lang = next(
            (lang.locale for lang in i18n.config.languages if getattr(lang, "default", False)),
            config.get("theme", {}).get("language", "en"),
        )
        dest_path = getattr(getattr(page, "file", None), "dest_path", "")
        page_locale = getattr(page.file, "locale", None) or default_lang
        is_404 = getattr(page, "url", "") == "404.html" or dest_path == "404.html"

        # 404s are handled in on_post_build so we do not double-inject language patches here
        if is_404:
            return output

        # Adjust base for locale pages
        if page_locale != default_lang:
            parts = [p for p in (page.url or "").split("/") if p]
            if parts and parts[0] == page_locale:
                depth = max(len(parts) - 1, 0)
            else:
                depth = len(parts)
            new_base = "../" * depth or "."

            m = re.search(r'(<script id="__config" type="application/json">)(.*?)(</script>)', output, flags=re.S)
            if m:
                try:
                    cfg = json.loads(m.group(2))
                    cfg["base"] = new_base
                    new_json = json.dumps(cfg, separators=(",", ":"))
                    output = output[: m.start(2)] + new_json + output[m.end(2) :]
                except Exception:
                    pass

        # Render inline trans() placeholders left in snippets
        translator = _build_translator(config)
        lang = page_locale

        def replace_translation(match):
            key = match.group(1).strip()
            return translator(key, lang=lang)

        # match {{ t("key") }} or {{ trans("key") }} including cases where quotes are escaped
        output = re.sub(
            r"{{\s*(?:trans|t)\(\s*\\?['\"]([^'\"]+)\\?['\"]\s*\)\s*}}",
            replace_translation,
            output,
        )

        # normalize html lang attribute to the resolved locale
        output = re.sub(
            r'(<html[^>]*?lang=")[^"]*(")',
            lambda m: f"{m.group(1)}{page_locale}{m.group(2)}",
            output,
            count=1,
        )

        # Inject external link modal strings for JS
        strings = {
            "header": translator("external_link_modal.header", lang=lang),
            "message": translator("external_link_modal.message", lang=lang),
            "cancel": translator("external_link_modal.cancel", lang=lang),
            "continue": translator("external_link_modal.continue", lang=lang),
        }
        payload = json.dumps({lang: strings}, ensure_ascii=False)
        injections = [f'<script>window.__externalLinkModalStrings={payload};</script>']

        head_close = output.find("</head>")
        if head_close != -1:
            output = output[:head_close] + "".join(injections) + output[head_close:]
        else:
            output = "".join(injections) + output

    return output


@event_priority(-1000)
def on_post_build(config):
    """
    Split the search index per locale so each language only sees its own pages
    and produce localized 404 pages with the proper header/footer and language toggle.
    """
    site_dir = Path(config["site_dir"])
    index_path = site_dir / "search" / "search_index.json"
    if not index_path.exists():
        return

    i18n_plugin = config.plugins.get("i18n")
    if not i18n_plugin:
        return

    languages = [lang.locale for lang in i18n_plugin.config.languages]
    default_lang = next((lang.locale for lang in i18n_plugin.config.languages if lang.default), None)
    if not default_lang:
        default_lang = i18n_plugin.config.default_language

    def _replace_config_base(doc_html: str, base_value: str) -> str:
        """
        Normalize the __config base setting. Prefer JSON rewrite, fall back to regex.
        """
        m = re.search(r'(<script id="__config" type="application/json">)(.*?)(</script>)', doc_html, re.S)
        if m:
            try:
                cfg = json.loads(m.group(2))
                cfg["base"] = base_value
                new_json = json.dumps(cfg, separators=(",", ":"))
                return doc_html[: m.start(2)] + new_json + doc_html[m.end(2) :]
            except Exception:
                pass
        return re.sub(r'"base"\s*:\s*"[^"]*"', f'"base":"{base_value}"', doc_html, count=1)

    def _strip_feedback_block(doc_html: str) -> str:
        """
        Remove the feedback/actions block from 404 pages.
        """
        return re.sub(
            r'<div class="feedback-actions-container">.*?<div class="edit-section">.*?</div>\s*</div>',
            "",
            doc_html,
            flags=re.S,
        )

    def _strip_404_lang_injection(doc_html: str) -> str:
        """
        Remove previously injected 404 language scripts to avoid duplicates.
        """
        doc_html = re.sub(r'<script id="lang-404-data".*?</script>', "", doc_html, flags=re.S)
        doc_html = re.sub(r'<script id="lang-404">.*?</script>', "", doc_html, flags=re.S)
        doc_html = re.sub(
            r"<script>\s*\(function\(\)\s*\{.*?swapShell\(\);.*?\}\)\(\);\s*</script>",
            "",
            doc_html,
            flags=re.S,
        )
        return doc_html

    try:
        data = json.loads(index_path.read_text(encoding="utf-8"))
    except Exception:
        return

    docs = data.get("docs", [])

    def is_lang_doc(doc, locale):
        location = doc.get("location", "")
        if locale == default_lang:
            # default language lives at the root; exclude other locales
            return not any(location.startswith(f"{lang}/") for lang in languages if lang != default_lang)
        return location.startswith(f"{locale}/")

    def _normalize_location(doc, locale):
        new_doc = dict(doc)
        if locale != default_lang:
            prefix = f"{locale}/"
            location = new_doc.get("location", "")
            if location.startswith(prefix):
                new_doc["location"] = location[len(prefix) :]
        return new_doc

    # write per-locale indexes; overwrite the root with default only
    for locale in languages:
        filtered_docs = [_normalize_location(doc, locale) for doc in docs if is_lang_doc(doc, locale)]
        if not filtered_docs:
            continue

        localized = dict(data)
        localized["docs"] = filtered_docs
        localized["config"] = dict(localized.get("config", {}))
        localized["config"]["lang"] = [locale]

        target_path = index_path if locale == default_lang else site_dir / locale / "search" / "search_index.json"
        target_path.parent.mkdir(parents=True, exist_ok=True)
        target_path.write_text(json.dumps(localized, ensure_ascii=False), encoding="utf-8")

    translator = _build_translator(config)
    title_map = {}
    for lang_cfg in i18n_plugin.config.languages:
        locale = lang_cfg.locale
        title = translator("material_overrides.404.404_not_found", lang=locale)
        if not title or title == "material_overrides.404.404_not_found":
            title = translator("error.404_title", lang=locale)
        title_map[locale] = title
    locale_payload = {
        "locales": languages,
        "default": default_lang,
        "titles": title_map,
    }
    locale_payload_json = json.dumps(locale_payload, ensure_ascii=False)

    lang_injection = f"""<script id="lang-404-data" type="application/json">{locale_payload_json}</script>
<script id="lang-404">
(function() {{
  function getData() {{
    var el = document.getElementById("lang-404-data");
    if (!el) return null;
    try {{
      return JSON.parse(el.textContent || el.innerText || "{{}}");
    }} catch (e) {{
      return null;
    }}
  }}

  function pickLocale(locales, fallback) {{
    var pathname = window.location.pathname || "/";
    var parts = pathname.split("/").filter(Boolean);
    for (var i = 0; i < parts.length; i++) {{
      if (locales.indexOf(parts[i]) !== -1) return parts[i];
    }}
    return fallback || locales[0] || "en";
  }}

  function setPicker(locale) {{
    if (window.__md_set) {{ try {{ __md_set("language", locale); }} catch(e) {{}} }}
    document.documentElement.setAttribute("lang", locale);
    var label = document.querySelector(".language-picker__label");
    var labelText = locale.toUpperCase();
    if (locale && locale.toLowerCase().indexOf("zh") === 0) labelText = "\\u4e2d\\u6587";
    if (label) label.textContent = labelText;
    document.querySelectorAll(".language-picker__code").forEach(function(el) {{
      var link = el.closest("a");
      var hrefLang = link ? (link.getAttribute("hreflang") || "") : "";
      if (hrefLang.toLowerCase().indexOf("zh") === 0) {{
        el.textContent = "\\u4e2d\\u6587";
      }} else {{
        el.textContent = el.textContent.trim().toUpperCase();
      }}
      if (link) link.classList.toggle("is-active", hrefLang === locale);
    }});
    document.querySelectorAll('.language-picker__menu a[hreflang]').forEach(function(a) {{
      a.classList.toggle("is-active", a.getAttribute("hreflang") === locale);
    }});
  }}

  function getLocaleLink(locale) {{
    var link = document.querySelector('[data-md-component="language"] a[hreflang="' + locale + '"]');
    return link ? link.getAttribute("href") || "" : "";
  }}

  function resolveLocaleRoot(locale) {{
    var href = getLocaleLink(locale);
    if (!href) return "/";
    try {{
      var resolved = new URL(href, window.location.href);
      var path = resolved.pathname || "/";
      if (!path.endsWith("/")) path += "/";
      return path;
    }} catch (e) {{
      return "/";
    }}
  }}

  function resolveIndexPath(locale) {{
    var href = getLocaleLink(locale);
    if (!href) return "index.html";
    try {{
      var resolved = new URL(href, window.location.href);
      var path = resolved.pathname || "";
      if (path.endsWith("/")) return path + "index.html";
      if (path.endsWith(".html")) return path;
      return path + "/index.html";
    }} catch (e) {{
      return "index.html";
    }}
  }}

  function resolve404Path(locale) {{
    var root = resolveLocaleRoot(locale);
    if (!root) return "/404.html";
    if (!root.endsWith("/")) root += "/";
    return root + "404.html";
  }}

  function resolveUrl(rootPath, value) {{
    if (!value) return value;
    if (/^(?:[a-z][a-z0-9+.-]*:|\\/\\/)/i.test(value)) return value;
    if (value[0] === "#") return value;
    try {{
      var resolved = new URL(value, window.location.origin + rootPath);
      return resolved.pathname + resolved.search + resolved.hash;
    }} catch (e) {{
      return value;
    }}
  }}

  function normalizeShellLinks(container, rootPath) {{
    if (!container) return;
    var withHref = container.querySelectorAll("[href]");
    withHref.forEach(function(el) {{
      var href = el.getAttribute("href");
      var resolved = resolveUrl(rootPath, href);
      if (resolved !== href) el.setAttribute("href", resolved);
    }});
    var withSrc = container.querySelectorAll("[src]");
    withSrc.forEach(function(el) {{
      var src = el.getAttribute("src");
      var resolved = resolveUrl(rootPath, src);
      if (resolved !== src) el.setAttribute("src", resolved);
    }});
  }}

  function swapShell(locale) {{
    var indexPath = resolveIndexPath(locale);
    var localeRoot = resolveLocaleRoot(locale);
    fetch(indexPath).then(function(resp) {{ return resp.text(); }}).then(function(html) {{
      var doc = new DOMParser().parseFromString(html, "text/html");
      var newHeader = doc.querySelector("header.md-header");
      var newFooter = doc.querySelector("footer.md-footer");
      var curHeader = document.querySelector("header.md-header");
      var curFooter = document.querySelector("footer.md-footer");
      if (newHeader && curHeader) {{
        normalizeShellLinks(newHeader, localeRoot);
        curHeader.replaceWith(newHeader);
      }}
      if (newFooter && curFooter) {{
        normalizeShellLinks(newFooter, localeRoot);
        curFooter.replaceWith(newFooter);
      }}
      setPicker(locale);
    }}).catch(function() {{ setPicker(locale); }});
  }}

  function apply() {{
    var data = getData();
    if (!data) return;
    var locales = Array.isArray(data.locales) ? data.locales : [];
    var locale = pickLocale(locales, data["default"]);
    if (!locale) return;
    var pathname = window.location.pathname || "/";
    var target404 = resolve404Path(locale);
    if (locale !== data["default"] && target404 && pathname !== target404) {{
      window.location.replace(target404);
      return;
    }}
    var title = document.getElementById("not-found-title");
    if (title && data.titles && data.titles[locale]) {{
      title.textContent = data.titles[locale];
    }}
    setPicker(locale);
  }}

  if (document.readyState === "loading") {{
    document.addEventListener("DOMContentLoaded", apply);
  }} else {{
    apply();
  }}
}})();
</script>"""

    # Generate locale-specific 404 pages
    base_404 = site_dir / "404.html"
    if base_404.exists():
        html_404 = base_404.read_text(encoding="utf-8")
        # Ensure 404 redirect targets the actual generated files.
        for locale in languages:
            html_404 = re.sub(
                rf'(["\'])/{re.escape(locale)}/404/\1',
                rf"\1/{locale}/404.html\1",
                html_404,
            )
        html_404 = re.sub(
            r'(["\'])/404/\1',
            r'\1/404.html\1',
            html_404,
        )
        html_404 = _strip_feedback_block(html_404)
        html_404 = _strip_404_lang_injection(html_404)
        base_html = html_404
        head_close = base_html.find("</head>")
        if head_close != -1:
            base_html = base_html[:head_close] + lang_injection + base_html[head_close:]
        else:
            base_html = lang_injection + base_html
        base_404.write_text(base_html, encoding="utf-8")
        for lang_cfg in i18n_plugin.config.languages:
            locale = lang_cfg.locale
            translated_title = title_map.get(locale, "404")

            localized = re.sub(
                r'(<html[^>]*?lang=")[^"]*(")',
                lambda m: f"{m.group(1)}{locale}{m.group(2)}",
                html_404,
                count=1,
            )
            localized = re.sub(
                r'(<h1[^>]*class="[^"]*\bnot-found\b[^"]*"[^>]*>)(.*?)(</h1>)',
                lambda m: f"{m.group(1)}{translated_title}{m.group(3)}",
                localized,
                count=1,
            )
            localized = _strip_feedback_block(localized)
            localized = _strip_404_lang_injection(localized)
            # Prefer a localized navigation block from the locale's index.html so the header renders in the right language
            localized_index = site_dir / ("index.html" if locale == default_lang else f"{locale}/index.html")
            header_fragment = footer_fragment = config_fragment = search_fragment = None
            if localized_index.exists():
                try:
                    idx_html = localized_index.read_text(encoding="utf-8")
                    header_match = re.search(r'(<header[^>]*class="[^"]*md-header[^"]*"[^>]*>.*?</header>)', idx_html, re.S)
                    footer_match = re.search(r'(<footer[^>]*class="[^"]*md-footer[^"]*"[^>]*>.*?</footer>)', idx_html, re.S)
                    config_match = re.search(
                        r'(<script id="__config" type="application/json">.*?</script>)',
                        idx_html,
                        re.S,
                    )
                    search_match = re.search(
                        r'(<script id="__(?:md_)?search" type="application/json">.*?</script>)',
                        idx_html,
                        re.S,
                    )
                    header_fragment = header_match.group(1) if header_match else None
                    footer_fragment = footer_match.group(1) if footer_match else None
                    config_fragment = config_match.group(1) if config_match else None
                    search_fragment = search_match.group(1) if search_match else None
                except Exception:
                    header_fragment = footer_fragment = config_fragment = search_fragment = None
            if header_fragment:
                localized = re.sub(
                    r'<header[^>]*class="[^"]*md-header[^"]*"[^>]*>.*?</header>',
                    lambda _m, frag=header_fragment: frag,
                    localized,
                    flags=re.S,
                )
            if footer_fragment:
                localized = re.sub(
                    r'<footer[^>]*class="[^"]*md-footer[^"]*"[^>]*>.*?</footer>',
                    lambda _m, frag=footer_fragment: frag,
                    localized,
                    flags=re.S,
                )
            if config_fragment:
                localized = re.sub(
                    r'<script id="__config" type="application/json">.*?</script>',
                    lambda _m, frag=config_fragment: frag,
                    localized,
                    flags=re.S,
                )
            if search_fragment:
                localized = re.sub(
                    r'<script id="__(?:md_)?search" type="application/json">.*?</script>',
                    lambda _m, frag=search_fragment: frag,
                    localized,
                    flags=re.S,
                )

            # 404 pages live at the locale root, so base should be the current dir
            base_value = "."
            localized = _replace_config_base(localized, base_value)

            head_close = localized.find("</head>")
            if head_close != -1:
                localized = localized[:head_close] + lang_injection + localized[head_close:]
            else:
                localized = lang_injection + localized

            dest = site_dir / ("" if getattr(lang_cfg, "default", False) else locale) / "404.html"
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_text(localized, encoding="utf-8")
