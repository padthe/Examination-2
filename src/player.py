"""Player class for the game of Blackjack."""
from deck import Deck
from hand import Hand

class Player:
    def __init__(self):
        self._hand = Hand()
        self._user_name = ""  

    def add_player(self, user_name):
        self._user_name = user_name

    def change_user_name(self):
        new_name = input("Enter your new name: ")
        self._user_name = new_name

    def draw_card(self, deck):
        card = deck.deal_card()
        self._hand.add_card(card)

    # Getter for hand
    def get_hand(self):
        return self._hand

    # Setter for hand
    def set_hand(self, new_hand):
        self._hand = new_hand

    # Getter for user_name
    def get_user_name(self):
        return self._user_name

    # Setter for user_name
    def set_user_name(self, new_name):
        self._user_name = new_name
