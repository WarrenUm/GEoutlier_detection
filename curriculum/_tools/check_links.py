"""Check the curriculum's supplemental-reading source URLs for reachability.

Extracts every URL from :mod:`phase_content` (the single source of truth for
supplemental sources) and, optionally, from the generated
``SUPPLEMENTAL_READING.md`` files, then issues a request per unique URL and
reports the outcome grouped as OK / REDIRECT / BROKEN.

Usage (from the repo root, with the project venv active or via .venv/bin/python)::

    python3 curriculum/_tools/check_links.py            # check phase_content URLs
    python3 curriculum/_tools/check_links.py --markdown # also scan generated .md
    python3 curriculum/_tools/check_links.py --timeout 15 --workers 16

Exit code is non-zero when any BROKEN links are found, so it can gate CI.

Only the Python standard library is used (urllib), so it runs without extra
dependencies. A realistic User-Agent is sent because several docs/CDN hosts
reject the default urllib agent with 403.
"""

from __future__ import annotations

import argparse
import concurrent.futures
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

TOOLS_DIR = Path(__file__).resolve().parent
CURRICULUM = TOOLS_DIR.parent
sys.path.insert(0, str(TOOLS_DIR))
import phase_content  # noqa: E402

_UA = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/124.0 Safari/537.36"
)
_URL_RE = re.compile(r"\((https?://[^)\s]+)\)")


def collect_from_phase_content() -> dict[str, list[str]]:
    """Return ``{url: [module_slug, ...]}`` for every source URL in the data."""
    urls: dict[str, list[str]] = {}
    for slug, sources in phase_content.MODULE_SOURCES.items():
        for src in sources:
            urls.setdefault(src["url"], []).append(slug)
    return urls


def collect_from_markdown() -> dict[str, list[str]]:
    """Return ``{url: [file, ...]}`` for URLs in generated SUPPLEMENTAL_READING.md."""
    urls: dict[str, list[str]] = {}
    for md in CURRICULUM.glob("phase*/**/SUPPLEMENTAL_READING.md"):
        text = md.read_text(encoding="utf-8")
        for match in _URL_RE.finditer(text):
            urls.setdefault(match.group(1), []).append(str(md.relative_to(CURRICULUM)))
    return urls


def check_one(url: str, timeout: float) -> tuple[str, int | None, str]:
    """Return ``(status_kind, http_code, detail)`` for a single URL.

    ``status_kind`` is one of ``"ok"``, ``"redirect"``, ``"broken"``. A GET is
    used (many hosts reject HEAD); only headers are read where possible. 403 is
    treated as ``ok`` because several doc hosts bot-block automated checks even
    though the page is live for browsers.
    """
    request = urllib.request.Request(url, method="GET", headers={"User-Agent": _UA})
    try:
        with urllib.request.urlopen(request, timeout=timeout) as resp:
            final = resp.geturl()
            code = resp.getcode()
            if final.rstrip("/") != url.rstrip("/"):
                return ("redirect", code, f"-> {final}")
            return ("ok", code, "")
    except urllib.error.HTTPError as exc:
        if exc.code in (403, 429, 999):
            # Bot-blocked / rate-limited, not a dead link.
            return ("ok", exc.code, "bot-blocked (likely live in a browser)")
        if exc.code in (301, 302, 303, 307, 308):
            return ("redirect", exc.code, exc.headers.get("Location", ""))
        return ("broken", exc.code, str(exc.reason))
    except (urllib.error.URLError, TimeoutError, ValueError) as exc:
        return ("broken", None, str(getattr(exc, "reason", exc)))
    except Exception as exc:  # noqa: BLE001 - report anything unexpected as broken
        return ("broken", None, repr(exc))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--markdown", action="store_true",
                        help="Also scan generated SUPPLEMENTAL_READING.md files.")
    parser.add_argument("--timeout", type=float, default=20.0)
    parser.add_argument("--workers", type=int, default=12)
    args = parser.parse_args()

    urls = collect_from_markdown() if args.markdown else collect_from_phase_content()
    print(f"Checking {len(urls)} unique URLs...\n")

    results: dict[str, tuple[str, int | None, str]] = {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = {pool.submit(check_one, u, args.timeout): u for u in urls}
        for fut in concurrent.futures.as_completed(futures):
            results[futures[fut]] = fut.result()

    ok = [u for u, r in results.items() if r[0] == "ok"]
    redirects = {u: r for u, r in results.items() if r[0] == "redirect"}
    broken = {u: r for u, r in results.items() if r[0] == "broken"}

    if redirects:
        print(f"REDIRECTS ({len(redirects)}) — reachable but the URL moved:")
        for u, (_, code, detail) in sorted(redirects.items()):
            print(f"  [{code}] {u}\n        {detail}")
            for where in urls[u]:
                print(f"        used in: {where}")
        print()

    if broken:
        print(f"BROKEN ({len(broken)}):")
        for u, (_, code, detail) in sorted(broken.items()):
            print(f"  [{code}] {u}  ({detail})")
            for where in urls[u]:
                print(f"        used in: {where}")
        print()

    print(f"Summary: {len(ok)} ok, {len(redirects)} redirect, {len(broken)} broken.")
    return 1 if broken else 0


if __name__ == "__main__":
    raise SystemExit(main())
