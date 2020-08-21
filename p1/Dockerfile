FROM python:3

ENV PYTHONUNBUFFERRED 1

WORKDIR /chanapp

ADD . /chanapp

COPY ./requirements.txt /chanapp/requirements.txt

RUN pip install -r requirements.txt

COPY . /chanapp
