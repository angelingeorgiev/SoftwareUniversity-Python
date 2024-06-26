def is_password_valid(password: str) -> list:
    list_of_errors = []

    if len(password) < 6 or len(password) > 10:
        list_of_errors.append("Password must be between 6 and 10 characters")
    if not password.isalnum():
        list_of_errors.append("Password must consist only of letters and digits")

    digit_count = 0
    for char in password:
        if char.isdigit():
            digit_count += 1
    if digit_count < 2:
        list_of_errors.append("Password must have at least 2 digits")
    return list_of_errors


password_input = input()
validated_password = (is_password_valid(password_input))

if len(validated_password) == 0:
    print("Password is valid")
else:
    print("\n".join(validated_password))
