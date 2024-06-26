numbers_input = list(map(int, input().split(", ")))

indices_even_numbers = [index for index in range(len(numbers_input)) if numbers_input[index] % 2 == 0]
print(indices_even_numbers)
