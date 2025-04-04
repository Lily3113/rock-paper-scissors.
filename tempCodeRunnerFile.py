
import random

while True:  # This will keep the game running until the player says 'no'
    user_choice = input("enter between rock,paper,scissors: ")
    computer_choice = random.choice(["rock","paper","scissors"])
    print("you chose:", user_choice)
    print("computer chose:", computer_choice)

    if user_choice == computer_choice:
        print("its a tie")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        print("you win")
    else:
        print("you lose")

    # Ask if player wants to continue
    play_again = input("\nDo you want to play again? (yes/no): ").lower().strip()
    if play_again != 'yes':
        print("\nThanks for playing!")
        break