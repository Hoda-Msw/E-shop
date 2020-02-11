# ./E-shop/Dockerfile
FROM python:2.7.17

# set work directory
WORKDIR /E-shop/manage.py

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /opt/app/requirements.txt 
RUN chmod +x /opt/app/requirements.txt
RUN pip install -r requirements.txt

# copy project
COPY . /E-shop/manage.py
