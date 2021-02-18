pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                sh '''set +x
                echo "========================================================="
                echo "                    MIMIC | BUILD                        "
                echo "========================================================="
                set -x'''

                git 'https://github.com/birthdaysgift/mimic'
                sh 'docker-compose \
                            --file docker-compose.prod.yml \
                            --env-file /.mimic.env \
                            up --build --remove-orphans --detach'
            }
        }
        stage('test') {
            steps {
                sh '''set +x
                echo "========================================================="
                echo "                    MIMIC | TEST                         "
                echo "========================================================="
                set -x'''
            }
        }
        stage('deploy') {
            steps {
                sh '''set +x
                echo "========================================================="
                echo "                    MIMIC | DEPLOY                       "
                echo "========================================================="
                set -x'''
            }
        }
    }
}