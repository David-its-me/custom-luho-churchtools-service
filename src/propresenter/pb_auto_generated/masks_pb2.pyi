import propresenter.pb_auto_generated.graphicsData_pb2 as _graphicsData_pb2
import propresenter.pb_auto_generated.basicTypes_pb2 as _basicTypes_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Mask(_message.Message):
    __slots__ = ("uuid", "name", "color", "mode", "shapes")
    class Mode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MODE_OVERLAY: _ClassVar[Mask.Mode]
        MODE_KEYHOLE: _ClassVar[Mask.Mode]
    MODE_OVERLAY: Mask.Mode
    MODE_KEYHOLE: Mask.Mode
    UUID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    SHAPES_FIELD_NUMBER: _ClassVar[int]
    uuid: _basicTypes_pb2.UUID
    name: str
    color: _basicTypes_pb2.Color
    mode: Mask.Mode
    shapes: _containers.RepeatedCompositeFieldContainer[_graphicsData_pb2.Graphics.Element]
    def __init__(self, uuid: _Optional[_Union[_basicTypes_pb2.UUID, _Mapping]] = ..., name: _Optional[str] = ..., color: _Optional[_Union[_basicTypes_pb2.Color, _Mapping]] = ..., mode: _Optional[_Union[Mask.Mode, str]] = ..., shapes: _Optional[_Iterable[_Union[_graphicsData_pb2.Graphics.Element, _Mapping]]] = ...) -> None: ...
