pipeline{
agent any
    stages{
        stage('initial'){
            steps{
                    git 'https://github.com/yakovtayar/DevOps_Project.git'
                }
            }
        }stage('run_file'){
            steps{
                    sh 'pipeline_testing.py'
                }   
            }
    }
