pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh "docker-compose up"
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