user_input = input().split(" ")

reversed_list = []

for i in user_input:
    i = int(i)
    reversed_list.append(-i)

print(reversed_list)
