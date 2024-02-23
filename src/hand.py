"""Hand class to represent a player's hand in a game of blackjack."""
class Hand:
    def __init__(self):
        self.cards = []  # starts with an empty list
        self.value = 0   # starts with zero value

    def add_card(self, card):
        self.cards.append(card)
        card_value = self.get_card_value(card)
        self.value += card_value

    def get_card_value(self, card):
        rank = card.split()[0]  # split the card string to get the rank
        if rank in ['Jack', 'Queen', 'King']:
            return 10
        elif rank == 'Ace':
            return 1
        else:
            return int(rank)  # convert numeric ranks to integers

    def calculate_value(self):
        return self.value