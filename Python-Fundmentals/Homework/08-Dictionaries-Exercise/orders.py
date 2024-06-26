products = {}
while True:
    command = input()

    if command == "buy":
        break

    order = command.split()
    product = order[0]
    price = float(order[1])
    quantity = int(order[2])
    if product not in products.keys():
        products[product] = []
        products[product].append(price)
        products[product].append(quantity)
    else:
        if products[product][0] != price:
            products[product][0] = price
        products[product][1] += quantity

for key, value in products.items():
    price_of_item = value[0] * value[1]
    print(f"{key} -> {price_of_item:.2f}")
