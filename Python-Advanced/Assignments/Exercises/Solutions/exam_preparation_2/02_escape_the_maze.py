direction_mapper = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}


n = int(input())
health = 100
maze = []
traveler_row, traveler_column = 0, 0

for row in range(n):
    maze.append([x for x in input()])
    for column in range(n):
        if maze[row][column] == "P":
            traveler_row, traveler_column = row, column

while True:
    move = input()
    if not (0 <= traveler_row + direction_mapper[move][0] < n and 0 <= traveler_column + direction_mapper[move][1] < n):
        continue

    maze[traveler_row][traveler_column] = "-"
    traveler_row += direction_mapper[move][0]
    traveler_column += direction_mapper[move][1]

    if maze[traveler_row][traveler_column] == "X":
        print("Player escaped the maze. Danger passed!")
        # The last known position of the traveller should always be marked with 'P' in the final state of the matrix
        maze[traveler_row][traveler_column] = "P"
        break
    elif maze[traveler_row][traveler_column] == "H":
        health = min(health + 15, 100)
    elif maze[traveler_row][traveler_column] == "M":
        health -= 40
        # traveller's health drops to 0 or below due to the encounter with a monster,
        # the traveller is considered defeated, health is set to zero
        if health <= 0:
            health = 0
            print("Player is dead. Maze over!")
            maze[traveler_row][traveler_column] = "P"
            break
    maze[traveler_row][traveler_column] = "P"

print(f"Player's health: {health} units")
for row in maze:
    print(''.join(row))
