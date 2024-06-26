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
position_of_the_bee = None
energy_restored = False
initial_energy = 15
collected_nectar = 0

# Read matrix input and find initial position of the bee
for row_index in range(n):
    row_data = list(input())
    matrix.append(row_data)
    if "B" in row_data:
        column_index = row_data.index("B")
        position_of_the_bee = (row_index, column_index)

# Read movements until energy runs out
while initial_energy > 0:
    bee_movement = input()

    current_row, current_column = position_of_the_bee
    row_movement_i, column_movement_i = direction_mapper[bee_movement]
    next_row_index = (row_movement_i + current_row) % n
    next_column_index = (column_movement_i + current_column) % n

    flower = matrix[next_row_index][next_column_index]
    matrix[current_row][current_column] = "-"
    matrix[next_row_index][next_column_index] = "B"

    position_of_the_bee = (next_row_index, next_column_index)
    initial_energy -= 1  # Decrease energy with each move

    # Check if the bee collects nectar or reaches the hive
    if flower.isdigit():
        collected_nectar += int(flower)
        if collected_nectar >= 30:
            break

    elif flower == "H":
        if collected_nectar >= 30:
            if not energy_restored:
                extra_nectar = collected_nectar - 30
                collected_nectar = 30
                energy_restored = True
            print(f"Great job, Beesy! The hive is full. Energy left: {initial_energy}")
        else:
            print("Beesy did not manage to collect enough nectar.")
        print_matrix_function(matrix)
        break

    # Check if the bee runs out of energy
    if initial_energy <= 0:
        if collected_nectar >= 30 and not energy_restored:
            extra_nectar = collected_nectar - 30
            initial_energy += extra_nectar
            if initial_energy > 15:  # cap energy to maximum of 15
                initial_energy = 15
            collected_nectar = 30
            energy_restored = True
        if energy_restored:
            print(f"This is the end! Beesy ran out of energy.")
        else:
            print("This is the end! Beesy ran out of energy.")
        print_matrix_function(matrix)