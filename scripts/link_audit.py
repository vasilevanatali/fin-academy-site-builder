#!/usr/bin/env python3
"""Audit links and anchors for Fin Academy landing pages.

Usage:
  python3 scripts/link_audit.py path/to/index.html
  python3 scripts/link_audit.py path/to/dist
  python3 scripts/link_audit.py https://example.com

By default, external URLs are checked for basic URL shape only. Add
--check-external to make network requests.
"""

from __future__ import annotations

import argparse
import html.parser
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path


TRACKING_PARAMS = {"utm_source", "utm_medium", "utm_campaign", "utm_content", "utm_term", "yclid", "gclid", "fbclid", "gcpc"}


class LinkParser(html.parser.HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.links: list[tuple[str, str]] = []
        self.ids: set[str] = set()

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attrs_dict = {name.lower(): value or "" for name, value in attrs}
        if "id" in attrs_dict:
            self.ids.add(attrs_dict["id"])
        if tag.lower() == "a" and "href" in attrs_dict:
            self.links.append((attrs_dict["href"].strip(), attrs_dict.get("data-goal", "")))


def load_target(target: str) -> tuple[str, str, str | None]:
    if target.startswith(("http://", "https://")):
        try:
            with urllib.request.urlopen(target, timeout=20) as response:
                final_url = response.geturl()
                html = response.read().decode("utf-8", errors="replace")
                return html, final_url, final_url
        except urllib.error.URLError as error:
            raise SystemExit(f"Could not load URL: {target}\nReason: {error}") from error

    path = Path(target).expanduser()
    if path.is_dir():
        path = path / "index.html"
    if not path.exists():
        raise SystemExit(f"Target not found: {path}")
    return path.read_text(encoding="utf-8", errors="replace"), str(path), None


def is_external(href: str) -> bool:
    parsed = urllib.parse.urlparse(href)
    return parsed.scheme in {"http", "https"}


def check_external_url(url: str) -> tuple[bool, str]:
    request = urllib.request.Request(url, method="HEAD", headers={"User-Agent": "fin-academy-site-builder-link-audit/1.0"})
    try:
        with urllib.request.urlopen(request, timeout=15) as response:
            return 200 <= response.status < 400, f"HTTP {response.status}"
    except urllib.error.HTTPError as error:
        return False, f"HTTP {error.code}"
    except urllib.error.URLError as error:
        return False, str(error.reason)


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit links and anchors in landing page HTML.")
    parser.add_argument("target", help="HTML file, directory containing index.html, or URL")
    parser.add_argument("--check-external", action="store_true", help="Make network requests for external URLs")
    args = parser.parse_args()

    html, label, base_url = load_target(args.target)
    parser_obj = LinkParser()
    parser_obj.feed(html)

    results: list[tuple[str, str]] = []
    warnings = 0
    payment_like = re.compile(r"(pay|payment|order|oplata|checkout|soho|tinkoff|yookassa|cloudpayments)", re.I)

    for href, goal in parser_obj.links:
        if not href:
            results.append(("WARN", "empty href"))
            warnings += 1
            continue
        if href.startswith(("mailto:", "tel:", "tg://", "javascript:")):
            continue
        if href.startswith("#"):
            anchor = urllib.parse.unquote(href[1:])
            ok = bool(anchor) and anchor in parser_obj.ids
            results.append(("OK" if ok else "WARN", f"anchor {href} {'found' if ok else 'missing'}"))
            warnings += not ok
            continue
        if is_external(href):
            parsed = urllib.parse.urlparse(href)
            ok = bool(parsed.netloc)
            results.append(("OK" if ok else "WARN", f"external URL shape: {href}"))
            warnings += not ok
            if payment_like.search(href):
                query_keys = set(urllib.parse.parse_qs(parsed.query).keys())
                if not query_keys.intersection(TRACKING_PARAMS) and "appendUtm" not in html and "utm" not in html.lower():
                    results.append(("WARN", f"payment/order-like link may not preserve UTM: {href}"))
                    warnings += 1
            if args.check_external:
                resolved = urllib.parse.urljoin(base_url or "", href)
                ok, detail = check_external_url(resolved)
                results.append(("OK" if ok else "WARN", f"external check {href}: {detail}"))
                warnings += not ok
            continue

        if base_url:
            results.append(("OK", f"relative URL retained for browser resolution: {href}"))
            continue

        local_path = Path(label).parent / urllib.parse.unquote(urllib.parse.urlparse(href).path)
        ok = local_path.exists()
        results.append(("OK" if ok else "WARN", f"local link {href} {'exists' if ok else 'missing'}"))
        warnings += not ok

    print(f"Link audit target: {label}")
    print(f"Links found: {len(parser_obj.links)}")
    for status, message in results:
        print(f"{status}: {message}")

    if warnings:
        print(f"Summary: {warnings} warning(s). Review before publishing.")
        return 1
    print("Summary: no warnings.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
