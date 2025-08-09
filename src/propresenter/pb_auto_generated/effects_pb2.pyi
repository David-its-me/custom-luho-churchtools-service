import propresenter.pb_auto_generated.basicTypes_pb2 as _basicTypes_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Effect(_message.Message):
    __slots__ = ("uuid", "enabled", "name", "render_id", "behavior_description", "category", "variables")
    class EffectVariable(_message.Message):
        __slots__ = ("name", "description", "int", "float", "color", "direction", "double")
        class EffectInt(_message.Message):
            __slots__ = ("value", "default_value", "min", "max")
            VALUE_FIELD_NUMBER: _ClassVar[int]
            DEFAULT_VALUE_FIELD_NUMBER: _ClassVar[int]
            MIN_FIELD_NUMBER: _ClassVar[int]
            MAX_FIELD_NUMBER: _ClassVar[int]
            value: int
            default_value: int
            min: int
            max: int
            def __init__(self, value: _Optional[int] = ..., default_value: _Optional[int] = ..., min: _Optional[int] = ..., max: _Optional[int] = ...) -> None: ...
        class EffectFloat(_message.Message):
            __slots__ = ("value", "default_value", "min", "max")
            VALUE_FIELD_NUMBER: _ClassVar[int]
            DEFAULT_VALUE_FIELD_NUMBER: _ClassVar[int]
            MIN_FIELD_NUMBER: _ClassVar[int]
            MAX_FIELD_NUMBER: _ClassVar[int]
            value: float
            default_value: float
            min: float
            max: float
            def __init__(self, value: _Optional[float] = ..., default_value: _Optional[float] = ..., min: _Optional[float] = ..., max: _Optional[float] = ...) -> None: ...
        class EffectDouble(_message.Message):
            __slots__ = ("value", "default_value", "min", "max")
            VALUE_FIELD_NUMBER: _ClassVar[int]
            DEFAULT_VALUE_FIELD_NUMBER: _ClassVar[int]
            MIN_FIELD_NUMBER: _ClassVar[int]
            MAX_FIELD_NUMBER: _ClassVar[int]
            value: float
            default_value: float
            min: float
            max: float
            def __init__(self, value: _Optional[float] = ..., default_value: _Optional[float] = ..., min: _Optional[float] = ..., max: _Optional[float] = ...) -> None: ...
        class EffectColor(_message.Message):
            __slots__ = ("color", "default_color")
            COLOR_FIELD_NUMBER: _ClassVar[int]
            DEFAULT_COLOR_FIELD_NUMBER: _ClassVar[int]
            color: _basicTypes_pb2.Color
            default_color: _basicTypes_pb2.Color
            def __init__(self, color: _Optional[_Union[_basicTypes_pb2.Color, _Mapping]] = ..., default_color: _Optional[_Union[_basicTypes_pb2.Color, _Mapping]] = ...) -> None: ...
        class EffectDirection(_message.Message):
            __slots__ = ("direction", "default_direction", "available_directions")
            class EffectDirection(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                EFFECT_DIRECTION_NONE: _ClassVar[Effect.EffectVariable.EffectDirection.EffectDirection]
                EFFECT_DIRECTION_TOP_LEFT: _ClassVar[Effect.EffectVariable.EffectDirection.EffectDirection]
                EFFECT_DIRECTION_TOP: _ClassVar[Effect.EffectVariable.EffectDirection.EffectDirection]
                EFFECT_DIRECTION_TOP_RIGHT: _ClassVar[Effect.EffectVariable.EffectDirection.EffectDirection]
                EFFECT_DIRECTION_LEFT: _ClassVar[Effect.EffectVariable.EffectDirection.EffectDirection]
                EFFECT_DIRECTION_CENTER: _ClassVar[Effect.EffectVariable.EffectDirection.EffectDirection]
                EFFECT_DIRECTION_RIGHT: _ClassVar[Effect.EffectVariable.EffectDirection.EffectDirection]
                EFFECT_DIRECTION_BOTTOM_LEFT: _ClassVar[Effect.EffectVariable.EffectDirection.EffectDirection]
                EFFECT_DIRECTION_BOTTOM: _ClassVar[Effect.EffectVariable.EffectDirection.EffectDirection]
                EFFECT_DIRECTION_BOTTOM_RIGHT: _ClassVar[Effect.EffectVariable.EffectDirection.EffectDirection]
            EFFECT_DIRECTION_NONE: Effect.EffectVariable.EffectDirection.EffectDirection
            EFFECT_DIRECTION_TOP_LEFT: Effect.EffectVariable.EffectDirection.EffectDirection
            EFFECT_DIRECTION_TOP: Effect.EffectVariable.EffectDirection.EffectDirection
            EFFECT_DIRECTION_TOP_RIGHT: Effect.EffectVariable.EffectDirection.EffectDirection
            EFFECT_DIRECTION_LEFT: Effect.EffectVariable.EffectDirection.EffectDirection
            EFFECT_DIRECTION_CENTER: Effect.EffectVariable.EffectDirection.EffectDirection
            EFFECT_DIRECTION_RIGHT: Effect.EffectVariable.EffectDirection.EffectDirection
            EFFECT_DIRECTION_BOTTOM_LEFT: Effect.EffectVariable.EffectDirection.EffectDirection
            EFFECT_DIRECTION_BOTTOM: Effect.EffectVariable.EffectDirection.EffectDirection
            EFFECT_DIRECTION_BOTTOM_RIGHT: Effect.EffectVariable.EffectDirection.EffectDirection
            DIRECTION_FIELD_NUMBER: _ClassVar[int]
            DEFAULT_DIRECTION_FIELD_NUMBER: _ClassVar[int]
            AVAILABLE_DIRECTIONS_FIELD_NUMBER: _ClassVar[int]
            direction: Effect.EffectVariable.EffectDirection.EffectDirection
            default_direction: Effect.EffectVariable.EffectDirection.EffectDirection
            available_directions: int
            def __init__(self, direction: _Optional[_Union[Effect.EffectVariable.EffectDirection.EffectDirection, str]] = ..., default_direction: _Optional[_Union[Effect.EffectVariable.EffectDirection.EffectDirection, str]] = ..., available_directions: _Optional[int] = ...) -> None: ...
        NAME_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        INT_FIELD_NUMBER: _ClassVar[int]
        FLOAT_FIELD_NUMBER: _ClassVar[int]
        COLOR_FIELD_NUMBER: _ClassVar[int]
        DIRECTION_FIELD_NUMBER: _ClassVar[int]
        DOUBLE_FIELD_NUMBER: _ClassVar[int]
        name: str
        description: str
        int: Effect.EffectVariable.EffectInt
        float: Effect.EffectVariable.EffectFloat
        color: Effect.EffectVariable.EffectColor
        direction: Effect.EffectVariable.EffectDirection
        double: Effect.EffectVariable.EffectDouble
        def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., int: _Optional[_Union[Effect.EffectVariable.EffectInt, _Mapping]] = ..., float: _Optional[_Union[Effect.EffectVariable.EffectFloat, _Mapping]] = ..., color: _Optional[_Union[Effect.EffectVariable.EffectColor, _Mapping]] = ..., direction: _Optional[_Union[Effect.EffectVariable.EffectDirection, _Mapping]] = ..., double: _Optional[_Union[Effect.EffectVariable.EffectDouble, _Mapping]] = ...) -> None: ...
    class Preset(_message.Message):
        __slots__ = ("uuid", "name", "effects")
        UUID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        EFFECTS_FIELD_NUMBER: _ClassVar[int]
        uuid: _basicTypes_pb2.UUID
        name: str
        effects: _containers.RepeatedCompositeFieldContainer[Effect]
        def __init__(self, uuid: _Optional[_Union[_basicTypes_pb2.UUID, _Mapping]] = ..., name: _Optional[str] = ..., effects: _Optional[_Iterable[_Union[Effect, _Mapping]]] = ...) -> None: ...
    UUID_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    RENDER_ID_FIELD_NUMBER: _ClassVar[int]
    BEHAVIOR_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    VARIABLES_FIELD_NUMBER: _ClassVar[int]
    uuid: _basicTypes_pb2.UUID
    enabled: bool
    name: str
    render_id: str
    behavior_description: str
    category: str
    variables: _containers.RepeatedCompositeFieldContainer[Effect.EffectVariable]
    def __init__(self, uuid: _Optional[_Union[_basicTypes_pb2.UUID, _Mapping]] = ..., enabled: bool = ..., name: _Optional[str] = ..., render_id: _Optional[str] = ..., behavior_description: _Optional[str] = ..., category: _Optional[str] = ..., variables: _Optional[_Iterable[_Union[Effect.EffectVariable, _Mapping]]] = ...) -> None: ...

class Transition(_message.Message):
    __slots__ = ("duration", "favorite_uuid", "effect")
    class Preset(_message.Message):
        __slots__ = ("uuid", "name", "transition")
        UUID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        TRANSITION_FIELD_NUMBER: _ClassVar[int]
        uuid: _basicTypes_pb2.UUID
        name: str
        transition: Transition
        def __init__(self, uuid: _Optional[_Union[_basicTypes_pb2.UUID, _Mapping]] = ..., name: _Optional[str] = ..., transition: _Optional[_Union[Transition, _Mapping]] = ...) -> None: ...
    DURATION_FIELD_NUMBER: _ClassVar[int]
    FAVORITE_UUID_FIELD_NUMBER: _ClassVar[int]
    EFFECT_FIELD_NUMBER: _ClassVar[int]
    duration: float
    favorite_uuid: _basicTypes_pb2.UUID
    effect: Effect
    def __init__(self, duration: _Optional[float] = ..., favorite_uuid: _Optional[_Union[_basicTypes_pb2.UUID, _Mapping]] = ..., effect: _Optional[_Union[Effect, _Mapping]] = ...) -> None: ...
