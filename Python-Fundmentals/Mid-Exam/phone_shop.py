phone_models = input().split(", ")

while True:
    action = input().split(' - ')
    if action[0] == "End":
        break

    phone = action[1]
    if action[0] == "Add":
        if phone not in phone_models:
            phone_models.append(phone)
    elif action[0] == "Remove":
        if phone in phone_models:
            phone_models.remove(phone)
    elif action[0] == "Bonus phone":
        old_phone, new_phone = phone.split(":")
        if old_phone in phone_models:
            index = phone_models.index(old_phone) + 1
            phone_models.insert(index, new_phone)
    elif action[0] == "Last":
        if phone in phone_models:
            index = phone_models.index(phone)
            last_phone = phone_models.pop(index)
            phone_models.append(last_phone)

print(", ".join(phone_models))
