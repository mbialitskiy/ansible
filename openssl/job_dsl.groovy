def git_repo='https://github.com/mbialitskiy/ansible-.git'
def git_branch='certificates_sign'
def ansible_name='ansible'
def jenkins_cred_for_job = 'certificate_passphrase'

job('AnsibleSSL') {

  scm {
    git (git_repo,git_branch)
  }

  wrappers {
    credentialsBinding {
       string('certificate_passphrase', jenkins_cred_for_job)
        }
    }

  steps {
    ansiblePlaybook('features/certificates_sign/certificates_roles.yml') {       
        ansibleName(ansible_name)       
              
    }
  }
  
}
