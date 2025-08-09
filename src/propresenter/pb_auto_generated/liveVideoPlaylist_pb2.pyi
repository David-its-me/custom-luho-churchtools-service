import propresenter.pb_auto_generated.basicTypes_pb2 as _basicTypes_pb2
import propresenter.pb_auto_generated.action_pb2 as _action_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LiveVideoPlaylist(_message.Message):
    __slots__ = ("actions", "targeted_layer_UUID", "uuid")
    ACTIONS_FIELD_NUMBER: _ClassVar[int]
    TARGETED_LAYER_UUID_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    actions: _containers.RepeatedCompositeFieldContainer[_action_pb2.Action]
    targeted_layer_UUID: _basicTypes_pb2.UUID
    uuid: _basicTypes_pb2.UUID
    def __init__(self, actions: _Optional[_Iterable[_Union[_action_pb2.Action, _Mapping]]] = ..., targeted_layer_UUID: _Optional[_Union[_basicTypes_pb2.UUID, _Mapping]] = ..., uuid: _Optional[_Union[_basicTypes_pb2.UUID, _Mapping]] = ...) -> None: ...
