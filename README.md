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
pip3 install -m requirements.txt
```
* Open django-project directory:
```shell
cd mysite
```
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
* Profit!