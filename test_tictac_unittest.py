# author: Robert (Bob) Young
# date: 12/29/2020
# test_tictac_unittest.py
# Testing for tictac.py
# This proved especially useful for refactoring the code.

from tictac import Board
import unittest

class TestTictac(unittest.TestCase):

	# Test board generation
	def test_board_generation(self):
		self.assertEqual(''.join([''.join(x) for x in Board().board]), ''.join([''.join(x) for x in Board('.........').board]))
		self.assertEqual(''.join([''.join(x) for x in Board('.O.XXX..O').board]), '.O.XXX..O')

	# Test where nobody wins
	def test_nobody_wins(self):
		self.assertFalse(Board('.........').over(), "Nobody wins yet")
		self.assertFalse(Board('X..O.O.XX').over(), "Nobody wins yet")

	# Test where either X or O wins across, down, diagonals
	def test_somebody_wins(self):
		self.assertTrue(Board('XXX......').over(), "X wins across")
		self.assertTrue(Board('.X..X..X.').over(), "X wins down")
		self.assertTrue(Board('O...O...O').over(), "O wins diagonal")
		self.assertTrue(Board('..X.X.X..').over(), "X wins reverse diagonal")
		self.assertTrue(Board('OXOOXOXXX').over(), "X wins across")

	# Test whether there is a tie game
	def test_tie_game(self):
		self.assertTrue(Board('XOXOOXOXO').over(), "Game over, tie game")

if __name__ == '__main__':
	unittest.main()