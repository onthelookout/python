#!/usr/bin/env python3

# Hangman game for JFC coding challenge

import random

attempts = 7
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

max_guesses = attempts

# read from file

text_file = open("word_list.txt", "r")
word_list = text_file.readlines()
text_file.close()

# initialise variables
rnumber = random.randrange(0, len(word_list))
word = word_list[rnumber].upper() # pick word to be guessed
word = word[:-1] # selected word from word_list comes with an extra empty char at the end, which needs to be removed.


progress = "*" * len(word) # masking with one asterisk for each letter of the word
wrong = 0
used_letters = [] # letters already guessed

print("Welcome to my Hangman Game\n\nYour word is: ", progress,". It is ", len(word)," letters long")

def makeaguess():
    global guess
    guess = input("\n\nPlease enter your next guess: ")
    guess = guess.upper()

while wrong < max_guesses and progress != word:
    print("\nYou have ", attempts, " guesses remaining.")
    print("\nYou've used the following letters: ", used_letters)
    print("\nSo far the word is: ", progress)
    makeaguess()
    

    if len(guess) > 1:
        print("\nSingle character only, please")
        makeaguess()

    while not guess in alphabet: # check that only letters and not numbers or chars are used.
        print("\nLetters only, please.")
        makeaguess()

    while guess in used_letters: # check that you've not already used the letter
        print("\nYou've used that letter already.")
        makeaguess()

    used_letters.append(guess) # add letter to the used_letters pile

    if guess in word:
        print("\nGood guess!", guess, " is in the word :D")

        # create a new word "progress" to include guess in all correct places.

        unmasking = ""

        for x in range(len(word)): # loop for the length of the word.
            if guess == word[x]: # if the guess letter appears at that position in the word
                unmasking += guess # then make the letter at "y" position in "unmasking" the guessed letter.
            else:
                unmasking += progress[x] # if the guess is not at the "y" position in the word, then replace that position with "*" from "progress"

        progress = unmasking # replace all in "progress" with the variable "unmasking"

    else:
       print("\nSorry, ", guess, " is not in the word.")
       wrong += 1
       attempts -= 1

if wrong == max_guesses:
    print("\nYou lose.")
else:
    print("\nCongratulations, you win.")

print("\nThe word was: ", word)

input("\nPress key to Finish")
    
