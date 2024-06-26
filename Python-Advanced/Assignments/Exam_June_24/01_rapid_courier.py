from collections import deque

# On the first line, you will receive integers representing the weight of the packages to be delivered,
# separated by a single space.
packages = deque(int(package) for package in input().split())
# On the second line, you will receive integers representing the capacities of the couriers,
# separated by a single space.
couriers = deque(int(courier) for courier in input().split())

# Track the total weight of packages delivered by your couriers.
total_delivered_weight = 0


while packages and couriers:
    package = packages[-1]
    courier = couriers.popleft()

    if courier >= package:
        total_delivered_weight += package
        packages.pop()

        if courier > 2 * package:
            courier -= 2 * package
            couriers.append(courier)
    else:
        total_delivered_weight += courier
        package -= courier
        packages[-1] = package

total_weight = total_delivered_weight
print(f"Total weight: {total_weight} kg")

if not packages and not couriers:
    print("Congratulations, all packages were delivered successfully by the couriers today.")

elif packages:
    print(f"Unfortunately, there are no more available couriers to deliver the following packages: "
          f"{', '.join(str(p) for p in packages)}")
elif couriers:
    print(f"Couriers are still on duty: {', '.join(str(c) for c in couriers)} but there are no more packages to deliver.")
