import basicTypes_pb2 as _basicTypes_pb2
import action_pb2 as _action_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MacrosDocument(_message.Message):
    __slots__ = ("application_info", "macros")
    class Macro(_message.Message):
        __slots__ = ("uuid", "name", "color", "actions", "trigger_on_startup")
        UUID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        COLOR_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        TRIGGER_ON_STARTUP_FIELD_NUMBER: _ClassVar[int]
        uuid: _basicTypes_pb2.UUID
        name: str
        color: _basicTypes_pb2.Color
        actions: _containers.RepeatedCompositeFieldContainer[_action_pb2.Action]
        trigger_on_startup: bool
        def __init__(self, uuid: _Optional[_Union[_basicTypes_pb2.UUID, _Mapping]] = ..., name: _Optional[str] = ..., color: _Optional[_Union[_basicTypes_pb2.Color, _Mapping]] = ..., actions: _Optional[_Iterable[_Union[_action_pb2.Action, _Mapping]]] = ..., trigger_on_startup: bool = ...) -> None: ...
    APPLICATION_INFO_FIELD_NUMBER: _ClassVar[int]
    MACROS_FIELD_NUMBER: _ClassVar[int]
    application_info: _basicTypes_pb2.ApplicationInfo
    macros: _containers.RepeatedCompositeFieldContainer[MacrosDocument.Macro]
    def __init__(self, application_info: _Optional[_Union[_basicTypes_pb2.ApplicationInfo, _Mapping]] = ..., macros: _Optional[_Iterable[_Union[MacrosDocument.Macro, _Mapping]]] = ...) -> None: ...
