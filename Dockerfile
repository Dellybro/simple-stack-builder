FROM ubuntu:18.04

COPY . /app

WORKDIR /app

RUN apt-get update

RUN apt-get install curl -y

RUN curl -sL https://deb.nodesource.com/setup_11.x  | bash -

RUN apt-get -y install nodejs

RUN npm i -g recursive-install

RUN apt-get install python-pip -y

RUN pip install cfn-tools

RUN pip install cfn_flip

RUN pip install awscli

RUN pip install .
