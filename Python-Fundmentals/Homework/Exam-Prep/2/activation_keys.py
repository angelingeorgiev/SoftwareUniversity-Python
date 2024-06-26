raw_key = input()

while True:
    command = input()
    if command == "Generate":
        break

    action = command.split(">>>")
    if action[0] == "Contains":
        substring = action[1]
        if substring in raw_key:
            print(f"{raw_key} contains {substring}")
        else:
            print("Substring not found!")
    elif action[0] == "Flip":
        upper_to_lower = action[1]
        start_index = int(action[2])
        end_index = int(action[3])
        substring = raw_key[start_index:end_index]
        if upper_to_lower == "Upper":
            new_substring = substring.upper()
        elif upper_to_lower == "Lower":
            new_substring = substring.lower()
        raw_key = raw_key.replace(substring, new_substring)
        print(raw_key)
    elif action[0] == "Slice":
        start_index = int(action[1])
        end_index = int(action[2])
        raw_key = raw_key[:start_index] + raw_key[end_index:]
        print(raw_key)

print(f"Your activation key is: {raw_key}")
