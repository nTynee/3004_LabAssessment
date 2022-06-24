# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: safeentry.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0fsafeentry.proto\x12\tSafeEntry\"\x1a\n\x07Request\x12\x0f\n\x07message\x18\x01 \x01(\t\"\x18\n\x05Reply\x12\x0f\n\x07message\x18\x01 \x01(\t\"\x1c\n\nStatusInfo\x12\x0e\n\x06status\x18\x01 \x01(\t\"y\n\x0eStatusResponse\x12\x39\n\x06status\x18\x01 \x01(\x0e\x32).SafeEntry.StatusResponse.SafeEntryStatus\",\n\x0fSafeEntryStatus\x12\x0b\n\x07\x43HECKIN\x10\x00\x12\x0c\n\x08\x43HECKOUT\x10\x01\"\x1b\n\x0bNRICRequest\x12\x0c\n\x04nric\x18\x01 \x01(\t\"@\n\x0c\x43heckRequest\x12\x0c\n\x04nric\x18\x01 \x03(\t\x12\x10\n\x08location\x18\x02 \x01(\t\x12\x10\n\x08\x64\x61tetime\x18\x03 \x01(\t\"\x1f\n\rCheckResponse\x12\x0e\n\x06status\x18\x01 \x01(\x08\"E\n\x11get_location_data\x12\x10\n\x08location\x18\x01 \x01(\t\x12\x0c\n\x04nric\x18\x02 \x01(\t\x12\x10\n\x08\x64\x61tetime\x18\x03 \x01(\t\"\x1c\n\x08location\x12\x10\n\x08response\x18\x01 \x03(\t\" \n\x10get_user_history\x12\x0c\n\x04nric\x18\x01 \x01(\t\"D\n\rHistoryRecord\x12\x10\n\x08location\x18\x01 \x01(\t\x12\x0f\n\x07\x63heckin\x18\x02 \x01(\t\x12\x10\n\x08\x63heckout\x18\x03 \x01(\t\"<\n\x0ehistory_record\x12*\n\x08response\x18\x01 \x03(\x0b\x32\x18.SafeEntry.HistoryRecord\"H\n\x0cget_password\x12\x14\n\x0cold_password\x18\x01 \x01(\t\x12\x14\n\x0cnew_password\x18\x02 \x01(\t\x12\x0c\n\x04nric\x18\x03 \x01(\t\"\x1c\n\x08password\x12\x10\n\x08response\x18\x01 \x01(\t\"1\n\x10get_notification\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x0c\n\x04nric\x18\x02 \x01(\t\"\x1c\n\tnoti_info\x12\x0f\n\x07message\x18\x01 \x01(\t\"\"\n\x0f\x44\x65\x63larationInfo\x12\x0f\n\x07message\x18\x01 \x01(\t\"\x07\n\x05\x45mpty\"F\n\x08UserInfo\x12\x0c\n\x04nric\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x10\n\x08password\x18\x03 \x01(\t\x12\x0c\n\x04role\x18\x04 \x01(\x05\"1\n\x0cUserInfoDict\x12!\n\x04info\x18\x01 \x03(\x0b\x32\x13.SafeEntry.UserInfo2\xb3\x02\n\tSafeEntry\x12\x31\n\x07Message\x12\x12.SafeEntry.Request\x1a\x10.SafeEntry.Reply\"\x00\x12\x35\n\x05Login\x12\x13.SafeEntry.UserInfo\x1a\x15.SafeEntry.StatusInfo\"\x00\x12>\n\x07\x43heckIn\x12\x17.SafeEntry.CheckRequest\x1a\x18.SafeEntry.CheckResponse\"\x00\x12?\n\x08\x43heckOut\x12\x17.SafeEntry.CheckRequest\x1a\x18.SafeEntry.CheckResponse\"\x00\x12;\n\x05\x43heck\x12\x15.SafeEntry.StatusInfo\x1a\x19.SafeEntry.StatusResponse\"\x00\x32\xa4\x01\n\x0cLocationData\x12\x46\n\x0f\x44\x65\x63lareLocation\x12\x1c.SafeEntry.get_location_data\x1a\x13.SafeEntry.location\"\x00\x12L\n\x10GetHistoryRecord\x12\x1b.SafeEntry.get_user_history\x1a\x19.SafeEntry.history_record\"\x00\x32R\n\x0ePaswordSetting\x12@\n\x0e\x43hangePassword\x12\x17.SafeEntry.get_password\x1a\x13.SafeEntry.password\"\x00\x32\x9a\x01\n\x0cNotification\x12\x44\n\x10SendNotification\x12\x10.SafeEntry.Empty\x1a\x1a.SafeEntry.DeclarationInfo\"\x00\x30\x01\x12\x44\n\x12ReceiveDeclaration\x12\x1a.SafeEntry.DeclarationInfo\x1a\x10.SafeEntry.Empty\"\x00\x62\x06proto3')



_REQUEST = DESCRIPTOR.message_types_by_name['Request']
_REPLY = DESCRIPTOR.message_types_by_name['Reply']
_STATUSINFO = DESCRIPTOR.message_types_by_name['StatusInfo']
_STATUSRESPONSE = DESCRIPTOR.message_types_by_name['StatusResponse']
_NRICREQUEST = DESCRIPTOR.message_types_by_name['NRICRequest']
_CHECKREQUEST = DESCRIPTOR.message_types_by_name['CheckRequest']
_CHECKRESPONSE = DESCRIPTOR.message_types_by_name['CheckResponse']
_GET_LOCATION_DATA = DESCRIPTOR.message_types_by_name['get_location_data']
_LOCATION = DESCRIPTOR.message_types_by_name['location']
_GET_USER_HISTORY = DESCRIPTOR.message_types_by_name['get_user_history']
_HISTORYRECORD = DESCRIPTOR.message_types_by_name['HistoryRecord']
_HISTORY_RECORD = DESCRIPTOR.message_types_by_name['history_record']
_GET_PASSWORD = DESCRIPTOR.message_types_by_name['get_password']
_PASSWORD = DESCRIPTOR.message_types_by_name['password']
_GET_NOTIFICATION = DESCRIPTOR.message_types_by_name['get_notification']
_NOTI_INFO = DESCRIPTOR.message_types_by_name['noti_info']
_DECLARATIONINFO = DESCRIPTOR.message_types_by_name['DeclarationInfo']
_EMPTY = DESCRIPTOR.message_types_by_name['Empty']
_USERINFO = DESCRIPTOR.message_types_by_name['UserInfo']
_USERINFODICT = DESCRIPTOR.message_types_by_name['UserInfoDict']
_STATUSRESPONSE_SAFEENTRYSTATUS = _STATUSRESPONSE.enum_types_by_name['SafeEntryStatus']
Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), {
  'DESCRIPTOR' : _REQUEST,
  '__module__' : 'safeentry_pb2'
  # @@protoc_insertion_point(class_scope:SafeEntry.Request)
  })
_sym_db.RegisterMessage(Request)

Reply = _reflection.GeneratedProtocolMessageType('Reply', (_message.Message,), {
  'DESCRIPTOR' : _REPLY,
  '__module__' : 'safeentry_pb2'
  # @@protoc_insertion_point(class_scope:SafeEntry.Reply)
  })
_sym_db.RegisterMessage(Reply)

StatusInfo = _reflection.GeneratedProtocolMessageType('StatusInfo', (_message.Message,), {
  'DESCRIPTOR' : _STATUSINFO,
  '__module__' : 'safeentry_pb2'
  # @@protoc_insertion_point(class_scope:SafeEntry.StatusInfo)
  })
_sym_db.RegisterMessage(StatusInfo)

StatusResponse = _reflection.GeneratedProtocolMessageType('StatusResponse', (_message.Message,), {
  'DESCRIPTOR' : _STATUSRESPONSE,
  '__module__' : 'safeentry_pb2'
  # @@protoc_insertion_point(class_scope:SafeEntry.StatusResponse)
  })
_sym_db.RegisterMessage(StatusResponse)

NRICRequest = _reflection.GeneratedProtocolMessageType('NRICRequest', (_message.Message,), {
  'DESCRIPTOR' : _NRICREQUEST,
  '__module__' : 'safeentry_pb2'
  # @@protoc_insertion_point(class_scope:SafeEntry.NRICRequest)
  })
_sym_db.RegisterMessage(NRICRequest)

CheckRequest = _reflection.GeneratedProtocolMessageType('CheckRequest', (_message.Message,), {
  'DESCRIPTOR' : _CHECKREQUEST,
  '__module__' : 'safeentry_pb2'
  # @@protoc_insertion_point(class_scope:SafeEntry.CheckRequest)
  })
_sym_db.RegisterMessage(CheckRequest)

CheckResponse = _reflection.GeneratedProtocolMessageType('CheckResponse', (_message.Message,), {
  'DESCRIPTOR' : _CHECKRESPONSE,
  '__module__' : 'safeentry_pb2'
  # @@protoc_insertion_point(class_scope:SafeEntry.CheckResponse)
  })
_sym_db.RegisterMessage(CheckResponse)

get_location_data = _reflection.GeneratedProtocolMessageType('get_location_data', (_message.Message,), {
  'DESCRIPTOR' : _GET_LOCATION_DATA,
  '__module__' : 'safeentry_pb2'
  # @@protoc_insertion_point(class_scope:SafeEntry.get_location_data)
  })
_sym_db.RegisterMessage(get_location_data)

location = _reflection.GeneratedProtocolMessageType('location', (_message.Message,), {
  'DESCRIPTOR' : _LOCATION,
  '__module__' : 'safeentry_pb2'
  # @@protoc_insertion_point(class_scope:SafeEntry.location)
  })
_sym_db.RegisterMessage(location)

get_user_history = _reflection.GeneratedProtocolMessageType('get_user_history', (_message.Message,), {
  'DESCRIPTOR' : _GET_USER_HISTORY,
  '__module__' : 'safeentry_pb2'
  # @@protoc_insertion_point(class_scope:SafeEntry.get_user_history)
  })
_sym_db.RegisterMessage(get_user_history)

HistoryRecord = _reflection.GeneratedProtocolMessageType('HistoryRecord', (_message.Message,), {
  'DESCRIPTOR' : _HISTORYRECORD,
  '__module__' : 'safeentry_pb2'
  # @@protoc_insertion_point(class_scope:SafeEntry.HistoryRecord)
  })
_sym_db.RegisterMessage(HistoryRecord)

history_record = _reflection.GeneratedProtocolMessageType('history_record', (_message.Message,), {
  'DESCRIPTOR' : _HISTORY_RECORD,
  '__module__' : 'safeentry_pb2'
  # @@protoc_insertion_point(class_scope:SafeEntry.history_record)
  })
_sym_db.RegisterMessage(history_record)

get_password = _reflection.GeneratedProtocolMessageType('get_password', (_message.Message,), {
  'DESCRIPTOR' : _GET_PASSWORD,
  '__module__' : 'safeentry_pb2'
  # @@protoc_insertion_point(class_scope:SafeEntry.get_password)
  })
_sym_db.RegisterMessage(get_password)

password = _reflection.GeneratedProtocolMessageType('password', (_message.Message,), {
  'DESCRIPTOR' : _PASSWORD,
  '__module__' : 'safeentry_pb2'
  # @@protoc_insertion_point(class_scope:SafeEntry.password)
  })
_sym_db.RegisterMessage(password)

get_notification = _reflection.GeneratedProtocolMessageType('get_notification', (_message.Message,), {
  'DESCRIPTOR' : _GET_NOTIFICATION,
  '__module__' : 'safeentry_pb2'
  # @@protoc_insertion_point(class_scope:SafeEntry.get_notification)
  })
_sym_db.RegisterMessage(get_notification)

noti_info = _reflection.GeneratedProtocolMessageType('noti_info', (_message.Message,), {
  'DESCRIPTOR' : _NOTI_INFO,
  '__module__' : 'safeentry_pb2'
  # @@protoc_insertion_point(class_scope:SafeEntry.noti_info)
  })
_sym_db.RegisterMessage(noti_info)

DeclarationInfo = _reflection.GeneratedProtocolMessageType('DeclarationInfo', (_message.Message,), {
  'DESCRIPTOR' : _DECLARATIONINFO,
  '__module__' : 'safeentry_pb2'
  # @@protoc_insertion_point(class_scope:SafeEntry.DeclarationInfo)
  })
_sym_db.RegisterMessage(DeclarationInfo)

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), {
  'DESCRIPTOR' : _EMPTY,
  '__module__' : 'safeentry_pb2'
  # @@protoc_insertion_point(class_scope:SafeEntry.Empty)
  })
_sym_db.RegisterMessage(Empty)

UserInfo = _reflection.GeneratedProtocolMessageType('UserInfo', (_message.Message,), {
  'DESCRIPTOR' : _USERINFO,
  '__module__' : 'safeentry_pb2'
  # @@protoc_insertion_point(class_scope:SafeEntry.UserInfo)
  })
_sym_db.RegisterMessage(UserInfo)

UserInfoDict = _reflection.GeneratedProtocolMessageType('UserInfoDict', (_message.Message,), {
  'DESCRIPTOR' : _USERINFODICT,
  '__module__' : 'safeentry_pb2'
  # @@protoc_insertion_point(class_scope:SafeEntry.UserInfoDict)
  })
_sym_db.RegisterMessage(UserInfoDict)

_SAFEENTRY = DESCRIPTOR.services_by_name['SafeEntry']
_LOCATIONDATA = DESCRIPTOR.services_by_name['LocationData']
_PASWORDSETTING = DESCRIPTOR.services_by_name['PaswordSetting']
_NOTIFICATION = DESCRIPTOR.services_by_name['Notification']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _REQUEST._serialized_start=30
  _REQUEST._serialized_end=56
  _REPLY._serialized_start=58
  _REPLY._serialized_end=82
  _STATUSINFO._serialized_start=84
  _STATUSINFO._serialized_end=112
  _STATUSRESPONSE._serialized_start=114
  _STATUSRESPONSE._serialized_end=235
  _STATUSRESPONSE_SAFEENTRYSTATUS._serialized_start=191
  _STATUSRESPONSE_SAFEENTRYSTATUS._serialized_end=235
  _NRICREQUEST._serialized_start=237
  _NRICREQUEST._serialized_end=264
  _CHECKREQUEST._serialized_start=266
  _CHECKREQUEST._serialized_end=330
  _CHECKRESPONSE._serialized_start=332
  _CHECKRESPONSE._serialized_end=363
  _GET_LOCATION_DATA._serialized_start=365
  _GET_LOCATION_DATA._serialized_end=434
  _LOCATION._serialized_start=436
  _LOCATION._serialized_end=464
  _GET_USER_HISTORY._serialized_start=466
  _GET_USER_HISTORY._serialized_end=498
  _HISTORYRECORD._serialized_start=500
  _HISTORYRECORD._serialized_end=568
  _HISTORY_RECORD._serialized_start=570
  _HISTORY_RECORD._serialized_end=630
  _GET_PASSWORD._serialized_start=632
  _GET_PASSWORD._serialized_end=704
  _PASSWORD._serialized_start=706
  _PASSWORD._serialized_end=734
  _GET_NOTIFICATION._serialized_start=736
  _GET_NOTIFICATION._serialized_end=785
  _NOTI_INFO._serialized_start=787
  _NOTI_INFO._serialized_end=815
  _DECLARATIONINFO._serialized_start=817
  _DECLARATIONINFO._serialized_end=851
  _EMPTY._serialized_start=853
  _EMPTY._serialized_end=860
  _USERINFO._serialized_start=862
  _USERINFO._serialized_end=932
  _USERINFODICT._serialized_start=934
  _USERINFODICT._serialized_end=983
  _SAFEENTRY._serialized_start=986
  _SAFEENTRY._serialized_end=1293
  _LOCATIONDATA._serialized_start=1296
  _LOCATIONDATA._serialized_end=1460
  _PASWORDSETTING._serialized_start=1462
  _PASWORDSETTING._serialized_end=1544
  _NOTIFICATION._serialized_start=1547
  _NOTIFICATION._serialized_end=1701
# @@protoc_insertion_point(module_scope)
