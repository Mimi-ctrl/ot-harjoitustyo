import unittest

from pong import Pong


class TestCore(unittest.TestCase):
    def setUp(self):
        print("Set up goes here")

    def test_points_are_correctly_at_the_start(self):
        points = Pong(0)
        answer = str(points)

        self.assertEqual(answer, "0")
   # def test_boar1_get_points_and_board2_not():

   # def test_boar2_get_points_and_board1_not():

   # def test_poits_reset_when_twenty():
