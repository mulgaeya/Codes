import random

def guess(x):
    randomNumber = random.randint(1, x)
    guess = 0
    try:
        while guess != randomNumber:
            guess = int(input(f"Guess a number between 1 and {x}: "))
            if guess < randomNumber:
                print("Higher")
            else:
                print("Lower")

        print(f"Correct! {randomNumber} is the correct answer")
    
    except: 
        print("not an number!")

def computerGuess(x):
    low = 1 
    high = x
    feedback = ""
    while feedback != "c":
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low #could also be high cus low = high
        feedback = input(f"is {guess} too high (H), too low (L), or correct (C)?: ").lower()
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1
    
    print(f"YASSZZZZ U KORIQUE!!! {guess} IZZ KOREK")

computerGuess(500)


