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
            if [ "$PARAM" = "C" ]; then
               yes i did
            else
               fuck off
            fi
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
