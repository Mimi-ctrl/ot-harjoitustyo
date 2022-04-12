from pkgutil import ModuleInfo
import unittest


from pong import Pong


class TestCore(unittest.TestCase):
    def setUp(self):
        self.board1.points = Pong(0)
        self.board2.points = Pong(0)

  # def test_points_are_correctly_at_the_start():

   # def test_boar1_get_points_and_board2_not():

   # def test_boar2_get_points_and_board1_not():

   # def test_poits_reset_when_twenty():
