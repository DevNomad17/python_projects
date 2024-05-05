import os

file_name = os.path.basename(__file__)
print(file_name) # Output: <name of the current script file>

print("\n---------- Start of program " + file_name + "-----------\n") 
n = 20
oddOrEven = "odd" if (n%2==1) else "even"
print(f"This is an {oddOrEven} number.")
print("\n------------ End of program " + file_name + "-----------\n") 