import random

def generate_number():
    return random.randint(1,10)

def get_player_input():
    while True:
        try:
            guess = int(input("Enter your guess from 1 to 10: "))
            if 1 <= guess <= 10:
                return guess
            else:
                print("Enter a number whithin 1 to 10: ")
        except ValueError:
            print("Invaild input.Please enter a vaild number.")
def play_round():
    target = generate_number()
    attempts = 0
    while True:
        guess = get_player_input()
        attempts += 1
        if guess < target:
            print("too low.give another guess.")
        elif guess > target:
            print("too high.give another guess.")
        else:
            print(f"Exelent.you reached the target in {attempts} attempts.")
def ask_replay():
    return input("\nWould you like to play another round (YES/NO): ").lower() == "y"

def guess_the_number():
    print("\nWelcome to the guess the number experiance!")
    print("The number is bettewen 1 & 10.\n")

    total_attempts = 0
    rounds_played = 0

    while True:
        print("\n------------Game round------------")
        attempts = play_round()

        total_attempts += attempts
        rounds_played += 1

        if not ask_replay():
            break
    print("\n--- Session Summary ---")

    print(f"Total Rounds Played: {rounds_played}")

    print(f"Total Attempts: {total_attempts}")

    print("Thank you for playing. Session terminated.\n")

guess_the_number()