#!/bin/sh

echo "Running migrations..."
python manage.py makemigrations
python manage.py migrate

echo "Starting the server..."
exec python manage.py runserver 0.0.0.0:8000
