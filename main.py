import json
from storing import *
from pprint import pprint
import PySimpleGUI as gui

def application():
    print("Welcome to your Application\n")
    c = input("Is there anything that you want to change in your profile?[Y/N] ").lower()
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
            print(job_des[0])
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
        cur.execute('SELECT name FROM log_in WHERE username =?', (username,))
        per_name = cur.fetchone()
        users_name = per_name[0]
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
            ["full name", "age", "email", "phone number", "place", "gender"]
            if change == "full name":
                new_change = input(f"What do you want to change in {change}? ")
                cur.execute('SELECT person.name FROM Person JOIN Log_in WHERE log_in.username = ?', (username,))
                name_check = cur.fetchone()
                old_name = name_check[0]
                cur.execute('UPDATE Person SET name = ? WHERE name = ?', (new_change, old_name))
                con.commit()
            elif change == "age":
                new_change = input(f"What do you want to change in {change}? ")
                if new_change.isdigit():
                    new_change = int(new_change)
                else:
                    print("Please enter a numerical value.")
                cur.execute('UPDATE Person SET age = ? WHERE name = ?', (new_change, users_name))
                con.commit()
            elif change == "email":
                while True:
                    new_change = input(f"What do you want to change in {change}? ")
                    cur.execute('SELECT email FROM Person WHERE email = ?', (new_change,))
                    emails = cur.fetchall()
                    if emails != []:
                        print("That email is already being used!")
                    elif emails == []:
                        cur.execute('UPDATE Person SET email = ? WHERE name = ?', (new_change, users_name))
                        break
                con.commit()
            elif change == "phone number":
                while True:
                    new_change = input(f"What do you want to change in {change}? ")
                    if new_change.isdigit() and len(list(new_change)) == 10:
                        new_change = int(new_change)
                        cur.execute('UPDATE Person SET phone_number = ? WHERE name = ?', (new_change, users_name))
                        con.commit()
                        break
                    else:
                        print("Please enter a 10 digit cell phone number.")
            elif change == "place":
                new_change = input(f"What do you want to change in {change}? ").upper()

                cur.execute('SELECT st_name FROM States WHERE st_name = ? or abbreviation = ?', (new_change, new_change))
                state_check = cur.fetchall()
                while state_check == []:
                    print("Please check spelling.")
                    new_change = input("What state do you live in now: ").upper()
                    cur.execute('SELECT st_name FROM States WHERE st_name = ? or abbreviation = ?', (new_change, new_change))
                    state_check = cur.fetchall()
                    if state_check != []:
                        break
                if len(list(new_change)) == 2:
                    cur.execute('SELECT st_name FROM States WHERE abbreviation = ?', (new_change,))
                    fetch_state = cur.fetchall()
                    state_name = fetch_state[0][0]
                else: 
                    cur.execute('SELECT st_name FROM States WHERE st_name = ?', (new_change,))
                    fetch_state = cur.fetchall()
                    state_name = fetch_state[0][0]
                cur.execute('UPDATE Person SET place = ? WHERE name = ?', (new_change, users_name))
                con.commit()
            elif change == 'job':
                look_for_job()
            elif change == 'gender':
                new_change = input(f"What do you want to change in {change}? ")
                if new_change != "male" and new_change != "female":
                    new_change = "other"
                cur.execute('UPDATE Person SET gender = ? WHERE name = ?', (new_change, users_name))
                con.commit()
            elif change  == "quit":
                break
            else:
                print(f"There is not {change} in the list.")
        


def admin():
    while True:

        admin_options = ["view jobs", "view users", "add jobs", "delete jobs", "sign out", "new admin"]
        admin_input = input("""
    Do you want to
        - View Jobs
        - View Users
        - Add Jobs
        - Delete Jobs
        - New Admin
    """).lower()
        
        while admin_input not in admin_options:
            print("No such command")
            admin_input = input("""
    Do you want to
        - View Jobs
        - View Users
        - Add Jobs
        - Delete Jobs
        - New Admin
    """).lower()
            if admin_input in admin_options:
                break
        
        if admin_input == "view jobs":
            
            cur.execute('SELECT DISTINCT job_name FROM Jobs')
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
                if one_user == "none":
                    break
                cur.execute('SELECT name FROM person WHERE name = ?', (one_user,))
                isuser = cur.fetchall()
                
                if isuser == []:
                    print(f"We don't have a user by the name of {one_user}.")
                elif isuser != []:
                    cur.execute('SELECT * FROM person WHERE name = ?', (one_user,))
                    print(cur.fetchone())
        elif admin_input == "add jobs":
            schedule = ["full-time", "part-time"]
            j_name = input("What is the name of the position? ")
            if j_name == "quit":
                break
            com_name = input("What is the company's name? ")
            if com_name == "quit":
                break
            j_description = input("What is the job description? ")
            if j_description == "quit":
                break
            salary = input("What is the salary for this job? ") 
            if salary == "quit":
                break

            job_type = input("Is this job full-time or part-time? ")
            if job_type == "quit":
                break
            while job_type not in schedule:
                print("part-time or full-time only")
                job_type = input("Is this job full-time or part-time? ")
                if job_type in schedule:
                    break

            hours = input("What is the schedule for this job? ")
            if hours == "quit":
                break
            req = input("What are the requirements for this job? ")
            if req == "quit":
                break

            located = input("What state is this job located? ").upper()
            if located == "QUIT":
                break
            cur.execute('SELECT st_name FROM States WHERE st_name = ? or abbreviation = ?', (located, located))
            state_check = cur.fetchall()
            while state_check == []:
                print("Please check spelling.")
                located = input("What state is this job located? ").upper()
                cur.execute('SELECT st_name FROM States WHERE st_name = ? or abbreviation = ?', (located, located))
                state_check = cur.fetchall()
                if state_check != []:
                    break

            

            cur.execute('INSERT INTO jobs VALUES (?, ?, ?, ?, ?, ?, ?, ?)', (j_name, com_name, j_description, salary, job_type, hours, req, located))
            con.commit()
        elif admin_input == "delete jobs":
            
            del_job = input("What is the position name? ")
            if del_job == "quit":
                break
            cur.execute('SELECT job_name FROM jobs WHERE job_name = ?', (del_job,))
            job_list = cur.fetchall()
            
            while job_list == []:
                print("We don't have that job listed.")
                del_job = input("What is the position name? ")
                cur.execute('SELECT job_name FROM jobs WHERE job_name = ?', (del_job,))
                job_list = cur.fetchall()
                if job_list != []:
                    break
               
            del_job2 = input("What is the company's name? ")
            if del_job2 == "quit":
                break

            cur.execute('SELECT company_name FROM jobs WHERE company_name = ?', (del_job2,))
            job_list = cur.fetchone()
            while job_list == []:
                print("We don't have that job listed.")
                del_job = input("What is the position name? ")
                cur.execute('SELECT company_name FROM jobs WHERE company_name = ?', (del_job2,))
                job_list = cur.fetchone()
                if job_list != []:
                    break
            cur.execute('DELETE FROM jobs WHERE job_name = ? AND company_name = ?', (del_job, del_job2) )
            con.commit()
        
        if admin_input == "new admin":
            pick_user = input("Enter the username for the user you want to give admin: ")
            cur.execute('SELECT username FROM log_in WHERE username = ?', (pick_user,))
            isuser = cur.fetchall()
            while isuser == []:
                print("That user doesn't exist.")
                pick_user = input("Enter the username for the user you want to give admin: ")
                cur.execute('SELECT username FROM log_in WHERE username = ?', (pick_user,))
                isuser = cur.fetchall()
                if isuser != []:
                    break
            cur.execute('UPDATE log_in SET admin = TRUE WHERE username = ?', (pick_user,))
            con.commit()
        
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
            print(f"Welcome {name[0].capitalize()}")
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
            account = User(name, password)
            if password == "quit":
                break
            if account.is_admin:
                print(f"Welcome admin {name}")
                admin()
                break
            else:
                print("Invalid account.")
            
    
    elif sign_in == "sign up":
        while True:
            admin = False
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
            else: 
                cur.execute('SELECT st_name FROM States WHERE st_name = ?', (place,))
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
            
            cur.execute('INSERT INTO Log_in VALUES (?, ?, ?, ?)', (name, username, password, admin))
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