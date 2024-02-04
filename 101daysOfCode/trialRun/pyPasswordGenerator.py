import os
import random

file_name = os.path.basename(__file__)
print(file_name) # Output: <name of the current script file>

print("\n---------- Start of program " + file_name + "-----------\n") 

n_letters = int(input("How many letters would you like to have in your password? "))
# ascii 65-90 for capital letters and 97-122 for small letters
n_numbers = int(input("How many numbers would you like to have in your password? "))
# ascii 48-57 for digits
n_symbols = int(input("How many symbols would you like to have in your password? "))
# ascii 33-47 for symbols

print(f"Here is your password: {password}")

print("\n------------ End of program " + file_name + "-----------\n") 


