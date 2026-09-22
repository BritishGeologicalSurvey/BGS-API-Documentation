"""Fail if any relative href/src/data in the built site points at a missing file.
    python scripts/check_links.py site
"""
import pathlib, re, sys, urllib.parse
root = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "site").resolve()
bad = []
for f in root.rglob("*.html"):
    if f.name == "404.html":
        continue  # uses absolute site_url paths
    for u in re.findall(r'(?:href|src|data)="([^"#?]+)', f.read_text(errors="ignore")):
        if re.match(r"^(https?:|mailto:|data:|//|javascript:|/)", u):
            continue
        t = (f.parent / urllib.parse.unquote(u)).resolve()
        if not str(t).startswith(str(root)):
            bad.append((f.relative_to(root), u, "escapes site root")); continue
        if u.endswith("/") or t.is_dir():
            t = t / "index.html"
        if not t.exists():
            bad.append((f.relative_to(root), u, "missing"))
for b in bad:
    print(*b)
print(f"{len(bad)} broken relative links")
sys.exit(1 if bad else 0)
