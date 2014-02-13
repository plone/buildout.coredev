#!/bin/sh
PACKAGES="cmfcore cmfdefault cmfdifftool cmfdynamicviewfti cmfeditions cmfformcontroller cmfplacefulworkflow cmfquickinstallertool cmfuid"
FOLDER=cmf-deps
if [ ! -d $FOLDER ]
then
    mkdir $FOLDER
fi

if [ ! -e package-dependencies.dot ]
then
    ./bin/jenkins-package-dependencies
fi

for cmf in $PACKAGES
do
    echo "Generating dependencies graph for $cmf"

    grep $cmf package-dependencies.dot > $FOLDER/$cmf.dot

    echo "digraph {" > $FOLDER/$cmf-tmp.dot
    cat $FOLDER/$cmf.dot >> $FOLDER/$cmf-tmp.dot
    echo "}" >> $FOLDER/$cmf-tmp.dot

    dot -Tpng $FOLDER/$cmf-tmp.dot -o $FOLDER/$cmf.png
done
