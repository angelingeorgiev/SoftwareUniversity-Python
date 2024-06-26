user_input = input()

vowels = ["a", "o", "u", "e", "i", "A", "O", "U", "E", "I"]
no_vowels = "".join(([letter for letter in user_input if letter not in vowels]))

print(no_vowels)
