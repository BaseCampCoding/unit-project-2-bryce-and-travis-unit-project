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
            p = input("\nPick a Job and we will pull up a quick summary about that\njob. Then you will write a short application to apply for that job.")
            if p == "Robotics Automation Engineer":
                print("\nRobotics Automation Engineer")
                print("""\nNoble Plastics is an established Design, Automation, and Manufacturing company. We are currently 
                        expanding our robotic automation team.Noble is searching for motivated, qualified candidates to 
                        lead and help shape this segment of our business.\n
                        Automation engineers develop robust system designs and programs for external and internal 
                        customers. Noble continually invests in new technology and training to ensure our team has access to 
                        the best tools.""")
                x = input("\nDo you want to write your application for this Job [Y/N] ").upper
                if x == "Y":
                    
            
            


    elif choice == "update profile":
        print("updated")


def admin():
    while True:
        with open('jobs.json') as json_file:
            JOB_LIST = json.load(json_file)
        admin_options = ["view jobs", "view users", "add jobs", "delete jobs", "sign out"]
        admin_input = input("""
        Do you want to
            - View Jobs
            - View Users
            - Add Jobs
            - Delete Jobs
        """).lower()
        
        while admin_input not in admin_options:
            print("No such command")
            admin_input = input("""
        Do you want to
            - View Jobs
            - View Users
            - Add Jobs
            - Delete Jobs
        """).lower()
            if admin_input in admin_options:
                break
        
        if admin_input == "view jobs":
            
            cur.execute('SELECT name FROM Jobs')
            jobs = cur.fetchall()
            for j in jobs:
                print(j[0])
        
        elif admin_input == "view users":
            yn = ["y", "yes", "n", "no", "quit"]
            choices = input("Do you want to see a list of ALL users?")
            while choices not in yn:
                print(f"{choices} is not a valid answer")
        
        elif admin_input == "sign out":
            break
        
    

    



print(f"Welcome to Ndeed")

sign_in_options = ["sign in", "sign up", "sign out", "admin", "quit"]



while True:
    sign_in = input("""
        Do you want to
            - Sign in
            - Sign up
            - Quit
        """).lower()
    while sign_in not in sign_in_options:
        print("Invalid choice")
        sign_in = input("""
        Do you want to
            - Sign in
            - Sign up
            - Quit
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
                admin()
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

            place = input("What state do you live in: ").upper()
            if place == "quit":
                break
            cur.execute('SELECT st_name FROM States WHERE st_name = ? or abbreviation = ?', (place, place))
            state_check = cur.fetchall()
            while state_check == []:
                print("Please check spelling.")
                place = input("What state do you live in: ").upper()
                cur.execute('SELECT st_name FROM States WHERE st_name = ? or abbreviation = ?', (place, place))
                state_check = cur.fetchall()
                if state_check != []:
                    break
            if len(list(place)) == 2:
                cur.execute('SELECT st_name FROM States WHERE abbreviation = ?', (place,))
                fetch_state = cur.fetchall()
                state_name = fetch_state[0][0]
        

            job = None
            gender = input("Gender: ")
            if gender == "quit":
                break
            if gender != "male" and gender != "female":
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
            cur.execute('INSERT INTO Person VALUES (?, ?, ?, ?, ?, ?, ?)', (name, age, email, str(cell), str(state_name), job, gender))
            con.commit()
            break
    elif sign_in == "quit":
        break
       
print(2+2)






























# def job_application():
#     do you want to apply? [y/n]

#     if yes:
#         do you need to change any of your personal information before it is sent?
#         if yes:
#            change =  what do you want to change?
#             phone number
#             new_change enter your number.

#             UPDATE person SET change = ?), (new_change,))