# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster



RUN apt-get update && apt-get -y install
RUN pip install --upgrade pip

RUN apt install -y build-essential

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

RUN apt install -y graphviz xdg-utils

RUN apt-get install -y lynx

RUN apt-get update \
  && apt-get install -y --no-install-recommends graphviz \
  && rm -rf /var/lib/apt/lists/* \
  && pip install --no-cache-dir pyparsing pydot

COPY dfg.py /app

VOLUME ["/dfg"]

ENTRYPOINT [ "python3", "dfg.py"]