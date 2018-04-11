#!/bin/bash

cd src
python BuildBrick.py
cd ..
python test/test.py
