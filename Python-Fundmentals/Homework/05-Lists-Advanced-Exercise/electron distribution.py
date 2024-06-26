number_of_electrons = int(input())

shells = []

# почваме ог 1 докато във всяка обвивка има поне 1 ел
for shell in range(1, number_of_electrons + 1):
    max_electron_in_shell = 2 * shell ** 2
    if number_of_electrons >= max_electron_in_shell:
        shells.append(max_electron_in_shell)
        number_of_electrons -= max_electron_in_shell

        if number_of_electrons == 0:
            break
    else:
        shells.append(number_of_electrons)
        break
print(shells)
