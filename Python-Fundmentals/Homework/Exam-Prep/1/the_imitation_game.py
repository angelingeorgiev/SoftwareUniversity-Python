# encrypted_message = input()
#
# while True:
#     command = input()
#     if command == "Decode":
#         break
#     instructions = command.split("|")
#     operation = instructions[0]
#
#     if operation == "Move":
#         num_of_letters = int(instructions[1])
#         counter = int(instructions[1])
#         for letter in encrypted_message:
#             encrypted_message += letter
#             counter -= 1
#             if counter == 0:
#                 break
#         encrypted_message = encrypted_message[num_of_letters::]
#     elif operation == "Insert":
#         index = int(instructions[1])
#         character_to_insert = instructions[2]
#         encrypted_message = encrypted_message[:index] + character_to_insert + encrypted_message[index:]
#     elif operation == "ChangeAll":
#         character_to_replace = instructions[1]
#         new_char = instructions[2]
#         encrypted_message = encrypted_message.replace(character_to_replace, new_char)
#
# decrypted_message = encrypted_message
# print(f"The decrypted message is: {decrypted_message}")


# -- Variant 2 --
def decode_message(msg, commands):
    for command in commands:
        tokens = command.split("|")
        instruction = tokens[0]

        if instruction == "Move":
            num_letters = int(tokens[1])
            msg = msg[num_letters:] + msg[:num_letters]
        elif instruction == "Insert":
            index = int(tokens[1])
            value = tokens[2]
            msg = msg[:index] + value + msg[index:]
        elif instruction == "ChangeAll":
            char_to_replace = tokens[1]
            new_character = tokens[2]
            msg = msg.replace(char_to_replace, new_character)
        elif instruction == "Decode":
            print(f"The decrypted message is: {msg}")


encrypted_message = input()
commands_list = []

while True:
    command = input()
    commands_list.append(command)

    if command == "Decode":
        break

decode_message(encrypted_message, commands_list)
