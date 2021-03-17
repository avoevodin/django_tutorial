# Tutorial for localization initializing

* Configure settings.py
    1. Import gettext:
    ```python
        from django.utils.translation import gettext_lazy as _ # noqa
    ```
    2. Path for storing locales:
    ```python
        LOCALE_PATHS = [
            'locale'
        ]
    ```
    3 Allowed languages:
    ```python
        LANGUAGES = [
            ('en', _('English')), # noqa
            ('ru', _('Russian'))  # noqa  
        ] 
    ```
    4. MIDLLEWARE:
       add `django.middleware.locale.LocaleMiddleware' after 
       the session middlware 'django.contrib.sessions.middleware.SessionMiddleware'. 

* Create locales:
```shell
./manage.py makemessages -l ru
./manage.py makemessages -l en

```
* Correct descriptions "Language: \n" to "Language: en\n" in the .po files.
* Create translations in modules:
    1. in views:
    ```python
    from django.utils.translation import gettext as _ # noqa
    ``` 
    2. in other objects of python:
    ```python
    from django.utils.translation import gettext_lazy as _ # noqa
    ```
    3. in base template:
    ```html
    {% load i18n %}
    
    {% get_current_language as LANGUAGE_CODE %}    
    
    <!doctype html>
    <html lang={{ LANGUAGE_CODE }}>
        ...
    </html>
    ```
    4. in other templates:
    ```html
    {% load i18n %}
    {% translate "Text for translation" %}
    ```
* Update messages
```shell
./manage.py makemessages -a
```
* Translate generated messages.
* Compile translated messages
```shell
./manage.py compilemessages
```
* Add compiled .po files to .gitignore.
* Refresh page or reboot server.
* !!! To translate the name of app in the admin-panel it needs
to add in settings.py INSTALLED APPS instead of 'polls'
'polls.apps.PollsConfig'
