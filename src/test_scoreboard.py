import unittest
import os
import pickle
from scoreboard import Scoreboard 

class TestScoreboard(unittest.TestCase):
    def setUp(self):
        """Create a new instance of Scoreboard before each test"""
        self.scoreboard = Scoreboard("test_scores.pkl")

    def tearDown(self):
        """Remove the test_scores.pkl file after each test"""
        if os.path.exists("test_scores.pkl"):
            os.remove("test_scores.pkl")

    def test_add_player(self):
        """Test if a new player is added to the scoreboard"""
        self.scoreboard.add_player("Player1")
        self.assertEqual(self.scoreboard.scores["Player1"], 0)

        self.scoreboard.add_player("Player2")
        self.assertEqual(self.scoreboard.scores["Player2"], 0)

    def test_update_score(self):
        """Test if the score is updated correctly"""
        self.scoreboard.update_score("Player1", "win")
        self.assertEqual(self.scoreboard.scores["Player1"], 1)

        self.scoreboard.update_score("Player2", "draw")
        self.assertEqual(self.scoreboard.scores["Player2"], 0.5)

    def test_display_scores(self):
        """Test if the scores are displayed correctly"""
        import sys
        from io import StringIO
        saved_stdout = sys.stdout
        sys.stdout = StringIO()

        # Display scores and check the printed output
        self.scoreboard.display_scores()
        output = sys.stdout.getvalue().strip()
        self.assertEqual(output, "No players in the scoreboard.")

        # Add a player and display scores again
        self.scoreboard.add_player("Player1")
        sys.stdout = StringIO()
        self.scoreboard.display_scores()
        output = sys.stdout.getvalue().strip()
        self.assertIn("Player1", output)
        self.assertIn("0", output)

        # Restore stdout
        sys.stdout = saved_stdout

    def test_update_user_name(self):
        """Test if the user name is updated correctly"""
        self.scoreboard.add_player("OldName")
        self.scoreboard.update_user_name("OldName", "NewName")
        self.assertNotIn("OldName", self.scoreboard.scores)
        self.assertIn("NewName", self.scoreboard.scores)

    def test_load_scores(self):
        """Test if the scores are loaded from a file correctly"""
        # Create a test file with scores
        with open("test_scores.pkl", "wb") as file:
            pickle.dump({"Player1": 2, "Player2": 1}, file)

        # Create a new instance of Scoreboard and load scores
        new_scoreboard = Scoreboard("test_scores.pkl")
        self.assertEqual(new_scoreboard.scores, {"Player1": 2, "Player2": 1})

    def test_save_scores(self):
        """"Test if the scores are saved to a file correctly"""
        self.scoreboard.add_player("Player1")
        self.scoreboard.update_score("Player1", "win")
        self.scoreboard.save_scores()

        # Create a new instance of Scoreboard and check if the score is saved
        new_scoreboard = Scoreboard("test_scores.pkl")
        self.assertEqual(new_scoreboard.scores, {"Player1": 1})

if __name__ == '__main__':
    unittest.main()
