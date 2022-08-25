#!bin/bash
apt update 
apt upgrade -y 

# install python
apt install python3.9 python3-pip vim -y 

# Python3.8 -> Python3.9
update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.9 9 
update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.8 8

# python module
python3 -m pip install Django
python3 -m pip install janome