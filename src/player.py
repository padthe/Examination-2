from deck import Deck
from hand import Hand

class Player:
    def __init__(self):
        self.hand = Hand()

    def draw_card(self, deck):
        card = deck.deal_card()
        self.hand.add_card(card)