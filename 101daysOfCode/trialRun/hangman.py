import hangman_res
import random

print(hangman_res.HANGMANLOGO)
word = hangman_res.words[random.randint(0, len(hangman_res.words) - 1)]
# word = 'llama'
display_word = ""
hang = 0
# Initialize display of the guess board
for char in word:
    display_word += "_ "
letter = '*'
missed_letters = []

while True:
    if word.count(letter.lower()) > 0:
        # Convert the string to a list
        display_word_list = list(display_word)
        j = -1
        for i in range(0, word.count(letter.lower())):
            j = word.find(letter.lower(), j+1)
            display_word_list[j * 2] = letter.lower()

        # Convert the list back to a string
        display_word = ''.join(display_word_list)
    elif letter == '*':
        print("\n")
    else:
        if letter.lower() not in missed_letters:
            print(f"You guessed '{letter}' - that's not in the word. You lose a life.\n")
            hang += 1
            missed_letters.append(letter)

    print(display_word)
    if len(missed_letters) > 0:
        print(f"Missed letters: {missed_letters}")

    if hang > 0:
        if hang == (len(hangman_res.HANGMANPICS)-1):
            print(hangman_res.HANGMANPICS[hang])
            print(f"GAME OVER, you've hanged the man and LOST. The word is: {word}")
            break
        print(hangman_res.HANGMANPICS[hang])
    else:
        print(hangman_res.HANGMANLOGO)

    if display_word.count('_') > 0:
        letter = input("\nGuess a letter: ")
        if display_word.find(letter.lower()) >= 0 or letter.lower() in missed_letters:
            print("You already tried this letter, shoot another one.")
    else:
        print(f"CONGRATULATIONS, you've WON and missed only {hang} attempts")
        break
