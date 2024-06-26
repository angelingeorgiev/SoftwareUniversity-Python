wagons = int(input())
command = input().split(" ")

train = [0] * wagons # Initialize the train list with zeros

while command[0] != "End":
    # Check the command, not the entire input

    if command[0] == "add":
        people = int(command[1])
        train[-1] += people
    elif command[0] == "insert":
        people = int(command[2])
        index = int(command[1])
        train[index] += people
    elif command[0] == "leave":
        people = int(command[2])
        index = int(command[1])
        train[index] -= people

    command = input().split(" ")
print(train)
