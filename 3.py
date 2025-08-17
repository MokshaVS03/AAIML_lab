import random

secret_number = random.randint(1, 100)
attempts = 0

print("Welcome to the Number Guessing Game!")
print("Guess the secret number between 1 and 100.")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1
    
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"Correct! The secret number was {secret_number}.")
        print(f"You guessed it in {attempts} attempts.")
        break
