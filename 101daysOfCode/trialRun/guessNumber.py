from common import art_guess_logo, art_guess_win, art_guess_low, art_guess_high
import random

while True:
    print(art_guess_logo)
    print("Welcome to the Numer Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = random.randint(1, 100)
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

    if difficulty == "easy":
        attempts = 10
    else:
        attempts = 5

    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess > answer:
            print(art_guess_high)
        elif guess < answer:
            print(art_guess_low)
        else:
            print(art_guess_win)
            break
        attempts -= 1
        if attempts > 0:
            print("Guess again")
    if attempts == 0:
        print(f"You've run out of attempts! The correct answer is {answer}")
    decision = input("Play again? Type 'y' for yes or 'n' for no: ")
    if decision == 'n':
        break
print("\nBye Bye")
