FROM python:3.9-slim-buster AS base

LABEL maintainer Udayan Manna <udayan.m@deductiveclouds.com>

ENV PYTHONUNBUFFERED=1

WORKDIR /code

RUN mkdir -p /usr/share/man/man1 /usr/share/man/man7 &&\
    apt-get update &&\
    apt-get install --yes --no-install-recommends \
    libpq-dev \
    gcc \
    file \
    make \
    libc-dev &&\
    rm -rf /var/lib/apt/* &&\
    apt-get clean

ADD ./requirements/base.txt /tmp
RUN pip3 install --no-cache-dir --upgrade pip &&\
    pip3 install --no-cache-dir -r /tmp/base.txt

EXPOSE 7000

FROM base AS dev

ADD ./requirements/dev.txt /tmp
RUN pip3 install --no-cache-dir -r /tmp/dev.txt

FROM dev as test

COPY ./ ./

FROM base AS dist

COPY ./ ./