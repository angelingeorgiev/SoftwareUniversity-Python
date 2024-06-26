given_numbers = input().split(" ")

round_numbers = []

for number in given_numbers:
    round_numbers.append(round(float(number)))

print(round_numbers)
