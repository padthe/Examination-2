"""Unit tests for the Deck class."""
import unittest
from deck import Deck


class TestDeck(unittest.TestCase):
    """Test the Deck class."""

    def setUp(self):
        """Create a Deck instance for testing."""
        self.deck = Deck()

    def test_create_deck(self):
        """Test the create_deck method."""
        self.assertEqual(len(self.deck.get_deck()), 52)

    def test_shuffle_deck(self):
        """Test the shuffle_deck method."""
        original_deck = self.deck.get_deck().copy()
        self.deck.shuffle_deck()
        shuffled_deck = self.deck.get_deck()
        self.assertNotEqual(original_deck, shuffled_deck)

    def test_deal_card(self):
        """Test the deal_card method."""
        original_deck = self.deck.get_deck().copy()
        card = self.deck.deal_card()
        self.assertIn(card, original_deck)

    def test_deal_card_empty_deck(self):
        """Test the deal_card method with an empty deck."""
        # Ensure dealing from an empty deck returns None
        self.deck.set_deck([])
        card = self.deck.deal_card()
        self.assertIsNone(card)

    def test_get_deck(self):
        """Test the get_deck method."""
        self.assertIsInstance(self.deck.get_deck(), list)

    def test_set_deck(self):
        """Test the set_deck method."""
        new_deck = ["Card1", "Card2"]
        self.deck.set_deck(new_deck)
        self.assertEqual(self.deck.get_deck(), new_deck)


if __name__ == "__main__":
    unittest.main()
