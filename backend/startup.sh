#!/bin/sh
export PATH="$HOME/antenv/bin:$PATH"
cd backend  # Change to the directory containing manage.py
gunicorn --workers=1 --bind=0.0.0.0:8000 backend.wsgi
