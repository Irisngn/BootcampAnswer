import random

# Function to choose the random number between 1 and 100 by randint function
def find_secret_number():
    return random.randint(1, 100)

def player_input():
    ''' Function to input the guessed number for player and check validity'''
    while True:  # Create loop to ensure the user is repeatedly prompted for input until they enter a valid number
        # Input the number (string)
        player_input = input("Choose a random number from 1 to 100: \n")
        # Check if the input is a number or not using isdigit()
        if player_input.isdigit():
            # If it's a valid number, convert it to an integer
            return int(player_input)
        else:
            print("Sorry. Please enter a valid number.")

def check_guess(secret_number, player_guess):
    '''Function to compare the secret number to guessed ones and give hints to players'''
    if player_guess < secret_number:
        print("Your guess is too low.")
    elif player_guess > secret_number:
        print("Your guess is too high.")
    else:
        print(f"Game over! You win. The secret number was {secret_number}.")

def play_game():
    '''Function to run the game'''
    print("Hi! Let's play the guessing number game!")
    # Call find_secret_number function to get the secret number
    secret_number = find_secret_number()

    while True:  # Ensure the game will continue until it meets the condition -> break
        # Call function to get the player number
        player_guess = player_input()
        # Call function to check if the guess is a match or not
        check_guess(secret_number, player_guess)

        # If the player guess is right, break the loop
        if player_guess == secret_number:
            break

# Call play_game function to start the game
play_game()
