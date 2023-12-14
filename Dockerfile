FROM ubuntu:22.04

RUN apt update && apt install python3 pip3 -y
RUN pip3 install --upgrade pip
RUN pip3 install mysql-connector-python

RUN mkdir /work
COPY src /work

WORKDIR /work
ENTRYPOINT ['python3' 'main.py']
