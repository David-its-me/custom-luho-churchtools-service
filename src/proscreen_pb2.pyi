import screens_pb2 as _screens_pb2
import basicTypes_pb2 as _basicTypes_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ProPresenterScreen(_message.Message):
    __slots__ = ("name", "screen_type", "background_color", "uuid", "background_color_enabled", "arrangement_single", "arrangement_combined", "arrangement_edge_blend")
    class ScreenType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SCREEN_TYPE_UNKNOWN: _ClassVar[ProPresenterScreen.ScreenType]
        SCREEN_TYPE_AUDIENCE: _ClassVar[ProPresenterScreen.ScreenType]
        SCREEN_TYPE_STAGE: _ClassVar[ProPresenterScreen.ScreenType]
    SCREEN_TYPE_UNKNOWN: ProPresenterScreen.ScreenType
    SCREEN_TYPE_AUDIENCE: ProPresenterScreen.ScreenType
    SCREEN_TYPE_STAGE: ProPresenterScreen.ScreenType
    class SingleArrangement(_message.Message):
        __slots__ = ("screens",)
        SCREENS_FIELD_NUMBER: _ClassVar[int]
        screens: _containers.RepeatedCompositeFieldContainer[_screens_pb2.Screen]
        def __init__(self, screens: _Optional[_Iterable[_Union[_screens_pb2.Screen, _Mapping]]] = ...) -> None: ...
    class CombinedArrangement(_message.Message):
        __slots__ = ("screens", "rows", "columns")
        SCREENS_FIELD_NUMBER: _ClassVar[int]
        ROWS_FIELD_NUMBER: _ClassVar[int]
        COLUMNS_FIELD_NUMBER: _ClassVar[int]
        screens: _containers.RepeatedCompositeFieldContainer[_screens_pb2.Screen]
        rows: int
        columns: int
        def __init__(self, screens: _Optional[_Iterable[_Union[_screens_pb2.Screen, _Mapping]]] = ..., rows: _Optional[int] = ..., columns: _Optional[int] = ...) -> None: ...
    class EdgeBlendArrangement(_message.Message):
        __slots__ = ("screen_count", "screens", "edge_blends")
        SCREEN_COUNT_FIELD_NUMBER: _ClassVar[int]
        SCREENS_FIELD_NUMBER: _ClassVar[int]
        EDGE_BLENDS_FIELD_NUMBER: _ClassVar[int]
        screen_count: int
        screens: _containers.RepeatedCompositeFieldContainer[_screens_pb2.Screen]
        edge_blends: _containers.RepeatedCompositeFieldContainer[_screens_pb2.EdgeBlend]
        def __init__(self, screen_count: _Optional[int] = ..., screens: _Optional[_Iterable[_Union[_screens_pb2.Screen, _Mapping]]] = ..., edge_blends: _Optional[_Iterable[_Union[_screens_pb2.EdgeBlend, _Mapping]]] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    SCREEN_TYPE_FIELD_NUMBER: _ClassVar[int]
    BACKGROUND_COLOR_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    BACKGROUND_COLOR_ENABLED_FIELD_NUMBER: _ClassVar[int]
    ARRANGEMENT_SINGLE_FIELD_NUMBER: _ClassVar[int]
    ARRANGEMENT_COMBINED_FIELD_NUMBER: _ClassVar[int]
    ARRANGEMENT_EDGE_BLEND_FIELD_NUMBER: _ClassVar[int]
    name: str
    screen_type: ProPresenterScreen.ScreenType
    background_color: _basicTypes_pb2.Color
    uuid: _basicTypes_pb2.UUID
    background_color_enabled: bool
    arrangement_single: ProPresenterScreen.SingleArrangement
    arrangement_combined: ProPresenterScreen.CombinedArrangement
    arrangement_edge_blend: ProPresenterScreen.EdgeBlendArrangement
    def __init__(self, name: _Optional[str] = ..., screen_type: _Optional[_Union[ProPresenterScreen.ScreenType, str]] = ..., background_color: _Optional[_Union[_basicTypes_pb2.Color, _Mapping]] = ..., uuid: _Optional[_Union[_basicTypes_pb2.UUID, _Mapping]] = ..., background_color_enabled: bool = ..., arrangement_single: _Optional[_Union[ProPresenterScreen.SingleArrangement, _Mapping]] = ..., arrangement_combined: _Optional[_Union[ProPresenterScreen.CombinedArrangement, _Mapping]] = ..., arrangement_edge_blend: _Optional[_Union[ProPresenterScreen.EdgeBlendArrangement, _Mapping]] = ...) -> None: ...
