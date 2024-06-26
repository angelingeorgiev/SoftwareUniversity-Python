def number_sums(*args):
    sum_negative = sum(number for number in args if number < 0)
    sum_positive = sum(number for number in args if number >= 0)

    return sum_negative, sum_positive


numbers = [int(x) for x in input().split()]
negative_sum, positive_sum = number_sums(*numbers)

print(negative_sum)
print(positive_sum)
if abs(negative_sum) > positive_sum:
    print("The negatives are stronger than the positive")
else:
    print("The positives are stronger than the negatives")

