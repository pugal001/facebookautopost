pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'sudo docker-compose up --build'
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