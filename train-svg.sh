#!/bin/bash

echo Encoding SVG...
python3 src/encode.py training/training-data.svg training/output.npz

echo Training on the SVG...
python3 src/train.py --dataset training/output.npz
