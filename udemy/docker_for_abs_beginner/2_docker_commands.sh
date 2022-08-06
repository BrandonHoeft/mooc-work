# images and containers
# image = package or template to create a template. images can be hosted for others to use on docker hub
# containers = instances of a particular image


# create a new container from existing centos docker image
# this container will exit immediately b/c there's no process running
docker run centos bash

# run centos interactively from a terminal with a bash shell
# if I run the -i and -t flags, I will be inside the container and a bash prompt will be up!
docker run -it centos bash

# list images downloaded
docker images

# show list of running containers
docker ps

# show list of running and previously running (not yet deleted) containers
docker ps -a

# d option is to run the container process in the background, so you can return to your main terminal
docker run -d

# stop a running <unique name of container>
docker stop #serene_pete

# reclaim disk space of dead containers. pass name of partial id of the container
docker rm 123123
docker rm serene_pete

# remove images from disk
# can't remove an image if you have running or stopped containers using that image
docker rmi python:3.9-slim-buster

# remove all images in a one liner using a command expansion
docker rmi $(docker images -aq)

# pull an image from a repo like dockerhub. downloads the image into your environment, without running it
docker pull 3.9-slim-buster

# run ubuntu with sleep process for 100 seconds in the background.
docker run -d ubuntu sleep 100

# while running in the background still, send a command to see the OS release notes. pretend above container ID was: ack23lkwdaf0
docker exec ack23lkwdaf0 cat /etc/*release*
