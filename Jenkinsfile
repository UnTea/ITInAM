pipeline{
  agent any
  stages{
    stage('build'){
      steps{
        echo '-----test-----'
        git 'https://github.com/UnTea/ITInAM'
        bat 'docker-compose up -d'
      }
    }
  }
}