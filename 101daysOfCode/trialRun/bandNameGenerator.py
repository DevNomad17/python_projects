import os

file_name = os.path.basename(__file__)
print(file_name) # Output: <name of the current script file>

print("\n---------- Start of program " + file_name + "-----------\n") 

print("Hello mister or missus ;o)")
print("Which noble village did you grew up in?")
city = input()
print("Suggest a reasonably silly name of a pet")
pet = input()
print("Generating a ba(n)d name suggestion >>> " + city + " " + pet)


print("\n------------ End of program " + file_name + "-----------\n") 




