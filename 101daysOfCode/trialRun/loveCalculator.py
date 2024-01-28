import os

file_name = os.path.basename(__file__)
print(file_name) # Output: <name of the current script file>

print("\n---------- Start of program " + file_name + "-----------\n") 

name1 = "Angela Yu"
name2 = "Jack Bauer"

name = name1.lower() + name2.lower()

digit1 = name.count("t") + name.count("r") + name.count("u") + name.count("e")
digit2 = name.count("l") + name.count("o") + name.count("v") + name.count("e")

score = digit1*10+digit2

#For Love Scores less than 10 or greater than 90, the message should be:

if (score < 10 or score > 90):
    print(f"Your score is {score}, you go together like coke and mentos.")
elif (score >= 40 and score <= 50):
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")


print("\n------------ End of program " + file_name + "-----------\n") 