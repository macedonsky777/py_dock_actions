FROM ubuntu:latest

RUN apt update && apt install python3 python3-pip -y
RUN pip3 install --upgrade pip
RUN pip3 install mysql-connector-python pymysql

RUN mkdir /work
COPY src /work

WORKDIR /work
ENTRYPOINT ["python3" "main.py"]
