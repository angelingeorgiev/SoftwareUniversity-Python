user_input = input().split(" ")
n = int(input())

numbers = [int(num) for num in user_input]

for _ in range(n):
    min_value = min(numbers)
    numbers.remove(min_value)

result = ", ".join(map(str, numbers))
print(result)
