from messages_pb2 import*
import socket
import sys
from functions import *
from mess import *
from handlers import*
from TicTacToe import*
from NumberGame import*
from states import *

class MyServer:
	def __init__(self, address, port, data_size):
		self.data_size = data_size
		self._createTcpIpSocket()
		self._bindSocketToThePort(address, port)
		self.numberGame = NumberGame(0,100)
		self.tttGame = TicTacToe(0)
		self.state = [State.NO_GAME]

	def handle_connection(self):
		self.sock.listen(1)
		connection, client_address = self.sock.accept()
		msgHandler.socket = connection
		send_message(connection,InitialMessage)
		while True:
			gotMessage = get_response(connection)
			if gotMessage.type == END_CONNECTION:
				connection.close()
				break
			if self.state[0] == State.NUMBER_GAME:
				myDictionary[gotMessage.type].handle(gotMessage,self.numberGame)
			if self.state[0] == State.TIC_TAC_TOE_GAME:
				myDictionary[gotMessage.type].handle(gotMessage,self.tttGame)
			if self.state[0] == State.NO_GAME:
				myDictionary[gotMessage.type].handle(gotMessage,0,self.state)


	def _createTcpIpSocket(self):
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	def _bindSocketToThePort(self, address, port):
		server_address = (address, port)
		print('bind to %s port %s' % server_address)
		self.sock.bind(server_address)


if __name__ == "__main__":
	host = 'localhost'
	port = 50001
	data_size = 1024
	server = MyServer(host, port, data_size)
	server.handle_connection()