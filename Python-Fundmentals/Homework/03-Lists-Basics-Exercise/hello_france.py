items = input().split("|")
budget = float(input())

new_prices = []
profit = 0

for item in items:
    token = item.split("->")
    type_item = token[0]
    price = float(token[1])
    is_valid = False

    if budget < price:
        continue

    if type_item == "Clothes" and price <= 50:
        is_valid = True
    elif type_item == "Shoes" and price <= 35:
        is_valid = True
    elif type_item == "Accessories" and price <= 20.50:
        is_valid = True

    if is_valid:
        budget -= price
        new_price = price * 1.4 #40% markup
        profit += new_price - price
        new_prices.append(new_price)
new_budget = budget + sum(new_prices)

print(" ".join([f"{j:.2f}" for j in new_prices]))
print(f"Profit: {profit:.2f}")

if new_budget >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")
