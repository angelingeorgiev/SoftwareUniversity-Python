first_input, second_input = input().split(" ")
total_sum = 0


if len(first_input) > len(second_input):
    # Multiplication
    for index in range(len(second_input)):
        total_sum += ord(first_input[index]) * ord(second_input[index])
    for index in range(len(second_input), len(first_input)):
        total_sum += ord(first_input[index])
elif len(second_input) > len(first_input):
    for index in range(len(first_input)):
        total_sum += ord(first_input[index]) * ord(second_input[index])
    for index in range(len(first_input), len(second_input)):
        total_sum += ord(second_input[index])
elif len(second_input) == len(first_input):
    for index in range(len(second_input)):
        total_sum += ord(first_input[index]) * ord(second_input[index])

print(total_sum)