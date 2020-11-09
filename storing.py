import sqlite3
import json

con = sqlite3.connect('store-data-info.db')

cur = con.cursor()

try:
    cur.execute('CREATE TABLE Person (Name TEXT, Age INTEGER, Email TEXT, Phone_number TEXT, Place TEXT, Job TEXT, Gender TEXT')
except:
    pass

with open("admin.json") as admin_file:
    ADMIN = json.load(admin_file)

class Admin:
    def __init__(self, name):
        self.name = name
        self.is_valid = name in ADMIN

    def __str__(self):
        return self.name

