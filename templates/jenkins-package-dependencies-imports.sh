#!/bin/sh
DISTRIBUTIONS="${distributions}"
FOLDER=deps
if [ ! -d $FOLDER ]
then
    mkdir $FOLDER
fi

for dist in $DISTRIBUTIONS
do
    echo "Scanning for imports of $dist"
    dist_folder=`echo $dist | sed 's/\./\//g'`
    dist_path="$FOLDER/$dist"

    grep --include=*.py -R $dist parts/packages | grep -v $dist_folder > $dist_path.txt
    sed -i 's/parts\/packages\///' $dist_path.txt

    counter=`wc -l $dist_path.txt |cut -d" " -f1`
    echo "Found $counter imports"
done
