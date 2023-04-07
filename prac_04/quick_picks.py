import random

NUMBERS_PER_LINE = 6
MAX_NUM = 45
MIN_NUM = 1


def main():
    """Get quick pick."""
    number_of_quick_picks = int(input("How many quick picks? "))
    while number_of_quick_picks < 0:
        print("Invalid")
        number_of_quick_picks = int(input("How many quick picks? "))
    generate_quick_pick(number_of_quick_picks)


def generate_quick_pick(number_of_quick_picks):
    """Generate random quick picks."""
    for row in range(number_of_quick_picks):
        quick_picks = []
        for column in range(NUMBERS_PER_LINE):
            number = random.randint(MIN_NUM, MAX_NUM)
            quick_picks.append(number)
        quick_picks.sort()
        print(" ".join(f"{number:2}" for number in quick_picks))


main()
