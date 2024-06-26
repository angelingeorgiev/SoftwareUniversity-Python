def is_palindrome(some_number: str) -> bool:
    if some_number == some_number[::-1]:
        return True
    else:
        return False


positive_integers = input().split(", ")
for num in positive_integers:
    print(is_palindrome(num))
