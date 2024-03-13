#!/bin/sh

python manage.py makemigrations
python manage.py migrate --run-syncdb

gunicorn MebelIvan.wsgi:application --bind 0.0.0.0:8000 --reload  -w 4
