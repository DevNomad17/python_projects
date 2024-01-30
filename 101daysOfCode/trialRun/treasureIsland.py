import os

file_name = os.path.basename(__file__)
print(file_name) # Output: <name of the current script file>

print("\n---------- Start of program " + file_name + "-----------\n") 

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************
''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.\n")
first = input("You are at the first crossroad in the deep forest. Do you turn left or right? ")
if (first == "left"):
    second = input("There is a high tide obstructing the passage to the island. Do you want to swim to the island or wait for the tide to recede? ")
    if (second == "wait"):
        third = input('''
            You find yourself standing in front of three doors,
            each painted in a different color: red, blue, and yellow.
                        
            As you approach the doors, you notice that each one has a different
            symbol etched into it: a dragon, a sword, and a shield. What do you do? ''')
        if (third == "red"):
            print("\nYou are burned by fire!!! ---*** GAME OVER ***---")
        elif (third == "blue"):
            print("\nYou are eaten by beasts!!! ---*** GAME OVER ***---")
        elif (third == "yellow"):
            print("\nYou found the treasure!!! ---*** YOU HAVE WON ***---")
        else:
            print("\nAll is lost!!! ---*** GAME OVER ***---")
    else:
        print("\nYou were attacked by giant trout and drowned!!! ---*** GAME OVER ***---")
else:
    print("\nYou fell into a hole and are trapped!!! ---*** GAME OVER ***---")
    


print("\n------------ End of program " + file_name + "-----------\n") 