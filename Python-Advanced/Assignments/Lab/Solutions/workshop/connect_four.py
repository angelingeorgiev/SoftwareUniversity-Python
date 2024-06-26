ROWS = 6
COLUMNS = 7

direction_mapper = {
    "up": (-1, 0),
    "down": (1, 0),

    "left": (0, -1),
    "right": (0, 1),

    "up_left": (-1, -1),
    "down_right": (1, 1),

    "down_left": (1, -1),
    "up_right": (-1, 1),
}


class FullColumnError(Exception):
    pass


def check_direction(board,row_index, column_index, row_movement_index, column_movement_index, player_number):
    count = 0
    for i in range(1, 4):
        current_row_index = row_index + row_movement_index
        current_column_index = column_index + column_movement_index

        if board[current_row_index][current_column_index] != player_number:
            return count
        count += 1


def check_opposite_direction(board,row_index, column_index, row_movement_index, column_movement_index, player_number):
    count = 0
    for i in range(1, 4):
        current_row_index = row_index - row_movement_index
        current_column_index = column_index - column_movement_index

        if board[current_row_index][current_column_index] != player_number:
            return count
        count += 1


def is_winner(board,row_index, column_index, player_number):
    for direction, values in direction_mapper.items():
        result = 1
        # Check current direction
        row_movement_index, column_movement_index = values
        direction_count = check_direction(board, row_index, column_index, row_movement_index, column_movement_index, player_number)
        # Check opposite direction
        opposite_count = check_opposite_direction(board, row_index, column_index, row_movement_index, column_movement_index, player_number)

        result += (direction_count + opposite_count)
        if result == 4:
            return True
    return False


board = []

for _ in range(ROWS):
    board.append([0 for element in range(COLUMNS)])


def print_board(board_visualisation):
    for data_row in board_visualisation:
        print(data_row)


def is_valid_column_choice(column_number):
    return 1 <= column_number <= COLUMNS


def place_player_choice(board, column_index, player_number):
    for row_index in range(len(board)-1, -1, -1):
        if board[row_index][column_index] == 0:
            board[row_index][column_index] = player_number
            return row_index, column_index
    raise FullColumnError


print_board(board)

#  -- MAIN PART --
turn = 1
while True:
    player_number = 2 if turn % 2 == 0 else 1
    try:
        selected_column = int(input(f"Player {player_number}, please choose a column: "))
    except ValueError:
        print("Please enter a valid digit")
        continue

    if not is_valid_column_choice(selected_column):
        print(f"Please select a number between 1 and {COLUMNS}")
        continue
    #  index 0-6, thus why we use selected_column -1
    selected_col_index = selected_column - 1
    try:
        current_row, current_column = place_player_choice(board, selected_col_index, player_number)
    except FullColumnError:
        print(f"This column is full. Please select another one.")
        continue

    if is_winner(board, current_row, current_column, player_number):
        print(f"Player {player_number} wins!")
        break

    print_board(board)
    # Change player number
    turn += 1


print_board(board)
