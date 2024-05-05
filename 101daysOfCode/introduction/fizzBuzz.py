import os

file_name = os.path.basename(__file__)
print(file_name) # Output: <name of the current script file>

print("\n---------- Start of program " + file_name + "-----------\n") 

for i in range(1,101):
    str = ""
    if (i%3==0):
        str = "Fizz"
    if (i%5==0):
        str += "Buzz"
    if (str==""):
        print(i)
    else:
        print(str)

print("\n------------ End of program " + file_name + "-----------\n") 


