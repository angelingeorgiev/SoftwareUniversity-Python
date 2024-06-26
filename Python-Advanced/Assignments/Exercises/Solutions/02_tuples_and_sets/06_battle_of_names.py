# save the result to a set of either odd or even number
odd_set = set()
even_set = set()

for row in range(1, int(input()) +1):
    # sum the ASCII values of each letter in the name and integer divide it by the number of the current row
    ascii_sum_of_name = sum(ord(letter) for letter in input()) // row

    if ascii_sum_of_name % 2 == 0:
        # save the result to a set of either odd or even numbers, depending on if the resulting number is odd or eve
        even_set.add(ascii_sum_of_name)
    else:
        odd_set.add(ascii_sum_of_name)

odd_set_sum, even_set_sum = sum(odd_set), sum(even_set)
# if the sums of the two sets are equal, print the union of the values, separated by ",
if even_set_sum == odd_set_sum:
    print(*odd_set.union(even_set), sep=", ")
# if the sum of the odd numbers is bigger than the sum of the even numbers, print the different value
elif odd_set_sum > even_set_sum:
    print(*odd_set.difference(even_set), sep=", ")
else:
    print(*odd_set.symmetric_difference(even_set), sep=", ")
