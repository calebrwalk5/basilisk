@echo off

echo Encoding...
python src\encode.py training\training-data.txt training\output.npz

echo Training...
python src\train.py --dataset training\output.npz