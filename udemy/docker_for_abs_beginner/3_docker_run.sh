# `docker run` reference: https://docs.docker.com/engine/reference/run/

# to run a specific version of a docker image, use tags
docker run redis:5.0.5

# STDIN
# `docker run` does not listen to standard input by default. by default, runs in a non-interactive mode
# even though you're attached it a docker console, it doesn't have a terminal to read your input from by default

# run container in interactive mode when I want to pass input to the process
# example: have container print hello to me, then exit
docker run -i centos echo 'hello brandon'

# interactive mode + attach a terminal. after container built, I will be inside the container with a python prompt up!
# -t option: attaches me to the container's terminal so I can interact
# https://stackoverflow.com/questions/30137135/confused-about-docker-t-option-to-allocate-a-pseudo-tty
docker run -it python:3.7-alpine

# PORT MAPPING -p flag
# how to map the container's internal IP address and ports to the external host and a free host port
# purpose: enables external traffic to communicate with the app running on my docker container

# -p [free external port]:[port inside docker container]
# -p 8306:3306 maps port 8306 of the local computer (outside of docker host) to the internal mySQL container port 3306
# on the local docker host I am running MySQL database instance with its default port is 3306.
# this can be mapped to an external port 8306 (for benefit of an external user outside of the docker host environment) or any other open port
# you get 1 port mapping for 1 instance of a docker container
docker run -p 8306:3306 mysql


# VOLUME MAPPING
# how data is persisted in a docker container. we want to map that data to a file storage outside of the docker host that the mysql container operates in.

# example with docker run mysql
# this db runs in a container, has its own mysql file storage system isolated inside the container.
# any changes to data in the database happen only inside the container. when the mysql container is stopped, all that data is lost with it.
# we should manage that so that the database data is not lost when the mysql container process exits or fails
# -v [external storage dir]:[internal storage dir in the container]
docker run -v /opt/datadir:/var/lib/mysql mysql

# see the details of a container in a JSON format
docker inspect 281a76b5b01a

# get logs output of a container
docker logs 281a76b5b01a
