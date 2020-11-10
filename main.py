import storing
from storing import *



def customer():
    check job listings
    pass

def admin():
    customer()

    



print(f"Welcome to Ndeed")

sign_in_options = ["sign in", "sign up", "sign out", "admin"]
sign_in = input("""
    Do you want to
        - Sign in
        - Sign up
    """).lower()


while sign_in not in sign_in_options:
    print("Not a valid option")
    sign_in = input("""
        Do you want to
            - Sign in
            - Sign up
        """).lower()

if sign_in == "sign in":
    print("Sign in your account")
    n = input("Name: ")
    p = input("Password: ")
    log = (n, p)
    print("signed in")
    customer()

elif sign_in == "admin":
    print("Enter your Admin account")
    name = input("Name: ")
    password = input("Password: ")
    account = Admin([name, password])
    if account.is_valid:
        print(f"Welcome{name}")
        admin()
    else:
        print("Invaild account")
    
elif sign_in == "sign up":
    name = input("Full name: ")
    while True:
        age = input("Age: ")
        if age.isdigit():
            age = int(age)
            break
        else:
            print("Please enter a numerical value.")

    email = input("Email: ")

    while True:    
        cell = input("Phone number: (digits only) ")
        if cell.isdigit() and len(list(cell)) == 10:
            cell = int(cell)
            break
        else:
            print("Please enter a 10 digit cell phone number.")
    
    place = input("What state do you live in: ").lower()
    while place not in all_states:
        print("Please check spelling.")
        place = input("What state do you live in: ")
        if place in all_states:
            break
        

    job = None
    gender = input("Gender: ")
    if gender != "male" or gender != "female":
        gender = "other"

    password = input("Please enter a password for your account: ")


    cur.execute('INSERT INTO Person VALUES (?, ?, ?, ?, ?, ?, ?)', (name, age, email, str(cell), place, job, gender))

