import random

def guess(x):
    randomNumber = random.randint(1, x)
    guess = 0
    while guess != randomNumber:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < randomNumber:
            print("Higher")
        elif guess > randomNumber:
            print("Lower")

    print(f"Correct! {randomNumber} is the correct answer")

guess(20)


