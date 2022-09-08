#!/bin/bash

echo Encoding SVG...
cp ./training/training-data.svg ./training/training-svg.txt
python3 src/encode.py training/training-svg.txt training/output.npz

echo Training on the SVG...
python3 src/train.py --dataset training/output.npz
