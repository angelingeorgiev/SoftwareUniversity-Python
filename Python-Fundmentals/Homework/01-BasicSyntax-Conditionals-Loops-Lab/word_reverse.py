word_input = input()

reversed_word = ""

for _ in range(len(word_input) - 1, -1, -1):
    reversed_word += word_input[_]
print(reversed_word)
