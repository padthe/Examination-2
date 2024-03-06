from deck import Deck
from player import Player
from scoreboard import Scoreboard
import time
from gameendexception import GameEndException

class Game:
    def __init__(self, player, scoreboard):
        self.scoreboard = scoreboard
        self.deck = None
        self.player = player
        self.dealer = None

    def start_game(self):
        self.player.user_name = input("Enter your name: ")
        while True:
            print("To start, type 'hit me' and press enter: ")
            user_input = input()
            
            if user_input == "hit me":
                self.play_round()
            else:
                print("Invalid input. Please try again.")

    def play_round(self):
        print("The dealer is getting ready....")
        print("Shuffling the deck...")
        self.deck = Deck()
        self.deck.shuffle_deck()
        self.dealer = Player()  # Initialize dealer here

        print("Dealing the cards.")
        for _ in range(4):
            time.sleep(0.5)
            print("Dealing the cards....")
            if _ % 2 == 0:
                self.player.draw_card(self.deck)
            else:
                self.dealer.draw_card(self.deck)

        print("Player's hand: ", self.player.hand.cards)
        print("Dealer's hand: ", self.dealer.hand.cards)

        while True:
            print("Do you want to hit or stand? (hit/stand)")
            user_input = input()
            if user_input == "hit":
                self.player.draw_card(self.deck)
                print("Player's hand: ", self.player.hand.cards)
                print("Dealer's hand: ", self.dealer.hand.cards)
                if self.player.hand.calculate_value() > 21:
                    print("Player busts! Dealer wins.")
                    self.save_results("lose")
                    break
            elif user_input == "stand":
                while self.dealer.hand.calculate_value() < 17:
                    self.dealer.draw_card(self.deck)
                print("Player's hand: ", self.player.hand.cards)
                print("Dealer's hand: ", self.dealer.hand.cards)
                if self.dealer.hand.calculate_value() > 21:
                    print("Dealer busts! Player wins.")
                    self.save_results("win")
                elif self.dealer.hand.calculate_value() == 21:
                    print("Dealer wins.")
                    self.save_results("lose")
                else:
                    print("Player wins.")
                    self.save_results("win")
                break
        print("Do you want to play another round? (yes/no)")
        play_again = input().lower()
        if play_again == "no":
            raise GameEndException
        
    def save_results(self, result):
        try:
            self.scoreboard.update_score(self.player.user_name, result)
            self.scoreboard.save_scores()
        except AttributeError:
                print("Scoreboard does not have the required methods.")
