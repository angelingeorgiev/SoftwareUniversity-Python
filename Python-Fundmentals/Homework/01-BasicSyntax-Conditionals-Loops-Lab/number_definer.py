number_input = float(input())

if number_input == 0:
    print("zero")
elif number_input > 0:
    if number_input < 1:
        print("small positive")
    elif number_input > 1000000:
        print("large positive")
    else:
        print("positive")
else:
    if abs(number_input) < 1:
        print("small negative")
    elif abs(number_input) > 1000000:
        print("large negative")
    else:
        print("negative")
