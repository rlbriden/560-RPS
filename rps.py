import random  

def get_user_choice():
    user_choice = input("Choose (rock, paper, or scissors): ").lower()
    return user_choice

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_win(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "User tied!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "User wins!"
    else:
        return "User loses!"

def play_game():
    print("Let's play rock, paper, scissors!")

    while True:
        user_choice = get_user_choice()  
        computer_choice = get_computer_choice()  

        print(f"User chose {user_choice}.")
        print(f"Computer chose {computer_choice}.")

        result = determine_win(user_choice, computer_choice)  
        print(result)

        play_again = input("Play again? (y/n): ").lower()  
        if play_again != 'y':
            print("Thanks. Bye!")
            break

if __name__ == "__main__":
    play_game()
