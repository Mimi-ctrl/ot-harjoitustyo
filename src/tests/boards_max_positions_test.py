import unittest
from sprites import board

class TestBoardPosition(unittest.TestCase):
    def setUp(self):
        self.b1 = board.Board1.self.rect.y(-1)
        self.b2 = board.Board2.self.rect.y(-1)
        self.b11 = board.Board1.self.rect.y(526)
        self.b22 = board.Board2.self.rect.y(526)

    def test_board1_down_max_position_is_right(self):
        self.b1.board_max_positions()
        self.assertEqual(self.b1,0)
    
    def test_board2_down_max_position_is_right(self):
        self.b2.board_max_positions()
        self.assertEqual(self.b2,0)

    def test_board1_up_max_position_is_right(self):
        self.b11.board_max_positions()
        self.assertEqual(self.b11,525)

    def test_board2_up_max_position_is_right(self):
        self.b22.board_max_positions()
        self.assertEqual(self.b22,525)