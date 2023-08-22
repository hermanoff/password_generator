import secrets
import string
import sys
import pyperclip

letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation


def generate_password(length, char_range):
    if length >= 8:
        pwd = ''
        try:
            for i in range(length):
                pwd += ''.join(secrets.choice(char_range))
            print(f'Generated password:\n{pwd}')
            return pwd
        except:
            print('There was an error!')


def copy_to_clipboard(text):
    pyperclip.copy(text)


def main():
    args = sys.argv[1:]

    if not args:
        print('Usage: [--charonly] password_length')
        sys.exit(1)

    if args[0] != '--charonly':
        pwd_length = int(args[0])
        alphabet = letters + digits + special_chars
        copy_to_clipboard(generate_password(pwd_length, alphabet))

    if args[0] == '--charonly':
        pwd_length = int(args[1])
        alphabet = letters + digits
        copy_to_clipboard(generate_password(pwd_length, alphabet))


if __name__ == '__main__':
    main()
