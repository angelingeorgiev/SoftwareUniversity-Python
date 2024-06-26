dungeon_rooms = input().split("|")

health = 100
BTC = 0
best_room = 0
is_killed = False

for room in dungeon_rooms:
    best_room += 1
    room = room.split()
    command = room[0]
    number = int(room[1])

    if command == "potion":
        temporary_health = health
        health += number

        if health > 100:
            health = 100
        amount = health - temporary_health
        print(f"You healed for {amount} hp.")
        print(f"Current health: {health} hp.")
    elif command == "chest":
        BTC += number
        print(f"You found {number} bitcoins.")
    else:
        health -= number
        if health > 0:
            print(f"You slayed {command}.")
        else:
            is_killed = True
            break

if is_killed:
    print(f"You died! Killed by {command}.")
    print(f"Best room: {best_room}")
else:
    print(f"You've made it!")
    print(f"Bitcoins: {BTC}")
    print(f"Health: {health}")
