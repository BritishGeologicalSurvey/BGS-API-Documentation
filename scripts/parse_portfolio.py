"""Extract product records from the BGS Product Portfolio PDF into YAML.

The PowerPoint export rasterises the visible (brand-font) text, but keeps an
invisible Calibri text layer with correct positions. We parse that layer.
"""
import re, sys, json, pathlib, yaml, pdfplumber

# usage: python scripts/parse_portfolio.py <portfolio.pdf>
# writes data/portfolio/{products/*.yml,themes.yml} and docs/assets/products/*.webp
# Hand-authored additions live in data/extra/ and are never touched by this script.
ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = sys.argv[1]
OUT = ROOT / "data/portfolio/products"
IMG = ROOT / "docs/assets/products"

THEMES = [  # (slug, title, first_page, last_page) 1-based, from contents page
    ("baseline-geology", "Baseline geology", 5, 16),
    ("engineering-geology", "Engineering geology", 17, 38),
    ("geochemistry", "Geochemistry", 39, 48),
    ("hazards", "Hazards", 49, 76),
    ("hydrogeology", "Hydrogeology", 77, 90),
    ("minerals", "Minerals", 91, 96),
]

# Known artefacts in the PowerPoint text layer (visible text is rasterised).
NAME_OVERRIDES = {"GeoClimate shrink–s well": "GeoClimate shrink–swell"}

def fix(s):
    s = re.sub(r"(\w) -(\w)", r"\1-\2", s)          # "site -specific"
    s = re.sub(r"(\w)- (\w)", r"\1-\2", s) if False else s
    s = re.sub(r"(\w) ?– ?(\w)", r"\1–\2", s)          # "shrink –swell" -> "shrink–swell"
    s = re.sub(r"(\w) /(\w)", r"\1/\2", s)
    s = s.replace("`s", "s").replace("km 2", "km²").replace(" ,", ",")
    s = re.sub(r"\(\s+", "(", s)
    return re.sub(r"\s+", " ", s).strip()

def slugify(s):
    s = s.replace("®", "").replace("–", "-").replace("/", "-")
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")

def lines_in(page, x0, x1):
    crop = page.crop((x0, 0, x1, page.height), strict=False)
    out = []
    for l in crop.extract_text_lines(layout=False, x_tolerance=1.5):
        ch = l["chars"][0]
        font = ch["fontname"].split("+")[-1]
        if l["x0"] < 0 or "Aptos" in font:        # off-slide labels, page numbers
            continue
        out.append(dict(x=l["x0"], top=l["top"], size=round(ch["size"]),
                        bold="Bold" in font, text=l["text"]))
    return out

def sections(lines, stop_top=None):
    """Group lines under size-14 headings; build bullets / paragraphs."""
    secs, cur = {}, None
    for ln in lines:
        if stop_top and ln["top"] > stop_top:
            break
        t = ln["text"].strip()
        if ln["size"] >= 14 and len(t) < 40:
            cur = t; secs[cur] = []
            continue
        if cur is None or ln["top"] < 100:
            continue
        secs[cur].append(ln)
    return secs

def to_items(lns):
    """Return list of {'text', 'sub':[...]} or paragraph strings."""
    items, para = [], []
    for ln in lns:
        t = ln["text"].strip()
        if t.startswith("▪"):
            subs = [fix(x) for x in t.split("▪") if x.strip()]
            if items: items[-1].setdefault("sub", []).extend(subs)
        elif t.startswith("•"):
            items.append({"text": fix(t.lstrip("•"))})
        elif items and ln["x"] > 60:
            items[-1]["text"] = fix(items[-1]["text"] + " " + t)
        else:
            para.append(t)
    if items:
        # sub-bullets laid out in 2 columns: restore reading order (col 1 then col 2)
        for it in items:
            if "sub" in it and len(it["sub"]) % 2 == 0:
                it["sub"] = it["sub"][0::2] + it["sub"][1::2]
        return items
    return fix(" ".join(para))

def lic_blocks(lns):
    """Sidebar licencing text -> [{heading, text}] using bold runs and vertical gaps."""
    blocks, prev = [], None
    for ln in lns:
        t = ln["text"].strip()
        gap = (ln["top"] - prev["top"]) if prev else 99
        if ln["bold"]:
            if prev and prev["bold"] and gap < 16.5:
                blocks[-1]["heading"] = fix(blocks[-1]["heading"] + " " + t)
            else:
                blocks.append({"heading": fix(t), "text": ""})
        elif not blocks or gap > 16.5:
            blocks.append({"heading": None, "text": fix(t)})
        else:
            b = blocks[-1]
            b["text"] = fix(b["text"] + (" " if b["text"] else "") + t)
        prev = ln
    # merge heading-only block with following text block
    out = []
    for b in blocks:
        if out and out[-1]["heading"] and not out[-1]["text"] and not b["heading"]:
            out[-1]["text"] = b["text"]
        else:
            out.append(b)
    return out

def links(page):
    return [(h["uri"], h["x0"], h["top"]) for h in page.hyperlinks]

def extract_image(page, pn, slug):
    imgs = [i for i in page.images if i["x0"] > 380 and 100 < i["top"] < 330
            and (i["x1"] - i["x0"]) > 100]
    if not imgs:
        # mosaics (e.g. BGS Civils) are built from many small tiles: take their union
        tiles = [i for i in page.images if i["x0"] > 380 and 100 < i["top"] and i["bottom"] < 312
                 and (i.get("bits") or 8) > 1]   # skip 1-bit masks = rasterised text
        if not tiles:
            return None
        i = {"x0": min(t["x0"] for t in tiles), "top": min(t["top"] for t in tiles),
             "x1": max(t["x1"] for t in tiles), "bottom": max(t["bottom"] for t in tiles)}
    else:
        i = max(imgs, key=lambda i: (i["x1"]-i["x0"]) * (i["bottom"]-i["top"]))
    p = IMG / f"{slug}.webp"
    page.crop((i["x0"], i["top"], i["x1"], i["bottom"])).to_image(resolution=200).original.save(p, quality=85)
    return f"assets/products/{p.name}"

def main():
    pdf = pdfplumber.open(SRC)
    IMG.mkdir(parents=True, exist_ok=True)
    products, themes = [], []
    for tslug, ttitle, a, b in THEMES:
        theme = {"slug": tslug, "title": ttitle, "intro": "", "products": []}
        pn = a - 1
        def title_of(page):
            L = lines_in(page, 0, 612)
            t = [l["text"] for l in L if l["size"] >= 18 and l["top"] < 70]
            n = fix(t[0]) if t else None
            return NAME_OVERRIDES.get(n, n), L
        while pn < b:
            page = pdf.pages[pn]
            name, L = title_of(page)
            if not name or not any(l["text"].strip() == "Overview" for l in L):
                prose = [l["text"] for l in L if l["size"] <= 16 and l["top"] > 100]
                if prose and not theme["intro"]:
                    full = fix(" ".join(prose))
                    theme["intro"] = full.split("These datasets include")[0].strip()
                    theme["_list"] = full.split("These datasets include", 1)[-1]
                pn += 1
                continue
            pages = [pn]
            while pn + len(pages) < b and title_of(pdf.pages[pn + len(pages)])[0] == name:
                pages.append(pn + len(pages))
            slug = slugify(name)
            secs = {}
            for i, q in enumerate(pages):
                for k, v in sections(lines_in(pdf.pages[q], 0, 405 if i == 0 else 612)).items():
                    k = k.split("  ")[0]
                    secs.setdefault(k, []).extend(v)
            side = sections(lines_in(page, 405, 612))
            lk = sum((links(pdf.pages[q]) for q in pages), [])
            def find(pred):
                return next((u for u, *_ in lk if pred(u)), None)
            rec = {
                "name": name, "slug": slug, "theme": tslug,
                "portfolio_pages": [q + 1 for q in pages],
                "overview": to_items(secs.get("Overview", [])),
                "benefits": to_items(secs.get("Product benefits", [])),
                "features": to_items(secs.get("Key features", [])),
                "licencing": lic_blocks(side.get("Licencing", [])),
                "target_markets": to_items(secs.get("Target markets", [])),
                "challenges": to_items(secs.get("Challenges faced by customers", [])),
                "use_cases": to_items(secs.get("Use cases", [])),
                "links": {
                    "web_page": find(lambda u: "bgs.ac.uk" in u and "download" not in u and "licensing" not in u and not u.startswith("mailto")),
                    "user_guide_source": find(lambda u: "download" in u or u.lower().endswith(".pdf")),
                    "enquiry": find(lambda u: u.startswith("mailto")),
                    "resellers": find(lambda u: "resellers" in u),
                },
                "image": extract_image(page, pn, slug),
            }
            products.append(rec)
            theme["products"].append(slug)
            pn += len(pages)
        lst = theme.pop("_list", "")
        names = [(p["slug"], p["name"]) for p in products if p["theme"] == tslug]
        theme["taglines"] = {}
        for i, (sl, nm) in enumerate(names):
            key = nm.replace("®", "")
            src = lst.replace("®", "")
            a0 = src.find(key)
            if a0 < 0:
                continue
            nxt = [src.find(n.replace("®", ""), a0 + len(key)) for _, n in names[i+1:]]
            nxt = [x for x in nxt if x > 0]
            theme["taglines"][sl] = src[a0 + len(key): min(nxt) if nxt else None].strip(" :.;")
        themes.append(theme)
    OUT.mkdir(parents=True, exist_ok=True)
    for p in products:
        (OUT / f"{p['slug']}.yml").write_text(yaml.safe_dump(p, sort_keys=False, allow_unicode=True, width=100))
    (OUT.parent / "themes.yml").write_text(yaml.safe_dump(themes, sort_keys=False, allow_unicode=True, width=100))
    print(len(products), "products")
    for p in products:
        miss = [k for k in ("overview","benefits","features","target_markets","challenges","use_cases") if not p[k]]
        print(f"{p['portfolio_pages']} {p['slug']:45} img={'y' if p['image'] else 'N'} miss={miss} guide={bool(p['links']['user_guide_source'])}")
main()
