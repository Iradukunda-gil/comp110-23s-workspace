"""EX02 - One-Shot Wordle - Loops!"""
__author__ = "730458371"
guess: str = str(input("What is your 6-letter guess? "))
secret_word: str = "python"
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
index_var: int = 0
box: str = ""

# if length of guess is not equal to 
while len(guess) != 6: 
    guess = input("That was not 6 letters! Try again: ")

# Will assign boxes
while index_var < len(secret_word):
    if guess[index_var] == secret_word[index_var]:
        box += GREEN_BOX

    else:
        yellow_check = False
        secret_check = 0
        while yellow_check is not True and secret_check < len(secret_word):
            if secret_word[secret_check] == guess[index_var]:
                yellow_check = True
            else:
                secret_check = secret_check + 1
        if yellow_check is True:
            box += YELLOW_BOX
        else:
            box += WHITE_BOX
    index_var += 1
print(box)

# if word guessed is incorrect 
if guess != secret_word:
    print("Not quite. Play again soon! ")

else:
    print("Woo! You got it!")
