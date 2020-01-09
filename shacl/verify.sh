#! /bin/bash

python generate_shacl.py
pyshacl -s shacl_test.ttl -i rdfs -f human $1 2> metaErros
