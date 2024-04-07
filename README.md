#!/bin/bash
sudo apt update
sudo apt install -y python3 python3-venv python3-pip
python3 -m venv myenv
source myenv/bin/activate
git clone https://github.com/mikamttr/django_project.git
cd django_project
git checkout feature/master
pip install -r requirements.txt
python3 manage.py import_data
python3 manage.py akemigrations
python3 manage.py migrate
