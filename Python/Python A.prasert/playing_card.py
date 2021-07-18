import random
def playing_card():
    suit = ("\u2660","\u2665","\u2666","\u2663")
    rank = list("A23456789") + ["10"] + list("JQK")
    # print(rank)
    deck = []
    for s in suit:
        for r in rank:
            deck.append(r + s)
    return deck

d = playing_card()
print(d)
random.shuffle(d)
print(d)