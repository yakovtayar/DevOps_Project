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
                        sh 'pipeline_testing.py'
                    } else {
                        bat 'pipeline_testing.py'
                    }
                }
            }
        }
    }
}
