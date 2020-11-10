import sqlite3
import json

con = sqlite3.connect('store-data-info.db')

cur = con.cursor()

cur.execute('CREATE TABLE IF NOT EXISTS Person (Name TEXT, Age INTEGER, Email TEXT, Phone_number TEXT, Place TEXT, Job TEXT, Gender TEXT)')

ADMIN = []
with open("admin.json") as admin_file:
    READER = json.load(admin_file)
    for entry in READER:
        ADMIN.append([entry["name"], entry["password"]])
        





class Admin:
    def __init__(self, log_in):
        self.log_in = log_in
        self.is_valid = log_in in ADMIN

    def __str__(self):
        return self.log_in

print(ADMIN)

cur.execute("CREATE TABLE IF NOT EXISTS Log_in (name TEXT, password TEXT)")



cur.execute("CREATE TABLE IF NOT EXISTS States (name TEXT, abbreviation TEXT)")
states = [("Alabama", "AL"),
("Alaska", "AK"),
("Arizona", "AZ"),
("Arkansas", "AR"),
("California", "CA"),
("Colorado", "CO"), 
("Connecticut", "CT"),
("Delaware", "DE"),
("Florida", "FL"),
("Georgia", "GA"),
("Hawaii", "HI"),
("Idaho", "ID"),
("Illinois", "IL"),
("Indiana", "IN"),
("Iowa", "IA"),
("Kansas", "KS"),
("Kentucky", "KY"),
("Louisiana", "LA"),
("Maine", "ME"),
("Maryland", "MD"),
("Massachusetts", "MA"),
("Michigan", "MI"),
("Minnesota", "MN"),
("Mississippi", "MS"),
("Missouri", "MO"),
("Montana", "MT"),
("Nebraska", "NE"),
("Nevada", "NV"),
("New Hampshire", "NH"),
("New Jersey", "NJ"),
("New Mexico", "NM"),
("New York", "NY"),
("North Carolina", "NC"),
("North Dakota", "ND"),
("Ohio", "OH"),
("Oklahoma", "OK"),
("Oregon",  "OR"),
("Pennsylvania", "PA"),
("Rhode Island", "RI"),
("South Carolina", "SC"),
("South Dakota", "SD"),
("Tennessee", "TN"),
("Texas", "TX"),
("Utah", "UT"),
("Vermont", "VT"),
("Virginia", "VA"),
("Washington", "WA"),
("West Virginia", "WV"),
("Wisconsin", "WI"),
("Wyoming", "WY")]

all_states = []
for state in states:
    for word in state:
        all_states.append(word.lower())