#!/bin/bash
set -x
export PYTHON_EGG_CACHE=/opt/plone-coredev-4.0/eggs

cd /opt/plone-coredev-4.0/plips &&
for version in plone*.cfg
do
    label=${version:0:${#version}-4}
    if [[ -z $(ls -d /opt/collective.loadtesting/var/funkload/diff_*-$label) ]]
    then

	cd /opt/plone-coredev-4.0 &&
	bin/instance stop
	rm -rf .installed.cfg parts/ develop-eggs/ fake-eggs .mr.developer plips/.installed.cfg plips/fake-eggs/ plips/.mr.developer var/filestorage/Data.fs
	python2.4 bootstrap.py &>/opt/collective.loadtesting/var/funkload/$label.log &&
	bin/buildout -vN -c plips/$version >>/opt/collective.loadtesting/var/funkload/$label.log 2>&1 &&
	bin/instance start &&
	sleep 30 &&

	cd /opt/collective.loadtesting &&
	bin/fl-run-bench -s collective.coreloadtests --label=$label

    fi
done

cd /opt/collective.loadtesting &&
bin/fl-build-label-reports --x-label='^plone4\.0-python2\.6$' --y-label='^plone4\.0-python2\.6$' --y-label='^plone[^4].[0-9]$' --reverse
mv var/funkload/index.html var/funkload/versions.html