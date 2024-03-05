from deck import Deck
from player import Player
from scoreboard import Scoreboard  #  in a file named 'scoreboard.py'
import time

def main():
    scoreboard = Scoreboard()

    print("Welcome to BlackJack!")
    print("Enter your username:")
    player = Player()

    while True:  # Outer loop to allow for multiple rounds
        start = False  # Reset the start variable for a new round

        print(f"Hello, {player.username}!")
        print("To start, type 'start' and press enter:")
        user_input = input()

        if user_input == "start":
            start = True
        else:
            print("Invalid input. Please try again.")

        if not start:
            continue  # Go back to the beginning of the outer loop if not started

        while True:  # Inner loop for the current round
            print("The round is about to start....")
            print("Shuffling the deck...")
            deck = Deck()
            deck.shuffle_deck()
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

            # ... (your existing game logic)

            print("Do you want to play another round? (yes/no)")
            play_again = input()
            if play_again.lower() != "yes":
                print(f"{player.username}'s score: {scoreboard.get_score(player.username)}")
                break  # Exit the inner loop and start a new game

        print("Do you want to change your username? (yes/no)")
        change_username = input()
        if change_username.lower() == "yes":
            player.change_username()

        print("Do you want to see the scoreboard? (yes/no)")
        show_scoreboard = input()
        if show_scoreboard.lower() == "yes":
            print("Scoreboard:")
            for username, score in scoreboard.scores.items():
                print(f"{username}: {score}")

        print("Do you want to play again? (yes/no)")
        play_again = input()
        if play_again.lower() != "yes":
            break  # Exit the outer loop and end the game

if __name__ == "__main__":
    main()
