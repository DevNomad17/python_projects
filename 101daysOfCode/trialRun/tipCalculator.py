import os

file_name = os.path.basename(__file__)
print(file_name) # Output: <name of the current script file>

print("\n---------- Start of program " + file_name + "-----------\n") 

print("Welcome to the tip calculator.")
bill = input("What was the total bill? $")
percentage = input("What percentage tip would you like to give? 10, 12 or 15? ")
people = input("How many people to split the bill? ")
splitBill = float(bill) * (float(percentage)/100+1) / int(people)
print(f"Each person should pay: ${splitBill:.2f}")

print("\n------------ End of program " + file_name + "-----------\n") 