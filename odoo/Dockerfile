# https://hub.docker.com/r/camptocamp/odoo-project
FROM camptocamp/odoo-project:12.0-latest
COPY . /odoo
COPY templates /templates
RUN apt-get update \
    && apt-get install -y --no-install-recommends git
RUN pip install -r /odoo/requirements.txt
RUN pip install -e /odoo
RUN pip install -e /odoo/src
