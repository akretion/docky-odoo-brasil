# https://hub.docker.com/r/camptocamp/odoo-project
FROM camptocamp/odoo-project:12.0-buster-latest

RUN apt-get update \
    && apt-get install -y --no-install-recommends vim wget libxmlsec1-dev build-essential python3-dev git locales libreoffice

RUN apt-get install swig3.0
RUN ln -s /usr/bin/swig3.0 /usr/bin/swig

RUN pip install --upgrade pip

RUN sed -i -e 's/# pt_BR.UTF-8 UTF-8/pt_BR.UTF-8 UTF-8/' /etc/locale.gen \
    && dpkg-reconfigure --frontend=noninteractive locales \
    && update-locale LANG=pt_BR.UTF-8

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
COPY ./templates /templates
