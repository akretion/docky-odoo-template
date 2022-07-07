FROM ghcr.io/camptocamp/odoo-project:14.0-4.4.4 as base

# syntax = docker/dockerfile:1.4

RUN --mount=type=cache,target=/var/cache/apt \
    apt-get update \
    && apt-get install -y --no-install-recommends git \
    && apt-get install -y vim po4a libpq-dev libmupdf-dev mupdf-tools mupdf python3-venv \
    && /install/dev_package.sh

COPY entrypoint/002_check_pending_jobs /start-entrypoint.d/002_check_pending_jobs
COPY entrypoint/003_click_odoo_update /start-entrypoint.d/003_click_odoo_update
RUN chmod 655 /start-entrypoint.d/*

ENV ADDONS_PATH=/odoo/src/addons,/odoo/local-src,/odoo/links

COPY .build/install/* /install/
RUN --mount=type=cache,target=/root/.cache /install/install_tool

COPY .build/repos.yaml /root/.config/git-autoshare/repos.yml
COPY .build/bin/* /odoo-bin/

FROM base as prod

# Build and install odoo
COPY odoo-spec.yaml /odoo/odoo-spec.yaml
ENV BUILD_RESTRICT_LANG=fr.po
RUN --mount=type=cache,target=/root/.cache /install/build-odoo
RUN --mount=type=cache,target=/root/.cache pip install -e /odoo/src

# Build external source
COPY spec.yaml /odoo/spec.yaml
RUN --mount=type=cache,target=/root/.cache /install/build-odoo-external
COPY ./requirements.txt /odoo/
RUN --mount=type=cache,target=/root/.cache cd /odoo && pip install -r requirements.txt

# Copy local project
COPY ./local-src /odoo/local-src
COPY ./script /odoo/script
COPY ./migration.yml /odoo/

# Note: In our case as we do not use anthem, this setup is useless
# But sadly is needed for the entrypoint so we keep it
COPY ./setup.py /odoo/setup.py

FROM base as dev

COPY ./requirements.txt /odoo/
RUN --mount=type=cache,target=/root/.cache pip install -r /odoo/requirements.txt
