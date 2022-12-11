#!/bin/bash

# Collect static files
echo "Collect static files"
python manage.py collectstatic --noinput

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate

# Create super user account
echo "Create super user account"
python manage.py createsuperuser --no-input

# Start server
echo "Starting server"
python manage.py runserver 0.0.0.0:8000
# gunicorn config.wsgi --config gunicorn-cfg.py