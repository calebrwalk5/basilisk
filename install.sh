#!/bin/sh
pip install -r requirements.txt
python3 basilisk.py 124M
touch training/training-data.txt
