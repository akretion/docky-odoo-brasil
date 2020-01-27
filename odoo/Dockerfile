FROM camptocamp/odoo-project:12.0-3.1.2-batteries

RUN apt-get update \
    && apt-get install -y --no-install-recommends vim wget git libxmlsec1-dev build-essential python3-dev locales

RUN apt-get install swig3.0
RUN ln -s /usr/bin/swig3.0 /usr/bin/swig

RUN pip install --upgrade pip

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

COPY ./templates/odoo.cfg.tmpl /templates/odoo.cfg.tmpl

RUN sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && \
    dpkg-reconfigure --frontend=noninteractive locales && \
    update-locale LANG=en_US.UTF-8

ENV LANG en_US.UTF-8

ENV ADDONS_PATH /odoo/src/addons,/odoo/src/odoo/addons,/odoo/links,/odoo/external-src/account-payment,/odoo/external-src/bank-payment,/odoo/external-src/currency,/odoo/external-src/server-tools,/odoo/external-src/server-env,/odoo/external-src/l10n-brazil
