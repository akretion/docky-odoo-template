FROM camptocamp/odoo-project:10.0-3.1.2

RUN echo "deb [check-valid-until=no] http://archive.debian.org/debian jessie-backports main" > /etc/apt/sources.list.d/jessie-backports.list \
    && sed -i '/deb http:\/\/deb.debian.org\/debian jessie-updates main/d' /etc/apt/sources.list \
    && echo 'Acquire::Check-Valid-Until "false";' > /etc/apt/apt.conf;

RUN DEBIAN_FRONTEND=noninteractive && \
    apt-get update && \
    apt-get install -y git vim && \
    apt-get clean

COPY ./src /odoo/src
RUN pip install -e /odoo/src

RUN apt-get clean && apt-get update && apt-get install -y locales
RUN locale-gen pt_BR.UTF-8 && \
     sed -i 's/^# *\(pt_BR.UTF-8\)/\1/' /etc/locale.gen && locale-gen

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
ENV ADDONS_PATH=/odoo/local-src,/odoo/src/addons,/odoo/links,/odoo/external-src/server-tools,/odoo/external-src/web,/odoo/external-src/reporting-engine,/odoo/external-src/fiscal-rule,/odoo/external-src/l10n-brazil,/odoo/external-src/bank-payment
