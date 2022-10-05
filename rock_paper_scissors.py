import random

while True:
    user_turn = input("Enter your choice(rock, paper, scissors): ")
    possible_actions = ["rock", "paper", "scissiors"]
    computer_turn = random.choice(possible_actions)
    print(f"You chose {user_turn} and computer chose {computer_turn}")

    if user_turn == computer_turn:
        print(f"Both selected {user_turn}. It's a tie!!")
    elif user_turn == "rock":
        if computer_turn == "paper":
            print("Paper covers rock. You LOSE!")
        else:
            print("Rock smashes scissors. You WIN!")
    elif user_turn == "paper":
        if computer_turn == "rock":
            print("Paper covers rock. You WIN!")
        else:
            print("Scissors cuts paper. You LOSE!")
    elif user_turn == "scissors":
        if computer_turn == "rock":
            print("Rock smashes scissors. You LOSE!")
        else:
            print("Scissors cuts paper. You WIN!")

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break
