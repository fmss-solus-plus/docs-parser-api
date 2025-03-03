#!/bin/bash

cd backend

# Check if Django is installed in the virtual environment
if ! python -c "import django" &> /dev/null; then
    pip install -r requirements.txt
fi

python manage.py migrate

gunicorn backend.wsgi:application
