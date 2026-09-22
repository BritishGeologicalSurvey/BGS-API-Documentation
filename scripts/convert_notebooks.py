"""Render notebooks/*.ipynb to docs/examples/*.md.

    python scripts/convert_notebooks.py            # use stored outputs
    python scripts/convert_notebooks.py --execute  # re-run against the live APIs first (CI)

Notebooks are committed WITHOUT outputs (see .pre-commit-config.yaml / nbstripout);
CI executes them, so the rendered pages always reflect the current API.
Very large HTML outputs (e.g. folium maps) are replaced with a link to nbviewer,
because they bloat the page and don't survive Markdown conversion well.
"""
import pathlib
import sys

import nbformat
from nbconvert import MarkdownExporter
from nbconvert.preprocessors import ExecutePreprocessor

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "notebooks"
OUT = ROOT / "docs" / "examples"
NBVIEWER = "https://nbviewer.org/github/BritishGeologicalSurvey/BGS-API-Documentation/blob/main/notebooks/"
MAX_HTML = 150_000  # bytes


def slim(nb, name):
    for cell in nb.cells:
        if cell.cell_type != "code":
            continue
        kept = []
        for out in cell.get("outputs", []):
            data = out.get("data", {})
            size = lambda v: len("".join(v) if isinstance(v, list) else v)
            if data.get("text/plain") and size(data["text/plain"]) > MAX_HTML and not data.get("text/html"):
                out = nbformat.v4.new_output("display_data", data={
                    "text/markdown": f"*Large text output truncated: [view it on nbviewer]({NBVIEWER}{name}).*"})
            html = out.get("data", {}).get("text/html")
            if html and size(html) > MAX_HTML:
                out = nbformat.v4.new_output("display_data", data={
                    "text/markdown": f"*Interactive map output omitted: [view it on nbviewer]({NBVIEWER}{name}).*"})
            kept.append(out)
        cell["outputs"] = kept
    return nb


def main(execute: bool):
    OUT.mkdir(parents=True, exist_ok=True)
    exporter = MarkdownExporter()
    for path in sorted(SRC.glob("*.ipynb")):
        nb = nbformat.read(path, as_version=4)
        if execute:
            ExecutePreprocessor(timeout=600, kernel_name="python3").preprocess(nb, {"metadata": {"path": str(SRC)}})
        nb = slim(nb, path.name)
        body, res = exporter.from_notebook_node(nb, resources={"output_files_dir": f"{path.stem}_files"})
        header = (f"<!-- GENERATED from notebooks/{path.name} by scripts/convert_notebooks.py -->\n\n"
                  f"[Download notebook](https://github.com/BritishGeologicalSurvey/BGS-API-Documentation/raw/main/notebooks/{path.name}){{ .md-button }}\n\n")
        (OUT / f"{path.stem}.md").write_text(header + body)
        for fname, data in res.get("outputs", {}).items():
            f = OUT / fname
            f.parent.mkdir(parents=True, exist_ok=True)
            f.write_bytes(data)
        print(f"{path.name}: {len(body)//1024} KB, {len(res.get('outputs', {}))} files")


if __name__ == "__main__":
    main("--execute" in sys.argv)
