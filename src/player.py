"""Player class for the game of Blackjack."""
from deck import Deck
from hand import Hand

class Player:
    def __init__(self):
        self.hand = Hand()
        self.user_name = ""  # Initialize user_name as an empty string

    def add_player(self, user_name):
        self.user_name = user_name

    def change_user_name(self):
        new_name = input("Enter your new name: ")
        self.user_name = new_name

    def draw_card(self, deck):
        card = deck.deal_card()
        self.hand.add_card(card)
