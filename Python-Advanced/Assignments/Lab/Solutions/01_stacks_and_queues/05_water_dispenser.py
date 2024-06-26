from collections import deque

lt_water = int(input())
queue = deque([])

name = input()

while name != "Start":
    queue.append(name)
    name = input()

command = input()

while command != "End":
    if command.isdigit():
        lt_wanted = int(command)
        person = queue.popleft()

        if lt_water >= lt_wanted:
            # person = queue.popleft()
            print(f"{person} got water")
            lt_water -= lt_wanted
        else:
            # person = queue.popleft()
            print(f"{person} must wait")
    else:
        _, lt_to_refill = command.split()
        lt_to_refill = int(lt_to_refill)
        lt_water += lt_to_refill
    command = input()
print(f"{lt_water} liters left")
