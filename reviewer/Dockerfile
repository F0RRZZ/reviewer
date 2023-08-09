FROM python:3.11-alpine

ENV PYTHONUNBUFFERED=1

WORKDIR /code
COPY requirements/prod.txt /code/
RUN pip install -r prod.txt
COPY . /code/
COPY .env.docker /code/.env