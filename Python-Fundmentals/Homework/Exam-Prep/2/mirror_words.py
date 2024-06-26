import re

text_string = input()
mirrored_words = []

regex = r"(\@|\#)([a-zA-Z]{3,})(\1{2})([a-zA-Z]{3,})(\1)"
pairs = re.findall(regex, text_string)

for pair in pairs:
    first_word = pair[1]
    second_word = pair[3]
    if first_word == second_word[::-1]:
        mirrored_words.append(f"{first_word} <=> {second_word}")

if not pairs:
    print("No word pairs found!")
else:
    print(f"{len(pairs)} word pairs found!")
if not mirrored_words:
    print(f"No mirror words!")
else:
    print(f"The mirror words are:")
    print(f"{', '.join(mirrored_words)}")
