#!/bin/bash

# Ensure DB is here
mysql -u root -p123123 --execute="create database if not exists app character set UTF8 collate utf8_bin"

# install requirements
pip install -r requirements.prod.txt

# migrate db
python manage.py migrate

# collectstatic files
python manage.py collectstatic --noinput -l

# restart uwsgi
supervisorctl restart uwsgi

echo "Deploy done!"
