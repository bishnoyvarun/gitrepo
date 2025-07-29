#!/bin/bash
cd /home/vakky/docker_image/
echo "**** Pulling Apache Image from Docker Hub ****"
docker pull bishnoyvarun/apache

echo "*** check running Containers***"
docker ps -a

echo "*** run the container***"
docker run -itd -p 8080:80 bishnoyvarun/apache

echo "*** adding docker volume ***"
docker volume create my_vol

echo "*** run the container using my_vol***"
