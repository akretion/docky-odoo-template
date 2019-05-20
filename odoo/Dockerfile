FROM camptocamp/odoo-project:12.0-3.1.2-batteries

RUN DEBIAN_FRONTEND=noninteractive && \
    apt-get update && \
    apt-get install --no-install-recommends vim wget -y git && \
    apt-get clean

COPY . /odoo
RUN pip install -r /odoo/requirements.txt
RUN pip install -e /odoo
RUN pip install -e /odoo/src


ENV LIST_DB=True
#ENV DEMO=False
ENV LIMIT_TIME_CPU=60000
ENV LIMIT_TIME_REAL=120000
ENV ADDONS_PATH=/odoo/local-src,/odoo/src/addons,/odoo/links,/odoo/external-src/server-tools
