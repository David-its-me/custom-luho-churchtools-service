import graphicsData_pb2 as _graphicsData_pb2
import basicTypes_pb2 as _basicTypes_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Background(_message.Message):
    __slots__ = ("is_enabled", "color", "gradient")
    IS_ENABLED_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    GRADIENT_FIELD_NUMBER: _ClassVar[int]
    is_enabled: bool
    color: _basicTypes_pb2.Color
    gradient: _graphicsData_pb2.Graphics.Gradient
    def __init__(self, is_enabled: bool = ..., color: _Optional[_Union[_basicTypes_pb2.Color, _Mapping]] = ..., gradient: _Optional[_Union[_graphicsData_pb2.Graphics.Gradient, _Mapping]] = ...) -> None: ...
