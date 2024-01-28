import os

file_name = os.path.basename(__file__)
print(file_name) # Output: <name of the current script file>

print("\n---------- Start of program " + file_name + "-----------\n") 
height = 1.85
weight = 72

bmi = weight / height**2

if (bmi<18.5):
    verdict = "are underweight"
else:
    if (bmi<25):
        verdict = "have a normal weight"
    else:
        if (bmi<30):
            verdict = "are slightly overweight"
        else:
            if (bmi<35):
                verdict = "are obese"
            else:
                verdict = "are clinically obese"


print(f"Your BMI is {bmi:.2f}, you {verdict}.")
print("\n------------ End of program " + file_name + "-----------\n") 