import propresenter.pb_auto_generated.hotKey_pb2 as _hotKey_pb2
import propresenter.pb_auto_generated.effects_pb2 as _effects_pb2
import propresenter.pb_auto_generated.basicTypes_pb2 as _basicTypes_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Layer(_message.Message):
    __slots__ = ("uuid", "name", "color", "muted", "hidden", "blend_mode", "opacity", "selected_target_set_uuid", "effects_preset_uuid", "effects_build_duration", "layer_preset_uuid", "hot_key", "transition", "effects", "blend")
    class BlendMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        BLEND_MODE_NORMAL: _ClassVar[Layer.BlendMode]
        BLEND_MODE_DISSOLVE: _ClassVar[Layer.BlendMode]
        BLEND_MODE_DARKEN: _ClassVar[Layer.BlendMode]
        BLEND_MODE_MULTIPLY: _ClassVar[Layer.BlendMode]
        BLEND_MODE_COLOR_BURN: _ClassVar[Layer.BlendMode]
        BLEND_MODE_LINEAR_BURN: _ClassVar[Layer.BlendMode]
        BLEND_MODE_DARKER_COLOR: _ClassVar[Layer.BlendMode]
        BLEND_MODE_LIGHTEN: _ClassVar[Layer.BlendMode]
        BLEND_MODE_SCREEN: _ClassVar[Layer.BlendMode]
        BLEND_MODE_COLOR_DODGE: _ClassVar[Layer.BlendMode]
        BLEND_MODE_LINEAR_DODGE: _ClassVar[Layer.BlendMode]
        BLEND_MODE_LIGHTER_COLOR: _ClassVar[Layer.BlendMode]
        BLEND_MODE_OVERLAY: _ClassVar[Layer.BlendMode]
        BLEND_MODE_SOFT_LIGHT: _ClassVar[Layer.BlendMode]
        BLEND_MODE_HARD_LIGHT: _ClassVar[Layer.BlendMode]
        BLEND_MODE_VIVID_LIGHT: _ClassVar[Layer.BlendMode]
        BLEND_MODE_LINEAR_LIGHT: _ClassVar[Layer.BlendMode]
        BLEND_MODE_PIN_LIGHT: _ClassVar[Layer.BlendMode]
        BLEND_MODE_HARD_MIX: _ClassVar[Layer.BlendMode]
        BLEND_MODE_DIFFERENCE: _ClassVar[Layer.BlendMode]
        BLEND_MODE_EXCLUSION: _ClassVar[Layer.BlendMode]
        BLEND_MODE_SUBTRACT: _ClassVar[Layer.BlendMode]
        BLEND_MODE_DIVIDE: _ClassVar[Layer.BlendMode]
        BLEND_MODE_HUE: _ClassVar[Layer.BlendMode]
        BLEND_MODE_SATURATION: _ClassVar[Layer.BlendMode]
        BLEND_MODE_COLOR: _ClassVar[Layer.BlendMode]
        BLEND_MODE_LUMINOSITY: _ClassVar[Layer.BlendMode]
    BLEND_MODE_NORMAL: Layer.BlendMode
    BLEND_MODE_DISSOLVE: Layer.BlendMode
    BLEND_MODE_DARKEN: Layer.BlendMode
    BLEND_MODE_MULTIPLY: Layer.BlendMode
    BLEND_MODE_COLOR_BURN: Layer.BlendMode
    BLEND_MODE_LINEAR_BURN: Layer.BlendMode
    BLEND_MODE_DARKER_COLOR: Layer.BlendMode
    BLEND_MODE_LIGHTEN: Layer.BlendMode
    BLEND_MODE_SCREEN: Layer.BlendMode
    BLEND_MODE_COLOR_DODGE: Layer.BlendMode
    BLEND_MODE_LINEAR_DODGE: Layer.BlendMode
    BLEND_MODE_LIGHTER_COLOR: Layer.BlendMode
    BLEND_MODE_OVERLAY: Layer.BlendMode
    BLEND_MODE_SOFT_LIGHT: Layer.BlendMode
    BLEND_MODE_HARD_LIGHT: Layer.BlendMode
    BLEND_MODE_VIVID_LIGHT: Layer.BlendMode
    BLEND_MODE_LINEAR_LIGHT: Layer.BlendMode
    BLEND_MODE_PIN_LIGHT: Layer.BlendMode
    BLEND_MODE_HARD_MIX: Layer.BlendMode
    BLEND_MODE_DIFFERENCE: Layer.BlendMode
    BLEND_MODE_EXCLUSION: Layer.BlendMode
    BLEND_MODE_SUBTRACT: Layer.BlendMode
    BLEND_MODE_DIVIDE: Layer.BlendMode
    BLEND_MODE_HUE: Layer.BlendMode
    BLEND_MODE_SATURATION: Layer.BlendMode
    BLEND_MODE_COLOR: Layer.BlendMode
    BLEND_MODE_LUMINOSITY: Layer.BlendMode
    class Preset(_message.Message):
        __slots__ = ("uuid", "name", "layer")
        UUID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        LAYER_FIELD_NUMBER: _ClassVar[int]
        uuid: _basicTypes_pb2.UUID
        name: str
        layer: Layer
        def __init__(self, uuid: _Optional[_Union[_basicTypes_pb2.UUID, _Mapping]] = ..., name: _Optional[str] = ..., layer: _Optional[_Union[Layer, _Mapping]] = ...) -> None: ...
    class Blending(_message.Message):
        __slots__ = ("standard", "matte")
        class Standard(_message.Message):
            __slots__ = ("mode", "opacity")
            class BlendMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                BLEND_MODE_NORMAL: _ClassVar[Layer.Blending.Standard.BlendMode]
                BLEND_MODE_DISSOLVE: _ClassVar[Layer.Blending.Standard.BlendMode]
                BLEND_MODE_DARKEN: _ClassVar[Layer.Blending.Standard.BlendMode]
                BLEND_MODE_MULTIPLY: _ClassVar[Layer.Blending.Standard.BlendMode]
                BLEND_MODE_COLOR_BURN: _ClassVar[Layer.Blending.Standard.BlendMode]
                BLEND_MODE_LINEAR_BURN: _ClassVar[Layer.Blending.Standard.BlendMode]
                BLEND_MODE_DARKER_COLOR: _ClassVar[Layer.Blending.Standard.BlendMode]
                BLEND_MODE_LIGHTEN: _ClassVar[Layer.Blending.Standard.BlendMode]
                BLEND_MODE_SCREEN: _ClassVar[Layer.Blending.Standard.BlendMode]
                BLEND_MODE_COLOR_DODGE: _ClassVar[Layer.Blending.Standard.BlendMode]
                BLEND_MODE_LINEAR_DODGE: _ClassVar[Layer.Blending.Standard.BlendMode]
                BLEND_MODE_LIGHTER_COLOR: _ClassVar[Layer.Blending.Standard.BlendMode]
                BLEND_MODE_OVERLAY: _ClassVar[Layer.Blending.Standard.BlendMode]
                BLEND_MODE_SOFT_LIGHT: _ClassVar[Layer.Blending.Standard.BlendMode]
                BLEND_MODE_HARD_LIGHT: _ClassVar[Layer.Blending.Standard.BlendMode]
                BLEND_MODE_VIVID_LIGHT: _ClassVar[Layer.Blending.Standard.BlendMode]
                BLEND_MODE_LINEAR_LIGHT: _ClassVar[Layer.Blending.Standard.BlendMode]
                BLEND_MODE_PIN_LIGHT: _ClassVar[Layer.Blending.Standard.BlendMode]
                BLEND_MODE_HARD_MIX: _ClassVar[Layer.Blending.Standard.BlendMode]
                BLEND_MODE_DIFFERENCE: _ClassVar[Layer.Blending.Standard.BlendMode]
                BLEND_MODE_EXCLUSION: _ClassVar[Layer.Blending.Standard.BlendMode]
                BLEND_MODE_SUBTRACT: _ClassVar[Layer.Blending.Standard.BlendMode]
                BLEND_MODE_DIVIDE: _ClassVar[Layer.Blending.Standard.BlendMode]
                BLEND_MODE_HUE: _ClassVar[Layer.Blending.Standard.BlendMode]
                BLEND_MODE_SATURATION: _ClassVar[Layer.Blending.Standard.BlendMode]
                BLEND_MODE_COLOR: _ClassVar[Layer.Blending.Standard.BlendMode]
                BLEND_MODE_LUMINOSITY: _ClassVar[Layer.Blending.Standard.BlendMode]
            BLEND_MODE_NORMAL: Layer.Blending.Standard.BlendMode
            BLEND_MODE_DISSOLVE: Layer.Blending.Standard.BlendMode
            BLEND_MODE_DARKEN: Layer.Blending.Standard.BlendMode
            BLEND_MODE_MULTIPLY: Layer.Blending.Standard.BlendMode
            BLEND_MODE_COLOR_BURN: Layer.Blending.Standard.BlendMode
            BLEND_MODE_LINEAR_BURN: Layer.Blending.Standard.BlendMode
            BLEND_MODE_DARKER_COLOR: Layer.Blending.Standard.BlendMode
            BLEND_MODE_LIGHTEN: Layer.Blending.Standard.BlendMode
            BLEND_MODE_SCREEN: Layer.Blending.Standard.BlendMode
            BLEND_MODE_COLOR_DODGE: Layer.Blending.Standard.BlendMode
            BLEND_MODE_LINEAR_DODGE: Layer.Blending.Standard.BlendMode
            BLEND_MODE_LIGHTER_COLOR: Layer.Blending.Standard.BlendMode
            BLEND_MODE_OVERLAY: Layer.Blending.Standard.BlendMode
            BLEND_MODE_SOFT_LIGHT: Layer.Blending.Standard.BlendMode
            BLEND_MODE_HARD_LIGHT: Layer.Blending.Standard.BlendMode
            BLEND_MODE_VIVID_LIGHT: Layer.Blending.Standard.BlendMode
            BLEND_MODE_LINEAR_LIGHT: Layer.Blending.Standard.BlendMode
            BLEND_MODE_PIN_LIGHT: Layer.Blending.Standard.BlendMode
            BLEND_MODE_HARD_MIX: Layer.Blending.Standard.BlendMode
            BLEND_MODE_DIFFERENCE: Layer.Blending.Standard.BlendMode
            BLEND_MODE_EXCLUSION: Layer.Blending.Standard.BlendMode
            BLEND_MODE_SUBTRACT: Layer.Blending.Standard.BlendMode
            BLEND_MODE_DIVIDE: Layer.Blending.Standard.BlendMode
            BLEND_MODE_HUE: Layer.Blending.Standard.BlendMode
            BLEND_MODE_SATURATION: Layer.Blending.Standard.BlendMode
            BLEND_MODE_COLOR: Layer.Blending.Standard.BlendMode
            BLEND_MODE_LUMINOSITY: Layer.Blending.Standard.BlendMode
            MODE_FIELD_NUMBER: _ClassVar[int]
            OPACITY_FIELD_NUMBER: _ClassVar[int]
            mode: Layer.Blending.Standard.BlendMode
            opacity: float
            def __init__(self, mode: _Optional[_Union[Layer.Blending.Standard.BlendMode, str]] = ..., opacity: _Optional[float] = ...) -> None: ...
        class Matte(_message.Message):
            __slots__ = ("alpha", "luma", "white")
            class Alpha(_message.Message):
                __slots__ = ("inverted",)
                INVERTED_FIELD_NUMBER: _ClassVar[int]
                inverted: bool
                def __init__(self, inverted: bool = ...) -> None: ...
            class Luma(_message.Message):
                __slots__ = ("inverted",)
                INVERTED_FIELD_NUMBER: _ClassVar[int]
                inverted: bool
                def __init__(self, inverted: bool = ...) -> None: ...
            class White(_message.Message):
                __slots__ = ()
                def __init__(self) -> None: ...
            ALPHA_FIELD_NUMBER: _ClassVar[int]
            LUMA_FIELD_NUMBER: _ClassVar[int]
            WHITE_FIELD_NUMBER: _ClassVar[int]
            alpha: Layer.Blending.Matte.Alpha
            luma: Layer.Blending.Matte.Luma
            white: Layer.Blending.Matte.White
            def __init__(self, alpha: _Optional[_Union[Layer.Blending.Matte.Alpha, _Mapping]] = ..., luma: _Optional[_Union[Layer.Blending.Matte.Luma, _Mapping]] = ..., white: _Optional[_Union[Layer.Blending.Matte.White, _Mapping]] = ...) -> None: ...
        STANDARD_FIELD_NUMBER: _ClassVar[int]
        MATTE_FIELD_NUMBER: _ClassVar[int]
        standard: Layer.Blending.Standard
        matte: Layer.Blending.Matte
        def __init__(self, standard: _Optional[_Union[Layer.Blending.Standard, _Mapping]] = ..., matte: _Optional[_Union[Layer.Blending.Matte, _Mapping]] = ...) -> None: ...
    UUID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    MUTED_FIELD_NUMBER: _ClassVar[int]
    HIDDEN_FIELD_NUMBER: _ClassVar[int]
    BLEND_MODE_FIELD_NUMBER: _ClassVar[int]
    OPACITY_FIELD_NUMBER: _ClassVar[int]
    SELECTED_TARGET_SET_UUID_FIELD_NUMBER: _ClassVar[int]
    EFFECTS_PRESET_UUID_FIELD_NUMBER: _ClassVar[int]
    EFFECTS_BUILD_DURATION_FIELD_NUMBER: _ClassVar[int]
    LAYER_PRESET_UUID_FIELD_NUMBER: _ClassVar[int]
    HOT_KEY_FIELD_NUMBER: _ClassVar[int]
    TRANSITION_FIELD_NUMBER: _ClassVar[int]
    EFFECTS_FIELD_NUMBER: _ClassVar[int]
    BLEND_FIELD_NUMBER: _ClassVar[int]
    uuid: _basicTypes_pb2.UUID
    name: str
    color: _basicTypes_pb2.Color
    muted: bool
    hidden: bool
    blend_mode: Layer.BlendMode
    opacity: float
    selected_target_set_uuid: _basicTypes_pb2.UUID
    effects_preset_uuid: _basicTypes_pb2.UUID
    effects_build_duration: float
    layer_preset_uuid: _basicTypes_pb2.UUID
    hot_key: _hotKey_pb2.HotKey
    transition: _effects_pb2.Transition
    effects: _containers.RepeatedCompositeFieldContainer[_effects_pb2.Effect]
    blend: Layer.Blending
    def __init__(self, uuid: _Optional[_Union[_basicTypes_pb2.UUID, _Mapping]] = ..., name: _Optional[str] = ..., color: _Optional[_Union[_basicTypes_pb2.Color, _Mapping]] = ..., muted: bool = ..., hidden: bool = ..., blend_mode: _Optional[_Union[Layer.BlendMode, str]] = ..., opacity: _Optional[float] = ..., selected_target_set_uuid: _Optional[_Union[_basicTypes_pb2.UUID, _Mapping]] = ..., effects_preset_uuid: _Optional[_Union[_basicTypes_pb2.UUID, _Mapping]] = ..., effects_build_duration: _Optional[float] = ..., layer_preset_uuid: _Optional[_Union[_basicTypes_pb2.UUID, _Mapping]] = ..., hot_key: _Optional[_Union[_hotKey_pb2.HotKey, _Mapping]] = ..., transition: _Optional[_Union[_effects_pb2.Transition, _Mapping]] = ..., effects: _Optional[_Iterable[_Union[_effects_pb2.Effect, _Mapping]]] = ..., blend: _Optional[_Union[Layer.Blending, _Mapping]] = ...) -> None: ...
