FROM python:3.11.12-slim-bookworm AS base
LABEL org.opencontainers.image.authors="magno.costa@akretion.com"

ENV BUILD_PACKAGE \
        build-essential \
        gcc \
        libffi-dev \
        git \
        git-lfs \
        gpg \
        less \
        openssh-client \
        patch \
        bash \
        libxml2 \
        libxslt-dev \
        libpq-dev \
        python3-dev \
        tk-dev tcl-dev \
        postgresql-client \
        npm \
        libxml2-dev \
        libxslt-dev \
        libevent-dev \
        libfreetype6-dev \
        libxml2-dev \
        libxslt1-dev \
        libsasl2-dev \
        libldap2-dev \
        libssl-dev \
        libjpeg-dev \
        libpng-dev \
        zlib1g-dev \
        gosu \
        cython3 \
        vim \
        cmake \
        libcairo2-dev \
        swig

# swig https://github.com/erpbrasil/erpbrasil.assinatura

RUN --mount=type=cache,target=/var/cache/apt \
    apt-get update \
    && apt-get install -y --no-install-recommends $BUILD_PACKAGE

RUN npm install -g rtlcss \
    && rm -Rf ~/.npm /tmp/*

RUN set -eux; \
        apt clean \
        ;

# User Odoo, check the ID of user with "$ id", if not 1000 change the value below
RUN groupadd odoo && useradd -u 1000 odoo -g odoo
COPY ./templates/odoo.cfg /home/odoo/.odoorc
RUN mkdir /home/odoo/app && chown -R odoo:users /home/odoo/app

COPY ./requirements.txt /home/odoo/requirements.txt

RUN mkdir -p /odoo /var/log/odoo && chown -R odoo:odoo /var/log/odoo/

WORKDIR /home/odoo

RUN set -aux; \
        pip install --upgrade pip \
        setuptools \
        PyYAML \
        cython \
        python-ldap \
        psycopg2-binary \
        lxml \
        lxml-html-clean \
        ;

# Install requirements
RUN --mount=type=cache,target=/root/.cache pip install -r requirements.txt --ignore-installed

# Install Odoo
RUN --mount=type=cache,target=/root/.cache \
    pip install -U git+https://github.com/oca/ocb@16.0 \
    --ignore-installed

RUN set -aux; \
        pip install \
        werkzeug==3.0.0 \
        freezegun \
        ;

RUN set -eux; \
        rm -rf /tmp/* \
        ;

RUN chown -R odoo:odoo /home/odoo/

# Install Wkhtmltopdf
RUN apt-get install -y curl wget fontconfig xfonts-75dpi xfonts-base
RUN wget https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6.1-3/wkhtmltox_0.12.6.1-3.bookworm_amd64.deb
RUN dpkg -i wkhtmltox_0.12.6.1-3.bookworm_amd64.deb

FROM base AS prod

FROM base AS dev
