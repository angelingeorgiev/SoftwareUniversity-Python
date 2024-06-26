items = {"shards": 0, "fragments": 0, "motes": 0}

obtained = False
while not obtained:
    current_items = input().split()

    for index in range(0, len(current_items), 2):
        current_material = current_items[index + 1].lower()
        current_quantity = int(current_items[index])

        if current_material not in items.keys():
            items[current_material] = 0
        items[current_material] += current_quantity
        if items["shards"] >= 250:
            items["shards"] -= 250
            print(f"Shadowmourne obtained!")
            obtained = True

        elif items["fragments"] >= 250:
            items["fragments"] -= 250
            print(f"Valanyr obtained!")
            obtained = True

        elif items["motes"] >= 250:
            items["motes"] -= 250
            print(f"Dragonwrath obtained!")
            obtained = True
        if obtained:
            break


for material, quantity in items.items():
    print(f"{material}: {quantity}")

