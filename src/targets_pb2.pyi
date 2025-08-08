import basicTypes_pb2 as _basicTypes_pb2
import graphicsData_pb2 as _graphicsData_pb2
import testPattern_pb2 as _testPattern_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TargetSet(_message.Message):
    __slots__ = ("uuid", "name", "color", "test_image_path", "source_size", "targets", "test_pattern")
    UUID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    TEST_IMAGE_PATH_FIELD_NUMBER: _ClassVar[int]
    SOURCE_SIZE_FIELD_NUMBER: _ClassVar[int]
    TARGETS_FIELD_NUMBER: _ClassVar[int]
    TEST_PATTERN_FIELD_NUMBER: _ClassVar[int]
    uuid: _basicTypes_pb2.UUID
    name: str
    color: _basicTypes_pb2.Color
    test_image_path: _basicTypes_pb2.URL
    source_size: _graphicsData_pb2.Graphics.Size
    targets: _containers.RepeatedCompositeFieldContainer[Target]
    test_pattern: _testPattern_pb2.TestPattern
    def __init__(self, uuid: _Optional[_Union[_basicTypes_pb2.UUID, _Mapping]] = ..., name: _Optional[str] = ..., color: _Optional[_Union[_basicTypes_pb2.Color, _Mapping]] = ..., test_image_path: _Optional[_Union[_basicTypes_pb2.URL, _Mapping]] = ..., source_size: _Optional[_Union[_graphicsData_pb2.Graphics.Size, _Mapping]] = ..., targets: _Optional[_Iterable[_Union[Target, _Mapping]]] = ..., test_pattern: _Optional[_Union[_testPattern_pb2.TestPattern, _Mapping]] = ...) -> None: ...

class Target(_message.Message):
    __slots__ = ("uuid", "name", "source_unit_rect", "test_image_fill", "shape", "flipMode")
    class FlipMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        FLIP_MODE_NONE: _ClassVar[Target.FlipMode]
        FLIP_MODE_VERTICAL: _ClassVar[Target.FlipMode]
        FLIP_MODE_HORIZONTAL: _ClassVar[Target.FlipMode]
        FLIP_MODE_BOTH: _ClassVar[Target.FlipMode]
    FLIP_MODE_NONE: Target.FlipMode
    FLIP_MODE_VERTICAL: Target.FlipMode
    FLIP_MODE_HORIZONTAL: Target.FlipMode
    FLIP_MODE_BOTH: Target.FlipMode
    UUID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SOURCE_UNIT_RECT_FIELD_NUMBER: _ClassVar[int]
    TEST_IMAGE_FILL_FIELD_NUMBER: _ClassVar[int]
    SHAPE_FIELD_NUMBER: _ClassVar[int]
    FLIPMODE_FIELD_NUMBER: _ClassVar[int]
    uuid: _basicTypes_pb2.UUID
    name: str
    source_unit_rect: _graphicsData_pb2.Graphics.Rect
    test_image_fill: _graphicsData_pb2.Media
    shape: _graphicsData_pb2.Graphics.Element
    flipMode: Target.FlipMode
    def __init__(self, uuid: _Optional[_Union[_basicTypes_pb2.UUID, _Mapping]] = ..., name: _Optional[str] = ..., source_unit_rect: _Optional[_Union[_graphicsData_pb2.Graphics.Rect, _Mapping]] = ..., test_image_fill: _Optional[_Union[_graphicsData_pb2.Media, _Mapping]] = ..., shape: _Optional[_Union[_graphicsData_pb2.Graphics.Element, _Mapping]] = ..., flipMode: _Optional[_Union[Target.FlipMode, str]] = ...) -> None: ...
