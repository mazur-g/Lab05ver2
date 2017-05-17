# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: messages.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='messages.proto',
  package='mess',
  syntax='proto2',
  serialized_pb=_b('\n\x0emessages.proto\x12\x04mess\"M\n\x07Message\x12\x18\n\x04type\x18\x02 \x02(\x0e\x32\n.mess.Type\x12\x0c\n\x04text\x18\x03 \x01(\t\x12\x0c\n\x04move\x18\x04 \x01(\x05\x12\x0c\n\x04game\x18\x05 \x01(\x05*\xd2\x01\n\x04Type\x12\x0c\n\x08INIT_REQ\x10\x00\x12\x0c\n\x08INIT_RES\x10\x01\x12\x0c\n\x08MOVE_REQ\x10\x02\x12\x0c\n\x08MOVE_RES\x10\x03\x12\x12\n\x0e\x42OARD_SIZE_REQ\x10\x04\x12\x12\n\x0e\x42OARD_SIZE_RES\x10\x05\x12\x12\n\x0e\x45ND_CONNECTION\x10\x06\x12\x14\n\x10PLAYER1_MOVE_REQ\x10\x07\x12\x14\n\x10PLAYER1_MOVE_RES\x10\x08\x12\x14\n\x10PLAYER2_MOVE_REQ\x10\t\x12\x14\n\x10PLAYER2_MOVE_RES\x10\n')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='mess.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='INIT_REQ', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INIT_RES', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MOVE_REQ', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MOVE_RES', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BOARD_SIZE_REQ', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BOARD_SIZE_RES', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='END_CONNECTION', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PLAYER1_MOVE_REQ', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PLAYER1_MOVE_RES', index=8, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PLAYER2_MOVE_REQ', index=9, number=9,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PLAYER2_MOVE_RES', index=10, number=10,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=104,
  serialized_end=314,
)
_sym_db.RegisterEnumDescriptor(_TYPE)

Type = enum_type_wrapper.EnumTypeWrapper(_TYPE)
INIT_REQ = 0
INIT_RES = 1
MOVE_REQ = 2
MOVE_RES = 3
BOARD_SIZE_REQ = 4
BOARD_SIZE_RES = 5
END_CONNECTION = 6
PLAYER1_MOVE_REQ = 7
PLAYER1_MOVE_RES = 8
PLAYER2_MOVE_REQ = 9
PLAYER2_MOVE_RES = 10



_MESSAGE = _descriptor.Descriptor(
  name='Message',
  full_name='mess.Message',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='mess.Message.type', index=0,
      number=2, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='text', full_name='mess.Message.text', index=1,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='move', full_name='mess.Message.move', index=2,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='game', full_name='mess.Message.game', index=3,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=24,
  serialized_end=101,
)

_MESSAGE.fields_by_name['type'].enum_type = _TYPE
DESCRIPTOR.message_types_by_name['Message'] = _MESSAGE
DESCRIPTOR.enum_types_by_name['Type'] = _TYPE

Message = _reflection.GeneratedProtocolMessageType('Message', (_message.Message,), dict(
  DESCRIPTOR = _MESSAGE,
  __module__ = 'messages_pb2'
  # @@protoc_insertion_point(class_scope:mess.Message)
  ))
_sym_db.RegisterMessage(Message)


# @@protoc_insertion_point(module_scope)
