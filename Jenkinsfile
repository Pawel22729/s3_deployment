pipeline {
    agent any
    environment {
        app_url = "https://github.com/Pawel22729/JS/archive/master.zip"
        bucket = "plasak-one"
    }
    stages {
        stage("Download") {
            steps {
                sh "python scripts/download.py -u https://github.com/Pawel22729/JS/archive/master.zip"
            }
        }
        stage("Unpack") {
            steps {
                sh "python scripts/unpack.py application_package.zip"
            }
        }
        stage("Sync") {
            steps {
                sh "python scripts/sync.py unpacked/ ${bucket}"
            }
        }
        stage("Verify") {
            steps {
                echo "Verify..."
            }
        }
    }
    post {
        always {
            sh "rm -rf unpacked"
            sh "rm -rf static_assets_app*"
        }
    }
}