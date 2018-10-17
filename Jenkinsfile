#!groovy
def layers

pipeline {
  agent any
  stages {
    stage('Buildout') {
      steps {
        deleteDir()
        withPythonEnv('Python2.7') {
          sh """
          git clone --branch ${branch} --depth 1 https://github.com/plone/buildout.coredev.git
          (
          cd buildout.coredev
          pip install -r requirements.txt
          buildout buildout:git-clone-depth=1 -c core.cfg install test
          bin/test --all --list-tests 2>/dev/null | grep -E '^Listing' | awk '{print \$2}' | sort -u | tee layers.txt
          )
          tar cf src.tar buildout.coredev/src
          """
          stash includes: 'src.tar', name: 'src.tar'
        }
        script {
          layers = readFile("${env.WORKSPACE}/buildout.coredev/layers.txt").trim().split('\n')
        }
      }
    }
    stage('Dispatch') {
      steps {
        script {
          def tests = [:]
          for (int i = 0; i < layers.length -1; i++) {
            def layername = "${layers[i]}"
            tests["${i}"] = {
              node {
                stage("Test ${layername}") {
                  deleteDir()
                  unstash 'src.tar'
                  withPythonEnv('Python2.7') {
                    sh """
                    git clone --branch ${branch} --depth 1 https://github.com/plone/buildout.coredev.git
                    tar xf src.tar
                    cd buildout.coredev
                    pip install -r requirements.txt
                    buildout buildout:git-clone-depth=1 buildout:always-checkout=false -c core.cfg install test
                    export ROBOT_BROWSER='chrome'
                    xvfb-run -a --server-args='-screen 0 1920x1200x24' bin/test --all --xml --layer '${layername}'
                    """
                  }
                }
              }
            }
          }
          parallel tests
        }
      }
    }
  }
}
