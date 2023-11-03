pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'kshanmukha1501/flask:v8'
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

		stage('Push to DockerHub') {
			steps {
				withCredentials([usernamePassword(credentialsId: 'DockerHubCredentials', passwordVariable: 'DOCKER_PASSWORD', usernameVariable: 'DOCKER_USERNAME')]) {
					script {
						// Login to Docker Hub
						bat "echo Password: %DOCKER_PASSWORD% , %DOCKER_USERNAME%"
						bat "docker login -u %DOCKER_USERNAME% --password %DOCKER_PASSWORD%"
						// Push the image to Docker Hub
						bat "docker push ${DOCKER_IMAGE}"
					}
				}
			}
		}

        stage('Deploy with Docker Compose') {
            steps {
                script {
                    // Stop the currently running services
                    bat "docker-compose down"

                    // Pull the new images from dockerhub
                    bat "docker-compose pull"

                    // Start the services again with the new images
                    bat "docker-compose up -d"
                }
            }
        }
    }
}
