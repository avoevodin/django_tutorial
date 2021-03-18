# Tutorial for getting start in Docker

* Download and start the Docker
> https://www.docker.com/get-started
* Create an account or sing in the Docker Hub
> https://hub.docker.com
* Download the image of Postgres. An alpine version of OS Linux is lighter
than a simple version of the image.
```shell
docker pull postgres:13.2-alpine
```
* Look at the list of started containers
```shell
docker ps
```
* Look at the list of all containers
```shell
docker ps -a
```
* Look at the Docker-images in the system
```shell
docker images
```
* Occupied open ports
```shell
netstat -Lan
```
* Create and run a container
```shell
docker run -d --hostname polls-postgres \
  -p 5432:5432 --name polls-postgres \
  -e POSTGRES_USER=polls \
  -e POSTGRES_PASSWORD=pollssecret \
  -e POSTGRES_DB=polls \
  postgres:13.2-alpine
```
> -d - start docker as a daemon
> <br/>-p - local port and container port
> <br/>-e - environment variables
> <br/>postgres:13.2-alpine - name of the run image.
* Look at the container's logs
```shell
docker logs polls-postgres
```
* Look at the container's continuous log
```shell
docker logs -f polls-postgres
```
* Connect to the started Linux container
```shell
docker exec -ti polls-postgres sh
ls -la # example
```
* Pause the container
```shell
docker stop polls-postgres
```
* Start paused container
```shell
docker start polls-postgres
```
* Hard stop of the container
```shell
docker kill polls-postgres
```
* Delete the container
```shell
docker rm polls-postgres
```
* Delete downloaded image
```shell
docker rmi postgres:13.2-alpine
```
* Install sql console for python
```shell
brew install libpg
brew install postgresql # sql console
```
* Connect to postgres via installed sql console
```shell
psql -U user -d database -p port -h host
# Input password
psql -U polls -d polls -p 5432 -h localhost # example
\d+ # list of all tables
```
* Connect created postgres DB to PyCharm
* Make a dump of all tables exclude sessions and contenttypes
```shell
# without excludes
./manage.py dumpdata polls
# or all DBs
./manage.py dumpdata -a
# dump to the file with excludes from DB
./manage.py dumpdata polls -e sessions contenttypes --indent=4 > bd_dump.json
```
* Install the connector from python to postgres into our venv
> https://docs.djangoproject.com/en/3.1/ref/settings/#databases
```shell
pip install psycopg2
# update requirements.txt
pip freeze > ../requirements.txt
```
* Migrate DB
```shell
./manage.py migrate
```
* Load data into created DB with migrations
```shell
./manage.py loaddata bd_dump.json -e contenttypes # example of excluding an app
```
* Profit!
