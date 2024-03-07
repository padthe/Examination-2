import unittest
from hand import Hand  

class TestHand(unittest.TestCase):
    """Test methods in the Hand class."""
    def setUp(self):
        self.hand = Hand()

    def test_add_card(self):
        """Test that a card is added to the hand and the value is updated correctly."""
        self.hand.add_card("Ace of Spades")
        self.assertEqual(self.hand.cards, ["Ace of Spades"])
        self.assertEqual(self.hand.value, 1)

        self.hand.add_card("10 of Hearts")
        self.assertEqual(self.hand.cards, ["Ace of Spades", "10 of Hearts"])
        self.assertEqual(self.hand.value, 11)  # 1 (Ace) + 10

    def test_get_card_value(self):
        """Test that the correct value is returned for a given card."""
        self.assertEqual(self.hand.get_card_value("Jack of Diamonds"), 10)
        self.assertEqual(self.hand.get_card_value("5 of Clubs"), 5)
        self.assertEqual(self.hand.get_card_value("Ace of Hearts"), 1)

    def test_calculate_value(self):
        """Test that the value of the hand is calculated correctly."""
        self.hand.add_card("King of Spades")
        self.hand.add_card("7 of Diamonds")
        self.assertEqual(self.hand.calculate_value(), 17)  # 10 (King) + 7

        self.hand.add_card("Ace of Clubs")
        self.assertEqual(self.hand.calculate_value(), 18)  # 17 + 1 (Ace)

if __name__ == '__main__':
    unittest.main()
