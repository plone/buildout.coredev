FROM python:3.12-slim-bullseye

# Dev dependencies
RUN apt-get update \
  && apt-get install -y build-essential git libmagic1 libbz2-dev libjpeg62-turbo-dev zlib1g-dev --no-install-recommends \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
