#!groovy

pipeline {

  agent any

  environment {
    git_commit_message = ''
    git_commit_diff = ''
    git_commit_author = ''
    git_commit_author_name = ''
    git_commit_author_email = ''
  }

  stages {

    // Build
    stage('Build') {
      agent {
        label 'virtualenv'
      }
      steps {
        deleteDir()
        checkout scm
        // Create virtual Python environment
        sh 'virtualenv --clear .'
        // Install setuptools and zc.buildout
        sh 'bin/pip install -r requirements.txt'
        // Build Plone
        sh 'bin/buildout'
        // Create a tar archive with the Plone build
        // (passing around too many files makes the build slow)
        sh 'tar cfz backend.tgz bin develop-eggs include lib parts src *.cfg requirements.txt'
        // Stash the tar archive for later stages
        stash includes: 'backend.tgz', name: 'backend.tgz'
      }
    }

    // Static Code Analysis
    stage('Static Code Analysis') {
      agent {
        label 'virtualenv'
      }
      steps {
        deleteDir()
        unstash 'backend.tgz'
        sh 'tar xfz backend.tgz'
        // sh 'bin/code-analysis'
        sh "echo 'Run Static Code Analysis'"
      }
    }

    // Unit Tests
    stage('Unit Tests') {
      agent {
        label 'virtualenv'
      }
      steps {
        deleteDir()
        unstash 'backend.tgz'
        sh 'tar xfz backend.tgz'
        sh 'bin/alltests'
      }
      post {
        always {
          step([
            $class: 'JUnitResultArchiver',
            testResults: 'parts/test/testreports/*.xml'
          ])
        }
      }
    }

    // Acceptance Tests
    stage('Acceptance Tests') {
      agent {
        label 'virtualenv'
      }
      steps {
        deleteDir()
        sh "sed -i 's/    mr.developer/    mr.developer\ngit-clone-depth = 100/' core.cfg"
        sh 'virtualenv .'
        sh 'bin/pip install -r requirements.txt'
        sh 'bin/buildout -c core.cfg'
        sh 'export ROBOTSUITE_PREFIX=ONLYROBOT'
        sh 'bin/alltests -t ONLYROBOT --all --xml'
        /*wrap([$class: 'Xvfb']) {
          sh 'bin/pybot test1.robot'
        }*/
      }
      post {
        always {
          step([
            $class: 'JUnitResultArchiver',
            testResults: 'parts/test/*.xml'
          ])
        }
      }
    }

  }
}
