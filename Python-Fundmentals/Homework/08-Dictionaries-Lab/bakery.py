items = input().split(" ")
bakery = {}

for i in range(0, len(items), 2):
    # През стъпка 2, защото вземаме два елемента!
    food = items[i]
    quantity = int(items[i + 1])
    bakery[food] = quantity


print(bakery)
