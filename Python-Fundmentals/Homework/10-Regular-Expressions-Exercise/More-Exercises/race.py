import re

participants = input().split(",")
names_regex = r"([A-Za-z]+)"
racers = {}

while True:
    command = input()
    if command == "end of race":
        break
    name = "".join(re.findall(names_regex, command))
    distance = sum((int(x.group()) for x in re.finditer(r"\d", command)))
    if name in participants:
        if name in racers:
            racers[name] += distance
        else:
            racers[name] = distance

sorted_racers = [k for k, v in sorted(racers.items(), key=lambda x: x[1], reverse=True)]

print(f"1st place: {sorted_racers[0]}")
print(f"2nd place: {sorted_racers[1]}")
print(f"3rd place: {sorted_racers[2]}")

