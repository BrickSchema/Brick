#!/bin/bash

set -ex

pushd ../../tools/convert

# install dependencies
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# run conversion script
for i in `ls examples/*.ttl`; do
    python convert.py --source 1.0.2 --target 1.1 $i
done

# cleanup
deactivate
rm -rf venv
rm -rf examples/*.ttl
git checkout examples/*.ttl
popd
