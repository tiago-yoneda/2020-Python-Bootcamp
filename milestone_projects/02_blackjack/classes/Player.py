class Player:
    def __init__(self, name):
        self.name = name
        self.cards_on_hand = []
        self.points = 0
        self.ace_counter = 0
        self.wallet = 100

    def add_card(self, card):
        self.cards_on_hand.append(card)
        if card.rank == "Ace":
            self.ace_counter += 1
        self.points += card.value
        self.check_status()

    def check_status(self):
        if self.points > 21:
            if self.ace_counter > 0:
                self.points -= 10
                self.ace_counter -= 1

    def has_ace(self):
        for card in self.cards_on_hand:
            if card.rank == "Ace":

                return True
        return False

    def pay(self, amount):
        self.wallet -= amount

    def receive(self, amount):
        self.wallet += amount

    def clear_hand(self):
        self.cards_on_hand = []
        self.points = 0

    def __len__(self):
        return len(self.cards_on_hand)

    def __str__(self):
        return f'{self.name} - {len(self)} cartas - {self.points} pontos'
