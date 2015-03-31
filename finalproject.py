# pseudo code
# Computer gets a word from the dictionary
# computer chooses a random word
#import random
#random_list=("Holli","hello","spark","kitty","while","thing")
#random_word=random.choice(random_list)
# the number of charachters in the word come up as blanks
#print "___ ___ ____ ___ ____ "
# there is one player
# player gueeses a letter
#letter=raw_input("choose a letter")
#print "%"
# if guess is correct, a letter is put in the correct spot in the word
#split_word=list(random_word)
#print split_word
# elif true, print letter in correct spot 
# if the guess is incorrect, a asterick goes on the screen
# else false, print *
# it is a loop that continues until one of two things happen
# if the player guesses the word then the player wins and something comes up on the screen
# if the player does not guess the word after five incorrect choices, the player loses and something comes up on the screen
import sys
import random

def PrintBlank():
    sys.stdout.write("___  ")
    return

def PrintMatch(character):
    string = " %s   " % character
    sys.stdout.write(string)
    return

def DisplayGuessStatus( guess ):
    wordLength = len(guess);
    for i in range (0,wordLength):
        character = guess[i]
        if character == '_':
            PrintBlank()
        else:
            PrintMatch(character)
        sys.stdout.write(' ')
        sys.stdout.write(' ')

    print ("")
    return

def FindMatch(letter, answer, guess):
    result = 0
    split_answer = list(answer)
    wordLength = len(guess);
    letter = letter.upper()

    for i in range (0,wordLength):
        if letter == split_answer[i]:
            guess[i] = letter
            result = 1
    return result

def CheckWinner(guess):
    winner = 1
    wordLength = len(guess);
    for i in range (0,wordLength):
        if guess[i] == '_':
            winner = 0
    return winner

def InitGuess(guess, random_word):
    wordLength = len(random_word)
    for i in range (0 ,wordLength):
       guess.append("_")

def drawman (triesRemaining):
    if triesRemaining==4:
        print "O"
    if triesRemaining==3:
        print "/O"
    if triesRemaining==2:
        print "/O\\"
    if triesRemaining==1:
        print "/O\ /"
    if triesRemaining==0: 
        print "/O\ \/\\"

# Computer gets a word from the dictionary
random_list=("Holli","hello","spark","kitty","while","thing")
random_word=random.choice(random_list)
random_word = random_word.upper()
triesRemaining = 5
winner = 0;
guess = []

print ("Welcome to Holli's Hangman!")
print ("You get %d tries to guess the word" % triesRemaining)

# the number of characters in the word come up as blanks
InitGuess(guess, random_word)

DisplayGuessStatus(guess)

# there is one player

while triesRemaining and winner == 0 :
    # player guesses a letter
    letter=raw_input("choose a letter")

    # if guess is correact, a letter is put in the correct spot in the word (guess)
    result = FindMatch(letter, random_word, guess)

    if result == 0:
        triesRemaining = triesRemaining - 1
        print ("%s does not match %d tries left" % (letter, triesRemaining))
        drawman(triesRemaining)

    else:
        print ("Matched %s - %d tries left" % (letter,triesRemaining))

    winner = CheckWinner(guess)
    DisplayGuessStatus(guess)


if triesRemaining == 0:
    print ("You are LOSER!! The secret word was %s" % random_word)
else:
    print ("CONGRATULATIONS. You are a GENIUS!!!")


