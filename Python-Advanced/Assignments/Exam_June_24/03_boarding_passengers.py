def boarding_passengers(capacity, *passenger_list):
    boarded = {}
    total_passengers = sum(group[0] for group in passenger_list)

    for group in passenger_list:
        num_of_passengers, benefit_program = group
        if num_of_passengers <= capacity:
            if benefit_program not in boarded:
                boarded[benefit_program] = 0
            boarded[benefit_program] += num_of_passengers
            capacity -= num_of_passengers
        # If the capacity is zero, stop boarding
        if capacity == 0:
            break

    # Sorting the boarding details
    sorted_boarding_details = sorted(boarded.items(), key=lambda x: (-x[1], x[0]))

    # Return the sorted boarding details per each benefit plan
    result = "Boarding details by benefit plan:\n"
    for benefit_plan, num_of_passengers in sorted_boarding_details:
        result += f"## {benefit_plan}: {num_of_passengers} guests\n"

    boarded_total = sum(boarded.values())
    if boarded_total == total_passengers:
        result += "All passengers are successfully boarded!"
    elif capacity == 0:
        result += "Boarding unsuccessful. Cruise ship at full capacity."
    else:
        result += f"Partial boarding completed. Available capacity: {capacity}."

    return result

# Test code
# print(boarding_passengers(150, (35, 'Diamond'), (55, 'Platinum'), (35, 'Gold'), (25, 'First Cruiser')))