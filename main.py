import random


def get_computer_choice():
    choices = ["Rock", "Paper", "Scissors"]
    return random.choice(choices)


def get_user_choice():
    user_choice = input("Enter your choice (Rock, Paper, or Scissors): ").capitalize()
    while user_choice not in ["Rock", "Paper", "Scissors"]:
        user_choice = input("Invalid choice. Please enter Rock, Paper, or Scissors: ").capitalize()
    return user_choice


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Scissors" and computer_choice == "Paper") or \
         (user_choice == "Paper" and computer_choice == "Rock"):
        return "You win!"
    else:
        return "Computer wins!"


def play_game():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    print(determine_winner(user_choice, computer_choice))


play_game()
