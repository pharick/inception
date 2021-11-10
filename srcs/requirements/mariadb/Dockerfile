FROM alpine:3.13

RUN apk update
RUN apk add mysql mysql-client

RUN mkdir -p /run/mysqld
COPY my.cnf /etc/
COPY init_file /
COPY wordpress.sql /
COPY start.sh /
RUN chmod +x start.sh

RUN echo "USE wordpress;" >> init_file
RUN cat wordpress.sql >> init_file

VOLUME ["/var/lib/mysql"]

EXPOSE 3306

CMD ["./start.sh"]
