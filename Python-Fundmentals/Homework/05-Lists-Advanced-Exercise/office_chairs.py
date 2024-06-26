num_of_rooms = int(input())

room = 0
free_chair = 0

for i in range(num_of_rooms):
    chairs = input().split(" ")
    room += 1

    if len(chairs[0]) >= int(chairs[1]):
        free_chair += len(chairs[0]) - int(chairs[1])

    else:
        needed_chairs = int(chairs[1]) - len(chairs[0])
        print(f"{needed_chairs} more chairs needed in room {room}")

if free_chair >= 0:
    print(f"Game On, {free_chair} free chairs left")
