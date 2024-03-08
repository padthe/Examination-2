import pickle

class Scoreboard:
    def __init__(self, filename="scores.pkl"):
        self._filename = filename
        self._scores = self.load_scores()
        self._user_name = ""

    def add_player(self, player_name):
        if player_name not in self._scores:
            self._scores[player_name] = 0

    def update_score(self, player_name, result):
        self.add_player(player_name)
        if result == "win":
            self._scores[player_name] += 1
        elif result == "draw":
            self._scores[player_name] += 0.5

    def display_scores(self):
        if not self._scores:
            print("No players in the scoreboard.")
        else:
            sorted_scores = sorted(self._scores.items(), key=lambda x: x[1], reverse=True)

            print("🌟 Let's see who is currently at the top! 🌟")
            print("------------------------------")
            print("Player      |  Score")
            print("------------------------------")
            for player, score in sorted_scores:
                print(f"{player.ljust(12)} | {score}")
            print("------------------------------")

    def update_user_name(self, old_name, new_name):
        if old_name in self._scores:
            self._scores[new_name] = self._scores.pop(old_name)
        else:
            print(f"Player {old_name} not found in the scoreboard.")

    def load_scores(self):
        try:
            with open(self._filename, "rb") as file:
                return pickle.load(file)
        except FileNotFoundError:
            print(f"No file found. Creating a new scoreboard.")
            return {}
        except Exception as e:
            print(f"An error occurred while loading scores: {e}")
            return {}

    def save_scores(self):
        with open(self._filename, "wb") as file:
            pickle.dump(self._scores, file)

    # Getter for scores
    def get_scores(self):
        return self._scores

    # Setter for scores
    def set_scores(self, new_scores):
        self._scores = new_scores

    # Getter for user_name
    def get_user_name(self):
        return self._user_name

    # Setter for user_name
    def set_user_name(self, new_name):
        self._user_name = new_name