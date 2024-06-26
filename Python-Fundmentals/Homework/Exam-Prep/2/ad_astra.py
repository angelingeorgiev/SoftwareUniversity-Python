import re

user_input = input()
regex = r"(?i)([#|])([a-z\s]+)(\1)(\d{2}\/\d{2}\/\d{2})(\1)(\d+)(\1)"
# needed indexes 1, 3, 5 (item, exp date, calories)

matches = re.findall(regex, user_input)
total_calories = sum([int(match[5]) for match in matches])
days = total_calories // 2000
print(f"You have food to last you for: {days} days!")

for element in matches:
    item_name = element[1]
    expiration_date = element[3]
    calories = element[5]
    print(f"Item: {item_name}, Best before: {expiration_date}, Nutrition: {calories}")
