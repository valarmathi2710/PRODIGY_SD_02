import random
def guess_the_number():
    # Generate a random number between 1 and 100
    target_number = random.randint(1, 100)
    attempts = 0

    while True:
        # Ask the user to guess the number
        guess = int(input("Guess the number between 1 and 100: "))
        attempts += 1

        # Compare the guess with the target number
        if guess < target_number:
            print("Too low! Try again.")
        elif guess > target_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {target_number} correctly in {attempts} attempts.")
            break

# Call the function to start the game
guess_the_number()