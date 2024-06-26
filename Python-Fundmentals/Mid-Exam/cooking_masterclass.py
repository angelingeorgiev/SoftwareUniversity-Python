import math

budget = float(input())
students = int(input())

price_flour = float(input())
price_egg = float(input())
price_apron = float(input())

free_flour = 0
for student in range(students + 1):
    if not student == 0 and student % 5 == 0:
        free_flour += 1

apron_total = price_apron * (math.ceil(students * 1.2))
egg_total = price_egg * 10 * students
flour_total = price_flour * (students - free_flour)
total_sum = apron_total + egg_total + flour_total

if total_sum <= budget:
    print(f"Items purchased for {total_sum:.2f}$.")
else:
    difference = abs(total_sum - budget)
    print(f"{difference:.2f}$ more needed.")
