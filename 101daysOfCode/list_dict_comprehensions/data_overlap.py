
with open("file1.txt", "r") as file1:
    file1_list = file1.readlines()

file1_list_int = [int(item) for item in file1_list]
# print(file1_list_int)

with open("file2.txt", "r") as file2:
    file2_list = file2.readlines()

file2_list_int = [int(item) for item in file2_list]
# print(file2_list_int)

result = [num for num in file1_list_int if num in file2_list_int]
print(result)


