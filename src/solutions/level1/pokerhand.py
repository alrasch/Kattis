from collections import Counter
hand = input().split()

ranks = [card[0] for card in hand]
counts = Counter(rank for rank in ranks)
print(counts.most_common(1)[0][1])
