import random

class Deck:
    def __init__(self):
        self._deck = []
        self.create_deck()

    def create_deck(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
        for suit in suits:
            for rank in ranks:
                self._deck.append(rank + ' of ' + suit)

    def shuffle_deck(self):
        random.shuffle(self._deck)

    def deal_card(self):
        if len(self._deck) > 0:
            return self._deck.pop()
        else:
            return None

    # Getter for deck
    def get_deck(self):
        return self._deck

    # Setter for deck
    def set_deck(self, new_deck):
        self._deck = new_deck