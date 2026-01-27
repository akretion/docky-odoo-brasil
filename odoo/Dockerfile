FROM python:3.12.12-slim-trixie AS base
LABEL org.opencontainers.image.authors="magno.costa@akretion.com.br"

ENV BUILD_PACKAGE="\
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
        libcairo2-dev"

RUN --mount=type=cache,target=/var/cache/apt,sharing=locked \
  --mount=type=cache,target=/var/lib/apt,sharing=locked \
    apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends $BUILD_PACKAGE

RUN --mount=type=cache,target=/root/.npm npm install -g rtlcss

# User Odoo, check the ID of user with "$ id", if not 1000 change the value below
RUN set -eux; \
        groupadd odoo && useradd -u 1000 odoo -g odoo -m \
        && mkdir /home/odoo/app \
        && mkdir -p /odoo /var/log/odoo && chown -R odoo:odoo /var/log/odoo/ \
        ;

WORKDIR /home/odoo/

COPY ./templates/odoo.cfg /home/odoo/.odoorc

# Avoid 
# => => # WARNING: Running pip as the 'root' user  
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN --mount=type=cache,target=/root/.cache/pip \
        pip install --no-cache-dir --upgrade pip \
        setuptools \
        PyYAML \
        cython \
        python-ldap \
        psycopg2-binary \
        lxml \
        lxml-html-clean

# Install Odoo
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install --no-cache-dir -U git+https://github.com/oca/ocb@16.0 \
    --ignore-installed \
    && pip install werkzeug==3.0.0 freezegun
        
RUN chown -R odoo:odoo /home/odoo

FROM base AS base_wkhtmltopdf

# Install Wkhtmltopdf
RUN --mount=type=cache,target=/var/cache/apt,sharing=locked \
    --mount=type=cache,target=/var/lib/apt,sharing=locked \
    apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends curl wget fontconfig xfonts-75dpi xfonts-base \
    && wget --progress=dot:giga https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6.1-3/wkhtmltox_0.12.6.1-3.bookworm_amd64.deb \
    && dpkg -i wkhtmltox_0.12.6.1-3.bookworm_amd64.deb \
    && rm -rf /var/lib/apt/lists/*

FROM base_wkhtmltopdf AS base_specific_python_libs

# swig https://github.com/erpbrasil/erpbrasil.assinatura
RUN --mount=type=cache,target=/var/cache/apt,sharing=locked \
    --mount=type=cache,target=/var/lib/apt,sharing=locked \
    apt-get update \
    && apt-get install -y --no-install-recommends swig

# Install requirements
RUN --mount=type=bind,source=./requirements.txt,target=/tmp/requirements.txt \
    pip install --no-cache-dir --requirement /tmp/requirements.txt

FROM base_specific_python_libs AS dev
