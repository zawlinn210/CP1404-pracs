"""
display menu
get choice
while choice != <quit option>
    if choice == <first option>
        <do first task>
    else if choice == <second option>
        <do second task>
    ...
    else if choice == <n-th option>
        <do n-th task>
    else
        display invalid input error message
    display menu
    get choice
<do final thing, if needed>
"""
MENU = """(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit"""
MINIMUM_SCORE = 0
MAXIMUM_SCORE = 100


def main():
    """Print score menu function program."""
    print(MENU)
    score = None
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            if score is None:
                print("Please enter the score first, Press 'G'.")
            else:
                print(determine_score_status(score))
        elif choice == "S":
            if score is None:
                print("Please enter the score first, Press 'G'.")
            else:
                print_stars(score)
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Farewell")


def get_valid_score():
    """Get valid score."""
    score = int(input("Enter score: "))
    while score < MINIMUM_SCORE or score > MAXIMUM_SCORE:
        print("Invalid score!")
        score = int(input("Enter score: "))
    return score


def determine_score_status(score):
    """Determine the score status."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def print_stars(score):
    """Print stars"""
    print(int(score) * "*")


main()
