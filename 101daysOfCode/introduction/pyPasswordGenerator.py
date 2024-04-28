import os
import random

file_name = os.path.basename(__file__)
print(file_name)  # Output: <name of the current script file>

print("\n---------- Start of program " + file_name + "-----------\n")

n_letters = int(input("How many letters would you like to have in your password? "))
# ascii 65-90 for capital letters and 97-122 for small letters
n_numbers = int(input("How many numbers would you like to have in your password? "))
# ascii 48-57 for digits
n_symbols = int(input("How many symbols would you like to have in your password? "))
# ascii 33-47 for symbols

settings = [[n_letters, "letters"], [n_numbers, "numbers"], [n_symbols, "symbols"]]

# print(settings)

for j in range(0, 3):
    for i, setting in enumerate(settings):
        if setting[0] == 0:
            settings.pop(i)

total_chars = n_letters + n_numbers + n_symbols
password = ""
for i in range(0, total_chars):
    if settings:
        rand_index = random.randint(0, len(settings) - 1)
        character = settings[rand_index][1]
        if character == "letters":
            if random.randint(0, 1) == 0:
                password += chr(random.randint(65, 90))
            else:
                password += chr(random.randint(97, 122))
        elif character == "numbers":
            password += chr(random.randint(48, 57))
        else:
            password += chr(random.randint(33, 47))
        if settings[rand_index][0] == 1:
            settings.pop(rand_index)
        else:
            settings[rand_index][0] -= 1

print(f"\nHere is your password: {password}")

print("\n------------ End of program " + file_name + "-----------\n")
