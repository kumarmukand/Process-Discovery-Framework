# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY heuristic_miner.py /app

VOLUME ["/heuristic_miner"]

ENTRYPOINT [ "python3", "heuristic_miner.py"]