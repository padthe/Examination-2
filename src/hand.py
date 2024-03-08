"""Hand class to represent a player's hand in a game of blackjack."""
class Hand:
    def __init__(self):
        self._cards = []  # starts with an empty list
        self._value = 0   # starts with zero value

    def add_card(self, card):
        self._cards.append(card)
        card_value = self.get_card_value(card)
        self._value += card_value

    def get_card_value(self, card):
        rank = card.split()[0]  # split the card string to get the rank
        if rank in ['Jack', 'Queen', 'King']:
            return 10
        elif rank == 'Ace':
            return 1
        else:
            return int(rank)  # convert numeric ranks to integers

    # Getter for cards
    def get_cards(self):
        return self._cards

    # Setter for cards
    def set_cards(self, new_cards):
        self._cards = new_cards

    # Getter for value
    def get_value(self):
        return self._value

    # Setter for value
    def set_value(self, new_value):
        self._value = new_value

    def reset_hand(self):
        """Reset the hand by clearing cards and resetting the value."""
        self._cards = []
        self._value = 0

    def calculate_value(self):
        return self._value