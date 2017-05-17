import struct
from messages_pb2 import *
def send_message(sock, message):
	s = message.SerializeToString()
	packed_len = struct.pack('>L', len(s))
	packed_message = packed_len + s
	sock.send(packed_message)

def socket_read_n(sock, n):
	buf = b''
	while n>0:
		data = sock.recv(n)
		if data =='':
			raise RuntimeError('unexpected connection close')
		buf += data
		n -=len(data)
	return buf

def get_response(sock):
	msg = Message()
	len_buf = socket_read_n(sock,4)
	msg_len = struct.unpack('>L', len_buf)[0]
	msg_buf = socket_read_n(sock, msg_len)
	msg.ParseFromString(msg_buf)
	return msg