import random

class Card:
    # Class that represent which rank and suit a card has.
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def card_rank(self):
        if self.rank in ["Jacks, Queens, Kings"]:
            return 10
        elif self.rank == 'Ace':
            return 11
        else:
            return int(self.rank)
    
    def card_value(self, rank):
        return self.rank


class Deck:
    # Class that represent a deck of cards.
    def __init__(self):
        self.cards = [Card(Suit, rank) for Suit in ['Hearts', 'Diamonds', 'Clubs', 'Spades']
                      for rank in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jacks', 'Queens', 'Kings', 'Ace']]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()


class Hand:
    # Class that represent a hand of cards.
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def get_value(self):
        return sum([card.card_rank() for card in self.cards])

    def busted(self):
        return self.get_value() > 21


class Player:

    def __init__(self):
        self.hand = Hand()

    def hit(self, deck):
        self.hand.add_card(deck.deal())

    def stand(self):
        print("Dealer's turn")


class black_jack_game:

    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.player = Player()
        self.dealer = Player()

if __name__ == '__main__':
    while True:
        print("Welcome to Black Jack!")
        print("The game is about to start!")
        print("For help or rules, type 'help' or 'rules' and press enter. To start the game, type 'start'")
        user_input = input().lower()
        
        if user_input == 'help' or user_input == 'rules':
            print("Here are the rules of Black Jack:")
            print("The goal of the game is to get as close to 21 as possible without going over.")
            print("The game is played with a standard deck of 52 cards.")
            print("The value of the cards are as follows: 2-10 are worth their face value, Jacks, Queens and Kings are worth 10, and Aces are worth 11 or 1.")
            print("The game starts with the dealer dealing two cards to the player and two cards to himself.")
            print("The player can choose to 'hit' or 'stand'.")
            print("If the player 'hits', the dealer will deal another card to the player.")
            print("If the player 'stands', the dealer will deal cards to himself until he reaches 17 or busts.")
            print("If the player's hand is closer to 21 than the dealer's hand, the player wins.")
            print("If the player's hand is over 21, the player busts and loses.")
            print("Good luck and have fun!")
            
        elif user_input == 'start':
            break
        else:
            print("Invalid input. Please try again.")

game = black_jack_game()
print("Player's turn")
game.player.hit(game.deck)
game.player.hit(game.deck)
print("The dealer gave you: ", game.player.hand.cards)
print("The value of your hand is: ", game.player.hand.get_value())
print("The dealer's turn")
print("The dealer gave himself: ", game.dealer.hand.cards)
print("The value of the dealer's hand is: ", game.dealer.hand.get_value())
