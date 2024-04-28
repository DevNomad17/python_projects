import os

file_name = os.path.basename(__file__)
print(file_name) # Output: <name of the current script file>

print("\n---------- Start of program " + file_name + "-----------\n") 
age = 56
yearsLeft = 90-age
weeksLeft = yearsLeft * 52

print(f"You have {weeksLeft} weeks left.")
print("\n------------ End of program " + file_name + "-----------\n") 