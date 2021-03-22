FROM alpine:3.13

RUN apk add python3 py3-pip py3-psycopg2 uwsgi uwsgi-python3 gettext

COPY requirements_docker.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt

COPY mysite/ /app/mysite/
WORKDIR /app/mysite/

RUN python3 manage.py collectstatic
RUN python3 manage.py compilemessages

CMD uwsgi --ini uwsgi.ini
