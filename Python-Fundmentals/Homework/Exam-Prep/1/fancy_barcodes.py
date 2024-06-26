import re

number_of_barcodes = int(input())

regex = r"(@#+)([A-Z][a-zA-Z0-9]{4,}[A-Z])(@#+)"
for entry in range(number_of_barcodes):
    current_barcode = input()
    matches = re.search(regex, current_barcode)

    if not matches:
        print("Invalid barcode")
    else:
        digit_pattern = r"\d"
        extract_numbers = re.findall(digit_pattern, matches.group())
        if not extract_numbers:
            print(f"Product group: 00")
        else:
            print(f"Product group: {''.join(extract_numbers)}")
