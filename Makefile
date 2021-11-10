start:
	mkdir -p /home/pharick/data/mariadb
	mkdir -p /home/pharick/data/wordpress
	mkdir -p /home/pharick/data/redis
	docker-compose --project-directory srcs up -d

stop:
	docker-compose --project-directory srcs down

clean:
	./clean.sh

re: stop clean start
