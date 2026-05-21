#/bin/sh
# Warning: the venv module of Python 3.13 edits the .gitignore file.
# We may want to create the venv in a sub directory.
`which python3.14` -m venv .
git checkout .gitignore
./bin/pip install -r requirements.txt
./bin/buildout $*
echo "run plone with: ./bin/instance fg"

