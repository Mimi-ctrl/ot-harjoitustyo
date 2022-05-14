import unittest
from game_loop import board1, board2

class TestGameOver(unittest.TestCase):
    def setUp(self):
        self.b1 = board1.points(19)
        self.b2 = board2.points(19)

