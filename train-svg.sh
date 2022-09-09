#!/bin/bash

echo Encoding SVG...
cp ./training/training-data.svg ./training/training-svg.txt           # refer to the next line's comment
python3 src/encode.py training/training-svg.txt training/output.npz   # i swear i only get lazy with bash files

echo Training on the SVG...
python3 src/train.py --dataset training/output.npz
