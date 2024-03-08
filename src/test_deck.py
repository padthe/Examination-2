import unittest
from unittest.mock import patch
from deck import Deck

class TestDeck(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()

    def test_create_deck(self):
        self.assertEqual(len(self.deck.get_deck()), 52)

    def test_shuffle_deck(self):
        original_deck = self.deck.get_deck().copy()
        self.deck.shuffle_deck()
        shuffled_deck = self.deck.get_deck()
        self.assertNotEqual(original_deck, shuffled_deck)

    def test_deal_card(self):
        original_deck = self.deck.get_deck().copy()
        card = self.deck.deal_card()
        self.assertIn(card, original_deck)

    def test_deal_card_empty_deck(self):
        # Ensure dealing from an empty deck returns None
        self.deck.set_deck([])
        card = self.deck.deal_card()
        self.assertIsNone(card)

    def test_get_deck(self):
        self.assertIsInstance(self.deck.get_deck(), list)

    def test_set_deck(self):
        new_deck = ['Card1', 'Card2']
        self.deck.set_deck(new_deck)
        self.assertEqual(self.deck.get_deck(), new_deck)

if __name__ == '__main__':
    unittest.main()
