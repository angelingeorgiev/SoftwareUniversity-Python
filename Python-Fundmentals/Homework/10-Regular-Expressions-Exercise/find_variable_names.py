import re

sentence_input = input()
regex = r"\b_([A-Za-z0-9]+)\b"
variables = re.findall(regex, sentence_input)

print(",".join(variables))
