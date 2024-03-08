"""Unit tests for the Scoreboard class."""
import os
from unittest.mock import patch
from unittest import TestCase, mock
from scoreboard import Scoreboard


class TestScoreboard(TestCase):
    """Test the Scoreboard class."""

    def setUp(self):
        """Create a Scoreboard instance for testing."""
        self.scoreboard = Scoreboard(filename="test_scores.pkl")

    def test_add_player(self):
        """Test the add_player method."""
        player_name = "Alice"
        self.scoreboard.add_player(player_name)
        self.assertEqual(self.scoreboard.get_scores()[player_name], 0)

    def test_update_score_win(self):
        """Test the update_score method with a win."""
        player_name = "Alice"
        self.scoreboard.update_score(player_name, "win")
        self.assertEqual(self.scoreboard.get_scores()[player_name], 1)

    def test_update_score_draw(self):
        """Test the update_score method with a draw."""
        player_name = "Alice"
        self.scoreboard.update_score(player_name, "draw")
        self.assertEqual(self.scoreboard.get_scores()[player_name], 0.5)

    @patch("builtins.print")
    def test_display_scores(self, mocked_print):
        """Test the display_scores method."""
        self.scoreboard.display_scores()
        mocked_print.assert_called_once_with("No players in the scoreboard.")

    @mock.patch("builtins.print")
    def test_display_scores_empty(self, mocked_print):
        """Test the display_scores method with an empty scoreboard."""
        self.scoreboard.set_scores({})  # Set an empty scoreboard for this test
        expected_string = "No players in the scoreboard."
        self.scoreboard.display_scores()
        mocked_print.assert_called_with(expected_string)

    def tearDown(self):
        """Remove the test_scores.pkl file if it exists."""
        if os.path.exists("test_scores.pkl"):
            os.remove("test_scores.pkl")
