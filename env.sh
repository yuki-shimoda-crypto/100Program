# docker
# ubuntu:20.04

#!bin/bash
apt update 
apt upgrade -y 

# install python
apt install curl python3.9 python3-pip python3.9-venv vim ssh git snapd -y

# Python3.8 -> Python3.9
update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.9 9 
update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.8 8

# python module
python3 -m pip install Django
python3 -m pip install janome
python3 -m pip install django-heroku

# install heroku
curl https://cli-assets.heroku.com/install-ubuntu.sh | sh