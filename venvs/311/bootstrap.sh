#/bin/sh
`which python3.11` -m venv .
cd ../../
./venvs/311/bin/pip install -r requirements.txt
./venvs/311/bin/pip install -r requirements-plone.txt
