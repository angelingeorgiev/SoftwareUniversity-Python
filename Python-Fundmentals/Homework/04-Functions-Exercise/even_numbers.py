user_input = input().split(" ")
numbers_as_digits = []

for number in user_input:
    numbers_as_digits.append(int(number))

# A lambda function is a small anonymous function.
is_even = lambda x: x % 2 == 0

result = list(filter(is_even, numbers_as_digits))
print(result)
