if __name__ == "__main__":
	import unittest
	from testTicTacToe import *
	suite1 = unittest.TestLoader().loadTestsFromTestCase(TicTacToeTest)
	suite = unittest.TestSuite([suite1])
	unittest.TextTestRunner(verbosity=2).run(suite)
	
