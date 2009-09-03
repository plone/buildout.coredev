#!/bin/bash
set -x

for i in python2.6 python2.5 python2.4
do
    if [[ -z $(ls -d /opt/collective.loadtesting/var/funkload/*-$i) ]]
    then
	echo "Begin with $i"

	cd /opt/plone-coredev-4.0 &&
	bin/instance stop
	rm -f var/filestorage/Data.fs
	$i bootstrap.py &&
	bin/buildout -vN &&
	bin/instance start &&
	sleep 30 &&
	
	cd /opt/collective.loadtesting &&
	bin/fl-run-bench -s collective.coreloadtests --label=$i

    fi
done &&

i=3.3-python2.4
if [[ -z $(ls -d /opt/collective.loadtesting/var/funkload/*-$i) ]]
then
    echo "Begin with $i"

    cd /opt/plone-coredev-4.0 &&
    bin/instance stop
    rm -rf .installed.cfg .mr.developer.cfg parts/ develop-eggs/ Data.fs
    python2.4 bootstrap.py &&
    bin/buildout -vN -c plips/released.cfg &&
    bin/instance start &&
    sleep 30 &&

    cd /opt/collective.loadtesting &&
    bin/fl-run-bench -s collective.coreloadtests --label=$i

fi

cd /opt/collective.loadtesting &&
bin/fl-build-label-reports
