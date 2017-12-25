## Cache plugin for ansible that stores facts in mysql. 

#You will need MySql for use:

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



