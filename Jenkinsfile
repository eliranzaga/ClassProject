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
            if [ "$PARAM" = "C" ] || [ "$PARAM" = "All" ]; then
               echo "yes i did"
            else
               echo "$PARAM commands only are chosen to be executed!"
            fi
            '''
         }
      }
      stage('Execute Python script') {
         steps {
            echo 'Execute Python script'
            sh '''
            if [ "$PARAM" = "Python" ] || [ "$PARAM" = "All" ]; then
               echo "yes i did"
            else
               echo "$PARAM commands only are chosen to be executed!"
            fi
            '''
            sh '''
              chmod 755 ${WORKSPACE}/scripts/checkUserName.py
              ${WORKSPACE}/scripts/checkUserName.py $USER
            '''
            
         }
      }
      stage('Execute bash script') {
         steps {
            echo 'bash script..'
            sh '''
            if [ "$PARAM" = "Bash" ] || [ "$PARAM" = "All" ]; then
               echo "yes i did"
            else
               echo "$PARAM commands only are chosen to be executed!"
            fi
            '''
         }
      }
      
   }
}
