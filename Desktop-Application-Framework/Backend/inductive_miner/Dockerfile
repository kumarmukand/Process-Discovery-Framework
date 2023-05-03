# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY inductive_miner.py /app

VOLUME ["/inductive_miner"]

ENTRYPOINT [ "python3", "inductive_miner.py"]