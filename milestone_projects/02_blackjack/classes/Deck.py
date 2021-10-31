from classes.Card import Card
from random import shuffle

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

class Deck:
    def __init__(self):
        cards = [Card(suit, rank) for suit in suits for rank in ranks]
        shuffle(cards)
        self.cards = cards

    def __len__(self):
        return len(self.cards)

    def deal_one(self):
        return self.cards.pop(0)