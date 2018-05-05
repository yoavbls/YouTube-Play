pipeline {
  agent any
  stages {
    stage('Install Requirements') {
      steps {
        sh 'pip install -r requirements.txt'
      }
    }
    stage('Sainity Test') {
      steps {
        sh 'python -m pytest -v test_gold.py'
      }
    }
  }
}