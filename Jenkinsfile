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
<<<<<<< HEAD
            if [ "$LANGUAGE" = "C" ] || [ "$LANGUAGE" = "All" ]; then
               echo "yes i did"
=======
            if [ "$PARAM" = "C" ] || [ "$PARAM" = "All" ]; then
               echo "yes i didk"
>>>>>>> fcec91c2bc3863d49fb77fef0a574c726606f10d
            else
               echo "$LANGUAGE commands only are chosen to be executed!"
            fi
            '''
         }
      }
      stage('Execute Python script') {
         steps {
            echo 'Execute Python script'
            sh '''
            if [ "$LANGUAGE" = "Python" ] || [ "$LANGUAGE" = "All" ]; then
               echo "yes i did"
            else
               echo "$LANGUAGE commands only are chosen to be executed!"
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
            echo 'Bash script..'
            sh '''
            if [ "$LANGUAGE" = "Bash" ] || [ "$LANGUAGE" = "All" ]; then
               echo "yes i didd"
            else
               echo "$LANGUAGE commands only are chosen to be executed!"
            fi
            '''
         }
      }
      
   }
}
