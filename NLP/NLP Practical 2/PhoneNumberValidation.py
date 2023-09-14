import re

def is_valid_phone_number(phone_number):
    pattern = r'^\d{10}$|^\d{3}-\d{3}-\d{4}$|^\(\d{3}\) \d{3}-\d{4}$'
    if re.match(pattern, phone_number):
        return True
    else:
        return False

user_input = input("Enter a phone number: ")

if is_valid_phone_number(user_input):
    print(f"{user_input} is a valid phone number.")
else:
    print(f"{user_input} is not a valid phone number.")

user_input1 = input("\nEnter a phone number: ")
if is_valid_phone_number(user_input1):
    print(f"{user_input1} is a valid phone number.")
else:
    print(f"{user_input1} is not a valid phone number.")
