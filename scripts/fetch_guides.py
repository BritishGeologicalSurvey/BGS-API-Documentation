"""Download user guides linked from the portfolio so they can be hosted here.

    python scripts/fetch_guides.py            # list what would be fetched
    python scripts/fetch_guides.py --download # fetch into docs/assets/guides/

Downloads are NOT added to data/guides.yml automatically: check each PDF (title,
report number, which products it really covers) and add the entry by hand.
"""
import pathlib, sys, urllib.request, yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
guides = yaml.safe_load((ROOT / "data/guides.yml").read_text()) or {}
covered = set(guides) | {s for g in guides.values() for s in g.get("covers", [])}
todo = []
for f in sorted((ROOT / "data/portfolio/products").glob("*.yml")):
    p = yaml.safe_load(f.read_text())
    url = (p.get("links") or {}).get("user_guide_source")
    if url and p["slug"] not in covered:
        todo.append((p["slug"], url))
for slug, url in todo:
    print(f"{slug:45} {url}")
if "--download" in sys.argv:
    out = ROOT / "docs/assets/guides"
    for slug, url in todo:
        req = urllib.request.Request(url, headers={"User-Agent": "bgs-docs-build"})
        with urllib.request.urlopen(req, timeout=60) as r:
            data = r.read()
        if not data.startswith(b"%PDF"):
            print(f"  ! {slug}: not a PDF ({r.headers.get('Content-Type')}), skipped"); continue
        (out / f"{slug}.pdf").write_bytes(data)
        print(f"  saved {slug}.pdf ({len(data)//1024} KB)")
