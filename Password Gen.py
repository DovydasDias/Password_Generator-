import random
import string

def generate_password(min_length1, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special

    password = ''
    meets_criteria = False
    has_number1 = False
    has_special1 = True

    while not meets_criteria or len(password) < min_length1:
        new_char = random.choice(characters)
        password += new_char

        if new_char in digits: has_number1 = True
        elif new_char in special:  has_special1 = True

        meets_criteria = True
        if numbers:
            meets_criteria = has_number1
        if special_characters:
            meets_criteria = meets_criteria and has_special1

    return password


min_length = int(input('Enter your passwords minimum length:'))
has_number = input('would you like to add numbers (yes/no)?: ').lower() == 'yes'
has_special = 'y' == input("Do you want add special characters (yes/no)? ").lower() == 'yes'
pwd = generate_password(min_length, has_number, has_special)
print('Your password is:',pwd)


