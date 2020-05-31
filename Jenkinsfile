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
            echo 'Compilation c script'
            sh '''
            if [ "$LANGUAGE" = "C" ] || [ "$LANGUAGE" = "All" ]; then
               cd ${WORKSPACE}/scripts/
               chmod 755 *.c
               gcc c_script.c -o c_script
				./c_script
				./c_script > results
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
              ${WORKSPACE}/scripts/python.py $LANGUAGE > results
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
               ./bashscript.sh > results
            else
               echo "$LANGUAGE commands only are chosen to be executed!"
            fi
            '''
         }
      }
      
            stage('Execute java script') {
         steps {
            echo 'Compilation java script..'
            sh '''
            if [ "$LANGUAGE" = "Java" ] || [ "$LANGUAGE" = "All" ]; then
               cd ${WORKSPACE}/scripts/
               chmod 755 *.java
               javac java.java
               java java > results
            else
               echo "$LANGUAGE commands only are chosen to be executed!"
            fi
            '''
         }
      }
            stage('Saving Log file') {
         steps {
            echo 'Saving log file process..'
            sh '''
	      log_file="${HOME}/Documents/ProjectLog/log"
              mkdir -p ${HOME}/Documents/ProjectLog/              
              if [ -f "${log_file}" ]; then
                echo "file ${log_file} exists"
              else
	              touch ${log_file}
              fi              
              echo "Build Number $BUILD_NUMBER" >> ${log_file}
              cat ${WORKSPACE}/scripts/results >> ${log_file}
	      echo "#############################" >> ${log_file}
            '''
         }
      }
      
   }
}
