import storing
from storing import Admin

print(f"Welcome to Ndeed")

sign_in_up = ["sign in", "sign up", "sign out"]
sign_in = input("""
    Do you want to
        - Sign in
        - Sign up
    """)

while sign_in not in sign_in_up:
    print("Not a valid option")
    sign_in = input("""
    Do you want to
        - Sign in
        - Sign up
    """
    )
    if sign_in == "sign in":
        print("signed in")
        break
    elif sign_in == "sign up":
        print("signing up")
        break

print(2+2)
