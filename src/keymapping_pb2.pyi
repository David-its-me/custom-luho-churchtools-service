import basicTypes_pb2 as _basicTypes_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class KeyMapping(_message.Message):
    __slots__ = ("keyboard", "midi", "menu_item", "clear_group_identifier", "cue_identifier", "group_identifier", "macro_identifier", "prop_identifier", "timer_identifier")
    class ComputerKeyboard(_message.Message):
        __slots__ = ("key_equivalent", "key_equivalent_modifier_flags")
        class ModifierFlags(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            MODIFIERFLAGS_COMMAND_KEY: _ClassVar[KeyMapping.ComputerKeyboard.ModifierFlags]
            MODIFIERFLAGS_SHIFT_KEY: _ClassVar[KeyMapping.ComputerKeyboard.ModifierFlags]
            MODIFIERFLAGS_OPTION_KEY: _ClassVar[KeyMapping.ComputerKeyboard.ModifierFlags]
            MODIFIERFLAGS_CONTROL_KEY: _ClassVar[KeyMapping.ComputerKeyboard.ModifierFlags]
            MODIFIERFLAGS_FUNCTION_KEY: _ClassVar[KeyMapping.ComputerKeyboard.ModifierFlags]
        MODIFIERFLAGS_COMMAND_KEY: KeyMapping.ComputerKeyboard.ModifierFlags
        MODIFIERFLAGS_SHIFT_KEY: KeyMapping.ComputerKeyboard.ModifierFlags
        MODIFIERFLAGS_OPTION_KEY: KeyMapping.ComputerKeyboard.ModifierFlags
        MODIFIERFLAGS_CONTROL_KEY: KeyMapping.ComputerKeyboard.ModifierFlags
        MODIFIERFLAGS_FUNCTION_KEY: KeyMapping.ComputerKeyboard.ModifierFlags
        KEY_EQUIVALENT_FIELD_NUMBER: _ClassVar[int]
        KEY_EQUIVALENT_MODIFIER_FLAGS_FIELD_NUMBER: _ClassVar[int]
        key_equivalent: str
        key_equivalent_modifier_flags: _containers.RepeatedScalarFieldContainer[KeyMapping.ComputerKeyboard.ModifierFlags]
        def __init__(self, key_equivalent: _Optional[str] = ..., key_equivalent_modifier_flags: _Optional[_Iterable[_Union[KeyMapping.ComputerKeyboard.ModifierFlags, str]]] = ...) -> None: ...
    class MIDIKeyboard(_message.Message):
        __slots__ = ("channel", "pitch", "velocity")
        CHANNEL_FIELD_NUMBER: _ClassVar[int]
        PITCH_FIELD_NUMBER: _ClassVar[int]
        VELOCITY_FIELD_NUMBER: _ClassVar[int]
        channel: int
        pitch: int
        velocity: int
        def __init__(self, channel: _Optional[int] = ..., pitch: _Optional[int] = ..., velocity: _Optional[int] = ...) -> None: ...
    KEYBOARD_FIELD_NUMBER: _ClassVar[int]
    MIDI_FIELD_NUMBER: _ClassVar[int]
    MENU_ITEM_FIELD_NUMBER: _ClassVar[int]
    CLEAR_GROUP_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    CUE_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    GROUP_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    MACRO_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    PROP_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    TIMER_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    keyboard: KeyMapping.ComputerKeyboard
    midi: KeyMapping.MIDIKeyboard
    menu_item: str
    clear_group_identifier: _basicTypes_pb2.CollectionElementType
    cue_identifier: _basicTypes_pb2.CollectionElementType
    group_identifier: _basicTypes_pb2.CollectionElementType
    macro_identifier: _basicTypes_pb2.CollectionElementType
    prop_identifier: _basicTypes_pb2.CollectionElementType
    timer_identifier: _basicTypes_pb2.CollectionElementType
    def __init__(self, keyboard: _Optional[_Union[KeyMapping.ComputerKeyboard, _Mapping]] = ..., midi: _Optional[_Union[KeyMapping.MIDIKeyboard, _Mapping]] = ..., menu_item: _Optional[str] = ..., clear_group_identifier: _Optional[_Union[_basicTypes_pb2.CollectionElementType, _Mapping]] = ..., cue_identifier: _Optional[_Union[_basicTypes_pb2.CollectionElementType, _Mapping]] = ..., group_identifier: _Optional[_Union[_basicTypes_pb2.CollectionElementType, _Mapping]] = ..., macro_identifier: _Optional[_Union[_basicTypes_pb2.CollectionElementType, _Mapping]] = ..., prop_identifier: _Optional[_Union[_basicTypes_pb2.CollectionElementType, _Mapping]] = ..., timer_identifier: _Optional[_Union[_basicTypes_pb2.CollectionElementType, _Mapping]] = ...) -> None: ...

class KeyMappingDocument(_message.Message):
    __slots__ = ("application_info", "keymappings", "macos_keymappings", "windows_keymappings")
    APPLICATION_INFO_FIELD_NUMBER: _ClassVar[int]
    KEYMAPPINGS_FIELD_NUMBER: _ClassVar[int]
    MACOS_KEYMAPPINGS_FIELD_NUMBER: _ClassVar[int]
    WINDOWS_KEYMAPPINGS_FIELD_NUMBER: _ClassVar[int]
    application_info: _basicTypes_pb2.ApplicationInfo
    keymappings: _containers.RepeatedCompositeFieldContainer[KeyMapping]
    macos_keymappings: _containers.RepeatedCompositeFieldContainer[KeyMapping]
    windows_keymappings: _containers.RepeatedCompositeFieldContainer[KeyMapping]
    def __init__(self, application_info: _Optional[_Union[_basicTypes_pb2.ApplicationInfo, _Mapping]] = ..., keymappings: _Optional[_Iterable[_Union[KeyMapping, _Mapping]]] = ..., macos_keymappings: _Optional[_Iterable[_Union[KeyMapping, _Mapping]]] = ..., windows_keymappings: _Optional[_Iterable[_Union[KeyMapping, _Mapping]]] = ...) -> None: ...
