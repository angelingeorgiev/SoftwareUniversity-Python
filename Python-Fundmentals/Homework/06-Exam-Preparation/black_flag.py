days = int(input())
plunder_per_day = int(input())
expected_plunder = float(input())

total_plunder = 0

for day in range(1, days + 1):
    total_plunder += plunder_per_day

    if day % 3 == 0:
        total_plunder += 0.5 * plunder_per_day
    if day % 5 == 0:
        total_plunder *= 0.7

if total_plunder >= expected_plunder:
    print(f"Ahoy! {total_plunder:.2f} plunder gained.")
else:
    needed = (total_plunder / expected_plunder) * 100
    print(f"Collected only {needed:.2f}% of the plunder.")
