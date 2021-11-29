import random

while True:
    choices = ["rock", "paper", "scissors"]

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("rock, paper, or scissors: ").lower()

    if player == computer:
            print("computer: ", computer)
            print("player: ", player)
            print("It's a TIE!")

    elif player == "rock":
        if computer == "paper":
            print("computer: ", computer)
            print("player: ", player)
            print("Oh....You lose!!!")
        if computer == "scissors":
            print("computer: ", computer)
            print("player: ", player)
            print("Yayyyy....You win!!!")

    elif player == "scissors":
        if computer == "rock":
            print("computer: ", computer)
            print("player: ", player)
            print("Oh....You lose!!!")
        if computer == "paper":
            print("computer: ", computer)
            print("player: ", player)
            print("Yayyyy....You win!!!")

    elif player == "paper":
        if computer == "rock":
            print("computer: ", computer)
            print("player: ", player)
            print("Yayyyy....You win!!!")
        if computer == "scissors":
            print("computer: ", computer)
            print("player: ", player)
            print("Oh....You lose!!!")

    play_again = input("Play again? (yes/no): ").lower()

    if play_again != "yes":
        break

print ("Bye!")
