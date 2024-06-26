import re

bought_furniture = []
total_cost = 0
regex = r">>([a-zA-Z]+)<<(\d+\.?\d+)!(\d+)"

command = input()
while command != "Purchase":
    matches = re.search(regex,command)
    if matches:
        furniture, price, quantity = matches.groups()
        bought_furniture.append(furniture)
        total_cost += float(price) * int(quantity)
    command = input()

print("Bought furniture:")
for furniture in bought_furniture:
    print(furniture)
print(f"Total money spend: {total_cost:.2f}")
