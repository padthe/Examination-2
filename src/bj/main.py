from game import Game
from scoreboard import Scoreboard
from player import Player
from game import GameEndException


def main_menu():
    print(f"{'🃏🃏🃏Welcome to BlackJack!🃏🃏🃏':^40}")

    player = Player()
    player.add_player(player._user_name)
    scoreboard = Scoreboard("scores.pkl")

    while True:
        try:
            print("1. Play")
            print("2. Check Scoreboard")
            print("3. See Rules")
            print("4. Settings")
            print("5. Credits")
            print("6. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                game = Game(player, scoreboard)
                game.start_game()
            elif choice == "2":
                scoreboard.display_scores()
            elif choice == "3":
                Game.game_rules()
            elif choice == "4":
                old_name = player.get_user_name()  # Get the current username
                player.change_user_name()
                new_name = player.get_user_name()  # Get the updated username
                scoreboard.update_user_name(old_name, new_name)
                scoreboard.save_scores()
                print(f"Username updated successfully!\nYour new username is {new_name}.")
            elif choice == "5":
                Game.game_credits()
            elif choice == "6":
                print("Exiting the game. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
        except GameEndException:
            print("Returning to the main menu.")


if __name__ == "__main__":
    main_menu()
