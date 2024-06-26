sequence_of_numbers = [int(s) for s in input().split(", ")]
current_group = 10

while sequence_of_numbers:
    filtered_numbers = [num for num in sequence_of_numbers if num <= current_group]
    print(f"Group of {current_group}'s: {filtered_numbers}")
    current_group += 10
    sequence_of_numbers = [num for num in sequence_of_numbers if num not in filtered_numbers]
    