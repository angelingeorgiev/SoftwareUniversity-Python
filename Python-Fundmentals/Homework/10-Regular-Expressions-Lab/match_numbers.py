import re

numbers_given = input()
regex = r"(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))"
matches = re.finditer(regex, numbers_given)

for match in matches:
    print(match.group(), end=" ")
