from collections import deque

command = input()
queue = deque([])

while command != "End":
    if command == "Paid":
        while queue:
            print(queue.popleft()) #Removes from left to right when 'paid' is engaged
    else:
        queue.append(command)
    command = input()

print(f"{len(queue)} people remaining.")
