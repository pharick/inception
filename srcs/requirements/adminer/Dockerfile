FROM alpine:3.13

RUN apk update
RUN apk add curl php7-fpm php7-mcrypt php7-soap php7-openssl php7-gmp php7-pdo_odbc php7-json php7-dom php7-pdo php7-zip php7-mysqli php7-sqlite3 php7-apcu php7-pdo_pgsql php7-bcmath php7-gd php7-odbc php7-pdo_mysql php7-pdo_sqlite php7-gettext php7-xmlreader php7-xmlrpc php7-bz2 php7-iconv php7-pdo_dblib php7-curl php7-ctype php7-session php7-mbstring

RUN mkdir -p /www/adminer
RUN curl -L https://github.com/vrana/adminer/releases/download/v4.8.1/adminer-4.8.1.php -s -o /www/adminer/adminer.php

RUN sed -e 's/listen\s*=\s*127.0.0.1:9000/listen = [::]:9000/g' -i /etc/php7/php-fpm.d/www.conf

EXPOSE 9000

CMD ["php-fpm7", "-F", "-R"]
