# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: counter.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='counter.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\rcounter.proto\"!\n\x10IncrementRequest\x12\r\n\x05value\x18\x01 \x01(\x05\"\x1f\n\x0eIncrementReply\x12\r\n\x05value\x18\x01 \x01(\x05\"\x13\n\x11GetCounterRequest\" \n\x0fGetCounterReply\x12\r\n\x05value\x18\x01 \x01(\x05\x32r\n\x07\x43ounter\x12\x31\n\tIncrement\x12\x11.IncrementRequest\x1a\x0f.IncrementReply\"\x00\x12\x34\n\nGetCounter\x12\x12.GetCounterRequest\x1a\x10.GetCounterReply\"\x00\x62\x06proto3'
)




_INCREMENTREQUEST = _descriptor.Descriptor(
  name='IncrementRequest',
  full_name='IncrementRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='IncrementRequest.value', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=17,
  serialized_end=50,
)


_INCREMENTREPLY = _descriptor.Descriptor(
  name='IncrementReply',
  full_name='IncrementReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='IncrementReply.value', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=52,
  serialized_end=83,
)


_GETCOUNTERREQUEST = _descriptor.Descriptor(
  name='GetCounterRequest',
  full_name='GetCounterRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=85,
  serialized_end=104,
)


_GETCOUNTERREPLY = _descriptor.Descriptor(
  name='GetCounterReply',
  full_name='GetCounterReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='GetCounterReply.value', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=106,
  serialized_end=138,
)

DESCRIPTOR.message_types_by_name['IncrementRequest'] = _INCREMENTREQUEST
DESCRIPTOR.message_types_by_name['IncrementReply'] = _INCREMENTREPLY
DESCRIPTOR.message_types_by_name['GetCounterRequest'] = _GETCOUNTERREQUEST
DESCRIPTOR.message_types_by_name['GetCounterReply'] = _GETCOUNTERREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

IncrementRequest = _reflection.GeneratedProtocolMessageType('IncrementRequest', (_message.Message,), {
  'DESCRIPTOR' : _INCREMENTREQUEST,
  '__module__' : 'counter_pb2'
  # @@protoc_insertion_point(class_scope:IncrementRequest)
  })
_sym_db.RegisterMessage(IncrementRequest)

IncrementReply = _reflection.GeneratedProtocolMessageType('IncrementReply', (_message.Message,), {
  'DESCRIPTOR' : _INCREMENTREPLY,
  '__module__' : 'counter_pb2'
  # @@protoc_insertion_point(class_scope:IncrementReply)
  })
_sym_db.RegisterMessage(IncrementReply)

GetCounterRequest = _reflection.GeneratedProtocolMessageType('GetCounterRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETCOUNTERREQUEST,
  '__module__' : 'counter_pb2'
  # @@protoc_insertion_point(class_scope:GetCounterRequest)
  })
_sym_db.RegisterMessage(GetCounterRequest)

GetCounterReply = _reflection.GeneratedProtocolMessageType('GetCounterReply', (_message.Message,), {
  'DESCRIPTOR' : _GETCOUNTERREPLY,
  '__module__' : 'counter_pb2'
  # @@protoc_insertion_point(class_scope:GetCounterReply)
  })
_sym_db.RegisterMessage(GetCounterReply)



_COUNTER = _descriptor.ServiceDescriptor(
  name='Counter',
  full_name='Counter',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=140,
  serialized_end=254,
  methods=[
  _descriptor.MethodDescriptor(
    name='Increment',
    full_name='Counter.Increment',
    index=0,
    containing_service=None,
    input_type=_INCREMENTREQUEST,
    output_type=_INCREMENTREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetCounter',
    full_name='Counter.GetCounter',
    index=1,
    containing_service=None,
    input_type=_GETCOUNTERREQUEST,
    output_type=_GETCOUNTERREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_COUNTER)

DESCRIPTOR.services_by_name['Counter'] = _COUNTER

# @@protoc_insertion_point(module_scope)