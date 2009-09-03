#!/bin/bash
set -x

i=plone-4.0
if [[ -z $(ls -d /opt/collective.loadtesting/var/funkload/*-$i) ]]
then

    cd /opt/plone-coredev-4.0 &&
    bin/instance stop
    rm -f var/filestorage/Data.fs
    bin/buildout -vN &&
    bin/instance start &&
    sleep 30 &&

    cd /opt/collective.loadtesting &&
    bin/fl-run-bench -s collective.coreloadtests --label=$i &&

fi

cd /opt/plone-coredev-4.0/plips &&
for i in *.cfg
do
    if [[ -z $(ls -d /opt/collective.loadtesting/var/funkload/*-$i) ]]
    then

	cd /opt/plone-coredev-4.0 &&
	bin/instance stop
	rm -f var/filestorage/Data.fs
	bin/buildout -vN -c plips/$i &&
	bin/instance start &&
	sleep 30 &&
	
	cd /opt/collective.loadtesting &&
	bin/fl-run-bench -s collective.coreloadtests --label=$i
    fi 

done

cd /opt/collective.loadtesting
bin/fl-build-label-reports --x-label='plone-4\.0' --y-label='!plone-4\.0'
