from messages_pb2 import *
from functions import *
from validator import *
from NumberGame import*
from states import *

class msgHandler:
	socket =''
	def __init__(self):
		self.newMessage = Message()
	def handle(self,message):
		pass

class INIT_REQ_H(msgHandler):
	def handle(self,message):
		print (message.text)
		self.newMessage.game = int(input())
		self.newMessage.type = INIT_RES
		send_message(msgHandler.socket,self.newMessage)



class INIT_RES_H(msgHandler):
	def handle(self,message,gameObject,state = 0):
		try:
			validator = GameChooseValidator(message.game)
			validator.validate()
		except BadNumberOfGamePassed:
			self.newMessage.text = "You have to choose 1 or 2 not %d. Type it again" % message.game
			self.newMessage.type = INIT_REQ	
		else:
			if message.game == 1:
				self.newMessage.text = "Type size of board"
				self.newMessage.type = BOARD_SIZE_REQ
				state[0] = State.TIC_TAC_TOE_GAME
			if message.game == 2:
				self.newMessage.text = "You have to guess number in 0-100 compartment. Type your first number"
				self.newMessage.type = MOVE_REQ
				state[0] = State.NUMBER_GAME
		finally:
			send_message(msgHandler.socket,self.newMessage)

class MOVE_REQ_H(msgHandler):
	def handle(self,message):
		print(message.text)
		self.newMessage.text = input()
		self.newMessage.type = MOVE_RES
		send_message(msgHandler.socket,self.newMessage)


class MOVE_RES_H(msgHandler):
	def handle(self,message,gameObject):
		try:
			validator = NumberChooseValidator(message.text)
			validator.validate()
		except BadNumberChoosen:
			self.newMessage.text = "You have to pass number in 0-100 range not %s\nType it again." % message.text
			self.newMessage.type = MOVE_REQ
		else:
			try:
				self.newMessage.text = gameObject.checkComplianceWithKeptNumber(message.text)
			except Exception as e:
				print(e)	
			if self.newMessage.text == 'True':
				self.newMessage.text = 'Congratulations you have won. Number to guess was %s.' % message.text
				self.newMessage.type = END_CONNECTION
			else:
				self.newMessage.text += "\nType it again."
				self.newMessage.type = MOVE_REQ
		finally:
			send_message(msgHandler.socket,self.newMessage)

class END_CONNECTION_H(msgHandler):
	def handle(self,message):
		os.system("clear")
		print(message.text)
		self.newMessage.type = END_CONNECTION
		send_message(msgHandler.socket,self.newMessage)

		


class BOARD_SIZE_REQ_H(msgHandler):
	def handle(self,message):
		print(message.text)
		self.newMessage.type = BOARD_SIZE_RES
		self.newMessage.text = input()
		send_message(msgHandler.socket,self.newMessage)


class BOARD_SIZE_RES_H(msgHandler):
	def handle(self,message,gameObject):
		try:
			gameObject.initializeSizeOfBoard(message.text)
		except BadSizeOfBoardError:
			self.newMessage.type = BOARD_SIZE_REQ
			self.newMessage.text = "Bad size of board. Should be number >=3.\nType it again."
		else:
			self.newMessage.type = PLAYER1_MOVE_REQ
			self.newMessage.text = gameObject.returnBoard() +"\nType number for player 'x' move."
		finally:
			send_message(msgHandler.socket,self.newMessage)

class PLAYER1_MOVE_REQ_H(msgHandler):
	def handle(self,message):
		os.system("clear")
		print(message.text)
		self.newMessage.type = PLAYER1_MOVE_RES
		self.newMessage.text = input()
		send_message(msgHandler.socket,self.newMessage)

class PLAYER1_MOVE_RES_H(msgHandler):
	def handle(self,message,gameObject):
		try:
			gameObject.putOnBoardPlayer1Move(message.text)
		except (TakenPlaceInBoardError, BadIndexPassed):
			self.newMessage.text = gameObject.returnBoard() + "\nBad index passed.\nTry again."
			self.newMessage.type = PLAYER1_MOVE_REQ
		else:
			if gameObject.isEnd():
				if gameObject.xWin:
					self.newMessage.text = gameObject.returnBoard() + "\nPlayer 'x' has won."
					self.newMessage.type = END_CONNECTION
				else:
					self.newMessage.text = gameObject.returnBoard() + "\nPlayer 'o' has won."
					self.newMessage.type = END_CONNECTION
			else:
				if gameObject.limitMovesReached():
					self.newMessage.text = gameObject.returnBoard() +"\nNobody has won."
					self.newMessage.type = END_CONNECTION
				else:
					self.newMessage.text = gameObject.returnBoard() +"\nType number for player 'o' move."
					self.newMessage.type = PLAYER2_MOVE_REQ
		finally:
			send_message(msgHandler.socket,self.newMessage)

class PLAYER2_MOVE_REQ_H(msgHandler):
	def handle(self,message):
		os.system("clear")
		print(message.text)
		self.newMessage.type = PLAYER2_MOVE_RES
		self.newMessage.text = input()
		send_message(msgHandler.socket,self.newMessage)

class PLAYER2_MOVE_RES_H(msgHandler):
	def handle(self,message,gameObject):
		try:
			gameObject.putOnBoardPlayer2Move(message.text)
		except (TakenPlaceInBoardError, BadIndexPassed):
			self.newMessage.text = gameObject.returnBoard() + "\nBad index passed.\nTry again."
			self.newMessage.type = PLAYER2_MOVE_REQ
		else:
			if gameObject.isEnd():
				if gameObject.xWin:
					self.newMessage.text = gameObject.returnBoard() + "\nPlayer 'x' has won."
					self.newMessage.type = END_CONNECTION
				else:
					self.newMessage.text = gameObject.returnBoard() + "\nPlayer 'o has won."
					self.newMessage.type = END_CONNECTION
			else:
				if gameObject.limitMovesReached():
					self.newMessage.text = gameObject.returnBoard() + "\nNobody has won."
					self.newMessage.type = END_CONNECTION	
				else:
					self.newMessage.text = gameObject.returnBoard() +"\nType number for player 'x' move"
					self.newMessage.type = PLAYER1_MOVE_REQ
		finally:
			send_message(msgHandler.socket,self.newMessage)





myDictionary =  {
				INIT_REQ : INIT_REQ_H(),
				INIT_RES : INIT_RES_H(),
				MOVE_REQ : MOVE_REQ_H(),
				MOVE_RES : MOVE_RES_H(),
				BOARD_SIZE_REQ : BOARD_SIZE_REQ_H(),
				BOARD_SIZE_RES : BOARD_SIZE_RES_H(),
				END_CONNECTION : END_CONNECTION_H(),
				PLAYER1_MOVE_REQ: PLAYER1_MOVE_REQ_H(),
				PLAYER1_MOVE_RES: PLAYER1_MOVE_RES_H(),
				PLAYER2_MOVE_REQ: PLAYER2_MOVE_REQ_H(),
				PLAYER2_MOVE_RES: PLAYER2_MOVE_RES_H()
				}
