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
               cd ${WORKSPACE}/scripts/
               chmod 755 *.c
               gcc c_script.c -o c_script
				./c_script
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
               cd ${WORKSPACE}/scripts/
               chmod 755 *.py
              ${WORKSPACE}/scripts/python.py $LANGUAGE
            else
               echo "$LANGUAGE commands only are chosen to be executed!"
            fi
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
               ./bashscript.sh 
            else
               echo "$LANGUAGE commands only are chosen to be executed!"
            fi
            '''
         }
      }
      
   }
}
