#!/bin/sh
sudo python -m pip install -r requirements.txt
sudo python -m pip install tensorflow           # YES I'M THAT LAZY
sudo python -m pip install numpy                # another example of laziness
python3 basilisk.py 124M                        # download and use OpenAI's 124M
