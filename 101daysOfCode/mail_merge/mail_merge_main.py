with open("names.txt", "r") as names:
    names_array = names.read().splitlines()
# print(names_array)
with open("template.txt", "r") as template:
    template_text = template.read()

for name in names_array:
    filename = f"mail_{name}.txt"
    with open(filename, "w") as letter:
        letter.write(template_text.replace('[name]', name))
