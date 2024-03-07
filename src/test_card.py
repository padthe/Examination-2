import unittest
from card import Card

class TestCard(unittest.TestCase):
    """Test methods in the Card class."""
    def test_init(self):
        """Test that the suit, rank, and value attributes are set correctly."""
        card = Card("Hearts", "Ace")
        self.assertEqual(card.suit, "Hearts")
        self.assertEqual(card.rank, "Ace")
        self.assertEqual(card.value, 1)

        card = Card("Diamonds", "10")
        self.assertEqual(card.suit, "Diamonds")
        self.assertEqual(card.rank, "10")
        self.assertEqual(card.value, 10)

    def test_assign_value(self):
        """Test that the correct value is assigned to the card."""
        card = Card("Clubs", "King")
        self.assertEqual(card.assign_value("King"), 10)

        card = Card("Spades", "2")
        self.assertEqual(card.assign_value("2"), 2)

        card = Card("Hearts", "Ace")
        self.assertEqual(card.assign_value("Ace"), 1)

    def test_str(self):
        """Test that the correct string representation of the card is returned."""
        card = Card("Diamonds", "Jack")
        self.assertEqual(str(card), "Jack of Diamonds")

        card = Card("Spades", "5")
        self.assertEqual(str(card), "5 of Spades")

if __name__ == '__main__':
    unittest.main()
