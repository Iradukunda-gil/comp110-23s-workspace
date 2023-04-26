"""File to define simmulation."""

from river import River


__author__ = "730458371"


def view_river(self):
    """Defining view_river function."""
    print("~~~ Day", self.day, ": ~~~")
    print("Fish population:", self.fish)
    print("Bear population:", self.bears)


def one_river_day(self):
    """Defining one_river_day."""
    for fish in self.fish:
        fish.one_day()
    for bear in self.bears:
        bear.one_day()
      

my_river = River(10, 2)
my_river.view_river()
my_river.one_river_week()
my_river.remove_fish(2)
my_river.bears[0].eat()
my_river.view_river()