#! /bin/bash

python generate_shacl.py
pyshacl -s shacl_test.ttl -i rdfs -a -m -f human -e Brick.ttl $1 2> metaErros
