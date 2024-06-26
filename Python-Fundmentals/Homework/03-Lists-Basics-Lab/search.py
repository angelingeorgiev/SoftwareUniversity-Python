number = int(input())
words = input()

strings = []

for i in range(number):
    current_string = input()
    strings.append(current_string)
print(strings)

for i in range(len(strings) - 1, -1, -1):
    element = strings[i]
    if words not in element:
        strings.remove(element)
print(strings)
