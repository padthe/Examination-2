"""Unit tests for the Hand class."""
import unittest
from hand import Hand


class TestHand(unittest.TestCase):
    """Test the Hand class."""

    def setUp(self):
        """Create a Hand instance for testing."""
        self.hand = Hand()

    def test_add_card(self):
        """Test the add_card method."""
        self.hand.add_card("Ace of Spades")
        self.assertEqual(len(self.hand.get_cards()), 1)
        self.assertEqual(self.hand.get_value(), 1)

    def test_get_card_value_face_card(self):
        """Test the get_card_value method with a face card."""
        value = self.hand.get_card_value("King of Hearts")
        self.assertEqual(value, 10)

    def test_get_card_value_number_card(self):
        """Test the get_card_value method with a number card."""
        value = self.hand.get_card_value("7 of Diamonds")
        self.assertEqual(value, 7)

    def test_reset_hand(self):
        """Test the reset_hand method."""
        self.hand.add_card("Ace of Clubs")
        self.hand.add_card("8 of Spades")
        self.hand.reset_hand()
        self.assertEqual(len(self.hand.get_cards()), 0)
        self.assertEqual(self.hand.get_value(), 0)

    def test_calculate_value(self):
        """Test the calculate_value method."""
        self.hand.add_card("10 of Diamonds")
        self.hand.add_card("6 of Clubs")
        value = self.hand.calculate_value()
        self.assertEqual(value, 16)


if __name__ == "__main__":
    unittest.main()
