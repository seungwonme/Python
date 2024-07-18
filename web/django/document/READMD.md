# Document

## Setup virtual environment
```bash
python -m venv venv
source venv/bin/activate
pip install django
pip freeze > requirements.txt
```

## Review
```bash
python
>>> import django
>>> print(django.get_version())
5.0.6
```

## Run Server
```bash
django-admin startproject mysite
cd mysite
python manage.py runserver
```

## Create a new app
```bash
python manage.py startapp polls
```
