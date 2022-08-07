import random
from classes.words import words 
import string 

def getValidWord(words):
    word = random.choice(words) # randomly chooses something from the list
    while "_" in word or " " in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    word = getValidWord(words)
    wordLetters = set(word) # letters in the word
    alphabet = set(string.ascii_uppercase)
    usedLetter = set() # what the user had guessed

    lives = 6

    # getting user input
    while len(wordLetters) > 0 and lives > 0:
        # used letters
        # " ".join(['a', 'b', 'c']) ==> 'a b c'
        print("You have", lives, " lives left and you have used these letters: ", " ".join(usedLetter))

        # what current word is (eg. W - R D)
        wordList = [letter if letter in usedLetter else "_" for letter in word]
        print("Current word: ", " ".join(wordList))

        userLetter = input("\nGuess a letter: ").upper()
        if userLetter in alphabet - usedLetter:
            usedLetter.add(userLetter) 
            if userLetter in wordLetters:
                wordLetters.remove(userLetter)

            else: 
                lives -= 1 # takes away life if wrong
                print("Letter is not in the word")
        elif userLetter in usedLetter:
            print("You have already used that character. Try again")
        
        else:
            print("Invalid character. Try again")

    # gets here when len(wordLetter) == 0 OR when lives == 0
    if lives == 0:
        print("LOLL YOU DEAD FRFR ONG!", word, "is the word")
    else:
        print("You guessed the word", word, "!")



hangman()




