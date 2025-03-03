#!/bin/bash

python manage.py collecstatic --noinput

python manage.py migrate

gunicorn backend.wsgi:application 