sudo rm -rf ~/data
docker rm $(docker ps -a -q) 2>/dev/null
docker rmi $(docker images -q) 2>/dev/null
docker volume rm $(docker volume ls -q) 2>/dev/null
docker system prune -a --volumes
