event_input = input().split("|")
total_coins = 100
total_energy = 100

is_open = True
for event in event_input:
    event_items = event.split("-")
    type_of_event = event_items[0]
    event_qty = int(event_items[1])
    # type_of_event, event_qty = event.split("-")

    if type_of_event == "rest":
        curr_energy = total_energy
        total_energy += event_qty
        if total_energy > 100:
            total_energy = 100
        gained_energy = total_energy - curr_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {total_energy}.")
    elif type_of_event == "order":
        if total_energy >= 30:
            total_energy -= 30
            total_coins += event_qty
            print(f"You earned {event_qty} coins.")
        else:
            total_energy += 50
            print("You had to rest!")
    else:
        if total_coins >= event_qty:
            total_coins -= event_qty
            print(f"You bought {type_of_event}.")
        else:
            print(f"Closed! Cannot afford {type_of_event}.")
            is_open = False
            break

if is_open:
    print("Day completed!")
    print(f"Coins: {total_coins}")
    print(f"Energy: {total_energy}")
