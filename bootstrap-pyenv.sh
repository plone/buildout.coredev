#!/bin/sh
# This script uses pyenv to install specific virtualenv
PY="3.11.2"
VENVBASE="plone-coredev-6.1"

if ! which pyenv &> /dev/null; then
  echo "Error: pyenv script is not installed." >&2
  exit 1
fi

eval "$(pyenv init -)"
export PYENV_VIRTUALENV_DISABLE_PROMPT=1
eval "$(pyenv virtualenv-init -)"


VENV=$VENVBASE-$PY
echo "---------------------------------------------------------------------------"
echo "Install with Python $PY using venv $VENV"
echo "---------------------------------------------------------------------------"
pyenv virtualenv $PY $VENV
pyenv local $VENV
pyenv activate $VENV
pip install -r requirements.txt
buildout -N
pyenv deactivate
