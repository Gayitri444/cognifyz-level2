#Evel-2

#Task-2


import random

def Number_guess():
    secret_number = random.randint(num1,num2)


    while True:
        guess = int(input("Enter your guess: "))

        if guess == secret_number:
            print(f"Congratulations! You've guessed the number {secret_number} correctly ")
            
        elif guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")


num1=int(input("Enter a number:"))
num2 =int(input("Entera number:"))
Number_guess()