import Hangman_images as hi
import re


def check_input(let):
    if let.isalpha() & len(let) == 1:
        return True
    else:
        print("please enter a single letter")
        return False


def check_letter(let, wrd):
    if let in wrd:
        print("Correct")
        return True
    else:
        print("Wrong")
        return False


def change_guessed_word(let, wrd, guessed_wrd):
    loc = [m.start() for m in re.finditer(let, wrd)]
    # loc = wrd.find(let)
    print(loc)
    for i in loc:
        guessed_wrd[loc[i]] = let
    loc.clear()
    print(*guessed_wrd, sep=' ')
    return guessed_wrd


def check_duplicates(let, guessed_let):
    if let in guessed_let:
        print("Guessed already")
        return guessed_let


guessed_letters = []
number_guesses = 0
word = "pytton"
guessed_word = ["_", "_", "_", "_", "_", "_"]
print(*guessed_word, sep=' ')

while not word == "".join(guessed_word):
    letter = input("Guess a letter: ").lower()
    if check_input(letter):
        if check_letter(letter, word):
            guessed_word = change_guessed_word(letter, word, guessed_word)
        else:
            number_guesses += 1
    hi.print_scaffold(number_guesses)
print("You win! \n", "you had", number_guesses, "guesses")
