from collections import deque


values_of_bees = deque(int(x) for x in input().split())
nectar = [int(x) for x in input().split()]
symbols = deque(input().split())

honey = 0
# a sequence of symbols – "+", "-", "*", or "/", representing the honey-making process
operations = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b if b != 0 else 0
}

while nectar and values_of_bees:
    if nectar[-1] >= values_of_bees[0]:
        honey += abs(operations[symbols[0]](values_of_bees[0], nectar[-1]))
        nectar.pop()
        values_of_bees.popleft()
        symbols.popleft()
    else:
        nectar.pop()

print(f"Total honey made: {honey}")
if values_of_bees:
    print(f"Bees left: {', '.join(str(x) for x in values_of_bees)}")
if nectar:
    print(f"Nectar left: {', '.join(str(x) for x in nectar)}")
