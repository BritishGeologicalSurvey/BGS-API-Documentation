# BGS Data Products & APIs

Source for the BGS documentation site: the product portfolio, data product user guides, API documentation and worked examples.

Built with [Zensical](https://zensical.org). The same `mkdocs.yml` also builds with Material for MkDocs 9.7.x as a fallback.

## Quick start

```bash
pip install -r requirements-docs.txt
python scripts/build_products.py      # generates docs/products/ from data/
python scripts/convert_notebooks.py   # renders notebooks/ into docs/examples/ (add --execute to run them)
zensical serve                        # http://localhost:8000
```

Or run `python scripts/dev_server.py`, which does the generation, serves the site and regenerates the product pages whenever `data/*.yml` changes.

### With Docker

```bash
docker compose up --build                              # dev server, live reload
#   -> http://localhost:8000/BGS-API-Documentation/
docker compose --profile preview up --build preview    # static build behind nginx, like GitHub Pages
#   -> http://localhost:8080/
```

- **Behind a proxy:** set `HTTP_PROXY`, `HTTPS_PROXY` and `NO_PROXY` in your shell or a `.env` file; they're passed to the build and the container.
- **HTTPS inspection:** drop the organisation's root CA as a `.crt` file into `docker/certs/` (git-ignored). It's added to the image's trust store and used by pip.
- **Notebooks:** to execute them inside the container, build with `WITH_NOTEBOOK_DEPS=true docker compose build`, then run `docker compose run --rm docs python scripts/convert_notebooks.py --execute`.
- **Windows live reload:** file-change events from Windows bind mounts don't always reach Linux containers. Edits to `data/` are polled, so they always trigger a regeneration. If edits under `docs/` don't reload, restart the container or clone the repo inside WSL2.

`docs/products/` and `docs/examples/*.md` are generated. Don't edit them; they're git-ignored and rebuilt in CI.

## How content is organised

| What | Where | Edited by |
| --- | --- | --- |
| Portfolio products (39) | `data/portfolio/products/*.yml`, `data/portfolio/themes.yml` | Regenerated from the portfolio PDF (below), then reviewed |
| Open-data products (not in the licensed portfolio) | `data/extra/products/*.yml`, `data/extra/themes.yml`; set `licence: OGL` for the "Open data" badge | By hand |
| Hosted user guides | `data/guides.yml` + `docs/assets/guides/*.pdf` | By hand |
| API docs | `docs/apis/*.md` | By hand |
| Examples | `notebooks/*.ipynb` (committed without outputs, via nbstripout) | By hand |
| Brand | `docs/stylesheets/bgs.css`, `docs/assets/brand/`, `docs/assets/fonts/` | Rarely |

### Updating from a new portfolio

```bash
python scripts/parse_portfolio.py path/to/BGS_Product_Portfolio_YYYY_YY.pdf
git diff data/portfolio   # review every change
```

The PowerPoint export rasterises the visible text but keeps an invisible text layer, and the parser reads that layer. It's reliable for structure, but the text layer has artefacts. `NAME_OVERRIDES` in the script patches known ones, such as "shrink –s well". Also check the theme ranges in `THEMES` against the new contents page.

### User guides

Guides are embedded PDFs for now. To host another one:

1. Add the PDF to `docs/assets/guides/`.
2. Add an entry to `data/guides.yml`, with `covers:` listing any other products it documents.

`python scripts/fetch_guides.py` lists the portfolio's guide links not yet hosted here, and `--download` fetches them.

When Markdown becomes the source of truth, a guide gets a `source:` folder and its PDF becomes a build output instead of a checked-in file.

## Brand

- **Colours:** earth `#002E40` and stone `#AD9C70`. Panels (`#E5E9EB`), paper (`#ECECEC`) and rule weights were measured from the 2026–27 portfolio.
- **Typeface:** Aileron (CC0), self-hosted. This is the face embedded in the BGS logo guidelines, and it matches the portfolio's rasterised text.
- **Logo:** the Primary Reversed logo on the navy header, as vector artwork taken from the logo guidelines. It is 134 px wide against a 120 px screen minimum, with clear space of about 12 px (the height of the "BGS" letters). The logo moves into the navigation drawer on small screens, which is Material's standard behaviour.
- **Links:** brand sea `#528791`. **Accessibility:** this is 4.01:1 on white and 3.28:1 on the grey panels, below the WCAG 2.2 AA 4.5:1 required for body text under the Public Sector Bodies Accessibility Regulations. A darker sea, `#3F6B74`, passes on every surface here (4.82:1 or better). Change `--bgs-link` in `bgs.css` to switch.
- **Theme circles:** six are taken from the portfolio. `circle-offshore-geology.webp` is my composition from the OR/21/009 cover map, using the same navy diagonal device, and needs sign-off from Comms.

## Deployment

`.github/workflows/docs.yml` does the following:

- Runs on push, pull request and a weekly schedule.
- Generates the product pages, executes the notebooks against the live APIs (falling back to an un-executed render if an API is down), builds the site and checks relative links.
- Deploys to GitHub Pages from `main`.
