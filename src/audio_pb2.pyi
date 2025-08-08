import basicTypes_pb2 as _basicTypes_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Audio(_message.Message):
    __slots__ = ()
    class SettingsDocument(_message.Message):
        __slots__ = ("output_setup", "monitor_device", "monitor_on_mains")
        OUTPUT_SETUP_FIELD_NUMBER: _ClassVar[int]
        MONITOR_DEVICE_FIELD_NUMBER: _ClassVar[int]
        MONITOR_ON_MAINS_FIELD_NUMBER: _ClassVar[int]
        output_setup: Audio.OutputSetup
        monitor_device: Audio.Device
        monitor_on_mains: bool
        def __init__(self, output_setup: _Optional[_Union[Audio.OutputSetup, _Mapping]] = ..., monitor_device: _Optional[_Union[Audio.Device, _Mapping]] = ..., monitor_on_mains: bool = ...) -> None: ...
    class OutputSetup(_message.Message):
        __slots__ = ("uuid", "audio_device", "logical_channels", "audio_delay", "master_level", "physical_chanels")
        UUID_FIELD_NUMBER: _ClassVar[int]
        AUDIO_DEVICE_FIELD_NUMBER: _ClassVar[int]
        LOGICAL_CHANNELS_FIELD_NUMBER: _ClassVar[int]
        AUDIO_DELAY_FIELD_NUMBER: _ClassVar[int]
        MASTER_LEVEL_FIELD_NUMBER: _ClassVar[int]
        PHYSICAL_CHANELS_FIELD_NUMBER: _ClassVar[int]
        uuid: _basicTypes_pb2.UUID
        audio_device: Audio.Device
        logical_channels: _containers.RepeatedCompositeFieldContainer[Audio.LogicalChannel]
        audio_delay: float
        master_level: float
        physical_chanels: _containers.RepeatedCompositeFieldContainer[Audio.PhysicalChannel]
        def __init__(self, uuid: _Optional[_Union[_basicTypes_pb2.UUID, _Mapping]] = ..., audio_device: _Optional[_Union[Audio.Device, _Mapping]] = ..., logical_channels: _Optional[_Iterable[_Union[Audio.LogicalChannel, _Mapping]]] = ..., audio_delay: _Optional[float] = ..., master_level: _Optional[float] = ..., physical_chanels: _Optional[_Iterable[_Union[Audio.PhysicalChannel, _Mapping]]] = ...) -> None: ...
    class Device(_message.Message):
        __slots__ = ("name", "renderID", "input_channel_count", "output_channel_count", "formats")
        class Format(_message.Message):
            __slots__ = ("sample_rate", "bit_depth", "type")
            class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                TYPE_INT: _ClassVar[Audio.Device.Format.Type]
                TYPE_FLOAT: _ClassVar[Audio.Device.Format.Type]
            TYPE_INT: Audio.Device.Format.Type
            TYPE_FLOAT: Audio.Device.Format.Type
            SAMPLE_RATE_FIELD_NUMBER: _ClassVar[int]
            BIT_DEPTH_FIELD_NUMBER: _ClassVar[int]
            TYPE_FIELD_NUMBER: _ClassVar[int]
            sample_rate: int
            bit_depth: int
            type: Audio.Device.Format.Type
            def __init__(self, sample_rate: _Optional[int] = ..., bit_depth: _Optional[int] = ..., type: _Optional[_Union[Audio.Device.Format.Type, str]] = ...) -> None: ...
        NAME_FIELD_NUMBER: _ClassVar[int]
        RENDERID_FIELD_NUMBER: _ClassVar[int]
        INPUT_CHANNEL_COUNT_FIELD_NUMBER: _ClassVar[int]
        OUTPUT_CHANNEL_COUNT_FIELD_NUMBER: _ClassVar[int]
        FORMATS_FIELD_NUMBER: _ClassVar[int]
        name: str
        renderID: str
        input_channel_count: int
        output_channel_count: int
        formats: _containers.RepeatedCompositeFieldContainer[Audio.Device.Format]
        def __init__(self, name: _Optional[str] = ..., renderID: _Optional[str] = ..., input_channel_count: _Optional[int] = ..., output_channel_count: _Optional[int] = ..., formats: _Optional[_Iterable[_Union[Audio.Device.Format, _Mapping]]] = ...) -> None: ...
    class LogicalChannel(_message.Message):
        __slots__ = ("uuid", "name", "index", "muted", "physical_audio_channels", "solo", "test_tone")
        class OutputChannel(_message.Message):
            __slots__ = ("index", "muted", "solo", "test_tone")
            INDEX_FIELD_NUMBER: _ClassVar[int]
            MUTED_FIELD_NUMBER: _ClassVar[int]
            SOLO_FIELD_NUMBER: _ClassVar[int]
            TEST_TONE_FIELD_NUMBER: _ClassVar[int]
            index: int
            muted: bool
            solo: bool
            test_tone: bool
            def __init__(self, index: _Optional[int] = ..., muted: bool = ..., solo: bool = ..., test_tone: bool = ...) -> None: ...
        UUID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        INDEX_FIELD_NUMBER: _ClassVar[int]
        MUTED_FIELD_NUMBER: _ClassVar[int]
        PHYSICAL_AUDIO_CHANNELS_FIELD_NUMBER: _ClassVar[int]
        SOLO_FIELD_NUMBER: _ClassVar[int]
        TEST_TONE_FIELD_NUMBER: _ClassVar[int]
        uuid: _basicTypes_pb2.UUID
        name: str
        index: int
        muted: bool
        physical_audio_channels: _containers.RepeatedCompositeFieldContainer[Audio.LogicalChannel.OutputChannel]
        solo: bool
        test_tone: bool
        def __init__(self, uuid: _Optional[_Union[_basicTypes_pb2.UUID, _Mapping]] = ..., name: _Optional[str] = ..., index: _Optional[int] = ..., muted: bool = ..., physical_audio_channels: _Optional[_Iterable[_Union[Audio.LogicalChannel.OutputChannel, _Mapping]]] = ..., solo: bool = ..., test_tone: bool = ...) -> None: ...
    class PhysicalChannel(_message.Message):
        __slots__ = ("index", "mute_enable", "solo_enable", "tone_enable")
        INDEX_FIELD_NUMBER: _ClassVar[int]
        MUTE_ENABLE_FIELD_NUMBER: _ClassVar[int]
        SOLO_ENABLE_FIELD_NUMBER: _ClassVar[int]
        TONE_ENABLE_FIELD_NUMBER: _ClassVar[int]
        index: int
        mute_enable: bool
        solo_enable: bool
        tone_enable: bool
        def __init__(self, index: _Optional[int] = ..., mute_enable: bool = ..., solo_enable: bool = ..., tone_enable: bool = ...) -> None: ...
    def __init__(self) -> None: ...
