# reasons for creating your own docker image:
# 1. you can't find an application to your need/liking that's already containerized
# 2. improve the ease of shipping and deploying your custom application

# Thought process of building your own docker image:
# What you might need built if you want to deploy the application manually?
# Think about those steps in the correct sequential order. When Docker builds images
# it does so in a layered way, each line of instructions, creates a new layer in the
# docker image, with just the changes from previous layer. For example you need
# an operating system (e.g. Ubuntu, RHEL) before you need python software, a database, ...

# All Dockerfiles start with a FROM command to source the base image being built.
# Every Docker Image is based off of another base image!
# Example: base OS image or another *nix distribution.
FROM ubuntu

# instructs to run a command on the base image
# Example: Update the apt repo, install dependencies using apt
RUN apt-get update && apt-get -y install python
# Example: install python dependencies
RUN pip install flask flask-mysql

# Copy files from local system onto the docker image
# Example: copy current dir of src code to /opt/source-code
COPY .. /opt/source-code

# allows us to specify a command when the image is run as container
# Example: flask command
ENTRYPOINT FLASK_APP=/opt/source-code/app.py flask run