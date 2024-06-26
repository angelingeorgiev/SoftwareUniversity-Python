# Factorial integer is the product of all positive integers less than or equal to n.

def factorial_devisioner(number):
    for current_number in range(1, number):
        number *= current_number
    return number  #initial number factorial


first_number = int(input())
second_number = int(input())

first_number_factorial = factorial_devisioner(first_number)
second_number_factorial = factorial_devisioner(second_number)

result = first_number_factorial // second_number_factorial
print(f"{result:.2f}")
