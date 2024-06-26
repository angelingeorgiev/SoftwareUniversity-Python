def blacksmith_shop(journal):
    while True:
        command = input()
        if command == "Craft!":
            break
        current_command = command.split(" - ")
        action = current_command[0]
        item = current_command[1]

        if action == "Collect":
            if item not in journal:
                journal.append(item)
        elif action == "Drop":
            if item in journal:
                journal.remove(item)
        elif action == "Combine Items":
            items = item.split(":")
            first_item = items[0]
            second_item = items[1]

            if first_item in journal:
                index_of_item = journal.index(first_item)
                journal.insert(index_of_item + 1, second_item)
        elif action == "Renew":
            if item in journal:
                journal.remove(item)
                journal.append(item)
    return ", ".join(journal)


collecting_items = input().split(", ")
print(blacksmith_shop(collecting_items))
