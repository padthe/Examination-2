import pickle


class Scoreboard:
    def __init__(self, filename="scores.pkl"):
        """Initialize the scoreboard."""
        self._filename = filename
        self._scores = self.load_scores()
        self._user_name = ""

    def add_player(self, player_name):
        """Add a player to the scoreboard."""
        if player_name not in self._scores:
            self._scores[player_name] = 0

    def update_score(self, player_name, result):
        """Update the score of a player."""
        self.add_player(player_name)
        if result == "win":
            self._scores[player_name] += 1
        elif result == "draw":
            self._scores[player_name] += 0.5

    def display_scores(self):
        """Display the current scores."""
        if not self._scores:
            print("No players in the scoreboard.")
        else:
            sorted_scores = sorted(
                self._scores.items(), key=lambda x: x[1], reverse=True
            )

            print("🌟 Let's see who is currently at the top! 🌟")
            print("------------------------------")
            print("Player      |  Score")
            print("------------------------------")
            for player, score in sorted_scores:
                print(f"{player.ljust(12)} | {score}")
            print("------------------------------")

    def change_username(self, old_name, new_name):
        """Change the player's username."""
        try:
            # Check if the player's old name is in the scoreboard
            old_name_score = self._scores.get(old_name)
            if old_name_score is not None:
                # Remove the old name and add the new name with the same score
                self._scores[new_name] = self._scores.pop(old_name, 0)
                self.save_scores()
            else:
                print("Player not found in the scoreboard.")

            # Update the player's username
            print(f"Username updated successfully! Your new username is {new_name}.")

        except AttributeError:
            print("Scoreboard does not have the required methods.")

    def load_scores(self):
        """Load the scores from the file."""
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
        """Save the scores to the file."""
        with open(self._filename, "wb") as file:
            pickle.dump(self._scores, file)

    def get_scores(self):
        """Get the scores."""
        return self._scores

    def set_scores(self, new_scores):
        """Set the scores."""
        self._scores = new_scores

    def get_user_name(self):
        """Get the user name."""
        return self._user_name

    def set_user_name(self, new_name):
        """Set the user name."""
        self._user_name = new_name
