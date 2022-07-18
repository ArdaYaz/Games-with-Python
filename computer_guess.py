import random


def user_guesses(h):
    x = random.choice(range(0, h))
    y = 0
    while y != x:
        y = int(input("Please enter a number: "))
        if y < x:
            print("Your guess is too low. Guess higher")

        elif y > x:
            print("Your guess is too high. Guess lower")

    print("Congratz! Thanks for playing")


user_guesses(100)

###############################################################################################################
###############################################################################################################


def comp_guesses(x):
    feedback = ""
    y = 0
    while feedback != "true":
        guess = random.choice(range(y, x))
        print(guess)
        feedback = input("Please say lower, higher or true ")
        if str(feedback) == "lower":
            x = guess
        elif str(feedback) == "higher":
            y = guess + 1

    print("Thanks for playing")


comp_guesses(100)