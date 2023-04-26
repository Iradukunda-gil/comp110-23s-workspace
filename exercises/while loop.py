"""Lesson: guessing game"""
SECRET: int = 4
guess:int = int(input("Guess a numbber? "))
number_of_guesses: int = 0
playing: bool = True
while playing and number_of_guesses <2:
    if number_of_guesses == 3:
         playing = False
    if guess == SECRET:
        print("Yay! You got it right! ")
        playing = False
    else:
        print("Wrong number. :(")
        if guess % 2 ==1: #guess is odd
            print("your guess is odd. The answer is even")
        if guess > SECRET:
            print("your geess is too high")
        else: #guess is too low
                print("your guess is too low. ")
        guess = int(input("Make another guess!"))
    number_of_guesses = number_of_guesses + 1
    print("Number of guesses " + str(number_of_guesses))