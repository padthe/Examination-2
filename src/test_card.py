import unittest
from card import Card

class TestCard(unittest.TestCase):
    def test_init(self):
        card = Card('Hearts', 'Ace')
        self.assertEqual(card.suit, 'Hearts')
        self.assertEqual(card.rank, 'Ace')
        self.assertEqual(card.value, 1)

    def test_assign_value_ace(self):
        card = Card('Diamonds', 'Ace')
        self.assertEqual(card.assign_value('Ace'), 1)

    def test_assign_value_face_card(self):
        card = Card('Spades', 'King')
        self.assertEqual(card.assign_value('King'), 10)

    def test_assign_value_number_card(self):
        card = Card('Clubs', '7')
        self.assertEqual(card.assign_value('7'), 7)

    def test_str_representation(self):
        card = Card('Hearts', 'Queen')
        self.assertEqual(str(card), 'Queen of Hearts')

if __name__ == '__main__':
    unittest.main()
