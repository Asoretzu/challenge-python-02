# Resolve the problem!!
import string
from random import randint, choice, shuffle

SYMBOLS = list('!"#$%&\'()*+,-./:;?@[]^_`{|}~')
UPPER_ALPHABET = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
LOWER_ALPHABET = list("abcdefghijklmnopqrstuvwxyz")
NUMBERS = list("1234567890")
ALL_ELEMENTS = SYMBOLS + UPPER_ALPHABET + LOWER_ALPHABET + NUMBERS


def pass_elements():
    password = choice(SYMBOLS) + choice(UPPER_ALPHABET) + choice(LOWER_ALPHABET) + choice(NUMBERS)

    return password


def other_elements(length):
    password = ""

    for _ in range(length):
        password += choice(ALL_ELEMENTS)

    return password


def generate_password():
    length = randint(8, 16) - 4

    temp_pass = pass_elements() + other_elements(length)
    password = list(temp_pass)

    shuffle(password)
    
    return "".join(password)


def validate(password):

    if len(password) >= 8 and len(password) <= 16:
        has_lowercase_letters = False
        has_numbers = False
        has_uppercase_letters = False
        has_symbols = False

        for char in password:
            if char in string.ascii_lowercase:
                has_lowercase_letters = True
                break

        for char in password:
            if char in string.ascii_uppercase:
                has_uppercase_letters = True
                break

        for char in password:
            if char in string.digits:
                has_numbers = True
                break

        for char in password:
            if char in SYMBOLS:
                has_symbols = True
                break

        if has_symbols and has_numbers and has_lowercase_letters and has_uppercase_letters:
            return True
    return False


def run():
    password = generate_password()
    if validate(password):
        print('Secure Password')
    else:
        print('Insecure Password')


if __name__ == '__main__':
    run()
