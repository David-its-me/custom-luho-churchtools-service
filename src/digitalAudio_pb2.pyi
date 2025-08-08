from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DigitalAudio(_message.Message):
    __slots__ = ()
    class Setup(_message.Message):
        __slots__ = ("buses", "monitor_device", "main_output_device", "enable_sdi_ndi_device", "sdi_ndi_device", "monitor_on_mains", "disable_main_output_device")
        BUSES_FIELD_NUMBER: _ClassVar[int]
        MONITOR_DEVICE_FIELD_NUMBER: _ClassVar[int]
        MAIN_OUTPUT_DEVICE_FIELD_NUMBER: _ClassVar[int]
        ENABLE_SDI_NDI_DEVICE_FIELD_NUMBER: _ClassVar[int]
        SDI_NDI_DEVICE_FIELD_NUMBER: _ClassVar[int]
        MONITOR_ON_MAINS_FIELD_NUMBER: _ClassVar[int]
        DISABLE_MAIN_OUTPUT_DEVICE_FIELD_NUMBER: _ClassVar[int]
        buses: _containers.RepeatedCompositeFieldContainer[DigitalAudio.Bus]
        monitor_device: DigitalAudio.Device
        main_output_device: DigitalAudio.Device
        enable_sdi_ndi_device: bool
        sdi_ndi_device: DigitalAudio.Device
        monitor_on_mains: bool
        disable_main_output_device: bool
        def __init__(self, buses: _Optional[_Iterable[_Union[DigitalAudio.Bus, _Mapping]]] = ..., monitor_device: _Optional[_Union[DigitalAudio.Device, _Mapping]] = ..., main_output_device: _Optional[_Union[DigitalAudio.Device, _Mapping]] = ..., enable_sdi_ndi_device: bool = ..., sdi_ndi_device: _Optional[_Union[DigitalAudio.Device, _Mapping]] = ..., monitor_on_mains: bool = ..., disable_main_output_device: bool = ...) -> None: ...
    class Bus(_message.Message):
        __slots__ = ("name", "muted", "solo", "test_tone", "master_level")
        NAME_FIELD_NUMBER: _ClassVar[int]
        MUTED_FIELD_NUMBER: _ClassVar[int]
        SOLO_FIELD_NUMBER: _ClassVar[int]
        TEST_TONE_FIELD_NUMBER: _ClassVar[int]
        MASTER_LEVEL_FIELD_NUMBER: _ClassVar[int]
        name: str
        muted: bool
        solo: bool
        test_tone: bool
        master_level: float
        def __init__(self, name: _Optional[str] = ..., muted: bool = ..., solo: bool = ..., test_tone: bool = ..., master_level: _Optional[float] = ...) -> None: ...
    class Device(_message.Message):
        __slots__ = ("name", "renderID", "formats", "routing")
        class Format(_message.Message):
            __slots__ = ("sample_rate", "bit_depth", "type")
            class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                TYPE_INT: _ClassVar[DigitalAudio.Device.Format.Type]
                TYPE_FLOAT: _ClassVar[DigitalAudio.Device.Format.Type]
            TYPE_INT: DigitalAudio.Device.Format.Type
            TYPE_FLOAT: DigitalAudio.Device.Format.Type
            SAMPLE_RATE_FIELD_NUMBER: _ClassVar[int]
            BIT_DEPTH_FIELD_NUMBER: _ClassVar[int]
            TYPE_FIELD_NUMBER: _ClassVar[int]
            sample_rate: int
            bit_depth: int
            type: DigitalAudio.Device.Format.Type
            def __init__(self, sample_rate: _Optional[int] = ..., bit_depth: _Optional[int] = ..., type: _Optional[_Union[DigitalAudio.Device.Format.Type, str]] = ...) -> None: ...
        class Map(_message.Message):
            __slots__ = ("channel_index", "mapped_indices")
            CHANNEL_INDEX_FIELD_NUMBER: _ClassVar[int]
            MAPPED_INDICES_FIELD_NUMBER: _ClassVar[int]
            channel_index: int
            mapped_indices: _containers.RepeatedScalarFieldContainer[int]
            def __init__(self, channel_index: _Optional[int] = ..., mapped_indices: _Optional[_Iterable[int]] = ...) -> None: ...
        class Channel(_message.Message):
            __slots__ = ("mute_enable", "solo_enable", "tone_enable", "audio_delay", "level")
            MUTE_ENABLE_FIELD_NUMBER: _ClassVar[int]
            SOLO_ENABLE_FIELD_NUMBER: _ClassVar[int]
            TONE_ENABLE_FIELD_NUMBER: _ClassVar[int]
            AUDIO_DELAY_FIELD_NUMBER: _ClassVar[int]
            LEVEL_FIELD_NUMBER: _ClassVar[int]
            mute_enable: bool
            solo_enable: bool
            tone_enable: bool
            audio_delay: float
            level: float
            def __init__(self, mute_enable: bool = ..., solo_enable: bool = ..., tone_enable: bool = ..., audio_delay: _Optional[float] = ..., level: _Optional[float] = ...) -> None: ...
        class Routing(_message.Message):
            __slots__ = ("channels", "map", "is_custom_map", "master_channel")
            CHANNELS_FIELD_NUMBER: _ClassVar[int]
            MAP_FIELD_NUMBER: _ClassVar[int]
            IS_CUSTOM_MAP_FIELD_NUMBER: _ClassVar[int]
            MASTER_CHANNEL_FIELD_NUMBER: _ClassVar[int]
            channels: _containers.RepeatedCompositeFieldContainer[DigitalAudio.Device.Channel]
            map: _containers.RepeatedCompositeFieldContainer[DigitalAudio.Device.Map]
            is_custom_map: bool
            master_channel: DigitalAudio.Device.Channel
            def __init__(self, channels: _Optional[_Iterable[_Union[DigitalAudio.Device.Channel, _Mapping]]] = ..., map: _Optional[_Iterable[_Union[DigitalAudio.Device.Map, _Mapping]]] = ..., is_custom_map: bool = ..., master_channel: _Optional[_Union[DigitalAudio.Device.Channel, _Mapping]] = ...) -> None: ...
        NAME_FIELD_NUMBER: _ClassVar[int]
        RENDERID_FIELD_NUMBER: _ClassVar[int]
        FORMATS_FIELD_NUMBER: _ClassVar[int]
        ROUTING_FIELD_NUMBER: _ClassVar[int]
        name: str
        renderID: str
        formats: _containers.RepeatedCompositeFieldContainer[DigitalAudio.Device.Format]
        routing: DigitalAudio.Device.Routing
        def __init__(self, name: _Optional[str] = ..., renderID: _Optional[str] = ..., formats: _Optional[_Iterable[_Union[DigitalAudio.Device.Format, _Mapping]]] = ..., routing: _Optional[_Union[DigitalAudio.Device.Routing, _Mapping]] = ...) -> None: ...
    def __init__(self) -> None: ...
