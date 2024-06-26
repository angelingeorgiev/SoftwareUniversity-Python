user_input = input()

while True:
    command = input()
    if command == "Complete":
        break

    action = command.split(" ")
    if action[0] == "Insert":
        index = int(action[1])
        character = action[2]
        if index < len(user_input):
            user_input = user_input[:index] + character + user_input[index:]
            print(user_input)
    elif action[0] == "Make":
        make_type = action[1]
        index = int(action[2])
        if index < len(user_input):
            if make_type == "Upper":
                user_input = user_input[:index] + user_input[index].upper() + user_input[index + 1:]
                print(user_input)
            elif make_type == "Lower":
                user_input = user_input[:index] + user_input[index].lower() + user_input[index + 1:]
                print(user_input)
    elif action[0] == "Replace":
        original_char = action[1]
        value = int(action[2])
        new_char = chr(ord(original_char) + value)
        if original_char in user_input:
            user_input = user_input.replace(original_char, new_char)
            print(user_input)
    elif action[0] == "Validation":
        if len(user_input) < 8:
            print('Password must be at least 8 characters long')
        elif user_input.isalnum() == False and "_!" not in user_input:
            print("Password must consist only of letters, digits and _!")
        elif not any(i.isupper() for i in user_input):
            print("Password must consist at least one uppercase letter!")
        elif not any(i.islower() for i in user_input):
            print("Password must consist at least one lowercase letter!")
        elif not any(i.isdigit() for i in user_input):
            print("Password must consist at least one digit!")
