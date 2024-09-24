#!/bin/sh

set -e

# Add a 5-second delay before starting the web service
echo "Waiting for MySQL to start..."
sleep 15

python manage.py makemigrations
python manage.py migrate
python manage.py runserver 0.0.0.0:8000