import json
import mysql.connector

from ansible.plugins.cache.base import BaseCacheModule
from ansible import constants as C
from ansible.utils.display import Display

class CacheModule(BaseCacheModule):

    db_name = 'docker_facts'

    def __init__(self, *args, **kwargs):
        self._cache = {}
        try:
            cnx = mysql.connector.connect(user="docker", password='password', port=3306)
            cur = cnx.cursor()
            cur.execute('CREATE DATABASE {0}'.format(self.db_name))
        except:
            Display().display('db exists')
        cnx.database = self.db_name
        try:
            cur.execute("CREATE TABLE `facts` (`data` json DEFAULT NULL) ENGINE=InnoDB DEFAULT CHARSET=utf8;")
        except:
            Display().display('Table exists')

    def get(self, key):
        cnx = mysql.connector.connect(user="docker", password="password", port=3306, database=self.db_name)
        insert = "INSERT INTO facts (data) VALUES (\'{0}\') ".format(json.dumps(self._cache),)
        cnx.cursor().execute(insert)
        cnx.commit()
        cnx.close
        return self._cache.get(key)

    def set(self, key, value):
        self._cache[key] = value

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





