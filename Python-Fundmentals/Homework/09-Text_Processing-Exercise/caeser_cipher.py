message = input()
encrypted_msg = ""

for character in message:
    encrypted_char = chr(ord(character) + 3)
    encrypted_msg += encrypted_char

print(encrypted_msg)
