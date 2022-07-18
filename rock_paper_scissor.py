import random

def game():
    user = input("Please choose your move. Rock, Paper, Scissor ")
    computer = random.choice(["Rock","Paper", "Scissor"])

    if user == computer:
        return f"Computer also choose {computer}.It's a tie!"

    elif (user == "Rock" and computer == "Scissor") or (user == "Paper" and computer =="Rock") or \
            (user == "Scissor" and computer == "Rock"):
        return "Congratulations! You win."


    else:
        return f"Sorry, you lost. Computer chose {computer}. Better luck next time!"

print(game())