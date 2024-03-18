from common import art_higherLower_logo, art_higherLower_vs
from higherLower_data import data
import random


def printFormatData(account):
    return f"{account['name']}, a {account['description']}, from {account['country']}."


while True:
    score = 0
    while True:
        print(art_higherLower_logo)
        if score > 0:
            print(f"You're right! Current score {score}.")
            a = b
        while True:
            if score == 0:
                a = random.choice(data)
            b = random.choice(data)
            if not a == b:
                break
        print(f"Compare A: {printFormatData(a)}")
        print(art_higherLower_vs)
        print(f"Against B: {printFormatData(b)}")
        answer = input(f"\nWho has more followers? Type 'a' or 'b': ")
        if (a['follower_count'] > b['follower_count'] and answer == 'a') or (
                a['follower_count'] < b['follower_count'] and answer == 'b'):
            score += 1
        else:
            print(art_higherLower_logo)
            print(f"\nSorry, that's wrong. Final score: {score}")
            break

    playAgain = input("\nDo you want to play again? Type 'y' or 'n': ")
    if playAgain == 'n':
        break
print("\nBye bye")
