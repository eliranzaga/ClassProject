<<<<<<< HEAD
pipeline {
  agent { node { label 'slave01' } }

   stages {
      stage('Clone Sources') {
        steps {
          checkout scm
        } 
      }
      stage('Build') {
         steps {
            echo 'Build process..'            
            sh '''
                cd ${WORKSPACE}/scripts/
                chmod 755 *.sh
            '''
         }
      }      
        stage("Env Variables") {
            steps {
                sh "printenv"
            }
        }    
      stage('Test') {
         steps {
            echo 'Test process..'
            sh '''
              echo "Testing input string $PARAM" 
              cd ${WORKSPACE}/scripts
              ./reverse.sh $PARAM
              ./reverse.sh $PARAM > results
            '''
         }
      }
      stage('Saving Results') {
         steps {
            echo 'Saving Results process..'
            sh '''
	      report_file="${HOME}/Documents/Deployment/report"
              mkdir -p ${HOME}/Documents/Deployment/              
              if [ -f "${report_file}" ]; then
                echo "file ${report_file} exists"
              else
	              touch ${report_file}
              fi              
              echo "Build Number $BUILD_NUMBER" >> ${report_file}
              cat ${WORKSPACE}/scripts/results >> ${report_file}
	      echo "#############################" >> ${report_file}
            '''
         }
      }
      
   }
}
=======
pipeline {
  agent { node { label 'slave01' } }

   stages {
      stage('Clone Sources') {
        steps {
          checkout scm
        } 
      }
      stage('Execute C exe file') {
         steps {
            echo 'Compilation process..'
            sh '''
            echo "Testing input string $Language"
            '''
            sh '''
                echo "Running bin file"
                
            '''
         }
      }
      stage('Execute python script') {
         steps {
            echo 'Execute python script'
            sh '''
              chmod 755 ${WORKSPACE}/scripts/checkUserName.py
              ${WORKSPACE}/scripts/checkUserName.py $USER
            '''
            
         }
      }
      stage('Execute bash script') {
         steps {
            echo 'bash script..'
         }
      }
      
   }
}
>>>>>>> f4ece583e94369d1355ae105833e025d3afe5f6e
