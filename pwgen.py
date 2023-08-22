import secrets
import string
import sys

letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation
alphabet = letters + digits + special_chars


def main():
    pwd_length = int(sys.argv[1])
    if pwd_length >= 8:
        pwd = ''

        try:
            for i in range(pwd_length):
                pwd += ''.join(secrets.choice(alphabet))
            print(f'Generated password:\n{pwd}')
            return (pwd)

        except:
            return ("There was an error!")

    else:
        print(f'Not secure enough, password should have at least 8 characters')


if __name__ == '__main__':
    main()
