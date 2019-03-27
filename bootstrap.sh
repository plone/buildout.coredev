#!/bin/sh
virtualenv --clear -p python2.7 .
./bin/pip install -r requirements.txt
./bin/buildout $*
