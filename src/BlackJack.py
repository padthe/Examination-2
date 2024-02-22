import random

class Deck:
    def __init__(self):
        self.deck = []
        self.create_deck()

    def create_deck(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
        for suit in suits:
            for rank in ranks:
                self.deck.append(rank + ' of ' + suit)

    def shuffle_deck(self):
        random.shuffle(self.deck)

    def deal_card(self):
        if len(self.deck) > 0:
            return self.deck.pop()
        else:
            return None
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

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = self.assign_value(rank)

    def assign_value(self, rank):
        if rank in ['Jack', 'Queen', 'King']:
            return 10
        elif rank == 'Ace':
            return 1
        else:
            return int(rank)

    def __str__(self):
        return self.rank + ' of ' + self.suit
    
class Player:
    def __init__(self):
        self.hand = Hand()

    def draw_card(self, deck):
        card = deck.deal_card()
        self.hand.add_card(card)
        


print("Welcome to BlackJack!")
print("The game is about to start...")
print("Shuffling the deck...")
deck = Deck()
deck.shuffle_deck()
player = Player()
dealer = Player()
print("Dealing the cards...")
player.draw_card(deck)
dealer.draw_card(deck)
player.draw_card(deck)
dealer.draw_card(deck)
print("Player's hand: ", player.hand.cards)
print("Dealer's hand: ", dealer.hand.cards)