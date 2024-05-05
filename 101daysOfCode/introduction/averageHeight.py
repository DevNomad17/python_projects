import os

file_name = os.path.basename(__file__)
print(file_name) # Output: <name of the current script file>

print("\n---------- Start of program " + file_name + "-----------\n") 

# Input a Python list of student heights
count = 0
total_height = 0
average_height = 0

student_heights = input("Enter all students' heights, use space as a separator: ").split()
for i in student_heights:
    count+=1
    total_height+=int(i)
average_height = round(total_height / count)

print(f"total height = {total_height}")
print(f"number of students = {count}")
print(f"average height = {average_height}")


print("\n------------ End of program " + file_name + "-----------\n") 


