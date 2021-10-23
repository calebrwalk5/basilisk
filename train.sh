#!/bin/bash

echo Encoding...
python3 src/encode.py training/*.txt training/output.npz

echo Training...
python3 src/train.py --dataset training/output.npz
