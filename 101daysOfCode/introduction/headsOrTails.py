import os
import random

file_name = os.path.basename(__file__)
print(file_name) # Output: <name of the current script file>

print("\n---------- Start of program " + file_name + "-----------\n") 

str_res = "Heads" if (random.random() > 0.5) else "Tails"
print(str_res)

print("\n------------ End of program " + file_name + "-----------\n") 


