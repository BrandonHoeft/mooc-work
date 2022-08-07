# Dockerfile to build my-simple-flask-webapp image

# Hack: Do a manual creation of your docker image steps. This will capture the process of what you need your image to do.
        #docker run -it ubuntu bash
        #this way, as soon as the image starts as a container, it attaches my user input and terminal to this container. Options
            #i: keeps me in interactively connected to container by listening for my standard input
            #t: basically makes the container start look like a terminal connection session

        # use this container shell's history command to grab the steps that led to a successful process
        # package up the right commands into a docker image Dockerfile (below result)

# example: follows https://github.com/mmumshad/simple-webapp-flask
FROM ubuntu

RUN apt-get update
RUN apt-get install -y python3
RUN apt-get install -y python3-pip
RUN pip install flask

COPY app.py /opt/app.py

ENTRYPOINT FLASK_APP=/opt/app.py flask run --host=0.0.0.0


# How to build this:
# cd into folder where this file and app.py are
# > docker build . -t my-simple-flask-webapp

# How to run this: map my local port 8080 to internal container port 5000
# > docker run -p 8080:5000 my-simple-flask-webapp
# go to http://<MYLOCALIP>:8080                           => Welcome
      # http://<MYLOCALIP>:8080/how%20are%20you           => I am good, how about you?


