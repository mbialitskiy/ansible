## This is an example of how to work with OpenSSL in Ansible.
#### Tested at:
* anisble 2.4.2.0
* jenkins 2.89.2
* docker 17.12.0-ce
### If you want to use playbook in Jenkins you must create a secret text credential called and add it to your job. If you want to automate the process you can use Job_dsl.groovy script or Jenkinsfile for pipeline. 
### If you prefer to add credentials manually this follow next steps:
1. In **Build envirinment** section of you job mark **Use secret text(s) or file(s)**
2. In **Bindings** section of your job press **Add** and select **Secret text**
3. In **Variable** edit type **certificate_passphrase**.
4. Select **Specific credentials**.
5. If you already created a secret credential select it from drop down list, if not see item 6.
6. Press **Add** button with a key picture. In **Kind** section choose **secret text**. Enter your desired passphrase in **Secret** edit. Don't neglact to fill **Description**.
#### Before using this script don't forget to change the variables on your own at the head of the file.
#### Both playbooks designed to use in Jenkins,but if you want to launch it from CLI you must add **-e "secretfraze=yoursecret"** at the end of your command:
> ansible-playbook -c local certificates_roles.yml -e "secretfraze=my_secret"
### Theare two Playbooks:
* certificates.yml : without roles
* certificates_roles.yml : with roles
#### CA_issue role:
##### This role is crafted to imitate Entermidiate CA. The role creates private key and selfsigned certificate during play.
##### In **templates** folder you can find a template config **csr_conf.j2** for CA certificate. Default variables values are stored in **vars** folder.
#### Cert-sign role:
##### This role is developed for releasing certificates signed by our CA. While playing it creates some folders:
* out/pk - this folder holds private keys of our certificates
* out/csr - this folder keeps certificate signing requests of our certificates
* out/crt - this is output folder for our certificates
* out/pcks12 -this folder stores certificates in pkcs12 format
* out/v3 - this folder stores extended configs for certificates
##### In **templates** folder the **v3_ext.j2** template config is placed for holding info about extended certificate usage.
##### In **vars** the default varaibles for certificate destinguished names are stored plus names of folders for create/delete
#### Docker_nginx role:
##### This role is developed to start docker container with nginx from playbook
##### The **templates** folder stores the **vhost.j2** template config file for nginx
##### Don't forget do add this lines to your sudoers file:
> jenkins ALL=(ALL) NOPASSWD:/bin/sh
> jenkins ALL=(ALL) NOPASSWD:/path/to/docker
#### Jenkins_cert_job role:
##### This role creates a new job for issue certificates in your Jenkins from ansible by copying preconfigured xml job config to your jenkins job directory. After that the jenkins is restarted and the job is called to run. 
##### In **templates** folder there is the xml j2 template for a jenkins job. Default variables values are stored in **vars**
##### To find a **token** go to url *http://jenkins/me/configure* and hit **show token**
#### Jenkins_cert_job_cli role:
##### This role do pretty much the same that previous one but uses jenkins-cli.jar for creating and running job.
# If you choose **certificates.yml** to use all output files will be placed in the current folder.
#### Both plays creates next files in the current folder:
* CA.pem - private key for our CA. Keep it in save place and use for signing your certificates.
* CA.crt - CA certificate. Use it to sign our certificates and to confirm released certificates authenticity
* CA.csr - certificate signing request. 
#### Site-names for certs are stored in **site_names** file in root folder in dict style:
> {'www.example.com','customer.example.com', '*.datastore.example.com'} .
