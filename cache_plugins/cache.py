import json

from ansible.plugins.cache.base import BaseCacheModule
from ansible.utils.display import Display
from ansible.errors import AnsibleError

try:
    import mysql.connector
except ImportError:
    raise AnsibleError("No mysql lib found. Please, install 'pip install mysql-connector-python'")

class CacheModule(BaseCacheModule):

    db_name = 'docker_facts'

    def __init__(self, *args, **kwargs):
        self._cache = {}
        try:
            cnx = mysql.connector.connect(user="docker", password='password', port=3306)
            cur = cnx.cursor()
        except mysql.connector.Error:
            raise AnsibleError("Cann't connect do MySql. Check your credentials and port")
        else:
            try:
                cnx.database = self.db_name
            except mysql.connector.DatabaseError:
                try:
                    cur.execute('CREATE DATABASE {0}'.format(self.db_name))
                except mysql.connector.DatabaseError as e:
                    raise AnsibleError("Cannot create database {0}: {1}".format(self.db_name,e.msg))
            try:
                cur.execute("CREATE TABLE `facts` (`data` json DEFAULT NULL) ENGINE=InnoDB DEFAULT CHARSET=utf8;")
            except:
                Display().display("Database '{0}' exists".format(self.db_name))

    def get(self, key):
        return self._cache.get(key)

    def set(self, key, value):
        self._cache[key] = value
        cnx = mysql.connector.connect(user="docker", password="password", port=3306, database=self.db_name)
        insert = "INSERT INTO facts (data) VALUES (\'{0}\') ".format(json.dumps(self._cache), )
        cnx.cursor().execute(insert)
        cnx.commit()
        cnx.close

    def keys(self):
        return self._cache.keys()

    def contains(self, key):
        return key in self._cache

    def delete(self, key):
        del self._cache[key]

    def flush(self):
        self._cache = {}

    def copy(self):
        return self._cache.copy()





