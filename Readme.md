# Trainig in writings plugins for ansible

1. lookup plugin search content in github (use with main.yml)
2. cache plagin stores facts in MySql db (use with main.yml)
3. action plagin download tar.gz from link in file and extract it to current dir (use with action.yml)

###### no encryption for creds done cause it is only for training

## To check lookup plugins:

sudo pip install PyGithub

#### fill requred fields

⋅⋅* repository_name - name of your repo
⋅⋅* file - filename in your repo

- debug:
      msg : "{{ lookup('lookup_git', username, password) }} " - show all repos for user

- debug:
      msg : "{{ lookup('lookup_git', username, password, repository_name) }} " - show files in repo

- debug:
      msg : "{{ lookup('lookup_git', username, password, repository_name, file) }} " - find file in repo

## To check cache plugin:

1. sudo docker pull mysql/mysql-server

2. sudo docker run --name=mysql1 -p 3306:3306 -p 33060:33060 -d mysql/mysql-server

3. sudo docker logs mysql1 2>&1 | grep GENERATED

4. Copy generated password

5. sudo docker exec -it mysql1 mysql -uroot -p

6. paste generated password

7. ALTER USER 'root'@'localhost' IDENTIFIED BY 'newpassword';

8. CREATE USER 'docker'@'%' IDENTIFIED BY 'password';

9. GRANT ALL PRIVILEGES ON *.* TO 'docker'@'%' WITH GRANT OPTION;

10. FLUSH PRIVILEGES;

11. \q

12. sudo pip install mysql-connector-python

```bash
ansible-playbook -c local main.yml 
```
## To check action plugin:
```bash
ansible-playbook -c local action.yml 
```
