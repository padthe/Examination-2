import unittest
from unittest.mock import patch
from game import Game, Player, Scoreboard

class TestGame(unittest.TestCase):
    def setUp(self):
        player = Player()
        scoreboard = Scoreboard()
        self.game = Game(player, scoreboard)

    @patch('builtins.input', side_effect=['John', 'hit me', 'no', ''])
    def test_start_game(self, mock_input):
        with self.assertRaises(SystemExit):
            self.game.start_game()

    # Add more test cases as needed...

if __name__ == '__main__':
    unittest.main()
