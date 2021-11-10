FROM alpine:3.13

RUN apk update
RUN apk add curl php7-fpm php7-mcrypt php7-soap php7-openssl php7-gmp php7-pdo_odbc php7-json php7-dom php7-pdo php7-zip php7-mysqli php7-sqlite3 php7-apcu php7-pdo_pgsql php7-bcmath php7-gd php7-odbc php7-pdo_mysql php7-pdo_sqlite php7-gettext php7-xmlreader php7-xmlrpc php7-bz2 php7-iconv php7-pdo_dblib php7-curl php7-ctype php7-session php7-mbstring

RUN curl https://wordpress.org/latest.tar.gz -s -o latest.tar.gz
RUN tar xf latest.tar.gz
RUN rm latest.tar.gz
RUN mv wordpress www
COPY wp-config.php /www/

RUN curl https://raw.githubusercontent.com/rhubarbgroup/redis-cache/2.0.21/includes/object-cache.php -s -o /www/wp-content/object-cache.php
RUN curl -L https://github.com/rhubarbgroup/redis-cache/archive/refs/tags/2.0.21.tar.gz -s -o redis-cache.tar.gz
RUN tar xf redis-cache.tar.gz
RUN mkdir -p /www/wp-content/plugins/redis-cache
RUN mv /redis-cache-2.0.21/* /www/wp-content/plugins/redis-cache/
RUN rm -rf /redis-cache-2.0.21
RUN rm redis-cache.tar.gz

RUN sed -e 's/listen\s*=\s*127.0.0.1:9000/listen = [::]:9000/g' -i /etc/php7/php-fpm.d/www.conf

COPY start.sh /
RUN chmod +x start.sh

VOLUME ["/wordpress"]

EXPOSE 9000

CMD ["./start.sh"]
