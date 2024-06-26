def find_min_max_sum(number):
    list_of_integers = []

    for character in user_input:
        list_of_integers.append(int(character))
    min_number = min(list_of_integers)
    max_number = max(list_of_integers)
    sum_of_numbers = 0

    for num in list_of_integers:
        sum_of_numbers += num
    return (f"The minimum number is {min_number}\n"
            f"The maximum number is {max_number}\n"
            f"The sum number is: {sum_of_numbers}")


user_input = input().split(" ")
print(find_min_max_sum(user_input))
