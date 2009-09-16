#!/bin/bash
set -x
export PYTHON_EGG_CACHE=eggs

for python in python2.6 python2.5 python2.4
do
    label=plipbase-$python
    if [[ $python == "python2.6" ]]
    then
	label=plipbase
    fi
    if [[ -z $(ls -d ../collective.loadtesting/var/funkload/diff_*-$label) ]]
    then

	cd .. &&
	bin/instance stop
	rm -rf .installed.cfg parts/ develop-eggs/ fake-eggs .mr.developer plips/.installed.cfg plips/.mr.developer var/filestorage/Data.fs
	svn status -v &>../collective.loadtesting/var/funkload/$label.log &&
	$python bootstrap.py >>../collective.loadtesting/var/funkload/$label.log 2>&1 &&
	bin/buildout -vN -c plips/plipbase.cfg >>../collective.loadtesting/var/funkload/$label.log 2>&1 &&
	bin/develop status -v >>../collective.loadtesting/var/funkload/$label.log 2>&1 && 
	bin/instance start &&
	sleep 30 &&
	
	cd ../collective.loadtesting &&
	bin/fl-run-bench -s collective.coreloadtests --label=$label
        bin/fl-build-label-reports --x-label='^plipbase$' --x-label='^plipbase-python2..$' --y-label='^plipbase$' --y-label='^plipbase-python2..$'
        mv var/funkload/index.html var/funkload/base.html

    fi
done &&
