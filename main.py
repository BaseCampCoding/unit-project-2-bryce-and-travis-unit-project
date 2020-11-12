import json
from storing import *
from pprint import pprint
import PySimpleGUI as gui

def application():
    print("Welcome to your Application\n")
    c = input("Is there anything that you want to change in your profile?[Y/N] ").lower
    if c == "y":
        print
def look_for_job():
    cur.execute('SELECT DISTINCT Job_name FROM Jobs') # Distinct only selects a value once
    for job in cur.fetchall():
        print(f'- {job[0]}')
    p = input("What job do you want to pick? ")
    questions = ["company_name", "description", "salary", "job_type", "schedule", "experience", "location"]
    while True:
        user_question = input("""
    What do you want to know about this job?
    -Company_Name
    -Description
    -Salary
    -Job_Type
    -Schedule
    -Experiece
    -Location
    If you are done looking type "quit"
    """).lower()
        if user_question in questions:
            index = questions.index(user_question)
            cur.execute(f'SELECT DISTINCT {questions[index]} FROM Jobs WHERE job_name = ?', (p,))
            job_des = cur.fetchall()
            print(job_des[0][0])
        elif user_question == "quit":
            y = input("Do you want to put this job in your profile? [Y/N] ")
            if y =="y":
                job = p
                break
            elif x == "n":
                break
    

def Employee():
    user_options = ["view jobs", "update profile", "application"]
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
        look_for_job()

    elif choice == "update profile":
        while True:
            print("""
- Full Name
- Age
- Email
- Phone Number
- Place
- Job
- Gender
""")
            change = input("What do you want to change?(If not type 'quit') ").lower()
            cc = ["full name", "age", "email", "phone number", "place", "gender"]
            if change in cc:
                new_change = input(f"What do you want to change in {change}? ")
                cur.execute(f'UPDATE Person SET {change} = {new_change} WHERE name = ?', (name, ))
            elif change == 'job':
                look_for_job()
            elif change  == "quit":
                break
        


def admin():
    while True:

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
            choices = input("Do you want to see a list of ALL users? [y/n] " ).lower()
            while choices not in yn:
                print(f"{choices} is not a valid answer")
                choices = input("Do you want to see a list of ALL users? [y/n] ").lower()
                if choices in yn:
                    break
            if choices == "y" or choices == "yes":
                cur.execute('SELECT name FROM PERSON')
                all_users = cur.fetchall()
                for user in all_users:
                    print(user[0])
            elif choices == "n" or choices == "no":
                pass

            while True:    
                one_user = input("What user so you want information for? ")
                cur.execute('SELECT name FROM person WHERE name = ?', (one_user,))
                isuser = cur.fetchall()
                if isuser == []:
                    print(f"We don't have a user by the name of {one_user}.")
                elif isuser != []:
                    cur.execute('SELECT * FROM person WHERE name = ?', (one_user,))
                    print(cur.fetchone())

                
        
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
            cur.execute('SELECT Name FROM log_in WHERE Username = ?', (username,))
            name = cur.fetchone()
            print(f"Welcome {name[0]}").upper
            Employee()
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
            name = input("Full name: ").lower()
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
            while True:
                username = input("\nPlease enter in a username: ")
                cur.execute('SELECT username FROM log_in WHERE username = ?', (username,))
                username_list = cur.fetchall()
                if username_list != []:
                    print("That username is already being used!")
                elif username_list == []:
                    break
            
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