items = input().split(" ")
bakery = {}

for i in range(0, len(items), 2):
    products = items[i]
    quantity = int(items[i + 1])
    bakery[products] = quantity

searched_products = input().split(" ")
for product in searched_products:
    if product in bakery:
        print(f"We have {bakery[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")
