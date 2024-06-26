user_input = input().split(" ")
sorted_numbers = []

for number in user_input:
    sorted_numbers.append(int(number))

result = list(sorted(sorted_numbers))
print(result)
