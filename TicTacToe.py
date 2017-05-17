import os
from validator import *

class TicTacToe:
	def __init__ (self,n):
		self.n = int(n);
		self.board = [['-' for i in range(self.n)] for j in range(self.n)]
		self.End = False
		self.xWin = False
		self.numberOfMoves = 0
	
	def initializeSizeOfBoard(self,n):
		validator = SizeOfBoardValidator(n)
		validator.validate()
		self.__init__(n)
	
	def returnBoard(self):
		toPrint =''
		for i in self.board:
			for j in i:
				#print j,
				toPrint+=j
			toPrint+='\n'
		return toPrint
	def printBoard(self):
		toPrint =''
		for i in self.board:
			for j in i:
				#print j,
				toPrint+=j
			toPrint+='\n'
		print (toPrint)	
	def putOnBoardPlayer1Move(self,index):
		validator = PassedIndexValidator(index,self.n)
		validator.validate()
		intIndex = int(index)
		if self.board[(intIndex-1)//self.n][(intIndex%self.n)-1] == '-':
			self.board[(intIndex-1)//self.n][(intIndex%self.n)-1] = 'x'
			self.numberOfMoves += 1
	
		else:
			raise TakenPlaceInBoardError()

	def putOnBoardPlayer2Move(self,index):
		validator = PassedIndexValidator(index,self.n)
		validator.validate()
		intIndex = int(index)
		if self.board[(intIndex-1)//self.n][(intIndex%self.n)-1] == '-':
			self.board[(intIndex-1)//self.n][(intIndex%self.n)-1] = 'o'
			self.numberOfMoves += 1
		else:
			raise TakenPlaceInBoardError()

	def limitMovesReached(self):
		if self.numberOfMoves == self.n**2:
			return True
		else:
			return False	


	
	def movePlayer1(self):
		index = int(input("Type position for PLAYER1 move "))
		self.putOnBoardPlayer1Move(index)
		self.isEnd()

	
	def movePlayer2(self):
		index = int(input("Type position for PLAYER2 move "))
		self.putOnBoardPlayer2Move(index)
		self.isEnd()

	def startGame(self):
		os.system("clear")
		print("Welcome to the tic-tac-toe game.\nFirst player is 'x' and second 'o'.\nTo enter your moves type numbers 1-9 which are another field in the board")
		self.printBoard()
		while not self.End:
			if self.numberOfMoves == self.n**2:
				break
			self.movePlayer1()
			os.system("clear")
			self.printBoard()
			if not self.End:
				if self.numberOfMoves == self.n**2:
					break
				
				self.movePlayer2()
				os.system("clear")
				self.printBoard()
		if self.xWin :
			print("Player 1 has won")
		elif self.End:
			print("Player 2 has won")
		else:
			print("Nobody has won")

	def isEnd(self):
		self.End = False
		for i in range(self.n):
			if self.board[i] == ['x' for i in range(self.n)]:
				self.xWin = True
				self.End = True
			if self.board[i] == ['o' for i in range(self.n)]:
				self.End = True
			for j in range(self.n):
				if self.board[j][i] != 'x':
					break
			else:
				self.xWin = True
				self.End = True

			for j in range(self.n):
				if self.board[j][i] != 'o':
					break
			else: 
				self.End = True
		for k in range (self.n):
			if self.board[k][k] != 'x':
				break
		else: 
			self.End = True
			self.xWin = True
		for k in range (self.n):
			if self.board[k][k] != 'o':
				break
		else: 
			self.End = True

		for i in range(self.n):
			if self.board[i][self.n-(i+1)] != 'o':
				break
		else:
			self.End = True

		for i in range(self.n):
			if self.board[i][self.n-(i+1)] != 'x':
				break
		else:
			self.End = True
			self.xWin = True
		return self.End		