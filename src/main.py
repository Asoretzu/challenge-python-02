# Resolve the problem!!
import string
from random import randint

SYMBOLS = list('!"#$%&\'()*+,-./:;?@[]^_`{|}~')
UPPER_ALPHABET = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
LOWER_ALPHABET = list("abcdefghijklmnopqrstuvwxyz")
NUMBERS = list("1234567890")


def choose_letter():
    select_list = randint(1, 12)

    if select_list <= 3:
        index = randint(0, len(UPPER_ALPHABET)-1)
        return UPPER_ALPHABET[index]

    if select_list <= 6:
        index = randint(0, len(LOWER_ALPHABET)-1)
        return LOWER_ALPHABET[index]

    if select_list <= 9:
        index = randint(0, len(SYMBOLS)-1)
        return SYMBOLS[index]

    index = randint(0, len(NUMBERS)-1)
    return NUMBERS[index]


def generate_password():
    password_len = randint(8, 16)
    password = ""

    for i in range(password_len):
        letter = choose_letter()
        password += letter
    
    return password


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
