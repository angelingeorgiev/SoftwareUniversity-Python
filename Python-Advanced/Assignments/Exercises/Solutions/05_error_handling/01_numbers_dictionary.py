numbers_dictionary = {}
line = input()


while line != "Search":
    number_as_string = line
    try:
        number = int(input())
    except ValueError:
        print("The variable number must be an integer")
    else:
        numbers_dictionary[number_as_string] = number

    # Going back to reading the input
    line = input()

line = input()

# Infinite loop*
while line != "Remove":
    searched = line
    try:
        print(numbers_dictionary[searched])
    except KeyError:
        print("Number does not exist in dictionary")
    # Added this line, so it exits the infinite loop by continuing reading the input
    line = input()

line = input()
while line != "End":
    searched = line
    try:
        del numbers_dictionary[searched]
    except KeyError:
        print("Number does not exist in dictionary")
    # Added this line
    line = input()
    print(numbers_dictionary)
