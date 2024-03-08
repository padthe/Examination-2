"""Player class for the game of Blackjack."""
from deck import Deck
from hand import Hand

class Player:
    def __init__(self):
        """Initialize the player."""
        self._hand = Hand()
        self._user_name = ""  

    def add_player(self, user_name):
        """Add a player to the game."""
        self._user_name = user_name

    def change_user_name(self):
        """Change the name of the player."""
        new_name = input("Enter your new name: ")
        self._user_name = new_name

    def draw_card(self, deck):
        """Draw a card from the deck and add it to the hand."""
        card = deck.deal_card()
        self._hand.add_card(card)

    def get_hand(self):
        """Get the hand of the player."""
        return self._hand

    def set_hand(self, new_hand):
        """Set the hand of the player."""
        self._hand = new_hand

    def get_user_name(self):
        """Get the name of the player."""
        return self._user_name

    def set_user_name(self, new_name):
        """Set the name of the player."""
        self._user_name = new_name
