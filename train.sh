#!/bin/bash

echo Encoding...
python3 src/encode.py training/training-data.txt training/output.npz    # yep, that's me. lazy

echo Training...
python3 src/train.py --dataset training/output.npz
