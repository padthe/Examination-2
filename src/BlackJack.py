import random
from deck import Deck
from player import Player
from hand import Hand



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