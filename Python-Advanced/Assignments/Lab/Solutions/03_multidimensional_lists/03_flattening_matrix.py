row_number = input()


matrix = []
for row in range(int(row_number)):
    row_data = [int(element) for element in input().split(", ")]
    # Extend makes them as separate elements not a list of elements
    matrix.extend(row_data)

print(matrix)
