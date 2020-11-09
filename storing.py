import sqlite3
import json

con = sqlite3.connect('store-data-info.db')

cur = con.cursor()

try:
    cur.execute('CREATE TABLE Person (Name TEXT, Email TEXT, Phone_number TEXT, Place TEXT, Job TEXT, Gender TEXT')
except:
    pass

ADMIN = []
with open("admin.json") as admin_file:
    READER = json.load(admin_file)
    for entry in READER:
        ADMIN.append(entry["name"])
    

class Admin:
    def __init__(self, name):
        self.name = name
        self.is_valid = name in ADMIN

    def __str__(self):
        return self.name
