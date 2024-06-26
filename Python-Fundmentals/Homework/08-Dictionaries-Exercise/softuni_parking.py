parking_lot = {}
num_of_commands = int(input())

for entry in range(num_of_commands):
    command = input().split(" ")

    action = command[0]
    username = command[1]
    if action == "register":
        license_plate = command[2]
        if username not in parking_lot.keys():
            parking_lot[username] = license_plate
            print(f"{username} registered {license_plate} successfully")
        else:
            print(f"ERROR: already registered with plate number {license_plate}")
    elif action == "unregister":
        if username not in parking_lot.keys():
            print(f"ERROR: user {username} not found")
        else:
            del parking_lot[username]
            print(f"{username} unregistered successfully")

for username, license_plate in parking_lot.items():
    print(f"{username} => {license_plate}")
