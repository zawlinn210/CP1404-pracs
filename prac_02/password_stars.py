MINIMUM_LENGTH = 4


def main():
    """Get and print password."""
    password = get_password(MINIMUM_LENGTH)
    print_asterisks(password)


def get_password(minimum_length):
    """Get password."""
    password = input("Enter password: ")
    while len(password) < minimum_length:
        print("Password Too Short!")
        password = input("Enter password: ")
    return password


def print_asterisks(password):
    """Print asterisks."""
    print(len(password) * "*")


main()
