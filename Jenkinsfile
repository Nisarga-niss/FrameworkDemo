pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Find Python Path') {
            steps {
                script {
                    def pythonPath = bat(
                        script: 'where python',
                        returnStdout: true
                    ).trim()

                    env.PYTHON_PATH = pythonPath.split("\r\n")[0]
                    echo "Python path is: ${env.PYTHON_PATH}"
                }
            }
        }

        stage('Create Virtual Environment') {
            steps {
                bat "\"${env.PYTHON_PATH}\" -m venv venv"
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '''
                venv\\Scripts\\python -m pip install --upgrade pip
                venv\\Scripts\\python -m pip install -r requirements.txt
                '''
            }
        }

        stage('Run All Tests') {
            steps {
                bat '''
                venv\\Scripts\\python -m pytest tests --alluredir=reports\\allure-results
                '''
            }
        }

        stage('Generate Allure Report') {
            steps {
                allure includeProperties: false,
                       jdk: '',
                       results: [[path: 'reports/allure-results']]
            }
        }
    }

    post {
        always {
            echo 'Test execution completed'
        }
        success {
            echo 'Build Passed'
        }
        failure {
            echo 'Build Failed'
        }
    }
}
