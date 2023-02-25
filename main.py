import random
import os


def choose_difficulty(difficulty):
    difficulty.lower()
    if difficulty == 'easy':
        return 10
    elif difficulty == 'hard':
        return 5


def rand_number():
    random_number = random.randint(1, 100)
    return random_number


def compare(player_number, computer_number):
    if player_number < computer_number:
        return "Too low"
    elif player_number > computer_number:
        return "Too high"
    else:
        return "You have won"


def play_game():
    is_game_over = False
    print("Welcome the number guessing game!")
    print("I'm thinking of a number between 1 and 100")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    lives = choose_difficulty(difficulty)
    computer_number = rand_number()
    while not is_game_over:
        print(f"You have {lives} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        answer = compare(guess, computer_number)
        if guess > 100 or guess < 1:
            os.system('clear')
            print(f"You put an invalid number {guess}, please guess between 1 and 100")

        elif guess != computer_number:
            lives -= 1
            print(answer)
        if guess == computer_number:
            print(answer)
            print(f"The answer was {computer_number}")
            is_game_over = True
            restart = input("Would you like to start over? 'y' or 'n' ")
            if restart == "y":
                os.system('clear')
                play_game()
        if lives == 0:
            print("You have run out of attempts")
            print(f"The answer was {computer_number}")
            is_game_over = True
            restart = input("Would you like to start over? 'y' or 'n' ")
            if restart == "y":
                os.system('clear')
                play_game()


play_game()
