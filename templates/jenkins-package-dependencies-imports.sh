#!/bin/sh
package_name="${distribution}"
echo "Scanning for imports of $package_name"

grep --include=*.py -R $package_name parts/packages | grep -v "plone/app/contenttypes" > $package_name.txt
sed -i 's/parts\/packages\///' $package_name.txt

counter=`wc -l $package_name.txt |cut -d" " -f1`
echo "Found $counter imports"
