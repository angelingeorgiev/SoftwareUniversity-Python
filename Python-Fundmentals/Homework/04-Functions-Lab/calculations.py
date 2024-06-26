operators = input()
first_number = int(input())
second_number = int(input())


def solve(operator, num1, num2):
    result = None

    if operator == "multiply":
        return num1 * num2
    elif operator == "divide":
        return num1 // num2
    elif operator == "add":
        return num1 + num2
    elif operator == "subtract":
        return num1 - num2

    return result


result = solve(operators, first_number, second_number)
print(result)
