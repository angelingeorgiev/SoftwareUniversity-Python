number_of_lines = int(input())

numbers = []
filtered_numbers = []

for number in range(number_of_lines):
    current_number = int(input())
    numbers.append(current_number)

command = input()
if command == "even":
    for number in numbers:
        if number % 2 == 0:
            filtered_numbers.append(number)
elif command == "odd":
    for number in numbers:
        if number % 2 != 0:
            filtered_numbers.append(number)
elif command == "negative":
    for number in numbers:
        if number < 0:
            filtered_numbers.append(number)
elif command == "positive":
    for number in numbers:
        if number >= 0:
            filtered_numbers.append(number)

print(filtered_numbers)
