#!/bin/sh

for i in python2.6, python2.5 python 2.4
do

    cd /opt/plone-coredev-4.0 &&
    bin/instance stop &&
    $i bootstrap.py &&
    bin/buildout -vN &&
    bin/instance start &&
    sleep 30 &&
    
    cd /opt/collective.loadtesting &&
    bin/fl-run-bench -s collective.coreloadtests --label=$i

done &&

cd /opt/collective.loadtesting &&
bin/fl-build-label-reports
