## This is an example of how to work with OpenSSL in Ansible.
### Theare two Playbooks:
* certificates.yml : without roles
* certificates_roles.yml : with roles
##### If you want to use playbook in Jenkins you must create a secret text credential called and add it to your job. 
##### To do this follow next steps:
1. In **Build envirinment** section of you job mark **Use secret text(s) or file(s)**
2. In **Bindings** section of your job press **Add** and select **Secret text**
3. In **Variable** edit type **certificate_passphrase**.
4. Select **Specific credentials**.
5. If you already created a secret credential select it from drop down list, if not see item 6.
6. Press **Add** button with a key picture. In **Kind** section choose **secret text**. Enter your desired passphrase in **Secret** edit. Don't neglact to fill **Description**.

##### Both playbooks designed to use in Jenkins, if you want to launch it from CLI you must add **-e "secretfraze=yoursecret"** at the end of your command:
> ansible-playbook -c local certificates_roles.yml -e "secretfraze=my_secret"

