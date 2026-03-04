pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Create Virtual Environment') {
            steps {
                bat '''
                python -m venv venv
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '''
                call venv\\Scripts\\activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run All Tests') {
            steps {
                bat '''
                call venv\\Scripts\\activate
                pytest tests --ignore=tests/test_orange_hrm_login.py --alluredir=reports\\allure-results
                '''
            }
        }

        stage('Generate Allure Report') {
            steps {
                allure includeProperties: false,
                       jdk: '',
                       commandline: 'allure',
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
