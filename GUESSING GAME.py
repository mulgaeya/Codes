
secretWord = "shabadabadoo"
guess = ""
guessCount = 0
guessLimit= 3
outOfGuesses = False 


while guess != secretWord and not(outOfGuesses):
    if guessCount < guessLimit:
        guess=input("Enter guess: ")
        guessCount += 1
        if guess != secretWord:
            print("wrong!")
    else:
        outOfGuesses = True

if outOfGuesses == True:
    print("YOU LOSE")
else:
    print("You guessed right!")
