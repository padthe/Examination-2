import pickle

class Scoreboard:
    def __init__(self, filename="scores.pkl"):
        self.filename = filename
        self.scores = self.load_scores()


    def add_player(self, player_name):
        if player_name not in self.scores:
            self.scores[player_name] = 0

    def update_score(self, player_name, result):
        self.add_player(player_name)  # Ensure the player is in the scoreboard
        if result == "win":
            self.scores[player_name] += 1
        elif result == "draw":
            self.scores[player_name] += 0.5  # Adjust based on your rules for a draw

    def display_scores(self):
        if not self.scores:
            print("No players in the scoreboard.")
        else:
            print("🌟 Let's see who is currently at the top! 🌟")
            print("------------------------------")
            print("Player      |  Score")
            print("------------------------------")
            for player, score in self.scores.items():
                print(f"{player.ljust(12)} | {score}")
            print("------------------------------")


    def load_scores(self):
        try:
            with open(self.filename, "rb") as file:
                return pickle.load(file)
        except FileNotFoundError:
            print(f"No file found. Creating a new scoreboard.")
            return {}
        except Exception as e:
            print(f"An error occurred while loading scores: {e}")
            return {}

    def save_scores(self):
        with open(self.filename, "wb") as file:
            pickle.dump(self.scores, file)