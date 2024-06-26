# A perfect number is a positive int that is equal to the sum of its divisors, excluding the number itself.

def is_perfect_number(some_number: int) -> str:
    divisors_sum = 0
    for divisor in range(1, some_number):
        if some_number % divisor == 0:
            divisors_sum += divisor
    if some_number == divisors_sum:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."


number = int(input())
print(is_perfect_number(number))
