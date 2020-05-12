# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flyteidl/plugins/raw_container.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='flyteidl/plugins/raw_container.proto',
  package='flyteidl.plugins',
  syntax='proto3',
  serialized_options=_b('Z3github.com/lyft/flyteidl/gen/pb-go/flyteidl/plugins'),
  serialized_pb=_b('\n$flyteidl/plugins/raw_container.proto\x12\x10\x66lyteidl.plugins\"\x9d\x01\n\x07\x43oPilot\x12\x12\n\ninput_path\x18\x01 \x01(\t\x12\x13\n\x0boutput_path\x18\x02 \x01(\t\x12\x38\n\x06\x66ormat\x18\x03 \x01(\x0e\x32(.flyteidl.plugins.CoPilot.MetadataFormat\"/\n\x0eMetadataFormat\x12\x08\n\x04JSON\x10\x00\x12\x08\n\x04YAML\x10\x01\x12\t\n\x05PROTO\x10\x02\x42\x35Z3github.com/lyft/flyteidl/gen/pb-go/flyteidl/pluginsb\x06proto3')
)



_COPILOT_METADATAFORMAT = _descriptor.EnumDescriptor(
  name='MetadataFormat',
  full_name='flyteidl.plugins.CoPilot.MetadataFormat',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='JSON', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='YAML', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROTO', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=169,
  serialized_end=216,
)
_sym_db.RegisterEnumDescriptor(_COPILOT_METADATAFORMAT)


_COPILOT = _descriptor.Descriptor(
  name='CoPilot',
  full_name='flyteidl.plugins.CoPilot',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='input_path', full_name='flyteidl.plugins.CoPilot.input_path', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='output_path', full_name='flyteidl.plugins.CoPilot.output_path', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='format', full_name='flyteidl.plugins.CoPilot.format', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _COPILOT_METADATAFORMAT,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=59,
  serialized_end=216,
)

_COPILOT.fields_by_name['format'].enum_type = _COPILOT_METADATAFORMAT
_COPILOT_METADATAFORMAT.containing_type = _COPILOT
DESCRIPTOR.message_types_by_name['CoPilot'] = _COPILOT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CoPilot = _reflection.GeneratedProtocolMessageType('CoPilot', (_message.Message,), dict(
  DESCRIPTOR = _COPILOT,
  __module__ = 'flyteidl.plugins.raw_container_pb2'
  # @@protoc_insertion_point(class_scope:flyteidl.plugins.CoPilot)
  ))
_sym_db.RegisterMessage(CoPilot)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
