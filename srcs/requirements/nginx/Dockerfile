FROM alpine:3.13

RUN apk update

RUN apk add nginx openssl
RUN adduser -D -g 'www' www
RUN mkdir /www
RUN mkdir -p /run/nginx
RUN chown -R www:www /var/lib/nginx
RUN chown -R www:www /www
RUN chown -R www:www /run/nginx

COPY nginx.conf /etc/nginx/

RUN mkdir /etc/nginx/ssl
RUN openssl req -newkey rsa:4096 -x509 -sha256 -days 365 -nodes -out /etc/nginx/ssl/cert.pem -keyout /etc/nginx/ssl/cert.key -subj "/C=RU/ST=Moscow/L=Moscow/O=School21/OU=cbelva/CN=inception"

EXPOSE 443

CMD ["nginx", "-g", "daemon off;"]