#!/bin/sh
# This script uses pyenv to install specific virtualenv
TAG=6.0
PY=3.7.6
VENVBASE=plone-coredev-$TAG

git clone -b $TAG git@github.com:plone/buildout.coredev.git

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
