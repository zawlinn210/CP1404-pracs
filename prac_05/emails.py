"""
Email
Estimate: 20 minutes
Actual:   23 minutes
"""


def main():
    """Store the user's email and name in a dictionary."""
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        username = get_name(email)
        confirmation = input(f"Is your name {username}? (Y/N) ")
        if confirmation.upper() != "Y" and confirmation != "":
            username = input("Name: ")
        email_to_name[email] = username
        email = input("Email: ")

    for email, username in email_to_name.items():
        print(username, f"({email})")


def get_name(email):
    """Get name from email."""
    prefix = email.split("@")[0]
    parts = prefix.split(".")
    username = " ".join(parts).title()
    return username


main()
