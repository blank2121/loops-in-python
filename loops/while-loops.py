# this is a small guess the number game using a while loop and see how it was implemented.



randomNumber = 73

print("guess a number between 1 and 100 (inclusive)")
userGuess = -1

while userGuess != randomNumber:
    userGuess = int(input(""))

    if userGuess > randomNumber:
        print("guess lower")

    elif userGuess < randomNumber:
        print("guess higher")

print("you guessed the number!!!")
