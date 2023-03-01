#!/bin/bash
# django
# echo "server create and chenge dir to server"
# mkdir server && cd server 

echo "initialision python venv"
python3 -m venv venv
echo "Activate venv"
source venv/bin/activate
echo "create requirements.txt"
touch requirements.txt
echo "write requirements"
echo "
Django==3.2.6

"  >> requirements.txt 
echo "install requirements"
pip3 install -r requirements.txt
echo "create django, app - users, first migrate"
django-admin startproject core .
python3 manage.py startapp users
python3 manage.py migrate
