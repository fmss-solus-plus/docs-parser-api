#!/bin/bash

cd backend

python manage.py migrate

gunicorn backend.wsgi:application
