FROM python:3.10-alpine

RUN python -m pip install --upgrade pip
RUN pip install poetry

# Copy in the config files:
COPY pyproject.toml pyproject.toml 
COPY poetry.lock poetry.lock

# Install only dependencies:

RUN apk update
RUN apk add postgresql-dev gcc python3-dev musl-dev

RUN poetry config virtualenvs.create false && poetry install --no-root --only main
 
# Copy in everything else and install:
COPY . .






