FROM python:3.10.12-slim

RUN ["apt-get", "update"]
RUN ["apt-get", "install", "-y", "vim"]

COPY ./requirements.pip ./
RUN pip install -r ./requirements.pip

COPY ./.env ./

COPY src/entry_point.sh /start-django
RUN chmod +x /start-django

COPY ./src /src

WORKDIR /src
