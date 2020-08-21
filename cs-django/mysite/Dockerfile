# The first instructtion is what image we want to base our container on
# We use an official python runtime as a parent image
FROM python:3

#The environment variable ensures that the python output is set straight
# to the terminal without buffering it first
ENV PYTHONUNBUFFERED 1

# create root directory for our project in the container
RUN mkdir /polls_app

# Set the working directory to /polls_app
WORKDIR /polls_app

ADD . /polls_app
# will install all of the required packages we have inside of requirements
RUN pip install -r requirements.txt


