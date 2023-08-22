import secrets
import string
import sys

letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation


def main():
    args = sys.argv[1:]

    if not args:
        print('Usage: [--charonly] password_length')
        sys.exit(1)

    if args[0] != '--charonly':
        pwd_length = int(args[0])
        alphabet = letters + digits + special_chars
        if pwd_length >= 8:
            pwd = ''
            try:
                for i in range(pwd_length):
                    pwd += ''.join(secrets.choice(alphabet))
                print(f'Generated password:\n{pwd}')
                # return (pwd)
            except:
                print("There was an error! (1)")

    if args[0] == '--charonly':
        pwd_length = int(args[1])
        alphabet = letters + digits
        if pwd_length >= 8:
            pwd = ''
            try:
                for i in range(pwd_length):
                    pwd += ''.join(secrets.choice(alphabet))
                print(f'Generated password:\n{pwd}')
                # return (pwd)
            except:
                print("There was an error! (2)")


if __name__ == '__main__':
    main()
