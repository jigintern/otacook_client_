FROM node:8.16.1-alpine

WORKDIR /vue

RUN apk update && \
  npm install -g npm vue-cli

ENV HOST 0.0.0.0
EXPOSE 8888

CMD ["/bin/ash"]