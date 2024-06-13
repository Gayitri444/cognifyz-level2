import random

def guessing_game():
    secret_number = random.randint(1,100)


    while True:
        guess = int(input("Enter your guess: "))

        if guess == secret_number:
            print(f"Congratulations! You've guessed the number {secret_number} correctly ")
            
        elif guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")


guessing_game()