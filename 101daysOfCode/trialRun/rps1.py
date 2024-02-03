import os
import random

file_name = os.path.basename(__file__)
print(file_name) # Output: <name of the current script file>

print("\n---------- Start of program " + file_name + "-----------\n") 

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
outcome = [rock,paper,scissors]

plays_nice = False
player = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors: "))
if (player >= 0 and player <= 2):
    print(f"\n{outcome[player]}\n\n")
    plays_nice = True
    print("Computer chose:\n")
    computer = random.randint(0,2)
    print(f"{outcome[computer]}\n")

if (not plays_nice):
    print("\n\nNo, no, no... Naughty kitty... Play nice!\n")
elif (player == computer):
    print("It's a draw")
elif ((player == (computer-1)) or (player-computer == 2)):
    print("You've lost")
else:
    print("You've won")


print("\n------------ End of program " + file_name + "-----------\n") 


