import socket
import sys
from messages_pb2 import*
from functions import *
from handlers import *


class MyClient:
	def __init__(self,address, port, data_size):
		self.data_size = data_size
		self._createTcpIpSocket()
		self._connectToServer(address, port)

	def _createTcpIpSocket(self):
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


	def _connectToServer(self,address,port):
		server_address = (address, port)
		print('connecting to %s port %s' % server_address)
		self.sock.connect(server_address)
		



if __name__ == "__main__":
	host = 'localhost'
	port = 50001
	data_size = 1024
	client = MyClient(host, port, data_size)
	msgHandler.socket = client.sock
	while True:
		myMsg = get_response(client.sock)
		myDictionary[myMsg.type].handle(myMsg)
		if myMsg.type == END_CONNECTION:
			client.sock.close()
			break
