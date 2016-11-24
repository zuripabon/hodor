#!/bin/bash
sudo apt-get update
sudo apt-get -y install screen git
sudo apt-get -y install python-pip python-dev
sudo apt-get -y install python-rpi.gpio
sudo apt-get -y install python-requests python-imaging python-imaging-tk
# if running python3
# sudo apt-get -y install python3-rpi.gpio
sudo pip install --upgrade pip
sudo pip install -r requirements.txt
