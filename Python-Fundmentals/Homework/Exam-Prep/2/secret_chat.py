concealed_message = input()

while True:
    command = input()
    if command == "Reveal":
        break

    action = command.split(":|:")
    if action[0] == "InsertSpace":
        index = int(action[1])
        concealed_message = concealed_message[:index] + " " + concealed_message[index:]
        print(concealed_message)
    elif action[0] == "Reverse":
        substring = action[1]
        if substring in concealed_message:
            concealed_message = concealed_message.replace(substring, "", 1) + substring[::-1]
            print(concealed_message)
        else:
            print("error")
    elif action[0] == "ChangeAll":
        substring = action[1]
        replace = action[2]
        concealed_message = concealed_message.replace(substring, replace)
        print(concealed_message)

print(f"You have a new text message: {concealed_message}")
