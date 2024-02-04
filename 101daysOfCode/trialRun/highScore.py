import os

file_name = os.path.basename(__file__)
print(file_name) # Output: <name of the current script file>

print("\n---------- Start of program " + file_name + "-----------\n") 

# Input a list of student scores
student_scores = input("Enter all students' scores, use space as a separator: ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

# Write your code below this row 👇

max = 0
for score in student_scores:
  if (score>max):
    max = score


print(f"The highest score in the class is: {max}")

print("\n------------ End of program " + file_name + "-----------\n") 


