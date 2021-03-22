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
http-socket=0.0.0.0:8000
chdir=%d
workers=%k
threads=%k
module=mysite.wsgi:application
master=True

pidfile=%duwsgi-master.pid
# denaemonize=%duwsgi.log

env DJANGO_DEBUG=False
env DJANGO_SETTINGS_MODULE=mysite.settings

plugin = python3

offload-threads = %k
static-map=/static=%dstatic
check-static=%dstatic
static-expires=%dstatic/* 86400
```
>http-socket - http socket of the project
><br/>chdir - root of the project
><br/>workers - amount of run workers
><br/>threads - amount of the threads in each worker 
><br/>module - wsgi app settings
><br/>master - enable the master process
><br/>pidfile - master process path
><br/>denaemonize - run uwsgi as daemon with 
> dumping logs in the selected path 
><br/>env - env vars
><br/>offload-threads - separate threads for static
><br/>static-map - path for the static files
><br/>check-static - check if the static files exist in 
> the selected path
><br/>static-expires - set expire date for static files
* Run uwsgi with ini file
```shell
uwsgi --ini uwsgi.ini
```
* Stop uwsgi with master process path
```shell
uwsgi --stop /tmp/project-master.pid
```