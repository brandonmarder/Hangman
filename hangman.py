# Hangman Game
# Copyright (c) 2017 Brandon Marder. All Rights Reserved.
# NOTE: THIS CONTAINS SIGNIFICANT SECURITY VULNERABILTIES IF RUNNING IN PYTHON 2.x

# Import Modules
# import sys
import os
from string import punctuation

# Checks if letter is in secret word. Adds letter to correct letter list or
# counts it as incorrect.
# def checkLetter(letter, word):
#    if letter in word:
#        add letter to list of correctly guessed letters
#    else:
#         subtract 1 from remaining mistakes allowed

# Clears screen and then prints game setup starting text.
def gameStartText():
    os.system('cls')
    print("Welcome to Hangman. First, please you will need to enter some information.")
    print()
    print("You will need to enter the secret word (no spaces) and set the allowed number of mistakes")
    print()
    print("The screen will clear after you start the game.")
    print()

# Gets secret word
def getSecretWord():
    validInput = False
    while validInput == False:
        secretWord = input('Enter Secret Word: ')
        if secretWord.isalpha():
            validInput = True
        else:
            print()
            print("Please enter only letters.")
            print()
    return secretWord

# Gets number of mistakes allowed.
def getMistakesAllowed():
    validInput = False
    while validInput == False:
        mistakesAllowed = input('Enter Number of Mistakes Allowed (1, 2, etc.): ')
        if mistakesAllowed.isdigit():
            mistakesAllowed = int(mistakesAllowed)
            if mistakesAllowed >= 1:
                validInput = True
            else:
                print()
                print("Please enter an integer greater than 0.")
                print()
        else:
            print()
            print("Please enter only digitis")
            print()
    return mistakesAllowed

# Asks user to start game. If no, starting questions are asked again.
def readyToStart(word, mistakes):
    print()
    print('The secret word is "%s"' % (word))
    print('The number of mistakes allowed is %d' % (mistakes))
    print('Ready to start? (Yes or No): ', end = "")
    ready = standardizedYesNo()
    return ready

# Displays instructions to player
def playerInstructions(mistakes):
    print("Welcome to Hangman!")
    print()
    print("Try to uncover the secret word by guessing letter one at a time.")
    print("But watch out, you only get '%d' mistakes before your man is hanged!" % (mistakes))
    print()

# Shows inbetween guess info to player.
def gameStatus():
   # Responds if guess was correct or incorrect
   # Gives word with remaining spaces
   # Tells player number remaining number of mistakes allowed
   pass

# Gets letter guess from player.
def letterGuess(priorGuesses, secret):
    if len(priorGuesses) == 0:
        printSecret(secret, priorGuesses)
        print()
    else:
        # print("So far, you have guessed: %s" % (printSecret(secret, priorGuesses)))
        print("You have already guessed: ", " ".join(priorGuesses))
    validInput = False
    while validInput == False:
        guess = input('Guess a Letter: ')
        if guess.isalpha() == True:
            guess = guess.lower()
        if guess.isalpha() == False:
            print('Input not valid. Please enter a single letter.')
        elif len(guess) != 1:
            print('Input not valid. Please enter a single letter.')
        # elif (guess in punctuation):
        #     print('Input not valid. Please enter a single letter.')
        elif guess in priorGuesses:
            print('You already guessed this letter. Please guess a different letter.')
        else:
            validInput = True

    return guess

# Checks if player guess is correct.
def checkGuess(guess, secret):
    if guess in secret:
        return 0
    else:
        return -1

# Prints secret word with remaining blanks.
def printSecret(secret, guesses):
    print("You have found so far: ", end = "")
    for char in secret:
        if char in guesses:
            print(char, end = " ")
        else:
            print("_", end = " ")

# standardizes yes/no response
def standardizedYesNo():
    inputValid = False
    while inputValid == False:
        standardized = input()
        if standardized.lower() == 'y':
            standardized = 'yes'
        elif standardized.lower() == 'n':
            standardized = 'no'
        standardized = standardized.lower()
        if not standardized == 'yes' and not standardized == 'no':
            print('Please enter either "Yes" or "No".')
        if standardized == 'yes' or standardized == 'no':
            inputValid = True
    return standardized

def main():
    playAgain = True
    while playAgain == True:
        gameStartText()
        startGame = "no"
        lettersGuessed = []
        while startGame == "no":
            secretWord = getSecretWord().lower()
            mistakesAllowed = getMistakesAllowed()
            startGame = readyToStart(secretWord, mistakesAllowed)
        os.system('cls')
        playerInstructions(mistakesAllowed)
        testChar = 'a'
        while mistakesAllowed > 0:
            playerGuess = letterGuess(lettersGuessed, secretWord)
            lettersGuessed += playerGuess
            lettersGuessed = sorted(lettersGuessed)
            mistakesAllowed += checkGuess(playerGuess, secretWord)
            print()
            print("You have '%d' mistakes remianing." % (mistakesAllowed))
            printSecret(secretWord, lettersGuessed)
            print()
            if all(char in lettersGuessed for char in secretWord):
                mistakesAllowed = 0
                print("Congrats! You Win!")
        if not all(char in lettersGuessed for char in secretWord):
            print()
            print("You lose. Better luck next time")
            print('The word was "%s"' % (secretWord))
            # print("Better luck next time")
        print()
        print("Would you like to play agian?(Yes or No): ", end = "")
        oneMoreTime = standardizedYesNo()
        if oneMoreTime == 'no':
            playAgain = False

    # print(secretWord)
    # print(mistakesAllowed)

if __name__ == '__main__':
    main()
