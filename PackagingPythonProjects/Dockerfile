ARG BASE_IMAGE=python:3.11

FROM ${BASE_IMAGE} as base

LABEL maintainer='timur <dev@tpitsuev.com>'

WORKDIR /opt

ENV PYTHONUNBUFFERED TRUE

COPY src/tg_bot.py src/
COPY src/config.py src/
COPY requirements.dev .
COPY requirements.prod .


# Install python dependencies
RUN pip install --upgrade pip \
    && pip install --no-cache-dir wheel -r requirements.dev -r requirements.prod \
    && pip list \
    && rm -rf /root/.cache/pip

ENTRYPOINT ["python", "src/tg_bot.py"]