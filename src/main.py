"""This is the main file for the BlackJack game."""
from deck import Deck
from player import Player
import time

while True:  # Outer loop to allow for multiple rounds
    start = False  # Reset the start variable for a new round
    print("Welcome to BlackJack!")
    print("To start the type 'start' and press enter: ")
    user_input = input()
    if user_input == "start":
        start = True
    else:
        print("Invalid input. Please try again.")
    if not start:
        continue  # Go back to the beginning of the outer loop if not started
    print("The game is about to start....")
    print("Shuffling the deck...")
    deck = Deck()
    deck.shuffle_deck()
    player = Player()
    dealer = Player()
    print("Dealing the cards")
    time.sleep(0.5)
    print("Dealing the cards.")
    time.sleep(0.5)
    print("Dealing the cards..")
    time.sleep(0.5)
    print("Dealing the cards...")
    time.sleep(0.5)
    print("Dealing the cards....")
    player.draw_card(deck)
    dealer.draw_card(deck)
    print("Player's hand: ", player.hand.cards)
    print("Dealer's hand: ", dealer.hand.cards)
    while True:  # Inner loop for the current round
        print("Do you want to hit or stand? (hit/stand)")
        user_input = input()
        if user_input == "hit":
            player.draw_card(deck)
            print("Player's hand: ", player.hand.cards)
            print("Dealer's hand: ", dealer.hand.cards)
            if player.hand.calculate_value() > 21:
                print("Player busts! Dealer wins.")
                break  # Exit the current round
        elif user_input == "stand":
            while dealer.hand.calculate_value() < 17:
                dealer.draw_card(deck)
            print("Player's hand: ", player.hand.cards)
            print("Dealer's hand: ", dealer.hand.cards)
            if dealer.hand.calculate_value() > 21:
                print("Dealer busts! Player wins.")
            elif dealer.hand.calculate_value() >= player.hand.calculate_value():
                print("Dealer wins.")
            else:
                print("Player wins.")
            break  # Exit the current round

    print("Do you want to play another round? (yes/no)")
    play_again = input()
    if play_again.lower() != "yes":
        break  # Exit the outer loop and end the game