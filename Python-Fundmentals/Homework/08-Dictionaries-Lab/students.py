command = input()
students = {}

while not students.get(command):
    command = command.split(":")
    name = command[0]
    ID = command[1]
    # Using -1 to access the last elem of the 'command'
    course = command[-1]

    if course not in students:
        students[course] = {}
    students[course][name] = ID
    command = input()
    command = command.replace("_", " ")

for name, ID in students[command].items():
    print(f"{name} - {ID}")
