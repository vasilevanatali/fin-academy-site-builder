#!/usr/bin/env python3
"""Lightweight audit for Fin Academy landing pages.

Usage:
  python3 scripts/site_audit.py path/to/index.html
  python3 scripts/site_audit.py path/to/dist
  python3 scripts/site_audit.py https://example.com
"""

from __future__ import annotations

import os
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path


SECRET_PATTERNS = [
    re.compile(r"(?i)(api[_-]?key|secret|password|passwd|token)\s*[:=]\s*['\"][^'\"]{8,}['\"]"),
    re.compile(r"(?i)authorization\s*:\s*bearer\s+[a-z0-9._-]{20,}"),
    re.compile(r"-----BEGIN (RSA|OPENSSH|PRIVATE) KEY-----"),
]

TRACKING_PARAMS = ["utm_source", "utm_medium", "utm_campaign", "utm_content", "utm_term", "yclid", "gclid", "fbclid", "gcpc"]
CTA_WORDS = ["зарегистр", "получить", "выбрать", "оплат", "забрать", "доступ", "оставить заявку", "записаться"]


def load_target(target: str) -> tuple[str, str]:
    if target.startswith(("http://", "https://")):
        try:
            with urllib.request.urlopen(target, timeout=20) as response:
                return response.read().decode("utf-8", errors="replace"), target
        except urllib.error.URLError as error:
            raise SystemExit(f"Could not load URL: {target}\nReason: {error}") from error

    path = Path(target).expanduser()
    if path.is_dir():
        html = path / "index.html"
        if not html.exists():
            raise SystemExit(f"index.html not found in directory: {path}")
        return html.read_text(encoding="utf-8", errors="replace"), str(html)
    return path.read_text(encoding="utf-8", errors="replace"), str(path)


def check(condition: bool, ok: str, fail: str, results: list[tuple[str, str]]) -> None:
    results.append(("OK", ok) if condition else ("WARN", fail))


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__.strip())
        return 2

    html, label = load_target(sys.argv[1])
    scan_html = re.sub(r"<!--.*?-->", "", html, flags=re.S)
    lower = scan_html.lower()
    results: list[tuple[str, str]] = []

    check("<title" in lower, "title present", "missing <title>", results)
    check("<h1" in lower, "h1 present", "missing <h1>", results)
    check('name="description"' in lower or "name='description'" in lower, "meta description present", "missing meta description", results)
    check('name="viewport"' in lower or "name='viewport'" in lower, "viewport present", "missing viewport meta", results)
    check("lang=\"ru\"" in lower or "lang='ru'" in lower, "html lang ru present", "missing html lang=\"ru\"", results)
    check(any(word in lower for word in CTA_WORDS), "CTA/action wording detected", "CTA/action wording not detected", results)
    check(
        "sticky" in lower or ("position: fixed" in lower and "bottom:" in lower),
        "sticky/fixed mobile CTA hint detected",
        "sticky/fixed mobile CTA not detected",
        results,
    )
    check("metrika.soholms.com/watch.js" in lower, "SOHO metrika present", "missing SOHO metrika", results)
    check("ym(" in html or "mc.yandex.ru/metrika" in lower, "Yandex metrika appears present", "Yandex metrika not detected", results)
    check(any(param in scan_html for param in TRACKING_PARAMS), "tracking params referenced", "UTM/tracking passthrough not detected", results)
    check("fonts.googleapis.com" not in lower and "fonts.gstatic.com" not in lower, "no Google Fonts dependency", "Google Fonts dependency detected", results)
    check(".env" not in lower, "no .env reference", ".env reference detected", results)
    check(".git/" not in lower and "/.git" not in lower, "no .git reference", ".git reference detected", results)

    for pattern in SECRET_PATTERNS:
        check(not pattern.search(scan_html), f"no secret pattern: {pattern.pattern[:24]}", f"possible secret pattern: {pattern.pattern}", results)

    print(f"Audit target: {label}")
    warnings = 0
    for status, message in results:
        print(f"{status}: {message}")
        warnings += status == "WARN"

    if warnings:
        print(f"Summary: {warnings} warning(s). Review before publishing.")
        return 1
    print("Summary: no warnings.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
