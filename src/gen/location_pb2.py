# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: location.proto
# Protobuf Python Version: 4.25.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0elocation.proto\"\x89\x02\n\x08location\x12\x10\n\x08utc_time\x18\x01 \x01(\x01\x12\x10\n\x08latitude\x18\x02 \x01(\t\x12\x15\n\rlat_direction\x18\x03 \x01(\t\x12\x11\n\tlongitude\x18\x04 \x01(\t\x12\x15\n\rlon_direction\x18\x05 \x01(\t\x12\x0f\n\x07quality\x18\x06 \x01(\x05\x12\x10\n\x08num_sats\x18\x07 \x01(\x05\x12\x0c\n\x04hdop\x18\x08 \x01(\x01\x12\x10\n\x08\x61ltitude\x18\t \x01(\x01\x12\x11\n\talt_units\x18\n \x01(\t\x12\x12\n\nundulation\x18\x0b \x01(\x01\x12\x11\n\tund_units\x18\x0c \x01(\t\x12\x0b\n\x03\x61ge\x18\r \x01(\x01\x12\x0e\n\x06stn_id\x18\x0e \x01(\tb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'location_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_LOCATION']._serialized_start=19
  _globals['_LOCATION']._serialized_end=284
# @@protoc_insertion_point(module_scope)
