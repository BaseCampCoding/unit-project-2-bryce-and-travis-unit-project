import storing
from storing import *

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
    print("signed in")

elif sign_in == "Admin":
    print("Enter your Admin account")
    name = input("Name: ")
    password = input("Password: ")
    account = (name, password)
    if account.is_valid:
        print("yay")
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

    cell = input("Phone number: ")

    while True:
        place = input("What state do you live in: ")
        while place not in states:
            print("Please check spelling.")
            place = input("What state do you live in: ")
        


    gender = input("Gender: ")



