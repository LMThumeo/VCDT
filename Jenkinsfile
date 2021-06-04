

pipeline {
    agent any
    stage {
       stage("build") {
            steps {
               echo "Build the project";
            }
        }
        stage("test") {
            steps {
                echo "Run test";
            }
        }
        stage("deploy") {
            steps {
               echo "Deploy project";
            }
        }
    }
}
