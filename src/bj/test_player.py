"""Unit tests for the Player class."""
import unittest
from unittest.mock import patch
from player import Player


class TestPlayer(unittest.TestCase):
    """Test the Player class."""
    def setUp(self):
        self.player = Player()

    def test_add_player(self):
        """Test the add_player method."""
        self.player.add_player("John")
        self.assertEqual(self.player.get_user_name(), "John")

    def test_change_user_name(self):
        """Test the change_user_name method."""
        with patch("builtins.input", return_value="NewName"):
            self.player.change_user_name()
        self.assertEqual(self.player.get_user_name(), "NewName")

    def test_draw_card(self):
        """Test the draw_card method."""
        deck_mock = unittest.mock.MagicMock()
        deck_mock.deal_card.return_value = "Ace of Spades"
        self.player.draw_card(deck_mock)
        self.assertEqual(len(self.player.get_hand().get_cards()), 1)
        self.assertEqual(self.player.get_hand().get_value(), 1)

    def test_set_hand(self):
        """Test the set_hand method."""
        new_hand_mock = unittest.mock.MagicMock()
        self.player.set_hand(new_hand_mock)
        self.assertEqual(self.player.get_hand(), new_hand_mock)

    def test_set_user_name(self):
        """Test the set_user_name method."""
        self.player.set_user_name("Jane")
        self.assertEqual(self.player.get_user_name(), "Jane")


if __name__ == "__main__":
    unittest.main()
