import secrets
import string
import sys
import pyperclip

letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation


def generate_password(char_range: str, length: int = 32) -> str | sys.exit:
    """Password generator, for given alphabet and length

    Args:
        char_range (str): Character range, --charonly makes password of only letters and digits
        length (int, optional): Desired password length. Defaults to 32.

    Returns:
        str | sys.exit: Either returns string or exits the program
    """
    if length >= 8:
        password = ""
        for i in range(length):
            password += "".join(secrets.choice(char_range))
        return password
    else:
        print("Password should be at least 8 characters long")
        sys.exit(1)


def main():
    args = sys.argv[1:]

    if not args:
        print("Usage: [--charonly] password_length")
        sys.exit(1)

    if args[0] != "--charonly":
        pwd_length = int(args[0])
        alphabet = letters + digits + special_chars
        pyperclip.copy(generate_password(pwd_length, alphabet))

    if args[0] == "--charonly":
        pwd_length = int(args[1])
        alphabet = letters + digits
        pyperclip.copy(generate_password(pwd_length, alphabet))


if __name__ == "__main__":
    main()
