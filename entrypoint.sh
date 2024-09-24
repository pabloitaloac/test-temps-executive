#!/bin/sh

# Exit immediately if a command exits with a non-zero status
set -e

# Make migrations and migrate the database
python manage.py makemigrations
python manage.py migrate

# Run the server
python manage.py runserver
