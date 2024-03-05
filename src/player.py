"""Player class for the game of Blackjack."""
from deck import Deck
from hand import Hand

class Player:
    def __init__(self):
        self.hand = Hand()
        self.username = self.set_username()

    def set_username(self):
        print("Enter your username:")
        return input()

    def change_username(self):
        print("Enter your new username:")
        self.username = input()

    def draw_card(self, deck):
        card = deck.deal_card()
        self.hand.add_card(card)