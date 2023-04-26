"""File to define Bear class."""


__author__ = "730458371"


class Bear:
    """Public class for bear."""
    def __init__(self):
        """Defining constract object."""
        self.age = 0
        self.hunger_score: int = 0
        return None
    
    def one_day(self):
        """Defining one day."""
        self.age += 1
        self.hunger_score -= 1
        
    def eat(self, num_fish: int):
        """Defining eat function."""
        self.hunger_score += num_fish