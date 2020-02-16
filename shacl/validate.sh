#! /bin/bash

echo "INFO: generate Brick.ttl in current directory..."
python ../generate_brick.py || exit
echo "INFO: generate shacl_test.ttl in current directory..."
python generate_shacl.py || exit
echo "INFO: execute python _pyshacl.py -s shacl_test.ttl -i rdfs -a -m -f human -e ModifiedBrick.ttl $1"
python _pyshacl.py -s shacl_test.ttl -i rdfs -a -m -f human -e ModifiedBrick.ttl $1
