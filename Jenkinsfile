pipeline {
  agent none
  stages {
    stage('Docker Build') {
      agent any
      steps {
        sh 'docker build -t alan1402/bigdata:0.1 .'
      }
    }
    stage('Docker push') {
      agent any
      steps {
        sh 'docker push alan1402/bigdata:0.1'
      }
    }
    stage('Deployment') {
      agent any
      steps {
        sh 'docker compose up --build'
      }
    }
    stage('Test') {
      agent any
      steps {
        sh 'python3 tests/test_api.py'
      }
    }
  }
}