FROM python:3.6.6
LABEL maintainer="CHUNGOBA"

ADD . /app
WORKDIR /app

RUN pip install -r requirements.txt

CMD ["uwsgi", "uwsgi.ini"]