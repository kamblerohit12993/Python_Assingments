# Number Guessing Game

secret_number = 37
max_attempts = 5
attempts = 0
guessed = False

while attempts < max_attempts:
    guess = int(input("Guess the secret number: "))
    attempts = attempts + 1

    if guess == secret_number:
        print("Congratulations! Correct Guess!")
        guessed = True
        break

    elif guess < secret_number:
        print("Too low!")

    else:
        print("Too high!")

if guessed == False:
    print("Sorry! You have used all attempts.")
    print("The secret number was:", secret_number)

print("Attempts Used:", attempts)