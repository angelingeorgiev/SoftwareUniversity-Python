user_input = input()
last_letter = ""

for letter in user_input:
    if letter != last_letter:
        print(letter, end="")
        last_letter = letter
