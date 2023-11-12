n = int(input())
cards = list(map(int, input().split()))
cards.sort(reverse=True)
level = cards[0]
gold = 0

for card in cards[1:]:
    gold += level+card
    if level>=card:
        pass
    else:
        level=card
print(gold)
