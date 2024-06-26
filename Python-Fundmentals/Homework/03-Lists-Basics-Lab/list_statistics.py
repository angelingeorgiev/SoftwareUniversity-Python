number = int(input())

positive = []
negative = []
count_positive = 0

for i in range(number):
    current_number = int(input())
    if current_number < 0:
        negative.append(current_number)
    else:
        positive.append(current_number)
        count_positive += 1

print(positive)
print(negative)
print(f"Count of positives: {count_positive}")
print(f"Sum of negatives: {sum(negative)}")
