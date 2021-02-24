pipeline {
  agent any
  stages {
    stage('Pull code') {
      steps {
        git 'https://github.com/yakovtayar/DevOps_Project.git'
      }
    }

    stage('Run rest_app') {
      steps {
        script {
          if (Boolean.valueOf(env.UNIX)) {
            sh 'start /min rest_app.py'
          } else {
            bat 'start /min rest_app.py'
          }
        }

      }
    }

    stage('Run web_app') {
      steps {
        script {
          if (Boolean.valueOf(env.UNIX)) {
            sh 'start /min web_app.py'
          } else {
            bat 'start /min web_app.py'
          }
        }

      }
    }

    stage('Run backend_testing') {
      steps {
        script {
          if (Boolean.valueOf(env.UNIX)) {
            sh 'backend_testing.py'
          } else {
            bat 'backend_testing.py'
          }
        }

      }
    }

    stage('Run frontend_testing') {
      steps {
        script {
          if (Boolean.valueOf(env.UNIX)) {
            sh 'frontend_testing.py'
          } else {
            bat 'frontend_testing.py'
          }
        }

      }
    }

    stage('Run combined_testing') {
      steps {
        script {
          if (Boolean.valueOf(env.UNIX)) {
            sh 'combined_testing.py'
          } else {
            bat 'combined_testing.py'
          }
        }

      }
    }

    stage('Run clean_environment') {
      steps {
        script {
          if (Boolean.valueOf(env.UNIX)) {
            sh 'clean_environment.py'
          } else {
            bat 'clean_environment.py'
          }
        }

      }
    }

  }
}