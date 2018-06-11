#/bin/sh
python3.6 -m venv .
./bin/pip install -r requirements.txt
./bin/buildout -c py3.cfg
echo "run plone with: ./bin/wsgi"

