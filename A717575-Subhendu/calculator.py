"""
Calculator Class to do the calculations
"""


class Calculator:
    # Calculator class to perform calculations
    def __init__(self, x: int, y: int):
        self.x : int = x
        self.y : int = y

    def add(self) -> int:
        # returns the addition of 2 numbers
        return self.x + self.y

    def subtract(self) -> int:
        # returns the subtraction of 2 numbers
        return self.x - self.y

    def multiply(self) -> int:
        # returns the multiplication of 2 numbers
        return self.x * self.y

    def divide(self) -> float:
        # returns the division of 2 numbers
        return self.x / self.y
