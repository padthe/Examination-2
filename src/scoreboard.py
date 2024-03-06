import pickle

class Scoreboard:
    def __init__(self):
        self.scores = {}

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
            print("Scoreboard:")
            for player, score in self.scores.items():
                print(f"{player}: {score}")

    def save_scores(self, filename="scores.pkl"):
        with open(filename, "wb") as file:
            pickle.dump(self.scores, file)

    def load_scores(self, filename="scores.pkl"):
        try:
            with open(filename, "rb") as file:
                self.scores = pickle.load(file)
        except FileNotFoundError:
            print(f"No file found. Creating a new scoreboard.")
        except Exception as e:
            print(f"An error occurred while loading scores: {e}")
