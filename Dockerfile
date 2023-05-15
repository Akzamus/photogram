FROM python:3.10-alpine

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt .

RUN pip install --no-cache --upgrade pip \
 && pip install --no-cache -r requirements.txt

COPY . .

EXPOSE 8000
