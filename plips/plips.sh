#!/bin/bash
set -x
export PYTHON_EGG_CACHE=eggs

cd plips &&
for plip in plipbase.cfg plip[0-9]*-*.cfg
do
    label=${plip:0:${#plip}-4}
    if [[ -z $(ls -d ../collective.loadtesting/var/funkload/diff_*$label*) ]]
    then

	cd .. &&
	bin/instance stop
	rm -rf .installed.cfg parts/ develop-eggs/ fake-eggs .mr.developer plips/.installed.cfg plips/.mr.developer var/filestorage/Data.fs
	svn status -v &>../collective.loadtesting/var/funkload/$label.log &&
	python2.6 bootstrap.py >>../collective.loadtesting/var/funkload/$label.log 2>&1 &&
	bin/buildout -vN -c plips/$plip >>../collective.loadtesting/var/funkload/$label.log 2>&1 &&
	bin/develop status -v >>../collective.loadtesting/var/funkload/$label.log 2>&1 && 
	bin/instance start &&
	sleep 30 &&
	
	cd ../collective.loadtesting &&
	bin/fl-run-bench -s collective.coreloadtests --label=$label
    fi 

done

cd ../collective.loadtesting
bin/fl-build-label-reports --x-label='^plipbase$' --y-label='^plip[0-9]*-.*'
mv var/funkload/index.html var/funkload/plips.html
