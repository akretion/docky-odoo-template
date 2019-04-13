FROM camptocamp/odoo-project:9.0-3.1.2

RUN DEBIAN_FRONTEND=noninteractive && \
    apt-get update && \
    apt-get install -y git vim && \
    apt-get clean

COPY ./src /odoo/src
RUN pip install -e /odoo/src

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


ENV LIST_DB=True
ENV DEMO=True
ENV LIMIT_TIME_CPU=60000
ENV LIMIT_TIME_REAL=120000
ENV ADDONS_PATH=/odoo/local-src,/odoo/src/addons,/odoo/links,/odoo/external-src/server-tools
