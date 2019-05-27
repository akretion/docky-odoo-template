FROM camptocamp/odoo-project:12.0-3.1.2-batteries

RUN DEBIAN_FRONTEND=noninteractive && \
    apt-get update && \
    apt-get install --no-install-recommends vim wget -y git && \
    apt-get clean

COPY . /odoo
COPY etc/odoo.cfg.tmpl /etc/odoo.cfg.tmpl
RUN pip install -r /odoo/requirements.txt
RUN pip install -e /odoo
RUN pip install -e /odoo/src

CMD ["odoo"]

