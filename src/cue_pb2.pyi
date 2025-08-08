import basicTypes_pb2 as _basicTypes_pb2
import hotKey_pb2 as _hotKey_pb2
import action_pb2 as _action_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Cue(_message.Message):
    __slots__ = ("uuid", "name", "completion_target_type", "completion_target_uuid", "completion_action_type", "completion_action_uuid", "trigger_time", "hot_key", "actions", "pending_imports", "isEnabled", "completion_time")
    class CompletionTargetType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        COMPLETION_TARGET_TYPE_NONE: _ClassVar[Cue.CompletionTargetType]
        COMPLETION_TARGET_TYPE_NEXT: _ClassVar[Cue.CompletionTargetType]
        COMPLETION_TARGET_TYPE_RANDOM: _ClassVar[Cue.CompletionTargetType]
        COMPLETION_TARGET_TYPE_CUE: _ClassVar[Cue.CompletionTargetType]
        COMPLETION_TARGET_TYPE_FIRST: _ClassVar[Cue.CompletionTargetType]
    COMPLETION_TARGET_TYPE_NONE: Cue.CompletionTargetType
    COMPLETION_TARGET_TYPE_NEXT: Cue.CompletionTargetType
    COMPLETION_TARGET_TYPE_RANDOM: Cue.CompletionTargetType
    COMPLETION_TARGET_TYPE_CUE: Cue.CompletionTargetType
    COMPLETION_TARGET_TYPE_FIRST: Cue.CompletionTargetType
    class CompletionActionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        COMPLETION_ACTION_TYPE_FIRST: _ClassVar[Cue.CompletionActionType]
        COMPLETION_ACTION_TYPE_LAST: _ClassVar[Cue.CompletionActionType]
        COMPLETION_ACTION_TYPE_AFTER_ACTION: _ClassVar[Cue.CompletionActionType]
        COMPLETION_ACTION_TYPE_AFTER_TIME: _ClassVar[Cue.CompletionActionType]
    COMPLETION_ACTION_TYPE_FIRST: Cue.CompletionActionType
    COMPLETION_ACTION_TYPE_LAST: Cue.CompletionActionType
    COMPLETION_ACTION_TYPE_AFTER_ACTION: Cue.CompletionActionType
    COMPLETION_ACTION_TYPE_AFTER_TIME: Cue.CompletionActionType
    class TimecodeTime(_message.Message):
        __slots__ = ("time",)
        TIME_FIELD_NUMBER: _ClassVar[int]
        time: float
        def __init__(self, time: _Optional[float] = ...) -> None: ...
    class PendingImportsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _basicTypes_pb2.URLs
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_basicTypes_pb2.URLs, _Mapping]] = ...) -> None: ...
    UUID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    COMPLETION_TARGET_TYPE_FIELD_NUMBER: _ClassVar[int]
    COMPLETION_TARGET_UUID_FIELD_NUMBER: _ClassVar[int]
    COMPLETION_ACTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    COMPLETION_ACTION_UUID_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_TIME_FIELD_NUMBER: _ClassVar[int]
    HOT_KEY_FIELD_NUMBER: _ClassVar[int]
    ACTIONS_FIELD_NUMBER: _ClassVar[int]
    PENDING_IMPORTS_FIELD_NUMBER: _ClassVar[int]
    ISENABLED_FIELD_NUMBER: _ClassVar[int]
    COMPLETION_TIME_FIELD_NUMBER: _ClassVar[int]
    uuid: _basicTypes_pb2.UUID
    name: str
    completion_target_type: Cue.CompletionTargetType
    completion_target_uuid: _basicTypes_pb2.UUID
    completion_action_type: Cue.CompletionActionType
    completion_action_uuid: _basicTypes_pb2.UUID
    trigger_time: Cue.TimecodeTime
    hot_key: _hotKey_pb2.HotKey
    actions: _containers.RepeatedCompositeFieldContainer[_action_pb2.Action]
    pending_imports: _containers.RepeatedCompositeFieldContainer[Cue.PendingImportsEntry]
    isEnabled: bool
    completion_time: float
    def __init__(self, uuid: _Optional[_Union[_basicTypes_pb2.UUID, _Mapping]] = ..., name: _Optional[str] = ..., completion_target_type: _Optional[_Union[Cue.CompletionTargetType, str]] = ..., completion_target_uuid: _Optional[_Union[_basicTypes_pb2.UUID, _Mapping]] = ..., completion_action_type: _Optional[_Union[Cue.CompletionActionType, str]] = ..., completion_action_uuid: _Optional[_Union[_basicTypes_pb2.UUID, _Mapping]] = ..., trigger_time: _Optional[_Union[Cue.TimecodeTime, _Mapping]] = ..., hot_key: _Optional[_Union[_hotKey_pb2.HotKey, _Mapping]] = ..., actions: _Optional[_Iterable[_Union[_action_pb2.Action, _Mapping]]] = ..., pending_imports: _Optional[_Iterable[_Union[Cue.PendingImportsEntry, _Mapping]]] = ..., isEnabled: bool = ..., completion_time: _Optional[float] = ...) -> None: ...
