import os

file_name = os.path.basename(__file__)
print(file_name) # Output: <name of the current script file>

print("\n---------- Start of program " + file_name + "-----------\n") 

target = int(input("Enter a number between 0 and 1000: ")) # Enter a number between 0 and 1000

sum = 0

for i in range(0,target+1,2):
    sum+=i

print(sum)

print("\n------------ End of program " + file_name + "-----------\n") 


