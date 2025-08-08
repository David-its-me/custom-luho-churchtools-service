import basicTypes_pb2 as _basicTypes_pb2
import hotKey_pb2 as _hotKey_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Group(_message.Message):
    __slots__ = ("uuid", "name", "color", "hotKey", "application_group_identifier", "application_group_name")
    UUID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    HOTKEY_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_GROUP_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    uuid: _basicTypes_pb2.UUID
    name: str
    color: _basicTypes_pb2.Color
    hotKey: _hotKey_pb2.HotKey
    application_group_identifier: _basicTypes_pb2.UUID
    application_group_name: str
    def __init__(self, uuid: _Optional[_Union[_basicTypes_pb2.UUID, _Mapping]] = ..., name: _Optional[str] = ..., color: _Optional[_Union[_basicTypes_pb2.Color, _Mapping]] = ..., hotKey: _Optional[_Union[_hotKey_pb2.HotKey, _Mapping]] = ..., application_group_identifier: _Optional[_Union[_basicTypes_pb2.UUID, _Mapping]] = ..., application_group_name: _Optional[str] = ...) -> None: ...

class ProGroupsDocument(_message.Message):
    __slots__ = ("groups",)
    GROUPS_FIELD_NUMBER: _ClassVar[int]
    groups: _containers.RepeatedCompositeFieldContainer[Group]
    def __init__(self, groups: _Optional[_Iterable[_Union[Group, _Mapping]]] = ...) -> None: ...
