import storing
from storing import *

print(f"Welcome to Ndeed")

sign_in_options = ["sign in", "sign up", "sign out", "Admin"]
sign_in = input("""
    Do you want to
        - Sign in
        - Sign up
    """)


while sign_in not in sign_in_options:
    print("Not a valid option")
    sign_in = input("""
        Do you want to
            - Sign in
            - Sign up
        """)

if sign_in == "sign in":
    print("signed in")
elif sign_in == "sign up":
    name = input("Full name: ")
elif sign_in == "Admin":
    print("Enter your Admin account")
    name = input("Name: ")
    password = input("Password: ")
    account = (name, password)
    if account.is_valid:
        print("yay")
    else:
        print("Invaild account")

    while True:
        age = input("Age: ")
        if age.isdigit():
            age = int(age)
            break
        else:
            print("Please enter a numerical value.")
    email = input("Email: ")

    cell = input("Phone number: ")

    place = input("What state do you live in: ")

    gender = input("Gender: ")



