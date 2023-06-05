pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh "sudo docker-compose up --build"
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