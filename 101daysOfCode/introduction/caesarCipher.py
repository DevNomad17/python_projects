from common import art_caesar


def encode(message, offset):
    offset = offset % 26
    message_list = list(message)
    message_encoded = []
    for char in message_list:
        # check if char is a letter, if yes, shift, if not leave as is
        if 97 <= ord(char) <= 122:
            shifted_char_ascii = ord(char) + int(offset)
            if shifted_char_ascii > 122:
                shifted_char_ascii -= 26
            if shifted_char_ascii < 97:
                shifted_char_ascii += 26
        else:
            shifted_char_ascii = ord(char)
        message_encoded.append(chr(shifted_char_ascii))
    res = ''.join(message_encoded)
    return res


print(art_caesar)
while True:
    decision_start = input("\nType 'encode' to encrypt, type 'decode' to decrypt: ").lower()
    msg = input("Type your message: ").lower()
    shift = int(input("Type the shift number: "))
    if decision_start == 'encode':
        print(f"Here's the encoded result: {encode(msg, shift)}")
    else:
        print(f"Here's the decoded result: {encode(msg, -shift)}")

    decision_continue = input("Type 'yes' if you want to go again, otherwise, type 'no': ").lower()

    if decision_continue != 'yes':
        break
