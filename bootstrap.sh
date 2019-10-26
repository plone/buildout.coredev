#/bin/sh
`which python3.7` -m venv .
./bin/pip install -r requirements.txt
./bin/buildout $*
echo "run plone with: ./bin/instance fg"

