import os

file_name = os.path.basename(__file__)
print(file_name) # Output: <name of the current script file>

print("\n---------- Start of program " + file_name + "-----------\n") 

year = 1777

if (year%4==0):
    if (year%100==0):
        if (year%400==0):
            print("Leap year")
        else:
            print("Not leap year")
    else:
        print("Leap year")
else:
    print("Not leap year")


print("\n------------ End of program " + file_name + "-----------\n") 