#!groovy

node {
  stage 'Build'
  sh '$PYTHON27 bootstrap.py --setuptools-version 21.0.0 -c jenkins.cfg'
  sh 'bin/buildout -c jenkins.cfg'
}

node {
  stage 'Test'
  parallel general: {
        sh 'bin/alltests --xml'
    }, archetypes: {
        sh 'bin/alltests-at --xml'
    }, robot: {
        sh 'ROBOTSUITE_PREFIX=ONLYROBOT'
        sh 'bin/alltests -t ONLYROBOT --all --xml'
    },
    failFast: false
}
