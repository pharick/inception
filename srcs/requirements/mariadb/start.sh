#!/bin/sh

mysql_install_db --user=root

sed -i "s/root_pass/$MYSQL_ROOT_PASSWORD/g" init_file
sed -i "s/wordpress_pass/$MYSQL_WORDPRESS_PASSWORD/g" init_file
sed -i "s/short_urls_pass/$MYSQL_SHORT_URLS_PASSWORD/g" init_file

mysqld --init_file=/init_file
