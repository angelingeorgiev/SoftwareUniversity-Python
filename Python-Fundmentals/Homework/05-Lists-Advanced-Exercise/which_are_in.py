sentence_one = input().split(", ")
sentence_two = input().split(", ")

new_list = []

for i in sentence_one:
    for j in sentence_two:
        if i in j:
            new_list.append(i)
            break

print(new_list)