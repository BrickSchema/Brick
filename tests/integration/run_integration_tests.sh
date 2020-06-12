#!/bin/bash

set -ex

for i in `ls *_test.sh`; do
    bash $i
done
