# Use Python as the base image
FROM python:3.12-slim

WORKDIR /app

# Install required system libraries (for Selenium)
RUN apt-get update && apt-get install -y \
    curl \
    unzip \
    && rm -rf /var/lib/apt/lists/*

ENV PIP_ROOT_USER_ACTION=ignore

RUN pip install pipenv
RUN bash
