import propresenter.pb_auto_generated.basicTypes_pb2 as _basicTypes_pb2
import propresenter.pb_auto_generated.graphicsData_pb2 as _graphicsData_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Screen(_message.Message):
    __slots__ = ("uuid", "name", "color", "bounds", "aspect_ratio_locked", "output_bounds_aspect_ratio_locked", "corner_pinning_enabled", "subscreen_unit_rect", "rotation", "gamma", "black_level", "blended_edges", "corner_values", "output_display", "color_enabled", "color_adjustment", "blend_compensation")
    class ColorAdjustment(_message.Message):
        __slots__ = ("gamma", "black_level", "red_level", "green_level", "blue_level", "brightness", "contrast")
        GAMMA_FIELD_NUMBER: _ClassVar[int]
        BLACK_LEVEL_FIELD_NUMBER: _ClassVar[int]
        RED_LEVEL_FIELD_NUMBER: _ClassVar[int]
        GREEN_LEVEL_FIELD_NUMBER: _ClassVar[int]
        BLUE_LEVEL_FIELD_NUMBER: _ClassVar[int]
        BRIGHTNESS_FIELD_NUMBER: _ClassVar[int]
        CONTRAST_FIELD_NUMBER: _ClassVar[int]
        gamma: float
        black_level: float
        red_level: float
        green_level: float
        blue_level: float
        brightness: float
        contrast: float
        def __init__(self, gamma: _Optional[float] = ..., black_level: _Optional[float] = ..., red_level: _Optional[float] = ..., green_level: _Optional[float] = ..., blue_level: _Optional[float] = ..., brightness: _Optional[float] = ..., contrast: _Optional[float] = ...) -> None: ...
    class BlendCompensation(_message.Message):
        __slots__ = ("black_level",)
        BLACK_LEVEL_FIELD_NUMBER: _ClassVar[int]
        black_level: float
        def __init__(self, black_level: _Optional[float] = ...) -> None: ...
    UUID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    BOUNDS_FIELD_NUMBER: _ClassVar[int]
    ASPECT_RATIO_LOCKED_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_BOUNDS_ASPECT_RATIO_LOCKED_FIELD_NUMBER: _ClassVar[int]
    CORNER_PINNING_ENABLED_FIELD_NUMBER: _ClassVar[int]
    SUBSCREEN_UNIT_RECT_FIELD_NUMBER: _ClassVar[int]
    ROTATION_FIELD_NUMBER: _ClassVar[int]
    GAMMA_FIELD_NUMBER: _ClassVar[int]
    BLACK_LEVEL_FIELD_NUMBER: _ClassVar[int]
    BLENDED_EDGES_FIELD_NUMBER: _ClassVar[int]
    CORNER_VALUES_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_DISPLAY_FIELD_NUMBER: _ClassVar[int]
    COLOR_ENABLED_FIELD_NUMBER: _ClassVar[int]
    COLOR_ADJUSTMENT_FIELD_NUMBER: _ClassVar[int]
    BLEND_COMPENSATION_FIELD_NUMBER: _ClassVar[int]
    uuid: _basicTypes_pb2.UUID
    name: str
    color: _basicTypes_pb2.Color
    bounds: _graphicsData_pb2.Graphics.Rect
    aspect_ratio_locked: bool
    output_bounds_aspect_ratio_locked: bool
    corner_pinning_enabled: bool
    subscreen_unit_rect: _graphicsData_pb2.Graphics.Rect
    rotation: float
    gamma: float
    black_level: float
    blended_edges: int
    corner_values: CornerValues
    output_display: OutputDisplay
    color_enabled: bool
    color_adjustment: Screen.ColorAdjustment
    blend_compensation: Screen.BlendCompensation
    def __init__(self, uuid: _Optional[_Union[_basicTypes_pb2.UUID, _Mapping]] = ..., name: _Optional[str] = ..., color: _Optional[_Union[_basicTypes_pb2.Color, _Mapping]] = ..., bounds: _Optional[_Union[_graphicsData_pb2.Graphics.Rect, _Mapping]] = ..., aspect_ratio_locked: bool = ..., output_bounds_aspect_ratio_locked: bool = ..., corner_pinning_enabled: bool = ..., subscreen_unit_rect: _Optional[_Union[_graphicsData_pb2.Graphics.Rect, _Mapping]] = ..., rotation: _Optional[float] = ..., gamma: _Optional[float] = ..., black_level: _Optional[float] = ..., blended_edges: _Optional[int] = ..., corner_values: _Optional[_Union[CornerValues, _Mapping]] = ..., output_display: _Optional[_Union[OutputDisplay, _Mapping]] = ..., color_enabled: bool = ..., color_adjustment: _Optional[_Union[Screen.ColorAdjustment, _Mapping]] = ..., blend_compensation: _Optional[_Union[Screen.BlendCompensation, _Mapping]] = ...) -> None: ...

class CornerValues(_message.Message):
    __slots__ = ("top_left", "top_right", "bottom_left", "bottom_right")
    TOP_LEFT_FIELD_NUMBER: _ClassVar[int]
    TOP_RIGHT_FIELD_NUMBER: _ClassVar[int]
    BOTTOM_LEFT_FIELD_NUMBER: _ClassVar[int]
    BOTTOM_RIGHT_FIELD_NUMBER: _ClassVar[int]
    top_left: _graphicsData_pb2.Graphics.Point
    top_right: _graphicsData_pb2.Graphics.Point
    bottom_left: _graphicsData_pb2.Graphics.Point
    bottom_right: _graphicsData_pb2.Graphics.Point
    def __init__(self, top_left: _Optional[_Union[_graphicsData_pb2.Graphics.Point, _Mapping]] = ..., top_right: _Optional[_Union[_graphicsData_pb2.Graphics.Point, _Mapping]] = ..., bottom_left: _Optional[_Union[_graphicsData_pb2.Graphics.Point, _Mapping]] = ..., bottom_right: _Optional[_Union[_graphicsData_pb2.Graphics.Point, _Mapping]] = ...) -> None: ...

class DisplayMode(_message.Message):
    __slots__ = ("name", "width", "height", "refresh_rate", "interlaced")
    NAME_FIELD_NUMBER: _ClassVar[int]
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    REFRESH_RATE_FIELD_NUMBER: _ClassVar[int]
    INTERLACED_FIELD_NUMBER: _ClassVar[int]
    name: str
    width: int
    height: int
    refresh_rate: float
    interlaced: bool
    def __init__(self, name: _Optional[str] = ..., width: _Optional[int] = ..., height: _Optional[int] = ..., refresh_rate: _Optional[float] = ..., interlaced: bool = ...) -> None: ...

class OutputDisplay(_message.Message):
    __slots__ = ("name", "model", "serial", "deviceName", "vendor", "modeIndex", "bounds", "type", "mode", "render_id", "black_magic_alpha_key_settings")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_UNKNOWN: _ClassVar[OutputDisplay.Type]
        TYPE_SCREEN: _ClassVar[OutputDisplay.Type]
        TYPE_CARD: _ClassVar[OutputDisplay.Type]
        TYPE_NDI: _ClassVar[OutputDisplay.Type]
        TYPE_SYPHON: _ClassVar[OutputDisplay.Type]
        TYPE_CUSTOM: _ClassVar[OutputDisplay.Type]
    TYPE_UNKNOWN: OutputDisplay.Type
    TYPE_SCREEN: OutputDisplay.Type
    TYPE_CARD: OutputDisplay.Type
    TYPE_NDI: OutputDisplay.Type
    TYPE_SYPHON: OutputDisplay.Type
    TYPE_CUSTOM: OutputDisplay.Type
    class BlackmagicAlphaKeySettings(_message.Message):
        __slots__ = ("enabled", "key_mode", "blend_value")
        class KeyMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            KEY_MODE_INTERNAL: _ClassVar[OutputDisplay.BlackmagicAlphaKeySettings.KeyMode]
            KEY_MODE_EXTERNAL: _ClassVar[OutputDisplay.BlackmagicAlphaKeySettings.KeyMode]
        KEY_MODE_INTERNAL: OutputDisplay.BlackmagicAlphaKeySettings.KeyMode
        KEY_MODE_EXTERNAL: OutputDisplay.BlackmagicAlphaKeySettings.KeyMode
        ENABLED_FIELD_NUMBER: _ClassVar[int]
        KEY_MODE_FIELD_NUMBER: _ClassVar[int]
        BLEND_VALUE_FIELD_NUMBER: _ClassVar[int]
        enabled: bool
        key_mode: OutputDisplay.BlackmagicAlphaKeySettings.KeyMode
        blend_value: float
        def __init__(self, enabled: bool = ..., key_mode: _Optional[_Union[OutputDisplay.BlackmagicAlphaKeySettings.KeyMode, str]] = ..., blend_value: _Optional[float] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    SERIAL_FIELD_NUMBER: _ClassVar[int]
    DEVICENAME_FIELD_NUMBER: _ClassVar[int]
    VENDOR_FIELD_NUMBER: _ClassVar[int]
    MODEINDEX_FIELD_NUMBER: _ClassVar[int]
    BOUNDS_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    RENDER_ID_FIELD_NUMBER: _ClassVar[int]
    BLACK_MAGIC_ALPHA_KEY_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    name: str
    model: str
    serial: str
    deviceName: str
    vendor: str
    modeIndex: int
    bounds: _graphicsData_pb2.Graphics.Rect
    type: OutputDisplay.Type
    mode: DisplayMode
    render_id: str
    black_magic_alpha_key_settings: OutputDisplay.BlackmagicAlphaKeySettings
    def __init__(self, name: _Optional[str] = ..., model: _Optional[str] = ..., serial: _Optional[str] = ..., deviceName: _Optional[str] = ..., vendor: _Optional[str] = ..., modeIndex: _Optional[int] = ..., bounds: _Optional[_Union[_graphicsData_pb2.Graphics.Rect, _Mapping]] = ..., type: _Optional[_Union[OutputDisplay.Type, str]] = ..., mode: _Optional[_Union[DisplayMode, _Mapping]] = ..., render_id: _Optional[str] = ..., black_magic_alpha_key_settings: _Optional[_Union[OutputDisplay.BlackmagicAlphaKeySettings, _Mapping]] = ...) -> None: ...

class EdgeBlend(_message.Message):
    __slots__ = ("uuid", "radius", "intensity", "mode", "first_screen", "second_screen", "left_screen", "right_screen", "top_screen", "bottom_screen")
    class Mode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MODE_LINEAR: _ClassVar[EdgeBlend.Mode]
        MODE_CUBIC: _ClassVar[EdgeBlend.Mode]
        MODE_QUADRATIC: _ClassVar[EdgeBlend.Mode]
    MODE_LINEAR: EdgeBlend.Mode
    MODE_CUBIC: EdgeBlend.Mode
    MODE_QUADRATIC: EdgeBlend.Mode
    class Screen(_message.Message):
        __slots__ = ("uuid", "edge", "gamma", "black_level", "mode", "radius", "intensity")
        class Edge(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            EDGE_UNKNOWN: _ClassVar[EdgeBlend.Screen.Edge]
            EDGE_LEFT: _ClassVar[EdgeBlend.Screen.Edge]
            EDGE_RIGHT: _ClassVar[EdgeBlend.Screen.Edge]
            EDGE_TOP: _ClassVar[EdgeBlend.Screen.Edge]
            EDGE_BOTTOM: _ClassVar[EdgeBlend.Screen.Edge]
        EDGE_UNKNOWN: EdgeBlend.Screen.Edge
        EDGE_LEFT: EdgeBlend.Screen.Edge
        EDGE_RIGHT: EdgeBlend.Screen.Edge
        EDGE_TOP: EdgeBlend.Screen.Edge
        EDGE_BOTTOM: EdgeBlend.Screen.Edge
        class Mode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            MODE_LINEAR: _ClassVar[EdgeBlend.Screen.Mode]
            MODE_CUBIC: _ClassVar[EdgeBlend.Screen.Mode]
            MODE_QUADRATIC: _ClassVar[EdgeBlend.Screen.Mode]
        MODE_LINEAR: EdgeBlend.Screen.Mode
        MODE_CUBIC: EdgeBlend.Screen.Mode
        MODE_QUADRATIC: EdgeBlend.Screen.Mode
        UUID_FIELD_NUMBER: _ClassVar[int]
        EDGE_FIELD_NUMBER: _ClassVar[int]
        GAMMA_FIELD_NUMBER: _ClassVar[int]
        BLACK_LEVEL_FIELD_NUMBER: _ClassVar[int]
        MODE_FIELD_NUMBER: _ClassVar[int]
        RADIUS_FIELD_NUMBER: _ClassVar[int]
        INTENSITY_FIELD_NUMBER: _ClassVar[int]
        uuid: _basicTypes_pb2.UUID
        edge: EdgeBlend.Screen.Edge
        gamma: float
        black_level: float
        mode: EdgeBlend.Screen.Mode
        radius: float
        intensity: float
        def __init__(self, uuid: _Optional[_Union[_basicTypes_pb2.UUID, _Mapping]] = ..., edge: _Optional[_Union[EdgeBlend.Screen.Edge, str]] = ..., gamma: _Optional[float] = ..., black_level: _Optional[float] = ..., mode: _Optional[_Union[EdgeBlend.Screen.Mode, str]] = ..., radius: _Optional[float] = ..., intensity: _Optional[float] = ...) -> None: ...
    UUID_FIELD_NUMBER: _ClassVar[int]
    RADIUS_FIELD_NUMBER: _ClassVar[int]
    INTENSITY_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    FIRST_SCREEN_FIELD_NUMBER: _ClassVar[int]
    SECOND_SCREEN_FIELD_NUMBER: _ClassVar[int]
    LEFT_SCREEN_FIELD_NUMBER: _ClassVar[int]
    RIGHT_SCREEN_FIELD_NUMBER: _ClassVar[int]
    TOP_SCREEN_FIELD_NUMBER: _ClassVar[int]
    BOTTOM_SCREEN_FIELD_NUMBER: _ClassVar[int]
    uuid: _basicTypes_pb2.UUID
    radius: float
    intensity: float
    mode: EdgeBlend.Mode
    first_screen: EdgeBlend.Screen
    second_screen: EdgeBlend.Screen
    left_screen: EdgeBlend.Screen
    right_screen: EdgeBlend.Screen
    top_screen: EdgeBlend.Screen
    bottom_screen: EdgeBlend.Screen
    def __init__(self, uuid: _Optional[_Union[_basicTypes_pb2.UUID, _Mapping]] = ..., radius: _Optional[float] = ..., intensity: _Optional[float] = ..., mode: _Optional[_Union[EdgeBlend.Mode, str]] = ..., first_screen: _Optional[_Union[EdgeBlend.Screen, _Mapping]] = ..., second_screen: _Optional[_Union[EdgeBlend.Screen, _Mapping]] = ..., left_screen: _Optional[_Union[EdgeBlend.Screen, _Mapping]] = ..., right_screen: _Optional[_Union[EdgeBlend.Screen, _Mapping]] = ..., top_screen: _Optional[_Union[EdgeBlend.Screen, _Mapping]] = ..., bottom_screen: _Optional[_Union[EdgeBlend.Screen, _Mapping]] = ...) -> None: ...
