# using python image slim version
FROM python:3.9

RUN apt-get update && apt-get install -y \
    redis-server

# making directory 
RUN mkdir -p /app

# marking it as working dir
WORKDIR /app

# copy requiremnt.txt from project dir to working dir
COPY requirements.txt ./

# installing project python dependencies
RUN pip install -r requirements.txt

# copy whole project files in working dir
COPY . .

# exposing container port
EXPOSE $PORT

# final command to start this backend container service on localhost port 8000
CMD redis-server & python manage.py runserver 0.0.0.0:8000