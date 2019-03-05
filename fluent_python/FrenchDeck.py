import collections
import itertools

Card = collections.namedtuple("Card",['rank','suit'])


# implement __getitem__ and __len__ to make class as sequence object
class FrenchDeck:
    ranks = [str(x) for x in range(2, 11)] + list('JQKA')
    suits = '方片 黑桃 梅花 红桃'.split(' ')

    def __init__(self):
#        self.cards = [Card(x, y) for x in self.ranks for y in self.suits]
        self.cards = [Card(x,y) for x,y in itertools.product(self.ranks, self.suits)]

    def __getitem__(self, item):  # make object iterable like for loop, [] operated etc.
        return self.cards[item]

    def __len__(self):
        return len(self.cards)
    suits_priority = {'黑桃':4,'红桃':3,'梅花':2, '方片':1}

    def rank_high(self, card):
        return self.ranks.index(card.rank) + 100 * self.suits_priority[card.suit]

deck = FrenchDeck()

for card in sorted(deck, key=deck.rank_high, reverse=True):
    print(card)