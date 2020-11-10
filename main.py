import json
from storing import *
import pprint



def customer():
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
        for entry in JOB_LIST:
            print(entry)


# def admin():
#     customer()

    



print(f"Welcome to Ndeed")

sign_in_options = ["sign in", "sign up", "sign out"]
# sign_in = input("""
#     Do you want to
#         - Sign in
#         - Sign up
#     """).lower()
# print("Not a valid option")


while True:
    
    sign_in = input("""
        Do you want to
            - Sign in
            - Sign up
        """).lower()
    
    if sign_in == "sign in":
        print("Sign in your account")
        name = input("Name: ")
        password = input("Password: ")
        log = User(name, password)
        if name == "quit" or password == "quit":
            break
        if log.is_valid:
            print(f"Welcome {name}")
            customer()
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

            while True:    
                cell = input("Phone number: (digits only) ")
                if cell == "quit":
                    break
                if cell.isdigit() and len(list(cell)) == 10:
                    cell = int(cell)
                    break
                else:
                    print("Please enter a 10 digit cell phone number.")
    
            place = input("What state do you live in: ").lower()
            if place == "quit":
                break
            while place not in all_states:
                print("Please check spelling.")
                place = input("What state do you live in: ")
                if place in all_states:
                    break
        

            job = None
            gender = input("Gender: ")
            if gender == "quit":
                break
            if gender != "male" or gender != "female":
                gender = "other"

            username = input("\nPlease enter in a username: ")
            password = input("Please enter a password for your account: ")
            if password == "quit":
                break
            cur.execute('INSERT INTO log_in VALUES (?, ?)', (username, password))
            cur.execute('INSERT INTO Person VALUES (?, ?, ?, ?, ?, ?, ?)', (name, age, email, str(cell), place, job, gender))
            cur.execute('SELECT * FROM Person')
            con.commit()
            break
        
print(2+2)




