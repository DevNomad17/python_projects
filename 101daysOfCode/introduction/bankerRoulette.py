import os
import random

file_name = os.path.basename(__file__)
print(file_name) # Output: <name of the current script file>

print("\n---------- Start of program " + file_name + "-----------\n") 

names_string = input("Enter the names for the roulette: ")

names = names_string.split(", ")

print(f"{names[random.randint(0,len(names)-1)]} is going to buy the meal today!")

#print(f"first: {names[0]}, second: {names[1]}, and so on...")


print("\n------------ End of program " + file_name + "-----------\n") 


