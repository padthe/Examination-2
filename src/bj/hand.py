"""Hand class to represent a player's hand in a game of blackjack."""


class Hand:
    def __init__(self):
        self._cards = []  # starts with an empty list
        self._value = 0  # starts with zero value

    def add_card(self, card):
        """Add a card to the hand and update the value."""
        self._cards.append(card)
        card_value = self.get_card_value(card)
        self._value += card_value

    def get_card_value(self, card):
        """Get the value of a card."""
        rank = card.split()[0]  # split the card string to get the rank
        if rank in ["Jack", "Queen", "King"]:
            return 10
        elif rank == "Ace":
            return 1
        else:
            return int(rank)  # convert numeric ranks to integers

    def get_cards(self):
        """Get the cards in the hand."""
        return self._cards

    def set_cards(self, new_cards):
        """Set the cards in the hand."""
        self._cards = new_cards

    def get_value(self):
        """Get the value of the hand."""
        return self._value

    def set_value(self, new_value):
        """Set the value of the hand."""
        self._value = new_value

    def reset_hand(self):
        """Reset the hand by clearing cards and resetting the value."""
        self._cards = []
        self._value = 0

    def calculate_value(self):
        """Calculate the value of the hand."""
        return self._value
