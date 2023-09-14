import re

def is_valid_email(email):

    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

    if re.match(pattern, email):
        return True
    else:
        return False

email_address = "Heramb@gmail.com"
if is_valid_email(email_address):
    print(f"{email_address} is a valid email address.")
else:
    print(f"{email_address} is not a valid email address.")
