import unittest
from random import randrange
from TicTacToe import *
class TicTacToeTest(unittest.TestCase):
	"""class responsible for testing TicTacToe game"""
	def setUp(self):
		self.n = randrange(3,10)
		self.TTTgame = TicTacToe(self.n)
	def test_whether_good_index_is_passed(self):
		self.assertRaises(BadIndexPassed,self.TTTgame.putOnBoardPlayer1Move,self.n**2+1)
		self.assertRaises(BadIndexPassed,self.TTTgame.putOnBoardPlayer2Move,-1)
		self.assertRaises(BadIndexPassed,self.TTTgame.putOnBoardPlayer1Move,2.34)
		self.assertRaises(BadIndexPassed,self.TTTgame.putOnBoardPlayer1Move,"someString")

	def test_whether_good_rules_are_set_up_for_1_player_win(self):
		for i in range(self.n):
			self.TTTgame.board[i][i] = 'x'
		self.TTTgame.isEnd()
		self.assertTrue(self.TTTgame.End)
		self.TTTgame.board[2][2] = 'o'
		self.TTTgame.isEnd()
		self.assertFalse(self.TTTgame.End)


	def test_wheter_good_rules_are_set_up_for_2_player_win(self):
		x = randrange(self.n)
		self.TTTgame.board[x] = ['o' for i in range(self.n) ]
		self.TTTgame.isEnd()
		self.assertTrue(self.TTTgame.End)
		self.TTTgame.board[x][1] = 'x'
		self.TTTgame.isEnd()
		self.assertFalse(self.TTTgame.End)

