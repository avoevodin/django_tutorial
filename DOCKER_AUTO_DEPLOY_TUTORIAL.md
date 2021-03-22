# Auto-deploy of the Docker Tutorial
> https://alpinelinux.org/
> <br/>https://uwsgi-docs.readthedocs.io/en/latest/Configuration.html
> <br/>https://docs.docker.com/engine/reference/builder/

* Create container from image alpine:3.13 and run sh in it. Three ways to do it:
```shell
docker run --tty --interactive --name test-alpine --hostname test-alpine alpine:3.13 sh
```
```shell
docker run -ti --name test-alpine --hostname test-alpine alpine:3.13 sh
```
```shell
docker run -it --name test-alpine --hostname test-alpine alpine:3.13 sh
```
* Join to a terminal of a started container
```shell
docker attach test-alpine
```
* Pocket manager of alpine
>https://pkgs.alpinelinux.org/packages
```shell
apk --help
```
```shell
apk add zsh
```
```shell
apk del zsh
```
* Commit, delete old and run created image with zsh
```shell
docker commit test-alpine alpine-zsh:3.13
docker run -it --name test-zsh --hostname test-zsh alpine-zsh:3.13 zsh
```
* Add python3 and pip to the created image
```shell
apk add python3
apk add py3-pip
```
* Commit and run another version of the image with a volume in /app directory
```shell
docker commit alpine-python3 test-python3
docker rm alpine-python3
docker run -ti --name test-python3 --hostname test-python3 \
--volume ${PWD}/django_tutorial:/app alpine-python3 zsh
```
* Get an error with requirements.txt when installing psycopg2 or uwsgi
```shell
pip3 install -r requirements.txt
```
* Correct an error with installing of psycopg2 from apk
```shell
apk add py3-psycopg2
```
* Commit updated image. Run it with PS1 env var for tune the bash rc
```shell
docker commit test-python3 python3-env
docker rm test-python3
export | grep PS1
# copy necessary prompts
docker run -ti --name python3-env --hostanme python3-env \
--env PS1=$'%n@%m %~ %% ' \
--volume ${PWD}/django_tutorial:/app python3-env zsh
```
* Add uwsgi and python module for uwsgi.
```shell
apk add uwsgi
apk add uwsgi-python3
uwsgi --ini app/mysite/uwsgi.ini
```
* Commit and run updated image with local and remote ports settings
```shell
docker commit python3-env python3-uwsgi
docker rm python3-env
docker run -ti --name polls-uwsgi --hostname polls-uwsgi \
--volume ${PWD}/django_tutorial:/app python3-uwsgi \
-e PS1=$'%n@%m %~ %% ' \
--publish 8000:8000 \
python-uwsgi \
# for tests to auto delete container
--rm \ 
zsh
```
* Export necessary env vars
```shell
export cat(app/.env)
```
> App is still not working, because the database isn't visible for the container.
* As the DB isn't work, it needs ot run docker uwsgi-container 
  with linking to polls-postgres container.
```shell
docker run -ti --name polls-uwsgi --hostname polls-uwsgi \
--volume ${PWD}/django_tutorial:/app python3-uwsgi \
-e PS1=$'%D %* %{\C-[[31m%}%n%{\C-[[00m%}@%{\C-[[36m%}%m %{\C-[[33m%}%~ %{\C-[[00m%}%% $(git_prompt_info)' \
- publish 8000:8000 \
# for tests to auto delete container
--rm \ 
--link polls-postgres \
- python-uwsgi \
zsh
```
```shell
ping polls-postgres
# correct ini and env vars
```
* Tag the name for created image. Every image may have several tags 
```shell
docker tag 1ee70d260010 polls-uwsgi:1.0
docker tag 1ee70d260010 polls-uwsgi:latest
```
* Start uwsgi with ti
```shell
docker run --name polls-uwsgi --hostname polls-uwsgi \
-ti \
--publish 8000:8000 \
--env-file /Users/avo888/Projects/django_tutorial/mysite/.env-docker \
--link polls-postgres \
--volume /Users/avo888/Projects/django_tutorial:/app \
polls-uwsgi \
uwsgi --ini /app/mysite/uwsgi.ini
```
* Start uwsgi as daemon
```shell
docker run --name polls-uwsgi --hostname polls-uwsgi \
-d \
--publish 8000:8000 \
--env-file /Users/avo888/Projects/django_tutorial/mysite/.env-docker \
--link polls-postgres \
--volume /Users/avo888/Projects/django_tutorial:/app \
polls-uwsgi \
uwsgi --ini /app/mysite/uwsgi.ini
```
* Look at the logs of the container
```shell
docker logs -f polls-uwsgi
```
* Docker build image with Dockerfile
```dockerfile
FROM alpine:3.13

RUN apk add python3 py3-pip py3-psycopg2 uwsgi uwsgi-python3 gettext

COPY requirements_docker.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt

COPY mysite/ /app/mysite/
WORKDIR /app/mysite/

RUN python3 manage.py collectstatic
RUN python3 manage.py compilemessages

CMD uwsgi --ini uwsgi.ini
```
```shell
docker build -f Dockerfile -t polls-uwsgi ./
```
```shell
docker run -d --name polls-uwsgi --hostname polls-uwsgi --env-file .env-docker \
-p 8000:8000 --link polls-postgres polls-uwsgi
```
## Push docker image to DockerHub
>https://docs.docker.com/docker-hub/repos/

* Build docker with a pointed name of a repository or just tag it with rep name
```shell
docker build -f Dockerfile -t avo888/polls:polls-uwsgi ./
```
```shell
docker tag avo888/polls:polls-uwsgi avo888/polls-uwsgi:latest
```
* Push created image to the remote rep
```shell
docker push avo888/polls:polls-uwsgi
```
* Docker Login/Logout to remote rep
```shell
docker login
docker logout
```