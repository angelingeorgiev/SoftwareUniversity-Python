cards = input().split(" ")
faro_shuffles_count = int(input())

for shuffles in range(faro_shuffles_count):
    current_deck = []

    half_deck = len(cards) // 2
    left_deck = cards[0: half_deck]
    right_deck = cards[half_deck: ]

    for i in range(0, len(left_deck)):
        current_deck.append(left_deck[i])
        current_deck.append(right_deck[i])

    cards = current_deck
print(cards)
