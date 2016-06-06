import sqlite3

# encoding=utf-8

class SQL(object):
    def __init__(self, test_db):
        self.connection = sqlite3.connect(test_db)
        self.cursor = self.connection.cursor()
        self.table = 'CREATE TABLE goods(id INTEGER, NAME TEXT, WEIGHT INTEGER, NUM INTEGER)'
        self.cursor.execute(self.table)
        #closed method
        #self.__data

    def insert(self, id, good, weight, num):
        query = 'INSERT into goods VALUES ({}, "{}", {}, {})'.format(id, good, weight, num)
        self.cursor.execute(query)
        self.connection.commit()

    def search_sql(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()



