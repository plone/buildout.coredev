#!/bin/bash

# to release version 1.0 and increment the version to 1.1 afterwards,
# call from the directory containing the egg folders with:
#  ./release-egg my.package 1.0 1.1

# Note that this assumes your python 2.4 interpreter is called 'python'.

package=${1}
version=${2}
new_version=${3}

# Get repository URL
trunk_url="$(svn info ${package} | sed -ne 's/.*URL: //p')"
svn_base=${trunk_url%${package}/*}

tag_url="${svn_base}/${package}/tags/${version}"

cd ${package}

function update_versions() {
    echo
    echo "Updating version in setup.cfg"
    mv setup.py setup.py.old
    cat setup.py.old | sed "s/^version = .*$/version = '${1}'/" > setup.py
    rm setup.py.old

    echo
    echo "Updating any version.txt files"
    for f in $(find . -name 'version.txt') ; do
        echo "${1}" > ${f}
    done
}

echo
echo "** Processing ${package} at ${trunk_url}"
echo

# echo
# echo "-> Please revise setup.py. Version will be handled separately."
# ${EDITOR} setup.py

echo
echo "-> Committing current trunk"
svn status
svn diff
read -p "Press enter to continue"
svn commit -m "Updating setup.py"

test $? == 0 || exit 1

echo
echo "-> Tagging release in subversion at ${tag_url}"
svn cp -m "Tagging ${version}" . "${tag_url}"

test $? == 0 || exit 1

echo
echo "-> Switching to tag"
svn switch "${tag_url}"

update_versions "${version}"

test $? == 0 || exit 1

echo
echo "-> Removing setup.cfg"
svn rm setup.cfg

echo
echo "-> About to commit changes to tag"
svn status
svn diff
svn commit -m "Updating version and removing setup.cfg for the tag"

test $? == 0 || exit 1

echo
echo "-> Cheesing it up"
export COPY_EXTENDED_ATTRIBUTES_DISABLE=true
export COPYFILE_DISABLE=true

python setup.py egg_info -RDb "" sdist bdist_egg register upload

test $? == 0 || exit 1

echo
echo "-> Switching back to trunk"
svn switch "${trunk_url}"

update_versions "${new_version}"

test $? == 0 || exit 1

echo
echo "-> About to commit new version to trunk"
svn status
svn diff
svn commit -m "Updating version on trunk after tagging"

test $? == 0 || exit 1

echo
echo "-> All done"
cd ..
