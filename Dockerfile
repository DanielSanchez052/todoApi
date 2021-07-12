FROM python:3.8.3

#set environment variables
ENV PYTHONUNBUFFERED=1
ENV PUTHONDONTWRITEBYTECODE=1

#set work directory
WORKDIR /code

#insall dependencies
RUN pip install --upgrade pip
COPY requirements.txt /code/
RUN pip install -r requirements.txt

#copy project
COPY . /code/
