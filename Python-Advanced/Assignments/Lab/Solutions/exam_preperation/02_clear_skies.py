def print_matrix_function(matrix):
    for row in matrix:
        print("".join(row))


direction_mapper = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}


n = int(input())

matrix = []
jet_position = None
# There will be always four enemy aircraft - fields marked with 'E'
enemy_count = 4
initial_armor = 300

for row_index in range(n):
    row_data = list(input())
    matrix.append(row_data)
    if "J" in row_data:
        column_index = row_data.index("J")
        jet_position = (row_index, column_index)

while enemy_count:
    direction = input()
    # The commands given will direct the jet-fighter only within the limits of the matrix (airspace)
    current_row, current_column = jet_position
    row_movement_index, column_movement_index = direction_mapper[direction]
    next_row_index = row_movement_index + current_row
    next_column_index = column_movement_index + current_column

    element = matrix[next_row_index][next_column_index]
    matrix[next_row_index][next_column_index] = "J"
    matrix[current_row][current_column] = "-"

    jet_position = (next_row_index, next_column_index)

    if element == "E":
        enemy_count -= 1
        if enemy_count == 0:
            print("Mission accomplished, you neutralized the aerial threat!")
            print_matrix_function(matrix)
            break
        initial_armor -= 100

        if initial_armor == 0:
            print(f"Mission failed, your jetfighter was shot down! "
                  f"Last coordinates [{jet_position[0]}, {jet_position[1]}]!")
            print_matrix_function(matrix)
            exit()
    elif element == "R":
        initial_armor = 300
