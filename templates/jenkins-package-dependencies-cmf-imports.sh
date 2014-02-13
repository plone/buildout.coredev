#!/bin/sh
PACKAGES="CMFCore CMFDefault CMFDiffTool CMFDynamicViewFTI CMFEditions CMFFormController CMFPlacefulWorkflow CMFQuickInstallerTool CMFUid"
FOLDER=cmf
if [ ! -d $FOLDER ]
then
    mkdir $FOLDER
fi

for cmf in $PACKAGES
do
    package_name="Products.$cmf"
    echo "Scanning for imports of $package_name"

    grep --include=*.py -R $package_name parts/packages | grep -v "Products/CMF[A-OQ-Z]" | grep -v "Products/CMFPlace" > $FOLDER/$cmf-imports.txt
    sed -i 's/parts\/packages\///' $FOLDER/$cmf-imports.txt

    counter=`wc -l $FOLDER/$cmf-imports.txt |cut -d" " -f1`
    echo "Found $counter imports"
done
