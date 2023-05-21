"""
CP1404/CP5632 Practical
Band class
"""


class Band:
    """Represent a Band object."""

    def __init__(self, name=""):
        """Initialise a Band instance."""
        self.name = name
        self.members = []
        self.member_instruments = {}

    def __str__(self):
        """Return string representation of a Band."""
        return f"{self.name} ({str(self.members).strip('[').strip(']')}"

    def __add__(self, musician):
        self.member_instruments[musician.name] = musician.instruments
        self.members.append(f"{musician.name} ({musician.instruments})")

    def play(self):
        for member in self.member_instruments:
            if not self.member_instruments[member]:
                print(f"{member} needs an instrument!")
            else:
                print(f"{member} is playing: {self.member_instruments[member][0]}")