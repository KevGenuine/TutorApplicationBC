import random


def HigherOrLower():
    print("[_______Welcome to HigherLower_______]")
    target = random.randint(1, 100)
    status = False
    count = 0
    while status is False:
        guess = checkInputValidation()
        message, status = end_of_game(guess, target)[0], end_of_game(guess, target)[1]
        count += 1
        print(message)
    print(f"You ended this round with {count} guesses")
    checkContinue()


def checkContinue():
    while True:
        yesNo = input("Do you wish to continue? [y,n]")

        if yesNo == "y":
            HigherOrLower()
        elif yesNo == "n":
            break
        else:
            print("Please enter [y,n]")


def checkInputValidation():
    while True:
        guess = input("Enter a guess: ")

        if not guess.isdigit():
            print("Please enter a numerical value.")
            continue

        guess = int(guess)

        if guess not in range(1, 101):
            print("Please enter a value within the range 1-100.")
        else:
            return guess


def end_of_game(guess, target):
    if guess == target:
        return "Congratulations you've guess it right!!", True
    elif guess > target:
        return "Lower! Try Again", False
    elif guess < target:
        return "Higher! Try Again", False


HigherOrLower()
