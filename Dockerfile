FROM tiangolo/uwsgi-nginx-flask:python3.9-2023-07-24

WORKDIR /app

COPY . /app

ENV NAME=CAIO

ENV PORT=80

RUN pip install -r requirements.txt

EXPOSE 80