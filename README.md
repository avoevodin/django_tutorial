# Tutorial for the Django framework

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
cat > .env << __EOF__
DATABASE_ENGINE=django.db.backends.postgresql
DATABASE_HOST=localhost
DATABASE_NAME=polls
DATABASE_PASSWORD=pollssecret
DATABASE_PORT=5432
DATABASE_USER=polls
POLLS_SECRET_KEY=test_secret_key
DJANGO_DEBUG=True
__EOF__
```
* Export variables
```shell
export $(cat .env)
```
* Migrate:
```shell
python3 manage.py migrate --no-input
```
* Compile messages
```shell
python3 manage.py compilemessages
```
* Collect static
```shell
python3 manage.py collectstatic --no-input
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
* Run server in a console or in a Framework. Ex:
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
## Docker
* Create .env-docker file
```shell
cd mysite
cat > .env-docker << __EOF__
DATABASE_ENGINE=django.db.backends.postgresql
DATABASE_HOST=polls-postgres
DATABASE_NAME=polls
DATABASE_PASSWORD=pollssecret
DATABASE_PORT=5432
DATABASE_USER=polls
PS1=$'%n@%m %~ %% '
__EOF__
```
* run 
