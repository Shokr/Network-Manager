ShokrNet
========

open source web application designed to help manage and document computer networks.


Settings
--------
Moved to config/settings/base.

Setup Commands
--------------
- pip install virtualenv
- cd shokrnet
- virtualenv env
- source env/bin/activate
- pip install requirements.txt

## run server:-

- python manage.py runserver

### Or

- gunicorn --bind 0.0.0.0:8000 config.wsgi


