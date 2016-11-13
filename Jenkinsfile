#!groovy

node ('master'){
  stage 'Build and Test'
  sh '$PYTHON27 bootstrap.py --setuptools-version 21.0.0 -c jenkins.cfg'
  sh 'bin/buildout -c jenkins.cfg'
  sh 'bin/alltests --xml'
  sh 'bin/alltests-at --xml'
  sh 'ROBOTSUITE_PREFIX=ONLYROBOT'
  sh 'bin/alltests -t ONLYROBOT --all --xml'
}
