pipeline {
    agent any
    stages {
        stage('Checkout Code') {
            steps {
                git url: 'https://github.com/ch4949/my-jenkins-project2.git', branch: 'main'
            }
        }
        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install -r requirements.txt'  # 修改为bat
            }
        }
        stage('Run Tests') {
            steps {
                bat 'python -m pytest test_main.py'  # 修改为bat
            }
        }
    }
}
