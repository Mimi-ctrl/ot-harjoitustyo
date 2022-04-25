import unittest
from pong import Board1, Board2

class BoardPosition(unittest.TestCase):
    def setUp(self):
        self.board1 = Board1()
        self.board2 = Board2()

    def test_board1_down_max_position_is_right(self):
        self.board1(15, -2)
        self.assertEqual(self.board1(15, 0))
