n = int(input())


def print_row(size, row):
    print(f'{" " * (size - row)}{"* "* row}')


def print_upper_part(size):
    for row in range(1, size+1):
        print_row(size, row)


def print_lower_part(size):
    for row in range(size - 1, 0, -1):
        print_row(size, row)


def print_rhombus(size):
    print_upper_part(n)
    print_lower_part(n)


print_rhombus(n)
