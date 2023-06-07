pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'sudo docker container ls'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}