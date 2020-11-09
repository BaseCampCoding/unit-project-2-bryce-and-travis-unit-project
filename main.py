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
["Alabama",
"Alaska",
"Arizona",
"Arkansas"
"California",
"Colorado",
"Connecticut",
"Delaware",
"Florida",
"Georgia",
"Hawaii",
"Idaho",
"Illinois",
"Indiana",
"Iowa",
"Kansas",
"Kentucky",
"Louisiana",
"Maine",
"Maryland",
"Massachusetts",
"Michigan",
"Minnesota",
"Mississippi",
"Missouri",
"Montana",
"Nebraska",
"Nevada",
"New Hampshire",
"New Jersey",
"New Mexico",
"New York",
"North Carolina",
"North Dakota",
"Ohio",
"Oklahoma",
"Oregon",
"Pennsylvania",
"Rhode Island",
"South Carolina",
"South Dakota",
"Tennessee",
"Texas",
"Utah",
"Vermont",
"Virginia",
"Washington",
"West Virginia",
"Wisconsin",
"Wyoming"]
if sign_in == "sign in":
    print("signed in")
elif sign_in == "sign up":
    name = input("Full name: ")

    age = input("Age: ")
    if age.isdigit():
        age = int(age)
    else:
        print("Please enter a numerical value.")
    email = input("Email: ")

    cell = input("Phone number: ")

    place = input("What state do you live in: ")

    gender = input("Gender: ")


print(2+2)
