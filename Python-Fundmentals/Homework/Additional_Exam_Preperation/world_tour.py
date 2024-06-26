all_stops = input()

while True:
    command = input().split(":")

    if command[0] == "Travel":
        print(f"Ready for world tour! Planned stops: {all_stops}")
        break
    elif command[0] == "Add Stop":
        index = int(command[1])
        string = command[2]
        if index in range(len(all_stops)):
            all_stops = all_stops[:index] + string + all_stops[index:]
            print(all_stops)
    elif command[0] == "Remove Stop":
        start_point = int(command[1])
        end_point = int(command[2])
        if start_point in range(len(all_stops)):
            all_stops = all_stops[:start_point] + all_stops[end_point + 1:]
            print(all_stops)
    elif command[0] == "Switch":
        old = command[1]
        new = command[2]
        if old in all_stops:
            all_stops = all_stops.replace(old, new)
        print(all_stops)
