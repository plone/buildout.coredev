#!/bin/sh
DISTRIBUTIONS="${distributions}"
FOLDER=deps
if [ ! -d $FOLDER ]
then
    mkdir $FOLDER
fi

./bin/jenkins-package-dependencies

for dist in $DISTRIBUTIONS
do
    echo "Generating dependencies graph for $dist"

    dist_lowercase=`echo $dist | tr '[:upper:]' '[:lower:]'`
    dist_path="$FOLDER/$dist"

    grep $dist_lowercase package-dependencies.dot > $dist_path.dot

    echo "digraph {" > tmp.dot
    cat $dist_path.dot >> tmp.dot
    echo "}" >> tmp.dot

    mv tmp.dot $dist_path.dot
done
