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
      }
    }
    stage('Testing'){
      steps{
        sh 'python test_app.py'
        sh 'python test_app.py'
      }
    }
    stage('Docker images down'){
      steps{
        sh 'docker rm -f redis'
        sh 'docker rm -f myflaskapp_c'
        sh 'docker rmi -f myflaskapp'
      }
    }
  }
}
