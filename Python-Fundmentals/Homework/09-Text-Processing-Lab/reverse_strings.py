while True:
    user_input = input()

    if user_input.lower() == "end":
        break

    print(f"{user_input} = {user_input[::-1]}")
