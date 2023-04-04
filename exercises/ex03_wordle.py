__author__ = "730458371"

def contains_char(first_str: str , single_char: str) -> bool:
    """defined character in a second parameter and single character. The return is True or False"""
    assert len(single_char) == 1
    counter_var = 0
    while counter_var < len(first_str):
        if single_char == first_str[counter_var]:
            return True
        counter_var += 1
    return False

def emojified(guess: str , secret: str) -> str:
    """Prompt user to guess the secret"""
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    box: str = ""
    counter_var = 0
    while counter_var < len(secret):
        if guess[counter_var] == secret[counter_var]:
            box += GREEN_BOX
        else:
            if contains_char(secret, guess[counter_var]) is True:
                box += YELLOW_BOX
            if contains_char(secret, guess[counter_var]) is False:
                box += WHITE_BOX
        counter_var += 1
    return box
def input_guess(guess: int) -> str:
    """Prompts user for guess of expected length"""
    guess_num: str = input(f"Enter a {guess} character word: ")
    while len(guess_num) != guess:
        guess_num = input(f"That wasn't {guess} chars! Try again: ")
    return guess_num
def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret_word = "codes"
    counter = 0
    start = 1
    word: str = ""
    while counter < 6 and secret_word != word:
        print(f"=== Turn {start}/6 ===")
        word = input_guess(len(secret_word))
        print(emojified(word, secret_word))
        counter += 1
        start += 1
    if word == secret_word:
            print(f"You won in {start - 1}/6 turns!") 
    else:
        print("X/6 - Sorry, try again tomorrow!")
    print(" ")
    