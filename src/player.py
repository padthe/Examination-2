"""Player class for the game of Blackjack."""
from deck import Deck
from hand import Hand


class Player:
    def __init__(self):
        self.hand = Hand()

    def add_player(self, user_name):
        self.user_name = user_name
        
    def user_name(self):
        user_name = input()
        return user_name
    
    def change_user_name(self):
        user_name = input()
        return user_name

    def draw_card(self, deck):
        card = deck.deal_card()
        self.hand.add_card(card)

