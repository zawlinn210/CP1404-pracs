"""
CP1404 Practical
State the color code in a dictionary
"""

COLOR_TO_CODE = {'Absolute Zero': "#0048ba", "Acid Green": "#b0bf1a", "Baby Blue": "#89cff0", "Baby Pink": "#f4c2c2",
                 "Cadet Grey": "#91a3b0", "CadetBlue": "#5f9ea0", "Daffodil": "#ffff31", "Dandelion": "#f0e130",
                 "Earth Yellow": "#e1a95f", "Ebony": "#555d50"}
print(COLOR_TO_CODE)

state_color = input("Enter the color name: ").title()
while state_color != "":
    if state_color in COLOR_TO_CODE:
        print(state_color, "is", COLOR_TO_CODE[state_color])
    else:
        print("Invalid color name")
    state_color = input("Enter the color name: ").title()
