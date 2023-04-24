"""
Code to use Guitar class.
Estimate: 10 minutes
Actual:   12 minutes
"""

from prac_06.guitar import Guitar


def main():
    gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
    print(Guitar.get_age(gibson))
    print(Guitar.is_vintage(gibson))
    print(gibson)

    another_guitar = Guitar("Another Guitar", 2013)
    print(Guitar.get_age(another_guitar))
    print(Guitar.is_vintage(another_guitar))
    print(another_guitar)


main()
