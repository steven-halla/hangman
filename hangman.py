import random
import sys


def guessing():  # creates a function for guessing
    dashes = "-" * len(current_word)

    guess_taking = 0  # set this to 0 so that players can have 10 trys
    while guess_taking < 10:  # sets boundrys , giving playing 10 trys

        print(dashes)

        guess = input()  # allows player to do input


        if guess in current_word:
            print("That letter is in the secret word!")
            dashes = test(current_word, dashes, guess)

    if input():  # setting it up so that everytime a command is put in, guess taking +1
        guess_taking += 1  # +1 for each command put into console
        print(dashes)


    if guess_taking == 10:   #sets up an exit statements for when guesses = 10
        print("you lose")    #print a statement letting player know they lost
        sys.exit            #exits out of game

def test(current_word,dashes,guess ):
    empty_list = ""

    for i in range(len(current_word)):
        if guess == current_word[i]:
            empty_list += guess
        else:
            empty_list += dashes[i]
    return empty_list

word_bank = ["i wish for a dog", "i wish for a cat", "i wish for a car"]  #a list of words that the player has to guess
current_word = random.choice(word_bank)     #chooses a word from word bank

guessing()                         #calls the function
# test(current_word,dashes,guess)

