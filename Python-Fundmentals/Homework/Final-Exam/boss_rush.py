import re

number_of_inputs = int(input())

for i in range(number_of_inputs):
    boss_details = input()
    regex = r"^\|([A-Z]{4,})\|(:)(#)(\w+\s\w+)(#)"
    match = re.search(regex, boss_details)

    if match:
        boss_name = match.group(1)
        title = match.group(4)
        print(f"{boss_name}, The {title}")
        print(f">> Strength: {len(boss_name)}")
        print(f">> Armor: {len(title)}")
    else:
        print("Access denied!")
