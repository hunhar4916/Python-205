#Hunter Harwood
#8/5/2026
#A number guessing game

userName = input("Please enter your name:  ")
studentID = input("Please enter your studentID: ")


secretNumber = 8

userGuess = 0
guessCount = 0


while userGuess != secretNumber:
    userGuess = int(input("Enter a number between 1 and 10: "))
    guessCount += 1

    if userGuess > secretNumber:
        print("Too high! Try again.")
    elif userGuess < secretNumber:
        print("Too low! Try again.")
    else:
        print(f"\nCongratulations, {userName}! You guess correctly.")

print("Output from the 'while' loop:")
loopCounter = 0
currentValue = secretNumber

while loopCounter < 5:
    currentValue += 1
    print(f"x incremented by 1 is {currentValue}")
    loopCounter += 1

print("\n" + "-" * 30 + "\n")

print("Output from the 'for' loop:")
currentValue = secretNumber

for loopIndex in range(5):
    currentValue += 1
    print(f"x incremented by 1 is {currentValue}")









    
