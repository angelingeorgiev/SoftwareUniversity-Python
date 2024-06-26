groceries_list = input().split("!")

while True:
    command = input()
    if command == "Go Shopping!":
        break

    action = command.split(" ")
    if action[0] == "Urgent":
        item = action[1]

        if item not in groceries_list:
            groceries_list.insert(0, item)
    elif action[0] == "Unnecessary":
        item = action[1]

        if item in groceries_list:
            groceries_list.remove(item)
    elif action[0] == "Correct":
        old_item = action[1]
        new_item = action[2]

        if old_item in groceries_list:
            index = groceries_list.index(old_item)
            groceries_list[index] = new_item
    elif action[0] == "Rearrange":
        item = action[1]

        if item in groceries_list:
            groceries_list.remove(item)
            groceries_list.append(item)

print(", ".join(groceries_list))
