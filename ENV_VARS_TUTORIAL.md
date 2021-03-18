# Tutorial for use of the environment variables

* Set env var in the console
```shell
MY_NAME=Andrey
echo $MY_NAME
# Andrey
echo ${MY_NAME}88
# Andrey88
unset MY_NAME
#
```
* Set env var in the bash and in the python
```shell
MY_NAME=Andrey bash
>>> env | grep MY_NAME
>>> # MY_NAME=Andrey
```
```python
MY_NAME=Andrey python3
>>> from os import environ as env
>>> env['MY_NAME']
>>> # Andrey
>>> # It's better to use get:
>>> env.get('MY_NAME', None)
>>> # Andrey
>>> env.get('MY_NAME')
>>> # Andrey
>>> env.get('MY_NAME', 'default')
>>> # Andrey
```
* For making var visible for all new processes
```shell
export MY_NAME=Andrey
python3
>>> from os import environ as env
>>> env.get('MY_NAME')
>>> # Andrey
```
* Print all/filtered export vars, export in the file example
```shell
export
export | grep MY_PREFIX_
export | grep MY_PREFIX_ > .env
```
