import os

file_name = os.path.basename(__file__)
print(file_name) # Output: <name of the current script file>

print("\n---------- Start of program " + file_name + "-----------\n") 

print("type number: ")
n = input()
out = int(n[0]) + int(n[1])
print("Sum of digits is: " + str(out))


print("\n------------ End of program " + file_name + "-----------\n") 
