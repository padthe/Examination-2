import unittest
from deck import Deck 

class TestDeck(unittest.TestCase):
    """Test methods in the Deck class."""
    def setUp(self):
        self.deck = Deck()

    def test_deck_creation(self):
        """Test that the deck is created with the correct number of cards."""
        self.assertEqual(len(self.deck.deck), 52)

    def test_shuffle_deck(self):
        """Test that the deck is shuffled."""
        original_order = self.deck.deck.copy()
        self.deck.shuffle_deck()
        self.assertNotEqual(self.deck.deck, original_order)
        self.assertEqual(set(self.deck.deck), set(original_order))

    def test_deal_card(self):
        """Test that a card is dealt from the deck."""
        initial_length = len(self.deck.deck)
        card = self.deck.deal_card()
        self.assertIsNotNone(card)
        self.assertEqual(len(self.deck.deck), initial_length - 1)

    def test_deal_card_empty_deck(self):
        """Test dealing from an empty deck."""
        self.deck.deck = []
        card = self.deck.deal_card()
        self.assertIsNone(card)

if __name__ == '__main__':
    unittest.main()
