def all_characters(first: str, second: str) -> list:
    characters = []
    for current_char in range(ord(first) + 1, ord(second)):
        characters.append(chr(current_char))
    return characters


first_char = input()
second_char = input()

final_result = all_characters(first_char, second_char)
print(" ".join(final_result))
