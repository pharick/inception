#!/bin/sh

sed -i "s/wordpress_pass/$MYSQL_WORDPRESS_PASSWORD/g" /www/wp-config.php
php-fpm7 -F -R
