"""EX06 - Choose Your Own Adventure"""
__author__ = "730458371"

import random

# Named constant with an emoji
FIRE_EMOJI = "\U0001F525"  
FOREST_EMOJI = "\U0001F332"
DRAGON_EMOJI = "\U0001F409"
SWORD_EMOJI = "\U0001F5E1"


#Initialize global variables
points: int = 0
player: str = ""


#greet function
def greet() -> None:
    global player
    print(f"Welcome to Adventure Game{FIRE_EMOJI}!")
    player = input("What's your name? ")
    print(f"Nice to meet you, {player}!")

#1st experience function
def experience1():
    global points
    print(f"Welcome to Forest{FOREST_EMOJI} experience!")
    print(f"You chose to take the left path, {player}.")
    print(f"Suddenly, a dragon{DRAGON_EMOJI} appears!")
    print("What would you like to do?")
    print("1. Run away")
    print("2. Try to fight the dragon")
    choice = input("Enter your choice (1 or 2): ")
    if choice == "1":
        print("You run away as fast as you can!")
        return 5
    elif choice == "2":
        print(f"You take out your sword{SWORD_EMOJI} and prepare to fight the dragon.")
        if random.randint(1, 2) == 1:
            print("You slay the dragon! Congratulations!")
            return 10
        else:
            print("The dragon is too strong for you and defeats you.")
            return -5
    else:
        print("Invalid choice, please try again.")
        return 0


#2nd experience function
def experience2():
    global points
    print(f"Welcome to Cave experience, {player}!")
    print("You find yourself in a dark cave. You hear strange noises coming from within.")
    print("Do you...")
    print("1. Explore the cave")
    print("2. Turn back and head to the beach")
    choice = input("Enter your choice: ")
    if choice == "1":
        print("As you explore the cave, you stumble upon a treasure chest!")
        print("Do you...")
        print("1. Open the chest")
        print("2. Leave the chest alone and head back to the beach")
        choice = input("Enter your choice: ")
        if choice == "1":
            print("Inside the chest, you find a shiny gem!")
            points += 10
        else:
            print("You decide not to risk it and head back to the beach.")
    else:
        print("You turn back and head to the beach.")
    print(f"You now have {points} adventure points.")


#3rd experience function
def experience3():
    global points
    print(f"Welcome to Jungle experience {player}")
    print("You find yourself in a jungle. You hear the sound of rushing water nearby.")
    print("Do you...")
    print("1. Follow the sound to the river")
    print("2. Turn back and head to the beach")
    choice = input("Enter your choice: ")
    if choice == "1":
        print("As you approach the river, you see a group of monkeys playing nearby.")
        print("Do you...")
        print("1. Join in the monkey fun")
        print("2. Leave the monkeys alone and head back to the beach")
        choice = input("Enter your choice: ")
        if choice == "1":
            print("You have a blast playing with the monkeys!")
            points += 5
        else:
            print("You decide not to disturb the monkeys and head back to the beach.")
    else:
        print("You turn back and head to the beach.")
    print(f"You now have {points} adventure points.")
    return points


#end_experience function
def end_experience(points: int):
    print(f"Thank you for playing! You accumulated {points} adventure points.")
    


#Main functions
def main() -> None:
    global points, player
    greet()
    options = ("1. Explore the forest", "2. Explore the cave", "3. Explore the jungle", "4. End the Experience")
    while True:
        print("Choose your experience")
        for choice in options:
            print(choice)
        Choice = input()
        if Choice == "1":
            experience1()
        if Choice == "2":
            experience2()
        if Choice == "3":
            experience3()
        if Choice == "4":
            end_experience(points)
            break

if __name__ == "__main__":
  main()