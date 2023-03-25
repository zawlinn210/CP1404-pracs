# 3. Loops

for i in range(1, 21, 2):
    print(i, end=' ')
print()

"""A. Count in 10s from 0 to 100."""
for i in range(0, 101, 10):
    print(i, end=" ")
print()

"""B. Count down from 20 to 1."""
for i in range(20, 0, -1):
    print(i, end=" ")
print()

"""C. Print n stars all on one line."""
number_of_stars = int(input("Enter the number of stars: "))
for i in range(0, number_of_stars, 1):
    print("*", end="")
print()

"""D. Print n lines of increasing stars."""
number_of_rows = int(input("Enter the number of rows: "))
for i in range(number_of_rows + 1):
    for j in range(i):
        print("*", end="")
    print()
