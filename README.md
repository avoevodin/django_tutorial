# Tutorial for Django framework

## Install the app:
* Clone repository:
```shell
git clone git@github.com:avoevodin/django_tutorial.git
```
* Open created directory:
```shell
cd django_tutorial
```
* Create venv:
```shell
python3 -m venv venv
```
* Activate venv:
```shell
source venv/bin/activate
```
* Install requirements.txt
```shell
pip install -r requirements.txt
```
* Open django-project directory:
```shell
cd mysite
```
* Create [docker_instance](DOCKER_TUTORIAL.md) with postgresql DB
* Create .env file
```shell
cat > .env << __EOF__ # __EOF__ is an example of delimiter, read heredoc
DATABASE_ENGINE=django.db.backends.postgresql
DATABASE_HOST=localhost
DATABASE_NAME=polls
DATABASE_PASSWORD=pollssecret
DATABASE_PORT=5432
DATABASE_USER=polls
__EOF__
```
* Example of heredoc
```shell
psql -U polls -d polls -h localhost << __SQL__
select * from django_content_type;
__SQL__
```
* Export variables
```shell
export $(cat .env)
```
* Copy exported vars to config of mysite
* Copy exported vars to config terminal in the PyCharm
> Preferences/Tools/Terminal/Environment variables
* Copy exported vars to config of Django and Python consoles
> Preferences/Build, Execution, Deployment/Console/Python console/Environment variables
> <br/>Preferences/Build, Execution, Deployment/Console/Django console/Environment variables 
* Migrate:
```shell
python3 manage.py migrate
```
* Create superuser
```shell
python3 manage.py createsuperuser
```
* Configure server
    1. Create django-server configuration.
    2. Point paths to django-project and its settings.
    3. In mysite/settings.py configure ALLOWED_HOSTS with '*',
        if it hasn't been done before.
* Run server in console or in Framework. Ex:
    ```shell
    python3 manage.py runserver 0:8000
    ```
* Create objects from admin console.
    1. Go to the browser and type '127.0.0.1:8000/admin'
    2. Login
    3. Create objects
* Run tests with coverage: 
```shell
coverage run --source='.' manage.py test polls
```
* Get report in html of coverage tests:
```shell
coverage html
open htmlcov/index.html
```
* Profit!
