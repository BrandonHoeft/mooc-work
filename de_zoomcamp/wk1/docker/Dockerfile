# To Run this Dockerfile: a docker host can build image by:
# 1: be in directory where Dockerfile is defined
# 2. `docker build -t <new_image_name>:<tag_name> .` The `.` will build the image in current dir

# the name of the base image to use
FROM python:3.9

# command to run and any parameters of that command
RUN pip install pandas

# image location where we will copy the file to when a container builds
WORKDIR /app

# name of local source file and destination file
COPY pipeline.py pipeline.py

ENTRYPOINT [ "python", "pipeline.py" ]