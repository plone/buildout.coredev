#!groovy

pipeline {

  agent any

  stages {

    // Build
    stage('Build') {
      agent {
        label 'virtualenv'
      }
      steps {
        deleteDir()
        checkout scm
        sh 'make build'
        sh 'tar cfz build.tgz bin develop-eggs include lib parts src *.cfg Makefile requirements.txt'
        stash includes: 'build.tgz', name: 'build.tgz'
      }
    }

    // Static Code Analysis
    /*
    stage('Static Code Analysis') {
      agent {
        label 'virtualenv'
      }
      steps {
        deleteDir()
        unstash 'build.tgz'
        sh 'tar xfz build.tgz'
        sh 'make code-analysis'
      }
    }*/

    // Unit Tests
    stage('Unit Tests') {
      agent {
        label 'virtualenv'
      }
      steps {
        deleteDir()
        unstash 'build.tgz'
        sh 'tar xfz build.tgz'
        sh 'make test'
        sh 'ls -al parts/test/testreports'
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
        unstash 'build.tgz'
        sh 'tar xfz build.tgz'
        wrap([$class: 'Xvfb']) {
          sh 'make test-acceptance'
        }
      }
      post {
        always {
          step([
            $class: 'RobotPublisher',
            disableArchiveOutput: false,
            logFileName: 'parts/test/robot_log.html',
            onlyCritical: true,
            otherFiles: '**/*.png',
            outputFileName: 'parts/test/robot_output.xml',
            outputPath: '.',
            passThreshold: 100,
            reportFileName: 'parts/test/robot_report.html',
            unstableThreshold: 0
          ]);
        }
      }
    }

  }
}
