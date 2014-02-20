#!/bin/sh
DISTRIBUTIONS="${distributions}"
FOLDER=deps
if [ ! -d $FOLDER ]
then
    mkdir $FOLDER
fi

if [ ! -e package-dependencies.dot ]
then
    ./bin/jenkins-package-dependencies
fi

for dist in $DISTRIBUTIONS
do
    echo "Generating dependencies graph for $dist"

    dist_lowercase=`echo $dist | tr '[:upper:]' '[:lower:]'`
    dist_path="$FOLDER/$dist"

    grep $dist_lowercase package-dependencies.dot > $dist_path.dot

    echo "digraph {" > $dist_path-tmp.dot
    cat $dist_path.dot >> $dist_path-tmp.dot
    echo "}" >> $dist_path-tmp.dot

    dot -Tpng $dist_path-tmp.dot -o $dist_path.png
done
