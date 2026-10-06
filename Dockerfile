# syntax=docker/dockerfile:1
# Targets:
#   dev      live-reload server with the repo bind-mounted (docker compose up)
#   site     static build only
#   preview  nginx serving the static build under the GitHub Pages sub-path
#            (docker compose --profile preview up preview)

FROM python:3.12-slim AS base
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DEFAULT_TIMEOUT=30 \
    PIP_CERT=/etc/ssl/certs/ca-certificates.crt \
    REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt \
    SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt

# Corporate CA certificates (optional): docker/certs/*.crt
COPY docker/certs/ /usr/local/share/ca-certificates/
RUN apt-get update \
 && apt-get install -y --no-install-recommends ca-certificates \
 && update-ca-certificates \
 && rm -rf /var/lib/apt/lists/*

WORKDIR /docs
COPY requirements-docs.txt requirements.txt ./
RUN pip install -r requirements-docs.txt 

# Notebook runtime deps (geopandas, folium, OWSLib...) are only needed to EXECUTE
# the examples. Off by default to keep the image small and quick to build.
ARG WITH_NOTEBOOK_DEPS=false
RUN if [ "$WITH_NOTEBOOK_DEPS" = "true" ]; then pip install -r requirements.txt; fi

FROM base AS dev
EXPOSE 8000
CMD ["python", "scripts/dev_server.py", "--addr", "0.0.0.0:8000"]

FROM base AS site
COPY . .
RUN python scripts/build_products.py \
 && python scripts/convert_notebooks.py \
 && zensical build --clean \
 && python scripts/check_links.py site

FROM nginx:1.27-alpine AS preview
COPY docker/nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=site /docs/site /usr/share/nginx/html/BGS-API-Documentation
EXPOSE 80
