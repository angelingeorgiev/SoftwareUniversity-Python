all_stops = input()
action = input().split(":")

while action[0] != "Travel":
    if action[0] == "Add Stop":
        index, some_string = int(action[1]), action[2]
        if index in range(len(all_stops)):
            all_stops = all_stops[:index] + some_string + all_stops[index:]

    elif action[0] == "Remove Stop":
        start_index, end_index = int(action[1]), int(action[2])
        if start_index in range(len(all_stops)) and end_index in range(len(all_stops)):
            all_stops = all_stops[:start_index] + all_stops[end_index+1:]

    elif action[0] == "Switch":
        old_string, new_string = action[1], action[2]
        if old_string in all_stops:
            all_stops = all_stops.replace(old_string, new_string)
    print(all_stops)
    action = input().split(":")

print(f"Ready for world tour! Planned stops: {all_stops}")
