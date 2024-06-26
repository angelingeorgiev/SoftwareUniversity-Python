notes = [0] * 10

while True:
    to_do_notes = input()

    if to_do_notes == "End":
        break

    parts = to_do_notes.split("-")

    priority = int(parts[0]) - 1
    note = parts[1]

    notes.pop(priority)
    notes.insert(priority, note)

result = [item for item in notes if item != 0]
print(result)
