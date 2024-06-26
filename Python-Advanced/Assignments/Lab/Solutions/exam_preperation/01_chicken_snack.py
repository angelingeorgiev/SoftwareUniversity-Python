from collections import deque

money = [int(element) for element in input().split()]
food_price = deque([int(element) for element in input().split()])

food_count = 0
while money and food_price:
    # If their values are equal, Henry buys the food. After that, you should remove both of them from their sequences.
    if money[-1] == food_price[0]:
        food_count += 1
        money.pop()
        food_price.popleft()

    elif money[-1] > food_price[0]:
        # Remove the current amount of money from its sequence and increase the next amount of money value in
        # the sequence by the resulting difference you have calculated.
        # Remove the price from the prices sequence.
        difference = money.pop() - food_price.popleft()
        food_count += 1
        if not money:
            money = [difference]
        else:
            money[-1] += difference

    else:
        # If the amount of money is lower than the price remove both of them from their sequence
        money.pop()
        food_price.popleft()


if food_count >= 4:
    print(f"Gluttony of the day! Henry ate {food_count} foods.")
elif 1 < food_count < 4:
    print(f"Henry ate: {food_count} foods.")
elif food_count == 1:
    print(f"Henry ate: {food_count} food.")
else:
    print("Henry remained hungry. He will try next weekend again.")
