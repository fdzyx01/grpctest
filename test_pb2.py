# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: test.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='test.proto',
  package='test',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\ntest.proto\x12\x04test\"\x19\n\tTest01Req\x12\x0c\n\x04name\x18\x01 \x01(\t\"k\n\x0bTest01Reply\x12-\n\x06result\x18\x01 \x03(\x0b\x32\x1d.test.Test01Reply.ResultEntry\x1a-\n\x0bResultEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x32\x36\n\x04Test\x12.\n\x06Test01\x12\x0f.test.Test01Req\x1a\x11.test.Test01Reply\"\x00\x62\x06proto3')
)




_TEST01REQ = _descriptor.Descriptor(
  name='Test01Req',
  full_name='test.Test01Req',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='test.Test01Req.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=20,
  serialized_end=45,
)


_TEST01REPLY_RESULTENTRY = _descriptor.Descriptor(
  name='ResultEntry',
  full_name='test.Test01Reply.ResultEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='test.Test01Reply.ResultEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='test.Test01Reply.ResultEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=109,
  serialized_end=154,
)

_TEST01REPLY = _descriptor.Descriptor(
  name='Test01Reply',
  full_name='test.Test01Reply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='test.Test01Reply.result', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_TEST01REPLY_RESULTENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=47,
  serialized_end=154,
)

_TEST01REPLY_RESULTENTRY.containing_type = _TEST01REPLY
_TEST01REPLY.fields_by_name['result'].message_type = _TEST01REPLY_RESULTENTRY
DESCRIPTOR.message_types_by_name['Test01Req'] = _TEST01REQ
DESCRIPTOR.message_types_by_name['Test01Reply'] = _TEST01REPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Test01Req = _reflection.GeneratedProtocolMessageType('Test01Req', (_message.Message,), {
  'DESCRIPTOR' : _TEST01REQ,
  '__module__' : 'test_pb2'
  # @@protoc_insertion_point(class_scope:test.Test01Req)
  })
_sym_db.RegisterMessage(Test01Req)

Test01Reply = _reflection.GeneratedProtocolMessageType('Test01Reply', (_message.Message,), {

  'ResultEntry' : _reflection.GeneratedProtocolMessageType('ResultEntry', (_message.Message,), {
    'DESCRIPTOR' : _TEST01REPLY_RESULTENTRY,
    '__module__' : 'test_pb2'
    # @@protoc_insertion_point(class_scope:test.Test01Reply.ResultEntry)
    })
  ,
  'DESCRIPTOR' : _TEST01REPLY,
  '__module__' : 'test_pb2'
  # @@protoc_insertion_point(class_scope:test.Test01Reply)
  })
_sym_db.RegisterMessage(Test01Reply)
_sym_db.RegisterMessage(Test01Reply.ResultEntry)


_TEST01REPLY_RESULTENTRY._options = None

_TEST = _descriptor.ServiceDescriptor(
  name='Test',
  full_name='test.Test',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=156,
  serialized_end=210,
  methods=[
  _descriptor.MethodDescriptor(
    name='Test01',
    full_name='test.Test.Test01',
    index=0,
    containing_service=None,
    input_type=_TEST01REQ,
    output_type=_TEST01REPLY,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_TEST)

DESCRIPTOR.services_by_name['Test'] = _TEST

# @@protoc_insertion_point(module_scope)