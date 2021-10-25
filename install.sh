#!/bin/sh
sudo pip3 install -r requirements.txt
sudo pip3 install numpy
python3 basilisk.py 1558M
touch training/training-data.txt
