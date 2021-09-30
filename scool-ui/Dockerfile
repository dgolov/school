FROM node:16.6.2 as build

WORKDIR /app

ENV PATH /app/node_modules/.bin:$PATH

COPY package.json /app/package.json
RUN npm install --silent
RUN npm install @vue/cli@3.7.0 -g

COPY . /app

RUN npm run build