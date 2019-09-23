"""
random library
"""
import random


class Apple():
    """
    Apple
    """

    def __init__(self, x, y):
        self.x = random.randint(0, (x-20)//20)*20+10
        self.y = random.randint(0, (y-20)//20)*20+10
