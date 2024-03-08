import random


class Deck:
    def __init__(self):
        """Initialize the deck."""
        self._deck = []
        self.create_deck()

    def create_deck(self):
        """Create a deck of cards."""
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        ranks = [
            "Ace",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "10",
            "Jack",
            "Queen",
            "King",
        ]
        for suit in suits:
            for rank in ranks:
                self._deck.append(rank + " of " + suit)

    def shuffle_deck(self):
        """Shuffle the deck of cards."""
        random.shuffle(self._deck)

    def deal_card(self):
        """Deal a card from the deck."""
        if len(self._deck) > 0:
            return self._deck.pop()
        else:
            return None

    def get_deck(self):
        """Get the deck of cards."""
        return self._deck

    def set_deck(self, new_deck):
        """Set the deck of cards."""
        self._deck = new_deck
