import unittest
from unittest.mock import patch
from player import Player

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player()

    def test_add_player(self):
        self.player.add_player("John")
        self.assertEqual(self.player.get_user_name(), "John")

    def test_change_user_name(self):
        with patch('builtins.input', return_value="NewName"):
            self.player.change_user_name()
        self.assertEqual(self.player.get_user_name(), "NewName")

    def test_draw_card(self):
        deck_mock = unittest.mock.MagicMock()
        deck_mock.deal_card.return_value = "Ace of Spades"
        self.player.draw_card(deck_mock)
        self.assertEqual(len(self.player.get_hand().get_cards()), 1)
        self.assertEqual(self.player.get_hand().get_value(), 1)

    def test_set_hand(self):
        new_hand_mock = unittest.mock.MagicMock()
        self.player.set_hand(new_hand_mock)
        self.assertEqual(self.player.get_hand(), new_hand_mock)

    def test_set_user_name(self):
        self.player.set_user_name("Jane")
        self.assertEqual(self.player.get_user_name(), "Jane")

if __name__ == '__main__':
    unittest.main()
