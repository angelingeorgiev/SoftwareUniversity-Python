file = open("numbers.txt", "r")
numbers_sum = 0

for number in file:
    numbers_sum += int(number)

print(numbers_sum)
