#!/bin/sh

virtualenv -p python3 django_venv
source django_venv/bin/activate
pip3 install -r ./requirements.txt
