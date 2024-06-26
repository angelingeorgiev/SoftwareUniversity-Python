def main():
    sequence_of_elements = input().split(" ")
    count_moves = 0

    while True:
        count_moves += 1
        command = input()
        if command == "end":
            print(f"Sorry you lose :(\n{' '.join(sequence_of_elements)}")
            break

        index_1, index_2 = map(int, command.split())

        if is_invalid(index_1, index_2, sequence_of_elements):
            handle_invalid_input(sequence_of_elements, count_moves)
        else:
            handle_valid_inputs(index_1, index_2, sequence_of_elements, count_moves)


def is_invalid(index_1, index_2, sequence):
    return (
        index_1 == index_2
        or index_1 < 0
        or index_2 < 0
        or index_1 >= len(sequence)
        or index_2 >= len(sequence)
    )


def handle_invalid_input(sequence_of_elem, count_moves):
    mid_index = len(sequence_of_elem) // 2
    sequence_of_elem.insert(mid_index, f'-{count_moves}a')
    sequence_of_elem.insert(mid_index, f'-{count_moves}a')
    print("Invalid input! Adding additional elements to the board")


def handle_valid_inputs(index_1, index_2, sequence_of_elements, count_moves):
    if sequence_of_elements[index_1] == sequence_of_elements[index_2]:
        print(f"Congrats! You have found matching elements - {sequence_of_elements[index_1]}!")
        second_elem = sequence_of_elements[index_2]
        sequence_of_elements.pop(index_1)
        sequence_of_elements.remove(second_elem)
    else:
        print(f"Try again!")

    if len(sequence_of_elements) == 0:
        print(f"You have won in {count_moves} turns!")
        exit()


main()
