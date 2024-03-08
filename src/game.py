import time
from deck import Deck
from player import Player
from scoreboard import Scoreboard
from gameendexception import GameEndException

class Game:
    def __init__(self, player, scoreboard):
        self.scoreboard = scoreboard
        self.deck = None
        self.player = player
        self.dealer = None

    def start_game(self):
        """Start the game."""
        self.player.user_name = input("Enter your name: ")
        while True:
            print("To start, type 'hit me' and press enter: ")
            user_input = input()
            if "hit" in user_input:
                self.play_round()
            else:
                print("Invalid input. Please try again.")

    def play_round(self):
        """Play a round of the game."""
        print("The dealer is getting ready....")
        print("Shuffling the deck...")
        self.deck = Deck()
        self.deck.shuffle_deck()
        self.dealer = Player()  # Initialize dealer here

        self.player.hand.reset_hand()
        self.dealer.hand.reset_hand()

        print("Dealing the cards.")
        for _ in range(2):
            time.sleep(0.5)
            print("Dealing the cards....")
            self.player.draw_card(self.deck)
            self.dealer.draw_card(self.deck)

        print("Player's hand: ", self.player.hand.cards)
        print("Dealer's hand: ", self.dealer.hand.cards)

        while True:
            print("Do you want to hit or stand? (hit/stand)")
            user_input = input().lower().strip()
            if "hit" in user_input:
                self.player.draw_card(self.deck)
                print("Player's hand: ", self.player.hand.cards)
                print("Dealer's hand: ", self.dealer.hand.cards)
                if self.player.hand.calculate_value() > 21:
                    print("Player busts! Dealer wins.")
                    self.save_results("lose")
                    break
            elif "stand" in user_input:
                while self.dealer.hand.calculate_value() < 17:
                    self.dealer.draw_card(self.deck)
                print("Player's hand: ", self.player.hand.cards)
                print("Dealer's hand: ", self.dealer.hand.cards)
    
                player_value = self.player.hand.calculate_value()
                dealer_value = self.dealer.hand.calculate_value()

                if dealer_value > 21 or player_value > dealer_value:
                    print("Player wins.")
                    self.save_results("win")
                elif dealer_value > player_value:
                    print("Dealer wins.")
                    self.save_results("lose")
                else:
                    print("It's a draw.")
                    self.save_results("draw")
                break

        print("Press any button to play a new round, or type 'no' to return to main menu.")
        play_again = input().lower().strip()
        if play_again == "no":
            raise GameEndException
        else:
            input("Press enter to continue.")

    def save_results(self, result):
        """Save the results of the game."""
        try:
            self.scoreboard.update_score(self.player.user_name, result)
            self.scoreboard.save_scores()
        except AttributeError:
            print("Scoreboard does not have the required methods.")

    @staticmethod
    def game_rules():
        """Print the game rules."""
        print("\n🃏🎰 Welcome to the Glamorous World of Blackjack! 🎰🃏\n")
        print("In this high-stakes game of chance, your mission is to chase the magic number 21 without going over.")
        print("Here's the dazzling rundown:")
        print("- Both you and the dealer kick off with a duo of tantalizing cards.")
        print("- Will you 'hit' for another card or 'stand' to savor the suspense?")
        print("- Exceed 21, and you'll be washed away in a wave of defeat. Dealer's bust? You're the star!")
        print("- Nail a perfect 21, and you're crowned with the Blackjack glory. Dealer hits it? They steal the show.")
        print("- Opt for 'stand,' and the dealer dances with the cards until reaching the swanky 17.")
        print("- The player closest to 21 without a bust claims the red carpet victory.")
        print("\nMay the cards be ever in your favor! 🌟\n")
        print("Feel the thrill? Ready to roll again or gracefully exit the stage? The choice is yours.")
        print(" ")
        print(" ")

    @staticmethod
    def game_credits():
        """Print the game credits."""
        credits = [
            "🎮🃏 Game Credits - A One-Man Extravaganza! 🃏🎮",
            "🚀 Taking you on a journey through code and chaos, it's none other than:",
            "🤠🎸 The Lone Ranger of Programming - Patrick! 🎸🤠",
            "Witness the breathtaking solo performance, where Patrick played all the roles:",
            "- Developer: Patrick (a true virtuoso)",
            "- UI Maestro: Patrick (creating symphonies with pixels)",
            "- Test Pilot: Patrick (bravely flying through lines of code)",
            "- Bug Whisperer: Patrick (taming bugs with a gentle touch)",
            "Special Thanks (drumroll):",
            "- Patrick (because who needs a team when you've got yourself?)",
            "🎉 Bravo! Encore! Bravo! 🎉",
            ]

        for line in credits:
            print(line)
            time.sleep(1)

        print("\nThat's a wrap! Thanks for playing and enjoy your solo standing ovation! 👏👏👏\n")