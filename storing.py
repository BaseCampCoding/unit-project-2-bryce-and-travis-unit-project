import sqlite3
import json

con = sqlite3.connect('store-data-info.db')

cur = con.cursor()

try:
    cur.execute('CREATE TABLE Person (Name TEXT, Age INTEGER, Email TEXT, Phone_number TEXT, Place TEXT, Job TEXT, Gender TEXT')
except:
    pass


class Admin:
    def 
        
