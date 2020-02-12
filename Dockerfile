# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:3.6

# The environment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

# create root directory for our project in the container
RUN mkdir /cloud

# Set the working directory to /fumcloud_api
WORKDIR /cloud

# Copy the current directory contents into the container at /fumcloud_api
ADD . /cloud

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# https://github.com/vishnubob/wait-for-it/blob/master/wait-for-it.sh
#RUN mv wait-for-it.sh /bin/wait-for-it

RUN mv run_server.sh /usr/local/bin/run_server.sh
RUN chmod 755 /usr/local/bin/run_server.sh
RUN chmod +x /usr/local/bin/run_server.sh
