import os

file_name = os.path.basename(__file__)
print(file_name) # Output: <name of the current script file>

print("\n---------- Start of program " + file_name + "-----------\n") 

print("Thank you for choosing Python Pizza Deliveries!")
size = "M" # What size pizza do you want? S, M, or L
add_pepperoni = "Y" # Do you want pepperoni? Y or N
extra_cheese = "N" # Do you want extra cheese? Y or N

match (size):
    case "S": bill = 15
    case "M": bill = 20
    case _: bill = 25

if (add_pepperoni == "Y"):
    bill += 2 if (size=="S") else 3

bill += 1 if (extra_cheese=="Y") else 0

print(f"Your final bill is: ${bill}.")

print("\n------------ End of program " + file_name + "-----------\n") 


