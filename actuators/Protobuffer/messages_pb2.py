# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: messages.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='messages.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0emessages.proto\x1a\x1bgoogle/protobuf/empty.proto\"(\n\x0b\x46\x65tchStatus\x12\x19\n\x04type\x18\x01 \x01(\x0e\x32\x0b.StatusType\"\x14\n\x06Killed\x12\n\n\x02id\x18\x01 \x01(\t\"\x13\n\x02Id\x12\r\n\x05value\x18\x01 \x01(\t\"w\n\x0eIdentification\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x1c\n\x04type\x18\x02 \x01(\x0e\x32\x0e.EquipmentType\x12\n\n\x02ip\x18\x03 \x01(\t\x12\x0c\n\x04port\x18\x04 \x01(\x05\x12\x1f\n\x08\x61\x63t_type\x18\x05 \x01(\x0e\x32\r.ActuatorType\"@\n\x06Status\x12\x19\n\x04type\x18\x01 \x01(\x0e\x32\x0b.StatusType\x12\x0f\n\x07payload\x18\x02 \x01(\x01\x12\n\n\x02id\x18\x03 \x01(\t\":\n\x0cUpdateStatus\x12\x19\n\x04type\x18\t \x01(\x0e\x32\x0b.StatusType\x12\x0f\n\x07payload\x18\n \x01(\x01*3\n\rEquipmentType\x12\x08\n\x04\x42OTH\x10\x00\x12\n\n\x06SENSOR\x10\x01\x12\x0c\n\x08\x41\x43TUATOR\x10\x02*2\n\x0c\x41\x63tuatorType\x12\x06\n\x02\x41r\x10\x00\x12\x0b\n\x07Lampada\x10\x01\x12\r\n\tSprinkler\x10\x02*C\n\nStatusType\x12\x0f\n\x0bTURN_ON_OFF\x10\x00\x12\x0f\n\x0bTEMPERATURE\x10\x01\x12\x13\n\x0f\x45NV_TEMPERATURE\x10\x02\x32\x87\x01\n\x0eGatewayService\x12$\n\x0cIdentificate\x12\x0f.Identification\x1a\x03.Id\x12!\n\rReceiveStatus\x12\x07.Status\x1a\x07.Status\x12,\n\rEquipmentDied\x12\x03.Id\x1a\x16.google.protobuf.Empty2\xa7\x01\n\x10\x45quipmentService\x12\x37\n\x0cIdentificate\x12\x16.google.protobuf.Empty\x1a\x0f.Identification\x12\x36\n\rReceiveUpdate\x12\r.UpdateStatus\x1a\x16.google.protobuf.Empty\x12\"\n\tGetStatus\x12\x0c.FetchStatus\x1a\x07.Statusb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])

_EQUIPMENTTYPE = _descriptor.EnumDescriptor(
  name='EquipmentType',
  full_name='EquipmentType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='BOTH', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SENSOR', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ACTUATOR', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=379,
  serialized_end=430,
)
_sym_db.RegisterEnumDescriptor(_EQUIPMENTTYPE)

EquipmentType = enum_type_wrapper.EnumTypeWrapper(_EQUIPMENTTYPE)
_ACTUATORTYPE = _descriptor.EnumDescriptor(
  name='ActuatorType',
  full_name='ActuatorType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Ar', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='Lampada', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='Sprinkler', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=432,
  serialized_end=482,
)
_sym_db.RegisterEnumDescriptor(_ACTUATORTYPE)

ActuatorType = enum_type_wrapper.EnumTypeWrapper(_ACTUATORTYPE)
_STATUSTYPE = _descriptor.EnumDescriptor(
  name='StatusType',
  full_name='StatusType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='TURN_ON_OFF', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TEMPERATURE', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ENV_TEMPERATURE', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=484,
  serialized_end=551,
)
_sym_db.RegisterEnumDescriptor(_STATUSTYPE)

StatusType = enum_type_wrapper.EnumTypeWrapper(_STATUSTYPE)
BOTH = 0
SENSOR = 1
ACTUATOR = 2
Ar = 0
Lampada = 1
Sprinkler = 2
TURN_ON_OFF = 0
TEMPERATURE = 1
ENV_TEMPERATURE = 2



_FETCHSTATUS = _descriptor.Descriptor(
  name='FetchStatus',
  full_name='FetchStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='FetchStatus.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
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
  serialized_start=47,
  serialized_end=87,
)


_KILLED = _descriptor.Descriptor(
  name='Killed',
  full_name='Killed',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Killed.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=89,
  serialized_end=109,
)


_ID = _descriptor.Descriptor(
  name='Id',
  full_name='Id',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='Id.value', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=111,
  serialized_end=130,
)


_IDENTIFICATION = _descriptor.Descriptor(
  name='Identification',
  full_name='Identification',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='Identification.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='Identification.type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ip', full_name='Identification.ip', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='port', full_name='Identification.port', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='act_type', full_name='Identification.act_type', index=4,
      number=5, type=14, cpp_type=8, label=1,
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
  serialized_start=132,
  serialized_end=251,
)


_STATUS = _descriptor.Descriptor(
  name='Status',
  full_name='Status',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='Status.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='payload', full_name='Status.payload', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='id', full_name='Status.id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=253,
  serialized_end=317,
)


_UPDATESTATUS = _descriptor.Descriptor(
  name='UpdateStatus',
  full_name='UpdateStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='UpdateStatus.type', index=0,
      number=9, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='payload', full_name='UpdateStatus.payload', index=1,
      number=10, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=319,
  serialized_end=377,
)

_FETCHSTATUS.fields_by_name['type'].enum_type = _STATUSTYPE
_IDENTIFICATION.fields_by_name['type'].enum_type = _EQUIPMENTTYPE
_IDENTIFICATION.fields_by_name['act_type'].enum_type = _ACTUATORTYPE
_STATUS.fields_by_name['type'].enum_type = _STATUSTYPE
_UPDATESTATUS.fields_by_name['type'].enum_type = _STATUSTYPE
DESCRIPTOR.message_types_by_name['FetchStatus'] = _FETCHSTATUS
DESCRIPTOR.message_types_by_name['Killed'] = _KILLED
DESCRIPTOR.message_types_by_name['Id'] = _ID
DESCRIPTOR.message_types_by_name['Identification'] = _IDENTIFICATION
DESCRIPTOR.message_types_by_name['Status'] = _STATUS
DESCRIPTOR.message_types_by_name['UpdateStatus'] = _UPDATESTATUS
DESCRIPTOR.enum_types_by_name['EquipmentType'] = _EQUIPMENTTYPE
DESCRIPTOR.enum_types_by_name['ActuatorType'] = _ACTUATORTYPE
DESCRIPTOR.enum_types_by_name['StatusType'] = _STATUSTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FetchStatus = _reflection.GeneratedProtocolMessageType('FetchStatus', (_message.Message,), {
  'DESCRIPTOR' : _FETCHSTATUS,
  '__module__' : 'messages_pb2'
  # @@protoc_insertion_point(class_scope:FetchStatus)
  })
_sym_db.RegisterMessage(FetchStatus)

Killed = _reflection.GeneratedProtocolMessageType('Killed', (_message.Message,), {
  'DESCRIPTOR' : _KILLED,
  '__module__' : 'messages_pb2'
  # @@protoc_insertion_point(class_scope:Killed)
  })
_sym_db.RegisterMessage(Killed)

Id = _reflection.GeneratedProtocolMessageType('Id', (_message.Message,), {
  'DESCRIPTOR' : _ID,
  '__module__' : 'messages_pb2'
  # @@protoc_insertion_point(class_scope:Id)
  })
_sym_db.RegisterMessage(Id)

Identification = _reflection.GeneratedProtocolMessageType('Identification', (_message.Message,), {
  'DESCRIPTOR' : _IDENTIFICATION,
  '__module__' : 'messages_pb2'
  # @@protoc_insertion_point(class_scope:Identification)
  })
_sym_db.RegisterMessage(Identification)

Status = _reflection.GeneratedProtocolMessageType('Status', (_message.Message,), {
  'DESCRIPTOR' : _STATUS,
  '__module__' : 'messages_pb2'
  # @@protoc_insertion_point(class_scope:Status)
  })
_sym_db.RegisterMessage(Status)

UpdateStatus = _reflection.GeneratedProtocolMessageType('UpdateStatus', (_message.Message,), {
  'DESCRIPTOR' : _UPDATESTATUS,
  '__module__' : 'messages_pb2'
  # @@protoc_insertion_point(class_scope:UpdateStatus)
  })
_sym_db.RegisterMessage(UpdateStatus)



_GATEWAYSERVICE = _descriptor.ServiceDescriptor(
  name='GatewayService',
  full_name='GatewayService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=554,
  serialized_end=689,
  methods=[
  _descriptor.MethodDescriptor(
    name='Identificate',
    full_name='GatewayService.Identificate',
    index=0,
    containing_service=None,
    input_type=_IDENTIFICATION,
    output_type=_ID,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ReceiveStatus',
    full_name='GatewayService.ReceiveStatus',
    index=1,
    containing_service=None,
    input_type=_STATUS,
    output_type=_STATUS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='EquipmentDied',
    full_name='GatewayService.EquipmentDied',
    index=2,
    containing_service=None,
    input_type=_ID,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_GATEWAYSERVICE)

DESCRIPTOR.services_by_name['GatewayService'] = _GATEWAYSERVICE


_EQUIPMENTSERVICE = _descriptor.ServiceDescriptor(
  name='EquipmentService',
  full_name='EquipmentService',
  file=DESCRIPTOR,
  index=1,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=692,
  serialized_end=859,
  methods=[
  _descriptor.MethodDescriptor(
    name='Identificate',
    full_name='EquipmentService.Identificate',
    index=0,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=_IDENTIFICATION,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ReceiveUpdate',
    full_name='EquipmentService.ReceiveUpdate',
    index=1,
    containing_service=None,
    input_type=_UPDATESTATUS,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetStatus',
    full_name='EquipmentService.GetStatus',
    index=2,
    containing_service=None,
    input_type=_FETCHSTATUS,
    output_type=_STATUS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_EQUIPMENTSERVICE)

DESCRIPTOR.services_by_name['EquipmentService'] = _EQUIPMENTSERVICE

# @@protoc_insertion_point(module_scope)