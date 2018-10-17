#!/bin/sh
virtualenv --clear -p `which python2.7` .
./bin/pip install -r requirements.txt
ln -sf buildout-py2.cfg buildout.cfg
./bin/buildout $*
echo "run plone with: ./bin/instance fg"