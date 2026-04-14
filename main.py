import random
import score_manager

choices = ["rock", "paper", "scissors"]

def get_computer_choice():
    return random.choice(choices)

def decide_winner(player, computer):
    if player == computer:
        return "Draw"
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        return "Player"
    else:
        return "Computer"

def main():
    print("===== Rock Paper Scissors =====")
    while True:
        print("\n1. Play Game")
        print("2. View Score")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            print("1.Rock 2.Paper 3.Scissors")
            user_choice = input("Enter choice (1-3): ")

            if user_choice not in ['1', '2', '3']:
                print("Invalid choice")
                continue

            player = choices[int(user_choice) - 1]
            computer = get_computer_choice()

            print("You chose:", player)
            print("Computer chose:", computer)

            winner = decide_winner(player, computer)

            if winner == "Draw":
                print("Match Draw!")
            elif winner == "Player":
                print("You Win!")
            else:
                print("Computer Wins!")

            score_manager.save_score(winner)

        elif choice == '2':
            scores = score_manager.get_scores()
            print("Player Wins:", scores["Player"])
            print("Computer Wins:", scores["Computer"])
            print("Draws:", scores["Draw"])

        elif choice == '3':
            break

if __name__ == "__main__":
    main()