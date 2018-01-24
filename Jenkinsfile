node {
  stage('Checkout') {
  	git url: 'https://github.com/mbialitskiy/ansible-.git', branch:'certificates_sign'
        checkout scm
  }        
 
 stage('AddAnsible') {      
   withCredentials([string(credentialsId:'certificate_passphrase',variable:'certificate_passphrase')]){
 	ansiblePlaybook(
	        playbook:'certificates_roles.yml',
                ansibleName: 'ansible'  
        )
   } 
 }
}
