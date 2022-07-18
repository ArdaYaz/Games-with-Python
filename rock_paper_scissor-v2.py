import random


def player_input():
    draw = 0
    win = 0
    lose = 0

    while True:
        player_input = input("Choose: Rock, Paper or Scissor ")
        computer = random.choice(["Rock", "Paper", "Scissor"])
        user = player_input.lower()
        comp = computer.lower()

        if user == comp:
            draw += 1
            print(f"Computer choose {computer}, it's a tie")
            print(f"{draw} Draws, {win} Wins, {lose} Loses")

        elif (user == "rock" and comp == "scissor") or (user == "paper" and comp == "rock") or\
            (user == "scissor" and comp == "paper"):
            win += 1
            print(f"Computer choose {computer}, it's your win")
            print(f"{draw} Draws, {win} Wins, {lose} Loses")

        else:
            lose += 1
            print(f"Computer choose {computer}, it's your lose")
            print(f"{draw} Draws, {win} Wins, {lose} Loses")

player_input()