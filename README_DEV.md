# Tutorial for the Django framework. Developers version

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
* Create .env file, add it to .gitignore
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
python3 manage.py compilemessages --no-input
```
* Find static
```python
./manage.py findstatic -v 3 test_file_name
```
* Config settings.py for static Root
```python
STATIC_ROOT = BASE_DIR / 'static'
```
* Collect static, add static directory to .gitignore
```shell
python3 manage.py collectstatic --no-input
```
* Create superuser
```shell
python3 manage.py createsuperuser
```
* Configure settings.py for test DB
```python
from os import environ as env

# other settings
# ...

if env.get('DATABASE_ENGINE') == 'django.db.backends.postgresql':
    DATABASES = {
        'default': {
            'ENGINE': env.get('DATABASE_ENGINE', 'django.db.backends.postgresql'),
            'NAME': env.get('DATABASE_NAME', 'polls'),
            'USER': env.get('DATABASE_USER', 'polls'),
            'PASSWORD': env.get('DATABASE_PASSWORD', ''),
            'HOST': env.get('DATABASE_HOST', 'localhost'),
            'PORT': env.get('DATABASE_PORT', '5432'),
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': env.get('DATABASE_ENGINE', 'django.db.backends.sqlite3'),
            'NAME': env.get('DATABASE_NAME', BASE_DIR / 'db.sqlite3'),
        }
    }
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
* Create objects from admin console
    1. Go to the browser and type '127.0.0.1:8000/admin'
    2. Login
    3. Create objects
* Run tests with coverage: 
```shell
coverage run --source='.' manage.py test polls
```
* Get report in html of coverage tests
```shell
coverage html
open htmlcov/index.html
```
* Config settings.py for getting SECRET_KEY and DEBUG from env vars
```python
from os import environ as env
#...
SECRET_KEY = env.get('POLLS_SECRET_KEY', 'test_secret_key')
#...
DEBUG = env.get('DJANGO_DEBUG', False) == 'True'
#...
```
* Generating new random SECRET_KEY:
```shell
python3 -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```
* Copy exported vars to config of mysite
* Copy exported vars to config terminal in the PyCharm
> Preferences/Tools/Terminal/Environment variables
* Copy exported vars to config of Django and Python consoles
> Preferences/Build, Execution, Deployment/Console/Python console/Environment variables
> <br/>Preferences/Build, Execution, Deployment/Console/Django console/Environment variables 
* Profit!
