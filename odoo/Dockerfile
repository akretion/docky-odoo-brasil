FROM python:3.11.12-alpine3.21 AS base
LABEL org.opencontainers.image.authors="magno.costa@akretion.com"

ENV BUILD_PACKAGE \
        build-base \
        libffi-dev \
        git \
        git-lfs \
        gpg \
        less \
        openssh \
        patch \
        bash \
        libxml2 \
        libxslt-dev \
        libpq-dev \
        python3-dev \
        jpeg-dev \
        zlib-dev \
        freetype-dev \
        lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev \
        openldap-dev \
        postgresql-client \
        npm \
        libxml2-dev \
        libxslt-dev \
        cython \
        cmake \
        cairo \
        cairo-dev \
        swig

RUN set -eux; \
        apk update && \
        apk upgrade && \
        apk fix && \
        apk --no-cache --update add $BUILD_PACKAGE &&\
        git lfs install \
        ;
RUN npm install -g rtlcss \
    && rm -Rf ~/.npm /tmp/*

RUN echo 'INPUT ( libldap.so )' > /usr/lib/libldap_r.so

RUN set -eux; \
        apk add gosu --update-cache --repository https://dl-cdn.alpinelinux.org/alpine/edge/testing/ --allow-untrusted \
        ;

RUN set -eux; \
        rm -rf /var/cache/apk/* \
        ;

# User Odoo, check the ID of user with "$ id", if not 1000 change the value below
RUN addgroup odoo \
    && adduser -G odoo -u 1000 odoo -D

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

RUN --mount=type=cache,target=/root/.cache pip install -r requirements.txt --no-cache-dir --ignore-installed

RUN --mount=type=cache,target=/root/.cache \
    pip install -U git+https://github.com/oca/ocb@16.0 \
    --no-cache-dir --ignore-installed

RUN set -aux; \
        pip install \
        werkzeug==3.0.0 \
        freezegun \
        ;

# add wkhtmltopdf
COPY --from=ghcr.io/surnet/alpine-wkhtmltopdf:3.12-0.12.6-full /bin/wkhtmltopdf /bin/wkhtmltopdf
COPY --from=ghcr.io/surnet/alpine-wkhtmltopdf:3.12-0.12.6-full /bin/wkhtmltoimage /bin/wkhtmltoimage
COPY --from=ghcr.io/surnet/alpine-wkhtmltopdf:3.12-0.12.6-full /bin/libwkhtmltox.so /bin/libwkhtmltox.so
COPY --from=ghcr.io/surnet/alpine-wkhtmltopdf:3.12-0.12.6-full /bin/libwkhtmltox.so.0 /bin/libwkhtmltox.so.0
COPY --from=ghcr.io/surnet/alpine-wkhtmltopdf:3.12-0.12.6-full /bin/libwkhtmltox.so.0.12 /bin/libwkhtmltox.so.0.12
COPY --from=ghcr.io/surnet/alpine-wkhtmltopdf:3.12-0.12.6-full /bin/libwkhtmltox.so.0.12.6 /bin/libwkhtmltox.so.0.12.6
COPY --from=ghcr.io/surnet/alpine-wkhtmltopdf:3.12-0.12.6-full /lib/libssl.so.1.1 /lib/libssl.so.1.1
COPY --from=ghcr.io/surnet/alpine-wkhtmltopdf:3.12-0.12.6-full /lib/libcrypto.so.1.1 /lib/libcrypto.so.1.1
COPY --from=ghcr.io/surnet/alpine-wkhtmltopdf:3.12-0.12.6-full /usr/share/fonts /usr/share/fonts

RUN set -eux; \
        rm -rf /tmp/* \
        ;

RUN chown -R odoo:odoo /home/odoo/

FROM base AS prod

FROM base AS dev
