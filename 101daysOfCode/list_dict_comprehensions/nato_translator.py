import pandas
IN_FILE = "nato_alphabet.csv"

df = pandas.read_csv(IN_FILE)
alphabet_dict = {row.letter:row.code for (index, row) in df.iterrows()}

while True:
    word = input("Enter a word to be translated: ").upper()
    if word == 'EXIT':
        break
    result = [alphabet_dict[char] for char in word]
    print(result)

print('Bye bye')


