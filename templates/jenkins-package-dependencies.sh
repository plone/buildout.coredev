#!/bin/sh
if [ ! -e package-dependencies.dot ]
then
    ./bin/jenkins-package-dependencies
fi

package_name="${distribution}"

echo "Generating dependencies graph for $package_name"

grep $package_name package-dependencies.dot > $package_name.dot

echo "digraph {" > $package_name-tmp.dot
cat $package_name.dot >> $package_name-tmp.dot
echo "}" >> $package_name-tmp.dot

dot -Tpng $package_name-tmp.dot -o $package_name.png
