__author__ = 'Bogdan'
import sqlite3
#sqlite3.connect(':memory:') create BD in memory
#connect returns connection object
#sqlite3.connect('test.db') create BD in file

#conn = sqlite3.connect('test.db')
#cursor = conn.cursor()

#query = 'CREATE TABLE students(id INTEGER, NAME TEXT, AGE INTEGER)'
#cursor.execute(query)
#insert = 'INSERT into students VALUES(1, "Nick", 20)'
#cursor.execute(insert)
#conn.commit()

#how to fill in table
#student_data = [('Vasya', 5), ('Tanya', 5), ('Vasya', 5)]
#cursor.executemany('VALUE(NULL, ?, ?)', student_data)




class Goods(object):
    def __init__(self, test_db):
        self.connection = sqlite3.connect(test_db)
        self.cursor = self.connection.cursor()
        self.table = 'CREATE TABLE goods(id INTEGER, NAME TEXT, WEIGHT INTEGER)'
        self.cursor.execute(self.table)
        self.id = 0
        #closed method
        #self.__data

    def insert(self, good, weight):
        query = 'INSERT into goods VALUES ({}, "{}", {})'.format(self.id, good, weight)
        self.cursor.execute(query)
        self.connection.commit()
        self.id += 1

    def db_search(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()



