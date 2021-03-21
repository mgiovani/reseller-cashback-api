FROM python:3.9.0-slim-buster

RUN pip install poetry

WORKDIR /app
COPY pyproject.toml poetry.lock /app/
RUN poetry config virtualenvs.create false && poetry install --no-dev

ADD . /app/

EXPOSE 8000

ENTRYPOINT ["poetry", "run", "gunicorn", "--bind", "0.0.0.0:8000", "--chdir", "reseller_cashback_api", "reseller_cashback_api.wsgi:application"]
