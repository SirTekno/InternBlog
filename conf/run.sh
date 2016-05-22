#!/bin/bash

# Generates a new secret key for the app
key=$(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 64 | head -n 1)
echo $key > app/secret_key.txt

set -e

MODULE=${MODULE:-newswangers}

sed -i "s/module=newswangers:application/module=${MODULE}.wsgi:application/g" /django/uwsgi.ini

if [ ! -f "/django/app/manage.py" ]
then
  django-admin.py startproject ${MODULE} /django/app/
fi

exec /usr/bin/supervisord
