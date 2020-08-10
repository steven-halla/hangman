import random
import sys


def start_guessing():  # creates a function for guessing
    dashes = "-" * len(current_word)
    dashes = replace_dashes_with_guess(current_word, dashes, ' ')

    guesses_taken = 0  # set this to 0 so that players can have 10 trys
    while guesses_taken < 10:  # sets boundrys , giving playing 10 trys

        print(dashes)

        guess = input()  # allows player to do input

        if guess in current_word:
            print("That letter is in the secret word!")
            dashes = replace_dashes_with_guess(current_word, dashes, guess)
        else:
            print("Sorry, that is an invalid guess.")
            guesses_taken += 1
            print("Guesses remaining " + str(10 - guesses_taken))


    # print a statement letting player know they lost/won
    if guesses_taken < 10:
        print("you win!")
    else:
        print("you lose")

    sys.exit()        # exits out of game

def replace_dashes_with_guess(current_word, dashes, guess):
    empty_list = ""

    for i in range(len(current_word)):
        if guess == current_word[i]:
            empty_list += guess
        else:
            empty_list += dashes[i]
    return empty_list

word_bank = ["i wish for a dog", "i wish for a cat", "i wish for a car"]  #a list of words that the player has to guess
current_word = random.choice(word_bank)     #chooses a word from word bank

start_guessing()

