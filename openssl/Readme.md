## This is an example of how to work with OpenSSL in Ansible.
### If you want to use playbook in Jenkins you must create a secret text credential called and add it to your job. 
#### To do this follow next steps:
1. In **Build envirinment** section of you job mark **Use secret text(s) or file(s)**
2. In **Bindings** section of your job press **Add** and select **Secret text**
3. In **Variable** edit type **certificate_passphrase**.
4. Select **Specific credentials**.
5. If you already created a secret credential select it from drop down list, if not see item 6.
6. Press **Add** button with a key picture. In **Kind** section choose **secret text**. Enter your desired passphrase in **Secret** edit. Don't neglact to fill **Description**.
### You can create the job in Jenkins using the job_dsl.groovy file (you will need Job DSL Plugin to do that)
#### If you will use this script don't forget to change the variables on your own at the head of the file.
#### Both playbooks designed to use in Jenkins,but if you want to launch it from CLI you must add **-e "secretfraze=yoursecret"** at the end of your command:
> ansible-playbook -c local certificates_roles.yml -e "secretfraze=my_secret"
### Theare two Playbooks:
* certificates.yml : without roles
* certificates_roles.yml : with roles
#### CA_issue role:
##### This role is crafted to imitate Entermidiate CA. The role creates private key and selfsigned certificate during play.
#### Cert-sign role:
##### This role is developed for releasing certificates signed by our CA. While playing it creates some folders:
* pk - this folder holds private keys of our certificates
* csr - this folder keeps certificate signing requests of our certificates
* crt - this is output folder for our certificates
### If you choose **certificates.yml** to use all output files will be placed in the current folder.
#### Both plays creates next files in the current folder:
* CA.pem - private key for our CA. Keep it in save place and use for signing your certificates.
* CA.crt - CA certificate. Use it to sign our certificates and to confirm released certificates authenticity
* CA.csr - certificate signing request. 
#### Site-names are stored in **site_names** file in root folder in dict style:
> {'www.example.com','customer.example.com', '*.datastore.example.com'} .
