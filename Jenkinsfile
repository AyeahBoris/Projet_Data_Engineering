pipeline{
  agent any
  stages {
    stage('Build Flask app'){
      steps{
        sh 'docker image build -t monapp .'
      }
    }
      stage('Run Flask App'){
          steps{
            sh 'docker run -p 5001:5001 -d monapp'
          }
        }
    stage('Testing'){
      steps{
        sh 'python integration_app.py'
        sh 'python other_app.py'
      }
    }
    stage('Docker images down'){
      steps{
        sh 'docker rm -f monapp'
      }
    }
}
