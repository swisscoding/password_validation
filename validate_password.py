#!/usr/local/bin/python3
# Made by @swisscoding on Instagram
# Follow now and share!

import colored
import re

# decoration
print(colored.stylize("\n---- | Validate your password | ----\n", colored.fg("red")))

# information
print(colored.stylize("Requirements: ", colored.fg("green")))
print("1. The password must contain at least one uppercase character.")
print("2. The password must contain at least one lowercase character.")
print("3. The password must contain at least one number.")
print("4. The password must contain at least one special character (!, ?, *, #).")
print("5. The password must be at least 8 characters in length.\n")

# user interaction
password = input("Enter your password: ")

# patterns
patterns = [r"[a-z]{1,}", r"[A-Z]{1,}", r"[0-9]{1,}", r"[\!\?\*\#]{1,}"]

# function
def validate(pw):
    # must be 5 -> 5 Requirements
    validation_count = 0
    if len(pw) >= 8:
        validation_count += 1
        for i in patterns:
            if re.search(i, pw):
                validation_count += 1
    else:
        return colored.stylize("\nYour password length is too short!\n", colored.fg("red"))
    if validation_count == 5:
        return colored.stylize("\nYour password satisfies every requirement!\n", colored.fg("green"))
    else:
        return colored.stylize("\nYour password does not satisfy one of the requirements 1 to 4!\n", colored.fg("red"))
print(validate(password))
