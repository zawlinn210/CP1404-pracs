from random import randint
from prac_09.car import Car


class UnreliableCar(Car):
    """An unreliable version of a car."""

    def __init__(self, name, fuel, reliability):
        """Initialize an UnreliableCar."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car, only sometimes based on reliability."""
        random_number = randint(0, 100)
        if random_number < self.reliability:
            distance_driven = super().drive(distance)
            return distance_driven
        else:
            return 0