longest_intersection = set()

# you will be given a number N.
for _ in range(int(input())):
    # on each of the next N lines you will be given two ranges in the format:
    # "{first_start},{first_end}-{second_start},{second_end}".
    first_data, second_data = [element.split(",") for element in input().split("-")]
    # The start and end numbers in the ranges are inclusive!
    first_set = set(range(int(first_data[0]), int(first_data[1]) + 1))
    second_set = set(range(int(second_data[0]), int(second_data[1]) + 1))

    # you should find the longest intersection of all N intersections,
    # print the numbers that are included and its length
    intersection = first_set.intersection(second_set)

    if len(intersection) > len(longest_intersection):
        longest_intersection = intersection

print(f"Longest intersection is [{', '.join(str(x) for x in longest_intersection)}] with length {len(longest_intersection)}")
