import re

sentence_input = input()
searched_word = input()

regex = fr"(?i)\b{searched_word}\b"
matches = re.findall(regex, sentence_input)

print(len(matches))
