#!/bin/sh
sudo pip3 install -r requirements.txt
sudo pip3 install tensorflow          # YES I'M THAT LAZY
sudo pip3 install numpy               # another example of laziness
python3 basilisk.py 124M              # download and use OpenAI's 124M
touch training/training-data.txt
