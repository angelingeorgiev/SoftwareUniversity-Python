names_input = input().split(", ")

sorted_names = sorted(names_input, key=lambda x: (-len(x), x))

print(sorted_names)
