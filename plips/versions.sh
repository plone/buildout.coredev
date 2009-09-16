#!/bin/bash
set -x
export PYTHON_EGG_CACHE=eggs
base=$(pwd)

cd ../plone-coredev-4.0/plips &&
for version in plone*.cfg
do
    label=${version:0:${#version}-4}
    if [[ -z $(ls -d $base/../collective.loadtesting/var/funkload/diff_*-$label) ]]
    then

	cd .. &&
	bin/instance stop
	rm -rf .installed.cfg parts/ develop-eggs/ fake-eggs .mr.developer plips/.installed.cfg plips/.mr.developer var/filestorage/Data.fs
	svn status -v &>$base/../collective.loadtesting/var/funkload/$label.log &&
	python2.4 bootstrap.py >>$base/../collective.loadtesting/var/funkload/$label.log 2>&1 &&
	bin/buildout -vN -c plips/$version >>$base/../collective.loadtesting/var/funkload/$label.log 2>&1 &&
	bin/develop status -v >>$base/../collective.loadtesting/var/funkload/$label.log 2>&1 && 
	bin/instance start &&
	sleep 30 &&

	cd $base/../collective.loadtesting &&
	bin/fl-run-bench -s collective.coreloadtests --label=$label
        bin/fl-build-label-reports --x-label='^plipbase' --y-label='^plipbase' --y-label='^plone[^4].[0-9]$' --reverse
        mv var/funkload/index.html var/funkload/versions.html

    fi
done
