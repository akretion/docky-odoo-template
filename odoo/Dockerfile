# https://hub.docker.com/r/camptocamp/odoo-project
FROM quay.io/akretion/odoo-prebuild:12.0-20190915

RUN apt-get update \
    && apt-get install -y --no-install-recommends vim wget git

COPY ./requirements.txt /odoo/requirements.txt
RUN pip install -r /odoo/requirements.txt

COPY ./external-src /odoo/external-src
COPY ./local-src /odoo/local-src
COPY ./VERSION /odoo/VERSION
COPY ./setup.py /odoo/setup.py
COPY ./songs /odoo/songs
COPY ./migration.yml /odoo/migration.yml
COPY ./links /odoo/links

RUN pip install -e /odoo
