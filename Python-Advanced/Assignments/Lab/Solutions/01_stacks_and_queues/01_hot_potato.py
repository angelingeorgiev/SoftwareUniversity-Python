from collections import deque

kids_names = deque(input().split())
n = int(input())
potato_toss = 0

while len(kids_names) > 1:
    for _ in range(0, n-1):
        # Get first kid on the line
        first_kid = kids_names.popleft()
        # Move the kid at the end
        kids_names.append(first_kid)
    print(f"Removed {kids_names.popleft()}")

print(f"Last is {kids_names.pop()}")
