def is_valid_name(name):

    if all(char.isalpha() or char.isspace() for char in name):
        return True
    else:
        return False
name1 = "Heramb"
name2 = "Heramb455235"

if is_valid_name(name1):
    print(f"{name1} is a valid name.")
else:
    print(f"{name1} is not a valid name.")

if is_valid_name(name2):
    print(f"{name2} is a valid name.")
else:
    print(f"{name2} is not a valid name.")
