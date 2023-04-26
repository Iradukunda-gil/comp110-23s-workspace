"""File to define River class."""
__author__ = "730458371"

from exercises.ex09.fish import Fish
from exercises.ex09.bear import Bear


class River:
    """Public class for river."""
    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Defining check_ages."""
        new_bears = []
        for bear in self.bears:
            if bear.age <= 5:
                new_bears.append(bear)
        self.bears = new_bears
        new_fish = []
        for fish in self.fish:
            if fish.age <= 3:
                new_fish.append(fish)
        self.fish = new_fish
        return None
    
    def remove_fish(self, amount: int):
        """Defining remove_fish."""
        count: int = 0
        while count < amount:
            self.fish.pop(0)
            count += 1

    def bears_eating(self):
        """Defining bears_eating."""
        for bear in self.bears:
            if len(self.fish) >= 5: 
                num_fish = self.remove_fish(3)
                bear.eat(num_fish)
        return None
    
    def check_hunger(self):
        """Defining check_hunger."""
        survivedBears = []
        for bear in self.bears: 
            bear.one_day
            if bear.hunger_score >= 0:
                survivedBears.append(bear)
        self.bears = survivedBears
        return None
        
    def repopulate_fish(self):
        """Defining repopulate_fish."""
        num_fish = len(self.fish)
        num_new_fish = (num_fish // 2) * 4
        for i in range(num_new_fish):
            self.fish.append(Fish())
        return None
    
    def repopulate_bears(self):
        """Defining repopulate_bears function."""
        num_bears = len(self.bears)
        num_new_bears = num_bears // 2
        for i in range(num_new_bears):
            self.bears.append(Bear())
        return None
    
    def view_river(self):
        """Defining view_river function."""
        num_fish = len(self.fish)
        num_bears = len(self.bears)
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {num_fish}")
        print(f"Bear population: {num_bears}")
        return None
            
    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """Definition for one_river_week."""
        i: int = 0
        for i in range(7):
            self.one_river_day()