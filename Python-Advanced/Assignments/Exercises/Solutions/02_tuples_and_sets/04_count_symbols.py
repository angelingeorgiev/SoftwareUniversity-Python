text = input()
unique_symbols = set()

for character in text:
    unique_symbols.add(character)

for character in sorted(unique_symbols): #tuple
    print(f"{character}: {text.count(character)} time/s")
    