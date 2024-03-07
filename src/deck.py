    """Deck class for the card game."""
    import random
    from random import shuffle

    class Deck:
        """Deck class for the card game."""
        def __init__(self):
            self.deck = []
            self.create_deck()
        """Create a deck of cards."""
        def create_deck(self):
            suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
            ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
            for suit in suits:
                for rank in ranks:
                    self.deck.append(rank + ' of ' + suit)
        """Shuffle the deck of cards."""
        def shuffle_deck(self):
            random.shuffle(self.deck)
        """Deal a card from the deck."""
        def deal_card(self):
            if len(self.deck) > 0:
                return self.deck.pop()
            else:
                return None