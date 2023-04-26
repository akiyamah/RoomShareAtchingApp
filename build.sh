#!/usr/bin/env bash
# exit on error
set -o errexit
pip install --upgrade pip 
pip install -r requirements-deploy.txt
python manage.py collectstatic --no-input 
python manage.py migrate 
python manage.py superuser