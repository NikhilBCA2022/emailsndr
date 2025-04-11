import re

email = input("Enter the email address: ")
number = input("Enter the number: ")



if re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9]+\.[a-zA-Z.-]{2,}$", email):
    print("Valid email address")
else:
    print("Invalid email address , Please enter a valid email address")
if re.match(r"^[_.+91\s]+\d{10}$", number):
    print("Valid number")
else:
    print("Invalid country code , Please enter a valid number")
    
