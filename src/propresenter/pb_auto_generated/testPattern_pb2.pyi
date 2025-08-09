import propresenter.pb_auto_generated.basicTypes_pb2 as _basicTypes_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TestPattern(_message.Message):
    __slots__ = ("type", "blend_grid", "custom_color", "intensity")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_UNKNOWN: _ClassVar[TestPattern.Type]
        TYPE_BLEND_GRID: _ClassVar[TestPattern.Type]
        TYPE_COLOR_BARS: _ClassVar[TestPattern.Type]
        TYPE_FOCUS: _ClassVar[TestPattern.Type]
        TYPE_GRAY_SCALE: _ClassVar[TestPattern.Type]
        TYPE_BLACK_COLOR: _ClassVar[TestPattern.Type]
        TYPE_WHITE_COLOR: _ClassVar[TestPattern.Type]
        TYPE_CUSTOM_COLOR: _ClassVar[TestPattern.Type]
    TYPE_UNKNOWN: TestPattern.Type
    TYPE_BLEND_GRID: TestPattern.Type
    TYPE_COLOR_BARS: TestPattern.Type
    TYPE_FOCUS: TestPattern.Type
    TYPE_GRAY_SCALE: TestPattern.Type
    TYPE_BLACK_COLOR: TestPattern.Type
    TYPE_WHITE_COLOR: TestPattern.Type
    TYPE_CUSTOM_COLOR: TestPattern.Type
    class BlendGrid(_message.Message):
        __slots__ = ("draw_grid", "draw_circles", "draw_lines", "invert_colors", "grid_spacing")
        DRAW_GRID_FIELD_NUMBER: _ClassVar[int]
        DRAW_CIRCLES_FIELD_NUMBER: _ClassVar[int]
        DRAW_LINES_FIELD_NUMBER: _ClassVar[int]
        INVERT_COLORS_FIELD_NUMBER: _ClassVar[int]
        GRID_SPACING_FIELD_NUMBER: _ClassVar[int]
        draw_grid: bool
        draw_circles: bool
        draw_lines: bool
        invert_colors: bool
        grid_spacing: float
        def __init__(self, draw_grid: bool = ..., draw_circles: bool = ..., draw_lines: bool = ..., invert_colors: bool = ..., grid_spacing: _Optional[float] = ...) -> None: ...
    class CustomColor(_message.Message):
        __slots__ = ("color",)
        COLOR_FIELD_NUMBER: _ClassVar[int]
        color: _basicTypes_pb2.Color
        def __init__(self, color: _Optional[_Union[_basicTypes_pb2.Color, _Mapping]] = ...) -> None: ...
    class IntensityColor(_message.Message):
        __slots__ = ("intensity",)
        INTENSITY_FIELD_NUMBER: _ClassVar[int]
        intensity: float
        def __init__(self, intensity: _Optional[float] = ...) -> None: ...
    TYPE_FIELD_NUMBER: _ClassVar[int]
    BLEND_GRID_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_COLOR_FIELD_NUMBER: _ClassVar[int]
    INTENSITY_FIELD_NUMBER: _ClassVar[int]
    type: TestPattern.Type
    blend_grid: TestPattern.BlendGrid
    custom_color: TestPattern.CustomColor
    intensity: TestPattern.IntensityColor
    def __init__(self, type: _Optional[_Union[TestPattern.Type, str]] = ..., blend_grid: _Optional[_Union[TestPattern.BlendGrid, _Mapping]] = ..., custom_color: _Optional[_Union[TestPattern.CustomColor, _Mapping]] = ..., intensity: _Optional[_Union[TestPattern.IntensityColor, _Mapping]] = ...) -> None: ...
