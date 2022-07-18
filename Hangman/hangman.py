import random
from words import words
import string


def computer_chooses(words):
    word = random.choice(words)
    while "-" in word or " " in word:
        word = random.choice(words)

    return word.upper()


def hangman_game():
    word = computer_chooses(words)
    used = set()
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    lives = 7

    while len(word_letters) > 0 and lives > 0:

        print("Letters you tried so far: ", " ".join(used))

        progress = [letters if letters in used else "_" for letters in word]
        print("Current word: ", " ".join(progress))

        user_input = input("Guess a letter: ").upper()
        if user_input in alphabet - used:
            used.add(user_input)
            if user_input in word_letters:
                word_letters.remove(user_input)

            else:
                lives -= 1
                print("Lives: ", lives)

        elif user_input in used:
            print("You already tried that")

        else:
            print("Invalid Value")
    if lives == 0:
        print(f"Sorry no more lives the word was", word)
    else:
        print("Congratz the word was ", word)

hangman_game()