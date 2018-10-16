#/bin/sh
`which python3.6` -m venv .
./bin/pip install -r requirements.txt
ln -sf buildout-py3.cfg buildout.cfg
./bin/buildout $*
echo "run plone with: ./bin/wsgi"

