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
            if [ "$LANGUAGE" = "C" ] || [ "$LANGUAGE" = "All" ]; then
               echo "yes i didd"
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
               cd ${WORKSPACE}/scripts/
               chmod 755 *.py
              ${WORKSPACE}/scripts/python.py 
            '''
            
         }
      }
      stage('Execute bash script') {
         steps {
            echo 'Bash script..'
            sh '''
            if [ "$LANGUAGE" = "Bash" ] || [ "$LANGUAGE" = "All" ]; then
               cd ${WORKSPACE}/scripts/
               chmod 755 *.sh
               ./bashscript.sh $LANGUAGE
            else
               echo "$LANGUAGE commands only are chosen to be executed!"
            fi
            '''
         }
      }
      
   }
}
