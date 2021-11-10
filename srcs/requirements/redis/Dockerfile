FROM alpine:3.13

RUN apk update
RUN apk add redis

COPY redis.conf /etc/

EXPOSE 6379

VOLUME ["/data"]

CMD ["redis-server", "/etc/redis.conf"]
