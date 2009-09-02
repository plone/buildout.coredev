#!/bin/sh

cd /opt/plone-coredev-4.0 &&
bin/instance stop
bin/buildout -vN &&
bin/instance start &&
sleep 30 &&

cd /opt/collective.loadtesting &&
bin/fl-run-bench -s collective.coreloadtests --label=plone-4.0 &&

cd /opt/plone-coredev-4.0/plips &&
for i in *.cfg
do
    if [[ ! -d /opt/plone-coredev-4.0/plips/funkload/*-$i ]]
    then
	cd /opt/plone-coredev-4.0 &&
	bin/instance stop
	bin/buildout -vN -c plips/$i &&
	bin/instance start &&
	sleep 30 &&
	
	cd /opt/collective.loadtesting &&
	bin/fl-run-bench -s collective.coreloadtests --label=$i
    fi &&
done &&

cd /opt/collective.loadtesting &&
bin/fl-build-label-reports --x-label=plone-4\.0 --y-label=!plone-4\.0
