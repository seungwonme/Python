# Django

## Set up Virtual Environment
```bash
python3 -m venv venv 
source venv/bin/activate
pip install django
```

```bash
# Verify that your virtual environment is set up correctly
which python

# To exit the virtual environment
deactivate

# Saving virtual environment packages 
pip freeze > requirements.txt

# Installing packages from requirements.txt
pip install -r requirements.txt
```

## Django commands

1. Create a new project
```bash
# django-admin startproject <project_name> <directory>
django-admin startproject my_project .
```

2. Create a new app
```bash
# python manage.py startapp <app_name>
python manage.py startapp my_app
```

3. Run development server
```bash
python manage.py runserver
```

4. Create database migrations
```bash 
python manage.py makemigrations
```

5. Apply database migrations
```bash
python manage.py migrate
```

6. Check actual SQL queries
```bash
# python manage.py sqlmigrate <app_name> <migration_number>
python manage.py sqlmigrate my_app 0001
```

7. Create superuser
```bash
python manage.py createsuperuser
```

8. Open django shell
```bash
python manage.py shell
```

9. Collect static files
```bash
python manage.py collectstatic
```

10. Run tests
```bash
python manage.py test
```

## URL and View

`localhost:8000/my_app`에 접속하면 `views.my_app` 함수가 실행된다.
```python
# my_project/urls.py
from django.contrib import admin
from django.urls import path
from my_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('my_app/', views.my_app),
]
```

## Django settings

1. Change the language and time zone
```python
LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'
```
