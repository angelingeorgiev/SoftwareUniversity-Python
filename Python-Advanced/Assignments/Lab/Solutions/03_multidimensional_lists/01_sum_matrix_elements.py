data = input().split(", ")
row_number, column_number = int(data[0]), int(data[1])


matrix = []
sum_numbers = 0
for row in range(row_number):
    # The matrix itself
    row_data = input().split(", ")
    row_numbers = []
    for i in range(len(row_data)):
        # The sum of all numbers in the matrix
        current_element = int(row_data[i])
        sum_numbers += current_element
        row_numbers.append(current_element)

    matrix.append(row_numbers)

print(sum_numbers)
print(matrix)
