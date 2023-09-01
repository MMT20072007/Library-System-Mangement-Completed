# settings.py

from pathlib import Path

# Django settings
DEBUG = True
ALLOWED_HOSTS = []

# Celery settings
CELERY_BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'

# App settings
APP_DIR = Path(__file__).parent

# Database settings
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'library',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'localhost',
        'PORT': 5432,
    }
}

# Internationalization settings
LANGUAGE_CODE = 'fa_IR'
TIME_ZONE = 'Asia/Tehran'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files settings
STATIC_URL = '/static/'

# Media files settings
MEDIA_URL = '/media/'
MEDIA_ROOT = Path(APP_DIR, 'media')

# Auth settings
AUTH_USER_MODEL = 'users.User'

# REST framework settings
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 10,
}
# urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('api.urls')),
]
# apps.py

from django.apps import AppConfig

class LibraryAppConfig(AppConfig):
    name = 'library'
# models.py

from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=255)
    authors = models.ManyToManyField(to='authors.Author')
    genre = models.ForeignKey(to='genres.Genre', on_delete=models.CASCADE)
    publication_date = models.DateField()
    ISBN = models.CharField(max_length=13)
    price = models.IntegerField()


class Author(models.Model):
    name = models.CharField(max_length=255)
    birth_city = models.ForeignKey(to='cities.City', on_delete=models.CASCADE)


class Genre(models.Model):
    name = models.CharField(max_length=255)


class City(models.Model):
    name = models.CharField(max_length=255)


class Member(models.Model):
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    membership_type = models.CharField(max_length=255)
    membership_expiration_date = models.DateField()


class Reservation(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    total_cost = models.IntegerField()

# utils.py

from datetime import datetime


def get_current_date():
    return datetime.today().date()


def get_next_day(date):
    return date + datetime.timedelta(days=1)


def is_date_valid(date):
    try:
        datetime.strptime(date, '%Y-%m-%d')
        return True
    except ValueError:
        return False

