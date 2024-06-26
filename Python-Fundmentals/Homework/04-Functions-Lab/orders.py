order = input()
quantity = int(input())


def calc_total_price(order, quantity):
    if order == "coffee":
        return f"{1.50 * quantity:.2f}"
    elif order == "water":
        return f"{1.00 * quantity:.2f}"
    elif order == "coke":
        return f"{1.40 * quantity:.2f}"
    elif order == "snacks":
        return f"{2.00 * quantity:.2f}"


result = calc_total_price(order, quantity)
print(result)
