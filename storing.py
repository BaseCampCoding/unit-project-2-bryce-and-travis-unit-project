import sqlite3
import json

con = sqlite3.connect('store-data-info.db')

cur = con.cursor()

try:
    cur.execute('CREATE TABLE Gender (Male TEXT, Women TEXT, Other TEXT')

class Person:
    def gender(g):
        if 
