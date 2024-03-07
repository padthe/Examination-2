import unittest
from unittest.mock import patch
from player import Player
from deck import Deck

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player()

    def test_add_player(self):
        """Test that the user_name attribute is set correctly."""
        self.player.add_player("John")
        self.assertEqual(self.player.user_name, "John", "Username not set correctly")

    @patch('builtins.input', side_effect=['NewName'])
    def test_change_user_name(self, mock_input):
        """Test that the user_name attribute is changed correctly."""
        self.player.add_player("John")
        self.player.change_user_name()
        self.assertEqual(self.player.user_name, "NewName", "Username not changed correctly")

    @patch('deck.Deck.deal_card', return_value='Ace of Spades')
    def test_draw_card(self, mock_deal_card):
        """Test that a card is added to the player's hand."""
        deck = Deck()
        self.player.draw_card(deck)
        self.assertEqual(len(self.player.hand.cards), 1, "Card not added to the player's hand")
        self.assertEqual(self.player.hand.cards[0], 'Ace of Spades', "Wrong card added to the player's hand")

if __name__ == '__main__':
    unittest.main()
