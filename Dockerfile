FROM ubuntu:20.04

LABEL maintainer="Iceship"
USER root

# change the locale to suppport unicode characters
ENV LC_ALL=en_US.UTF-8
ENV LANG=en_US.UTF-8
ENV PYTHONIOENCODING=UTF-8

# install python and related dependencies
RUN apt update -y
RUN apt upgrade -y

RUN apt install -y git vim
RUN apt install -y wget curl
RUN apt install -y language-pack-en
RUN DEBIAN_FRONTEND=noninteractive apt install -y unzip openjdk-8-jre-headless xvfb libxi6 libgconf-2-4
RUN apt install -y python3 python3-pip python3-scipy
RUN apt install -y mysql-client mysql-server libmysqlclient-dev

### The following lines are adapted from: https://nander.cc/using-selenium-within-a-docker-container
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
RUN apt-get -y update
RUN apt-get install -y google-chrome-stable
RUN apt-get install -yqq unzip
RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/` \
    curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE \
    `/chromedriver_linux64.zip
RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/
ENV DISPLAY=:99

RUN mkdir /nonexistent
COPY encar.sql ./
RUN /etc/init.d/mysql start && mysql < encar.sql

WORKDIR /usr/src/app
COPY requirements.txt ./
RUN python3 -m pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["./run.sh"]
