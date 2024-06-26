taxed_vehicles = input().split(">>")

initial_tax = 0
total_tax = 0
total_collected_taxes = 0

# First elem [0], second elem [1], third elem[2]
# car type, years taxed, kilometers
for vehicles in taxed_vehicles:
    vehicles_type = vehicles.split()
    taxed_years = int(vehicles_type[1])
    kilometers_travelled = int(vehicles_type[2])

    if vehicles_type[0] == "family":
        initial_tax = 50
        kilometers_tax_increase = kilometers_travelled // 3000
        total_tax = initial_tax + (kilometers_tax_increase * 12) - (taxed_years * 5)
    elif vehicles_type[0] == "heavyDuty":
        initial_tax = 80
        kilometers_tax_increase = kilometers_travelled // 9000
        total_tax = initial_tax + (kilometers_tax_increase * 14) - (taxed_years * 8)
    elif vehicles_type[0] == "sports":
        initial_tax = 100
        kilometers_tax_increase = kilometers_travelled // 2000
        total_tax = initial_tax + (kilometers_tax_increase * 18) - (taxed_years * 9)
    else:
        print("Invalid car type.")
        continue

    total_collected_taxes += total_tax
    print(f"A {vehicles_type[0]} car will pay {total_tax:.2f} euros in taxes.")
print(f"The National Revenue Agency will collect {total_collected_taxes:.2f} euros in taxes.")