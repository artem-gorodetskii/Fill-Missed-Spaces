# syntax=docker/dockerfile:1

FROM python:3.7.7-slim

# Set the environment variables inside the container
ARG VERSION_FROM_GIT
ENV VERSION_FROM_GIT ${VERSION_FROM_GIT}

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt \
    && rm -rf /root/.cache/pip

COPY . /app/
WORKDIR /app

EXPOSE 5100
CMD [ "flask", "run","--host","0.0.0.0","--port","5100"]
