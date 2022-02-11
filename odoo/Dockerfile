FROM camptocamp/odoo-project:14.0-latest as base
RUN apt-get update \
    && apt-get install -y --no-install-recommends git \
    && apt install postgresql-client-common

COPY ./requirements.txt /odoo/requirements.txt
RUN pip install -r /odoo/requirements.txt

COPY ./VERSION /odoo/VERSION
COPY ./setup.py /odoo/setup.py
COPY ./songs /odoo/songs
COPY ./migration.yml /odoo/migration.yml
COPY ./templates /templates
COPY ./links /odoo/links

# entrypoint scripts that will run before the container starts
COPY entrypoint/002_check_pending_jobs /start-entrypoint.d/002_check_pending_jobs
COPY entrypoint/003_click_odoo_update /start-entrypoint.d/003_click_odoo_update
RUN chmod 655 /start-entrypoint.d/*

FROM base as dev

# Put here some stuff only for dev
COPY ./src/setup.py /odoo/src/setup.py
COPY ./src/setup.cfg /odoo/src/setup.cfg
COPY ./src/setup /odoo/src/setup
COPY ./src/odoo/release.py /odoo/src/odoo/release.py
COPY ./src/requirements.txt /odoo/requirements.txt
RUN pip install -e /odoo/src
RUN pip install -e /odoo

FROM base as prod

# Used by prod and ci

COPY ./external-src /odoo/external-src
COPY ./local-src /odoo/local-src
COPY ./src /odoo/src
RUN pip install -e /odoo
RUN pip install -e /odoo/src
ARG SENTRY_RELEASE
ENV SENTRY_RELEASE=${SENTRY_RELEASE}