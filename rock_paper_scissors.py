import random

def play_game():
    choices = ["rock", "paper", "scissors"]
    user_choice = input("Enter your choice (rock/paper/scissors): ").lower()
    
    if user_choice not in choices:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        return
    
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")
    
    if user_choice == computer_choice:
        print("It's a tie!")
    elif user_choice == "rock":
        if computer_choice == "scissors":
            print("You win!")
        else:
            print("Computer wins!")
    elif user_choice == "paper":
        if computer_choice == "rock":
            print("You win!")
        else:
            print("Computer wins!")
    elif user_choice == "scissors":
        if computer_choice == "paper":
            print("You win!")
        else:
            print("Computer wins!")

def main():
    play_again = "yes"
    
    while play_again == "yes":
        play_game()
        play_again = input("Do you want to play again? (yes/no): ").lower()

if __name__ == "__main__":
    main()
