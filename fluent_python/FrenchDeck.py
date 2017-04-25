import collections
Card = collections.namedtuple("Card",['rank','suit'])


# implement __getitem__ and __len__ to make class as sequence object
class FrenchDeck:
    ranks = [str(x) for x in range(2, 11)] + list('AJQK')
    suits = 'spades diamonds clubs hearts'.split(' ')
    cards = []

    def __init__(self):
        self.cards = [Card(x, y) for x in self.ranks for y in self.suits]

    def __getitem__(self, item):  # make object iterable like for loop, [] operated etc.
        return self.cards[item]

    def __len__(self):
        return len(self.cards)


deck = FrenchDeck()
for card in reversed(deck):  # deck is sequence object, so we can use reverse method
    print(card)

print(Card('7', 'hearts') in deck)
