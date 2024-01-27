import os

file_name = os.path.basename(__file__)
print(file_name) # Output: <name of the current script file>

print("\n---------- Start of program " + file_name + "-----------\n") 
height = 1.85
weight = 72

bmi = weight / height**2
print(int(bmi))
print("\n------------ End of program " + file_name + "-----------\n") 