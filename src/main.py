from game import Game
from scoreboard import Scoreboard
from player import Player
from game import GameEndException


def main_menu():
    print("Welcome to BlackJack!")

    player = Player()
    player.add_player(player.user_name)
    scoreboard = Scoreboard("scores.pkl")

    while True:
        try:
            print("1. Play")
            print("2. Check Scoreboard")
            print("3. See Rules")
            print("4. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                game = Game(player, scoreboard)
                game.start_game()
            elif choice == "2":
                scoreboard.display_scores()
            elif choice == "3":
                print("Rules")
            elif choice == "4":
                print("Exiting the game. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
        except GameEndException:
            print("Returning to the main menu.")

if __name__ == "__main__":
    main_menu()