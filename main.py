import json
from storing import *
import pprint
import PySimpleGUI as gui



def User():
    with open('jobs.json') as json_file:
        JOB_LIST = json.load(json_file)

    user_options = ["view jobs", "update profile"]
    choice = input("""
    Do you want to
        -View Jobs
        -Update Profile
    """).lower()
    while choice not in user_options:
        print(f"{choice} is not a valid option.")
        choice = input("""
    Do you want to
        -View Jobs
        -Update Profile
    """).lower()
        if choice in user_options:
            
            break
    
    if choice == "view jobs":
        cur.execute('SELECT * FROM Jobs')
        pprint(cur.fetchall())


    elif choice == "update profile":
        print("updated")


# def admin():
#     User()

    



print(f"Welcome to Ndeed")

sign_in_options = ["sign in", "sign up", "sign out", "admin"]



while True:
    sign_in = input("""
        Do you want to
            - Sign in
            - Sign up
        """).lower()
    while sign_in not in sign_in_options:
        print("Invalid choice")
        sign_in = input("""
        Do you want to
            - Sign in
            - Sign up
        """).lower()
        if sign_in in sign_in_options:
            break
    
    if sign_in == "sign in":
        print("Sign in your account")
        username = input("Username: ")
        if username == "quit":
            break
        password = input("Password: ")
        log = User(username, password)
        if password == "quit":
            break
        if log.is_valid:
            cur.execute('SELECT name FROM log_in WHERE username = ?', (username,))
            print(f"Welcome {name}")
            User()
            break
        else:
            print("This account doesn't exist.")
    

    elif sign_in == "admin":
        print("Enter your Admin account")
        while True:
            name = input("Name: ")
            if name == "quit":
                break
            password = input("Password: ")
            account = Admin([name, password])
            if password == "quit":
                break
            if account.is_valid:
                print(f"Welcome {name}")
                break
            else:
                print("Invalid account.")
            
    
    elif sign_in == "sign up":
        while True:
            name = input("Full name: ")
            if name == "quit":
                break
            while True:
                age = input("Age: ")
                if age == "quit":
                    break
                if age.isdigit():
                    age = int(age)
                    break
                else:
                    print("Please enter a numerical value.")

            if age == "quit":
                break
            email = input("Email: ")
            if email == "quit":
                break
            cur.execute('SELECT email FROM Person WHERE email = ?', (email,))
            emails = cur.fetchall()
            if emails != []:
                print("That email is already being used! You should sign in.")
                break

            while True:    
                cell = input("Phone number: (digits only) ")
                if cell == "quit":
                    break
                if cell.isdigit() and len(list(cell)) == 10:
                    cell = int(cell)
                    break
                else:
                    print("Please enter a 10 digit cell phone number.")
            
            if cell == "quit":
                    break

            place = input("What state do you live in: ").lower()
            if place == "quit":
                break
            cur.execute('SELECT st_name FROM States WHERE st_name = ? or abbreviation = ?', (place))
            state_check = cur.fetchall()
            while state_check == []:
                print("Please check spelling.")
                place = input("What state do you live in: ").lower()
                if state_check != []:
                    break
            if len(list(place)) == 2:
                cur.execute('SELECT name FROM States WHERE abbreviation = ?', (place))
                fetch_state = cur.fetchall()
                state_name = fetch_state[0]
        

            job = None
            gender = input("Gender: ")
            if gender == "quit":
                break
            if gender != "male" or gender != "female":
                gender = "other"

            username = input("\nPlease enter in a username: ")
            cur.execute('SELECT username FROM log_in WHERE username = ?', (username,))
            cur.fetchall()
            if username != []:
                print("That username is already being used!")
            
            password = input("Please enter a password for your account: ")
            if password == "quit":
                break
            cur.execute('INSERT INTO log_in VALUES (?, ?, ?)', (name, username, password))
            cur.execute('INSERT INTO Person VALUES (?, ?, ?, ?, ?, ?, ?)', (name, age, email, str(cell), state_name, job, gender))
            cur.execute('SELECT * FROM Person')
            con.commit()
            break
        
print(2+2)




