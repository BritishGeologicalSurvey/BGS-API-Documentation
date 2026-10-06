"""Local dev server: generate pages, serve with live reload, regenerate on data/ edits.

    python scripts/dev_server.py [--addr 0.0.0.0:8000]

Zensical reloads when docs/ changes, but product pages are generated from data/*.yml,
so this polls data/ (polling works on Windows/macOS bind mounts where file events
often don't) and re-runs build_products.py, which rewrites docs/products/.
"""
import pathlib, subprocess, sys, time

ROOT = pathlib.Path(__file__).resolve().parent.parent
addr = sys.argv[sys.argv.index("--addr") + 1] if "--addr" in sys.argv else "localhost:8000"
py = sys.executable


def snapshot():
    return {p: p.stat().st_mtime for p in (ROOT / "data").rglob("*.yml")}


subprocess.run([py, "scripts/build_products.py"], cwd=ROOT, check=True)
if not [p for p in (ROOT / "docs/examples").glob("*.md") if p.name != "index.md"]:
    subprocess.run([py, "scripts/convert_notebooks.py"], cwd=ROOT, check=True)

server = subprocess.Popen(["zensical", "serve", "-a", addr], cwd=ROOT)
seen = snapshot()
try:
    while server.poll() is None:
        time.sleep(2)
        now = snapshot()
        if now != seen:
            print("data/ changed: regenerating product pages", flush=True)
            subprocess.run([py, "scripts/build_products.py"], cwd=ROOT)
            seen = now
finally:
    server.terminate()
