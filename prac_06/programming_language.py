"""
ProgrammingLanguage Class
Estimate: 10 minutes
Actual:   12 minutes
"""


class ProgrammingLanguage:
    """Represent a ProgrammingLanguage object."""
    def __init__(self, field="", typing="", reflection="", year=0):
        """Initialise a ProgrammingLanguage instance."""
        self.field = field
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Check the field is dynamic or not."""
        if self.typing == "Dynamic" or self.typing == "dynamic":
            print(self.field)
            return True
        else:
            return False

    def __str__(self):
        return f"{self.field}, {self.typing} Typing, Reflection = {self.reflection}, First appeared in {self.year}"
