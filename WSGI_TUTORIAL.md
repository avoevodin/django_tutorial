# Tutorial for wsgi apps

## Apache Benchmark:
* Run ab in 10 threads for 1000 iterations
```shell
ab -c 10 -n 1000 http://127.0.0.1:8000/polls/
```
## gunicorn 
>It's not recommended using in production
* Install gunicorn
```shell
pip3 install gunicorn
```
* Run server with gunicorn, then test it with ab.
```shell
gunicorn --workers=8 \
 --threads=8 \
 -e DJANGO_DEBUG=False \
 -e DJANGO_SETTINGS_MODULE=mysite.settings mysite.wsgi
```

## uwsgi
* Install uwsgi
```shell
pip3 install uwsgi
```
* Count of parameters uswsgi:
```shell
uwsgi --help | wc
```
* Run in CLI
```shell
uwsgi --chdir=${PWD}/mysite \
--module=mysite.wsgi:polls \
--env DJANGO_SETTINGS_MODULE=mysite.settings
--env DJANGO_DEBUG=True \
--http-socket=0.0.0.0:8000 \
--wsgi-file=${PWD}/mysite/mysite/wsgi.py \
--workers=8
```
* Create uwsgi.ini in the root of the project
```ini
[uwsgi]
chdir=%v
module=mysite.wsgi:polls
wsgi-file=%v/mysite/wsgi.py
http-socket=0.0.0.0:8000
workers=%k
static-map=/static=%v/static
enable-threads=True
env DJANGO_DEBUG=True
env DJANGO_SETTINGS_MODULE=mysite.settings
```
>chdir - root of the project
><br/>module - wsgi app settings
><br/>env - env vars
><br/>http-socket - http socket of the project
><br/>wsgi-file - path of the wsgi file
><br/>workers - amount of run workers
><br/>master - enable the master process
><br/>pidfile=/tmp/project-master.pid - master process path
* Run uwsgi with ini file
```shell
uwsgi --ini uwsgi.ini
```
* Stop uwsgi with master process path
```shell
uwsgi --stop /tmp/project-master.pid
```