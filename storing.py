import sqlite3
import json

con = sqlite3.connect('store-data-info.db')

cur = con.cursor()

cur.execute('CREATE TABLE IF NOT EXISTS Person (Name TEXT, Age INTEGER, Email TEXT, Phone_number INTEGER, Place TEXT, Job TEXT, Gender TEXT)')
cur.execute("CREATE TABLE IF NOT EXISTS Log_in (Name TEXT, Username TEXT, Password TEXT)")

ADMIN = []
with open("admin.json") as admin_file:
    READER = json.load(admin_file)
    for entry in READER:
        ADMIN.append([entry["name"], entry["password"]])

class User:
    def __init__ (self, username, password):
        self.username = username
        self.password = password
        cur.execute('SELECT Username, Password FROM Log_in WHERE Username = ? AND Password = ?', (username, password))
        user_check = cur.fetchall()
        self.is_valid = user_check != []


class Admin:
    def __init__(self, log_in):
        self.log_in = log_in
        self.is_valid = log_in in ADMIN

    def __str__(self):
        return self.log_in

print(ADMIN)

cur.execute("CREATE TABLE IF NOT EXISTS Jobs(Name TEXT, Company_name TEXT, Salary TEXT, Job_Type TEXT, Schedule TEXT,  Experience TEXT, Location TEXT)")

cur.execute('''INSERT INTO Jobs VALUES 
        ("Robotics Automation Engineer", "Noble Plastics Inc.", "$60,000 - $75,000 a year", "Full-time", "None", "Robotics: 2 years (Preferred)", "Mississippi"),
        ("Plant Electrician", "Express Grain Terminals, LLC", "$23 - $30 an hour", "Full-time", "8 hour shift", "Industrial electrician experience: 5 years (Preferred)", "Greenwood, MS 38930"),
        ("Full Stack Developer", "Power Fusion Media", "$75,000 - $85,000 a year", "Full time", "10 - 12 hour shift", "Two years of experience as a Developer or related", "Memphis, TN")
        ''')


cur.execute("CREATE TABLE IF NOT EXISTS States (st_name TEXT, abbreviation TEXT)")
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





for state in states:
    cur.execute('INSERT INTO states VALUES (?, ?)', (state[0].lower(), state[1].lower()))
    print(state[0])
    print(state[1])


