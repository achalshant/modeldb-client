# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ArtifactStore.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='ArtifactStore.proto',
  package='com.mitdbg.artifactstore',
  syntax='proto3',
  serialized_options=_b('P\001'),
  serialized_pb=_b('\n\x13\x41rtifactStore.proto\x12\x18\x63om.mitdbg.artifactstore\"s\n\rStoreArtifact\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x18\n\x10\x63lient_file_path\x18\x02 \x01(\t\x1a;\n\x08Response\x12\x16\n\x0e\x63loud_file_key\x18\x01 \x01(\t\x12\x17\n\x0f\x63loud_file_path\x18\x02 \x01(\t\"x\n\x17StoreArtifactWithStream\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x13\n\x0b\x63lient_file\x18\x02 \x01(\x0c\x1a;\n\x08Response\x12\x16\n\x0e\x63loud_file_key\x18\x01 \x01(\t\x12\x17\n\x0f\x63loud_file_path\x18\x02 \x01(\t\"8\n\x0bGetArtifact\x12\x0b\n\x03key\x18\x01 \x01(\t\x1a\x1c\n\x08Response\x12\x10\n\x08\x63ontents\x18\x01 \x01(\x0c\"9\n\x0e\x44\x65leteArtifact\x12\x0b\n\x03key\x18\x01 \x01(\t\x1a\x1a\n\x08Response\x12\x0e\n\x06status\x18\x01 \x01(\x08\x32\xdb\x03\n\rArtifactStore\x12j\n\rstoreArtifact\x12\'.com.mitdbg.artifactstore.StoreArtifact\x1a\x30.com.mitdbg.artifactstore.StoreArtifact.Response\x12\x88\x01\n\x17storeArtifactWithStream\x12\x31.com.mitdbg.artifactstore.StoreArtifactWithStream\x1a:.com.mitdbg.artifactstore.StoreArtifactWithStream.Response\x12\x64\n\x0bgetArtifact\x12%.com.mitdbg.artifactstore.GetArtifact\x1a..com.mitdbg.artifactstore.GetArtifact.Response\x12m\n\x0e\x64\x65leteArtifact\x12(.com.mitdbg.artifactstore.DeleteArtifact\x1a\x31.com.mitdbg.artifactstore.DeleteArtifact.ResponseB\x02P\x01\x62\x06proto3')
)




_STOREARTIFACT_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='com.mitdbg.artifactstore.StoreArtifact.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cloud_file_key', full_name='com.mitdbg.artifactstore.StoreArtifact.Response.cloud_file_key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cloud_file_path', full_name='com.mitdbg.artifactstore.StoreArtifact.Response.cloud_file_path', index=1,
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=105,
  serialized_end=164,
)

_STOREARTIFACT = _descriptor.Descriptor(
  name='StoreArtifact',
  full_name='com.mitdbg.artifactstore.StoreArtifact',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='com.mitdbg.artifactstore.StoreArtifact.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='client_file_path', full_name='com.mitdbg.artifactstore.StoreArtifact.client_file_path', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_STOREARTIFACT_RESPONSE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=49,
  serialized_end=164,
)


_STOREARTIFACTWITHSTREAM_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='com.mitdbg.artifactstore.StoreArtifactWithStream.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cloud_file_key', full_name='com.mitdbg.artifactstore.StoreArtifactWithStream.Response.cloud_file_key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cloud_file_path', full_name='com.mitdbg.artifactstore.StoreArtifactWithStream.Response.cloud_file_path', index=1,
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=105,
  serialized_end=164,
)

_STOREARTIFACTWITHSTREAM = _descriptor.Descriptor(
  name='StoreArtifactWithStream',
  full_name='com.mitdbg.artifactstore.StoreArtifactWithStream',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='com.mitdbg.artifactstore.StoreArtifactWithStream.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='client_file', full_name='com.mitdbg.artifactstore.StoreArtifactWithStream.client_file', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_STOREARTIFACTWITHSTREAM_RESPONSE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=166,
  serialized_end=286,
)


_GETARTIFACT_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='com.mitdbg.artifactstore.GetArtifact.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='contents', full_name='com.mitdbg.artifactstore.GetArtifact.Response.contents', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=316,
  serialized_end=344,
)

_GETARTIFACT = _descriptor.Descriptor(
  name='GetArtifact',
  full_name='com.mitdbg.artifactstore.GetArtifact',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='com.mitdbg.artifactstore.GetArtifact.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_GETARTIFACT_RESPONSE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=288,
  serialized_end=344,
)


_DELETEARTIFACT_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='com.mitdbg.artifactstore.DeleteArtifact.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='com.mitdbg.artifactstore.DeleteArtifact.Response.status', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=377,
  serialized_end=403,
)

_DELETEARTIFACT = _descriptor.Descriptor(
  name='DeleteArtifact',
  full_name='com.mitdbg.artifactstore.DeleteArtifact',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='com.mitdbg.artifactstore.DeleteArtifact.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_DELETEARTIFACT_RESPONSE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=346,
  serialized_end=403,
)

_STOREARTIFACT_RESPONSE.containing_type = _STOREARTIFACT
_STOREARTIFACTWITHSTREAM_RESPONSE.containing_type = _STOREARTIFACTWITHSTREAM
_GETARTIFACT_RESPONSE.containing_type = _GETARTIFACT
_DELETEARTIFACT_RESPONSE.containing_type = _DELETEARTIFACT
DESCRIPTOR.message_types_by_name['StoreArtifact'] = _STOREARTIFACT
DESCRIPTOR.message_types_by_name['StoreArtifactWithStream'] = _STOREARTIFACTWITHSTREAM
DESCRIPTOR.message_types_by_name['GetArtifact'] = _GETARTIFACT
DESCRIPTOR.message_types_by_name['DeleteArtifact'] = _DELETEARTIFACT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

StoreArtifact = _reflection.GeneratedProtocolMessageType('StoreArtifact', (_message.Message,), dict(

  Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), dict(
    DESCRIPTOR = _STOREARTIFACT_RESPONSE,
    __module__ = 'ArtifactStore_pb2'
    # @@protoc_insertion_point(class_scope:com.mitdbg.artifactstore.StoreArtifact.Response)
    ))
  ,
  DESCRIPTOR = _STOREARTIFACT,
  __module__ = 'ArtifactStore_pb2'
  # @@protoc_insertion_point(class_scope:com.mitdbg.artifactstore.StoreArtifact)
  ))
_sym_db.RegisterMessage(StoreArtifact)
_sym_db.RegisterMessage(StoreArtifact.Response)

StoreArtifactWithStream = _reflection.GeneratedProtocolMessageType('StoreArtifactWithStream', (_message.Message,), dict(

  Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), dict(
    DESCRIPTOR = _STOREARTIFACTWITHSTREAM_RESPONSE,
    __module__ = 'ArtifactStore_pb2'
    # @@protoc_insertion_point(class_scope:com.mitdbg.artifactstore.StoreArtifactWithStream.Response)
    ))
  ,
  DESCRIPTOR = _STOREARTIFACTWITHSTREAM,
  __module__ = 'ArtifactStore_pb2'
  # @@protoc_insertion_point(class_scope:com.mitdbg.artifactstore.StoreArtifactWithStream)
  ))
_sym_db.RegisterMessage(StoreArtifactWithStream)
_sym_db.RegisterMessage(StoreArtifactWithStream.Response)

GetArtifact = _reflection.GeneratedProtocolMessageType('GetArtifact', (_message.Message,), dict(

  Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), dict(
    DESCRIPTOR = _GETARTIFACT_RESPONSE,
    __module__ = 'ArtifactStore_pb2'
    # @@protoc_insertion_point(class_scope:com.mitdbg.artifactstore.GetArtifact.Response)
    ))
  ,
  DESCRIPTOR = _GETARTIFACT,
  __module__ = 'ArtifactStore_pb2'
  # @@protoc_insertion_point(class_scope:com.mitdbg.artifactstore.GetArtifact)
  ))
_sym_db.RegisterMessage(GetArtifact)
_sym_db.RegisterMessage(GetArtifact.Response)

DeleteArtifact = _reflection.GeneratedProtocolMessageType('DeleteArtifact', (_message.Message,), dict(

  Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), dict(
    DESCRIPTOR = _DELETEARTIFACT_RESPONSE,
    __module__ = 'ArtifactStore_pb2'
    # @@protoc_insertion_point(class_scope:com.mitdbg.artifactstore.DeleteArtifact.Response)
    ))
  ,
  DESCRIPTOR = _DELETEARTIFACT,
  __module__ = 'ArtifactStore_pb2'
  # @@protoc_insertion_point(class_scope:com.mitdbg.artifactstore.DeleteArtifact)
  ))
_sym_db.RegisterMessage(DeleteArtifact)
_sym_db.RegisterMessage(DeleteArtifact.Response)


DESCRIPTOR._options = None

_ARTIFACTSTORE = _descriptor.ServiceDescriptor(
  name='ArtifactStore',
  full_name='com.mitdbg.artifactstore.ArtifactStore',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=406,
  serialized_end=881,
  methods=[
  _descriptor.MethodDescriptor(
    name='storeArtifact',
    full_name='com.mitdbg.artifactstore.ArtifactStore.storeArtifact',
    index=0,
    containing_service=None,
    input_type=_STOREARTIFACT,
    output_type=_STOREARTIFACT_RESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='storeArtifactWithStream',
    full_name='com.mitdbg.artifactstore.ArtifactStore.storeArtifactWithStream',
    index=1,
    containing_service=None,
    input_type=_STOREARTIFACTWITHSTREAM,
    output_type=_STOREARTIFACTWITHSTREAM_RESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='getArtifact',
    full_name='com.mitdbg.artifactstore.ArtifactStore.getArtifact',
    index=2,
    containing_service=None,
    input_type=_GETARTIFACT,
    output_type=_GETARTIFACT_RESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='deleteArtifact',
    full_name='com.mitdbg.artifactstore.ArtifactStore.deleteArtifact',
    index=3,
    containing_service=None,
    input_type=_DELETEARTIFACT,
    output_type=_DELETEARTIFACT_RESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_ARTIFACTSTORE)

DESCRIPTOR.services_by_name['ArtifactStore'] = _ARTIFACTSTORE

# @@protoc_insertion_point(module_scope)