#!/bin/bash
set -x
export PYTHON_EGG_CACHE=eggs
base=$(pwd)

for python in python2.6 python2.5 python2.4
do
    label=plipbase-$python
    if [[ $python == "python2.6" ]]
    then
	label=plipbase
    fi
    if [[ -z $(ls -d $base/../collective.loadtesting/var/funkload/diff_*-$label) ]]
    then

        cd $base &&
	bin/instance stop
	rm -rf .installed.cfg parts/ develop-eggs/ fake-eggs .mr.developer plips/.installed.cfg plips/.mr.developer var/filestorage/Data.fs
	svn status -v &>$base/../collective.loadtesting/var/funkload/$label.log &&
	$python bootstrap.py >>$base/../collective.loadtesting/var/funkload/$label.log 2>&1 &&
	bin/buildout -vN -c plips/plipbase.cfg >>$base/../collective.loadtesting/var/funkload/$label.log 2>&1 &&
	bin/develop status -v >>$base/../collective.loadtesting/var/funkload/$label.log 2>&1 && 
	bin/instance start &&
	sleep 30 &&
	
	cd $base/../collective.loadtesting &&
	bin/fl-run-bench -s collective.coreloadtests --label=$label
        bin/fl-build-label-reports --x-label='^plipbase$' --x-label='^plipbase-python2..$' --y-label='^plipbase$' --y-label='^plipbase-python2..$'
        mv var/funkload/index.html var/funkload/base.html

    fi
done &&
