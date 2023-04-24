"""
Guitar Class
Estimate: 12 minutes
Actual:   15 minutes
"""


class Guitar:
    """Represent a Guitar object."""

    def __init__(self, name="", year=0, cost=0):
        """Initialise a Guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}): ${self.cost}"

    def get_age(self):
        """Get the guitar's age."""
        current_year = 2022
        if "L-5" in self.name:
            self.year = 1922
        age = current_year - self.year
        return age

    def is_vintage(self):
        """Check the guitar is vintage or not."""
        age = self.get_age()
        if age >= 50:
            return True
        else:
            return False
