#
# This file maybe used to compile js files with docker's webpack:
# $ docker build -t genius-webpack react/
# $ docker run -v `pwd`:/app -it genius-webpack webpack

FROM node:8.11.4-slim

ADD package.json /package.json
RUN npm install

VOLUME /app

WORKDIR /app/react

ENV PATH=/node_modules/.bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
CMD webpack


