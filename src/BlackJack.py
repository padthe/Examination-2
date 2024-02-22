"""This is the main file for the BlackJack game."""
from deck import Deck
from player import Player

start = False
while start is False:
    print("Welcome to BlackJack!")
    print("To start the type 'start' and press enter: ")
    user_input = input()
    if user_input == "start":
        start = True
    else:
        print("Invalid input. Please try again.")

    print("The game is about to start....")
    print("Shuffling the deck...")
    deck = Deck()
    deck.shuffle_deck()
    player = Player()
    dealer = Player()
    print("Dealing the cards....")
    player.draw_card(deck)
    dealer.draw_card(deck)
    print("Player's hand: ", player.hand.cards)
    print("Dealer's hand: ", dealer.hand.cards)
    print("Do you want to hit or stand? (hit/stand)")
    user_input = input()
    if user_input == "hit":
        player.draw_card(deck)
        print("Player's hand: ", player.hand.cards)
        print("Dealer's hand: ", dealer.hand.cards)
        if player.hand.calculate_value() > 21:
            print("Player busts! Dealer wins.")
        elif user_input == "stand":
            break
    while dealer.hand.calculate_value() < 17:
        dealer.draw_card(deck)
        if dealer.hand.calculate_value() > 21:
            print("Dealers hand: ", dealer.hand.cards)
            print("Dealer busts! Player wins.")
