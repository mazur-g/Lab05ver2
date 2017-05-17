from messages_pb2 import*

InitialMessage = Message()
InitialMessage.type = INIT_REQ
InitialMessage.text = "Choose the game.\n1.TicTacToe Game.\n2.Number Game\n"
