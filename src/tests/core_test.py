import unittest
from game_loop import BOARD1, BOARD2, BALL, board_get_point

class TestCore(unittest.TestCase):
    def setUp(self):
        self.b1 = BOARD1
        self.b2 = BOARD2
        self.ball = BALL
    
    def test_board1_get_point(self):
        self.ball.rect.x = 691
        board_get_point()
        self.assertEqual(self.b1.points,1)

    def test_board2_get_point(self):
        self.ball.rect.x = -1
        board_get_point()
        self.assertEqual(self.b2.points,1)