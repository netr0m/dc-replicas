FROM nginx:latest AS base

COPY ./nginx.conf /etc/nginx/nginx.conf

COPY ./proxy.conf /etc/nginx/config/proxy.conf

RUN rm /etc/nginx/conf.d/default.conf

COPY server.conf /etc/nginx/sites-enabled/server.conf
