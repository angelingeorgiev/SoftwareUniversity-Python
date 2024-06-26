gifts_to_buy = input().split()
command = input()

while command != "No Money":
    command = command.split()

    if command[0] == "OutOfStock":
        for i in range(len(gifts_to_buy)):
            if command[1] == gifts_to_buy[i]:
                gifts_to_buy[i] = "None"
    elif command[0] == "Required":
        index = int(command[2])
        if 0 < index < len(gifts_to_buy):
            gifts_to_buy[index] = command[1]
    elif command[0] == "JustInCase":
        gifts_to_buy[-1] = command[1]

    command = input()

if "None" in gifts_to_buy:
    for elem in range(len(gifts_to_buy) - 1, -1, -1):
        if "None" in gifts_to_buy[elem]:
            gifts_to_buy.remove(gifts_to_buy[elem])
print(" ".join(gifts_to_buy))
