pipeline {
    agent any
    stages {
        stage('checkout') {
            steps {
                git 'https://github.com/yakovtayar/DevOps_Project.git'
            }
        }
        stage('run python') {
            steps {
                script {
                    if (Boolean.valueOf(env.UNIX)) {
                        sh 'rest_app.py'
                    } else {
                        bat 'rest_app.py'
                    }
                }
            }
        }
    }
}
