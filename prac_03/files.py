# Task 1
name = input("Enter your name: ")
out_file = open("name.txt", 'w')
print(name, file=out_file)
out_file.close()

# Task 2
in_file = open("name.txt", 'r')
name = in_file.read()
in_file.close()
print(f"Your name is {name}")

# Task 3
in_file = open("numbers.txt", 'r')
num_1 = int(in_file.readline())
num_2 = int(in_file.readline())
in_file.close()
result = num_1 + num_2
print(result)

# Task 4
in_file = open("numbers.txt", 'r')
total = 0
for lines in in_file:
    total += int(lines)
print(total)
in_file.close()
