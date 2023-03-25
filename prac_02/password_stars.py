password = input("Enter password: ")
while len(password) < 4:
    print("Password Too Short!")
    password = input("Enter password: ")
print(len(password) * "*")