#! /bin/bash

echo "INFO: generate Brick.ttl in current directory..."
python ../generate_brick.py
echo "INFO: generate shacl_test.ttl in current directory..."
python generate_shacl.py
echo "INFO: execute python _pyshacl.py -s shacl_test.ttl -i rdfs -a -m -f human -e Brick.ttl $1"
python _pyshacl.py -s shacl_test.ttl -i rdfs -a -m -f human -e Brick.ttl $1
