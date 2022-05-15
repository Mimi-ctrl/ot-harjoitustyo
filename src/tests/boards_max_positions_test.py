import unittest
from game_loop import BOARD1, BOARD2, boards_max_positions

class TestBoardPosition(unittest.TestCase):
    def setUp(self):
        self.b1 = BOARD1
        self.b2 = BOARD2

    def test_board1_down_max_position_is_right(self):
        self.b1.rect.y = -1
        boards_max_positions()
        self.assertEqual(self.b1.rect.y,0)
    
    def test_board2_down_max_position_is_right(self):
        self.b2.rect.y = -1
        boards_max_positions()
        self.assertEqual(self.b2.rect.y,0)

    def test_board1_up_max_position_is_right(self):
        self.b1.rect.y = 526
        boards_max_positions()
        self.assertEqual(self.b1.rect.y,525)

    def test_board2_up_max_position_is_right(self):
        self.b2.rect.y = 526
        boards_max_positions()
        self.assertEqual(self.b2.rect.y,525)