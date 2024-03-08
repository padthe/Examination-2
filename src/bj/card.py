"""Card class for the blackjack game."""


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = self.assign_value(rank)

    def assign_value(self, rank):
        if rank in ["Jack", "Queen", "King"]:
            return 10
        elif rank == "Ace":
            return 1
        else:
            return int(rank)

    def __str__(self):
        return self.rank + " of " + self.suit
