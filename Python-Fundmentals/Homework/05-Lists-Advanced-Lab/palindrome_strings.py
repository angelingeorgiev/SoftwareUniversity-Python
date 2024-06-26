user_input = input().split(" ")
palindrome = input()

palindromes_in_sequence = []

for word in user_input:
    if word == word[::-1]:
        palindromes_in_sequence.append(word)

palindrome_count = palindromes_in_sequence.count(palindrome)

print(palindromes_in_sequence)
print(f"Found palindrome {palindrome_count} times")
