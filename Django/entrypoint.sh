#!/bin/sh

echo "Waiting for database..."
python manage.py wait_for_db

echo "Database started"
python manage.py migrate
python manage.py collectstatic --noinput

exec gunicorn config.wsgi:application --bind 0.0.0.0:8000 --reload
