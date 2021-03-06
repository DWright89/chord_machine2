FROM python:3.9

ENV PIP_DISABLE_PIP_VERSION_CHECK=on \
    POETRY_VIRTUALENVS_CREATE=false \
    PIP_NO_CACHE_DIR=off \
    POETRY_VERSION=1.1.12

WORKDIR /src

COPY pyproject.toml poetry.lock /src/

RUN pip install "poetry==$POETRY_VERSION" && poetry install --no-dev

# last to prevent layer conflicts when changing code
COPY ./migrations /src/migrations
COPY ./scripts /src/scripts
COPY ./src /src/
