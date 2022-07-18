import random


#Unlike madlib codes i saw i wanted to make input system cleaner, better and more unpredictable.
def madlib():
    adj = input("Please enter multiple adj (Preferred at least 3) : ").split()
    number = input("Please enter multiple number : ").split()
    noun = input("Please enter multiple noun (Preferred at least 2) : ").split()

    story = f"\nAs i was walking down the road i noticed some {random.choice(adj)} people. I tried "  \
f"approaching them but they ran. They said i was {random.choice(adj)} looking. "\
f"So i got sad and ate {random.choice(number)} kid(s)\nwhich tasted {random.choice(adj)}."\
f" After thanking god for the food i left the kindergarten to continue my {random.choice(noun)} king adventure. I was" \
f" known as the {random.choice(adj)} {random.choice(noun)}. I encountered a {random.choice(adj)} man \nwho claimed he "\
f"was an adventurer like me but he took an arrow in the knee and know  was forced to work as a cashier. I said "\
f"{random.choice(adj)} story bro and left.\nThen went to sleep to dream about talking with Jaden concerning political"\
f" and economical state of the world right now"

    print(story)


madlib()