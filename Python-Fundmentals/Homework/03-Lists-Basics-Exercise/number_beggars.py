string_of_integers = input().split(", ")
count_of_beggars = int(input())

list_of_beggars_sum = []

for current_beggar in range(count_of_beggars):
    current_beggar_sum = 0

    for i in range(current_beggar, len(string_of_integers), count_of_beggars):
        current_sum = int(string_of_integers[i])
        current_beggar_sum += current_sum

    list_of_beggars_sum.append(current_beggar_sum)
    current_beggar_sum -= current_beggar_sum

print(list_of_beggars_sum)
