pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        echo 'Let\'s build the image'
        sh 'docker build -t monapp .'
      }
    }

    stage('Runnning the image') {
      steps {
        echo 'Running the image'
        sh 'docker run --name myflaskcontainer -d -p 5001:5001 monapp'
      }
    }

    stage('Final') {
      steps {
      
        sh 'docker rmi -f monapp'

      }
    }

  }
