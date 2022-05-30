pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        echo 'Let\'s build the image'
        sh 'docker image build -t monapp .'
      }
    }

    stage('Runnning the image') {
      steps {
        echo 'Running the image'
        sh 'docker run -p 5001:5001 -d monapp'
      }
    }

    stage('Final') {
      steps {
      
        sh 'docker rmi -f monapp'

      }
    }

  }
}
