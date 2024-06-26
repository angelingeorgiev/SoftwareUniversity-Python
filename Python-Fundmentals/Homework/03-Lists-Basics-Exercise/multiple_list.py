factor = int(input())
count = int(input())

new_list = []

for number in range(factor, factor * count + 1, factor):
    new_list.append(number)

print(new_list)
