# syntax=docker/dockerfile:1
ARG PYTHON_VERSION
FROM python:${PYTHON_VERSION}
RUN apt-get update && apt-get install -y libgl1-mesa-glx
WORKDIR /app
COPY . /app