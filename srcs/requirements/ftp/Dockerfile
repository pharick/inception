FROM alpine:3.13

RUN apk update
RUN apk add vsftpd openssl

RUN openssl req -newkey rsa:2048 -x509 -days 365 -nodes -out /etc/vsftpd/vsftpd.pem -keyout /etc/vsftpd/vsftpd.pem -subj "/C=RU/ST=Moscow/L=Moscow/O=School21/OU=cbelva/CN=inception"

RUN mkdir -p /home/vsftpd/
RUN chown -R ftp:ftp /home/vsftpd/
COPY vsftpd.conf /etc/vsftpd/
COPY start.sh /
RUN chmod +x start.sh

EXPOSE 20-21 30020-30021

CMD ["./start.sh"]
