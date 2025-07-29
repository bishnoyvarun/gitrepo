#!/bin/bash
cd /home/vakky/docker_image/
"**** Pulling Apache Image from Docker Hub ****"
docker pull bishnoyvarun/apache

"*** check running Containers***"
docker ps -a

"*** run the container***"
docker run -itd -p 8080:80 apache
