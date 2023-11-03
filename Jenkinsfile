pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'kshanmukha1501/flask:v5'
        DOCKER_CREDENTIALS = 'DockerHubCredentials'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${DOCKER_IMAGE}")
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    docker.withRegistry('https://registry.hub.docker.com', '${DOCKER_CREDENTIALS}') {
                        docker.image("${DOCKER_IMAGE}").push()
                    }
                }
            }
        }
		
        stage('Deploy with Docker Compose') {
            steps {
                script {
                    // Stop the currently running services
                    sh "docker-compose down"

                    // Pull the new images
                    sh "docker-compose pull"

                    // Start the services again with the new images
                    sh "docker-compose up -d"
                }
            }
        }
    }
}
