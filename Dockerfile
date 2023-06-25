FROM python:3.8

RUN mkdir /tests
WORKDIR /tests

RUN apt-get update && apt-get install -y git software-properties-common
RUN apt-get update

COPY . /tests
RUN pip install --upgrade setuptools
RUN python -m pip install --no-cache-dir -r requirements.txt

CMD tail -f /dev/null