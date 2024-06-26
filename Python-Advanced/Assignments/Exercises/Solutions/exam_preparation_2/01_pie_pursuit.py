from collections import deque

# The first sequence represents contestants, each value indicating the total count of pieces of pie a contestant can
# consume, while the second sequence represents the pies, signifying the number of pieces each pie contains.
contestants = deque(int(contestant) for contestant in input().split())
pies = [int(pie) for pie in input().split()]

while contestants and pies:
    contestant = contestants.popleft()
    pie_size = pies.pop()

    if contestant >= pie_size:
        contestant -= pie_size

        if contestant > 0:
            contestants.append(contestant)
    else:
        pie_size -= contestant

        if pies and pie_size == 1:
            pies[-1] += pie_size
        else:
            pies.append(pie_size)

# The following result should be printed on the Console, on separate lines:
if not pies and not contestants:
    print("We have a champion!")

elif contestants:
    print("We will have to wait for more pies to be baked!")
    print(f"Contestants left: {', '.join(str(c) for c in contestants)}")

elif pies:
    print("Our contestants need to rest!")
    print(f"Pies left: {', '.join(str(p) for p in pies)}")

