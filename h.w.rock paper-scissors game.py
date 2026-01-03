import random

def display_rules():
    print("\n-----------GAME RULES-----------")
    print("rock beats scisors.")
    print("paper beats rock.")
    print("scisors beats paper.\n")

def determine_winner(player,AI):
    if player == AI:
        return "tie"
    elif(player == "rock" and AI == "scissors") or \
        (player == "scissors" and AI == "paper") or \
        (player == "paper" and AI == "rock"):
        return "player"
    else:
        return "AI"
    
def rock_paper_scissors():
    total_choices = ["rock","paper","scissors"]
    while True:
        player_score = 0
        AI_score = 0
        round_number = 1

        print("\nWelcome to the rock-paper-scissor game!")
        print("Type 'rules' to see how to play and type 'x' to exit the game.\n")
        
        while True:
            print(f"\n----------- ROUND {round_number}-----------")
            print("Available choices - rock,paper,scissors.")
            player_choice = (input("Enter your choice: ")).lower()

            if player_choice == "x":
                print("\nThank you for playing!")
                print(f"Final score => you : {player_score} | AI score => {AI_score}\n")
                break
            elif player_choice == "rules":
                display_rules()
                continue
            elif player_choice not in total_choices:
                print("INVAILD INPUT.Please enter rock,paper,sissors.")
            AI_choice = random.choice(total_choices)
            print(f"AI choosed: {AI_choice}")

            result = determine_winner(player_choice,AI_choice)

            if result == "tie":
                print("Itis a tie!")
            elif result == "player":
                print("you won the round!")
                player_score += 1
            else:
                print("AI won this round!")
                AI_score += 1

            print(f"current score => you : {player_score} | AI score => {AI_score}\n")
            round_number += 1

        play_again = input("Do you want to play again (YES/NO): ").lower()
        if play_again != "yes":
            print("GODBYE!")

rock_paper_scissors()