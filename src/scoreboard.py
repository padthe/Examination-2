import json

class Scoreboard:
    def __init__(self, file_path="scores.json"):
        self.scores = {}
        self.file_path = file_path
        self.load_scores()

    def load_scores(self):
        try:
            with open(self.file_path, "r") as file:
                self.scores = json.load(file)
        except FileNotFoundError:
            pass  # If the file doesn't exist, start with an empty scoreboard

    def save_scores(self):
        with open(self.file_path, "w") as file:
            json.dump(self.scores, file)

    def update_score(self, player_name, result):
        if player_name not in self.scores:
            self.scores[player_name] = 0

        if result == "win":
            self.scores[player_name] += 1
        elif result == "lose":
            self.scores[player_name] -= 1

        self.save_scores()

    def get_score(self, player_name):
        return self.scores.get(player_name, 0)