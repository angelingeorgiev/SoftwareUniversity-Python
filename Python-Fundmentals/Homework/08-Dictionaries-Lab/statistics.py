products = {}

while True:
    command = input()

    if command == "statistics":
        break

    product, quantity = command.split(": ")
    quantity = int(quantity)

    if product in products:
        products[product] += quantity
    else:
        products[product] = quantity

product_count = len(products)
quantity_count = sum(products.values())

print("Products in stock:")
for product, quantity in products.items():
    print(f"- {product}: {quantity}")

print(f"Total Products: {product_count}")
print(f"Total Quantity: {quantity_count}")
