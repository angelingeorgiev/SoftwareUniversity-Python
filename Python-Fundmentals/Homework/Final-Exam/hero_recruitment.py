collection_of_heros = {}

while True:
    command = input()
    if command == "End":
        break

    action = command.split(" ")
    if action[0] == "Enroll":
        hero_name = action[1]
        if hero_name not in collection_of_heros:
            collection_of_heros[hero_name] = []
        else:
            print(f"{hero_name} is already enrolled.")
    elif action[0] == "Learn":
        hero_name = action[1]
        spell_name = action[2]
        if hero_name not in collection_of_heros:
            print(f"{hero_name} doesn't exist.")
        elif spell_name in collection_of_heros[hero_name]:
            print(f"{hero_name} has already learnt {spell_name}.")
        else:
            collection_of_heros[hero_name].append(spell_name)
    elif action[0] == "Unlearn":
        hero_name = action[1]
        spell_name = action[2]
        if hero_name not in collection_of_heros:
            print(f"{hero_name} doesn't exist.")
        elif spell_name not in collection_of_heros[hero_name]:
            print(f"{hero_name} doesn't know {spell_name}.")
        else:
            collection_of_heros[hero_name].remove(spell_name)

print("Heroes:")
for hero_name, spells in collection_of_heros.items():
    print(f"== {hero_name}: {', '.join(spells)}")
