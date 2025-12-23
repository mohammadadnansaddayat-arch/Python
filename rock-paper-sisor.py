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