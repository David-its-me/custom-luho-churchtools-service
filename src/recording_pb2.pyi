import basicTypes_pb2 as _basicTypes_pb2
import digitalAudio_pb2 as _digitalAudio_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Recording(_message.Message):
    __slots__ = ()
    class SettingsDocument(_message.Message):
        __slots__ = ("streams",)
        STREAMS_FIELD_NUMBER: _ClassVar[int]
        streams: _containers.RepeatedCompositeFieldContainer[Recording.Stream]
        def __init__(self, streams: _Optional[_Iterable[_Union[Recording.Stream, _Mapping]]] = ...) -> None: ...
    class Stream(_message.Message):
        __slots__ = ("id", "encoder", "destinations", "audio_map", "isAudioCustomMapped", "output_screen")
        class Encoder(_message.Message):
            __slots__ = ("codec", "video_width", "video_height", "is_interlaced", "frameRate", "video_bitrate")
            class Codec(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                CODEC_AUTOMATIC: _ClassVar[Recording.Stream.Encoder.Codec]
                CODEC_H264: _ClassVar[Recording.Stream.Encoder.Codec]
                CODEC_H265: _ClassVar[Recording.Stream.Encoder.Codec]
                CODEC_PRORES_422_PROXY: _ClassVar[Recording.Stream.Encoder.Codec]
                CODEC_PRORES_422_LT: _ClassVar[Recording.Stream.Encoder.Codec]
                CODEC_PRORES_422: _ClassVar[Recording.Stream.Encoder.Codec]
                CODEC_PRORES_422_HQ: _ClassVar[Recording.Stream.Encoder.Codec]
                CODEC_PRORES_4444: _ClassVar[Recording.Stream.Encoder.Codec]
                CODEC_PRORES_4444_XQ: _ClassVar[Recording.Stream.Encoder.Codec]
                CODEC_HAP: _ClassVar[Recording.Stream.Encoder.Codec]
                CODEC_HAP_ALPHA: _ClassVar[Recording.Stream.Encoder.Codec]
                CODEC_HAP_Q: _ClassVar[Recording.Stream.Encoder.Codec]
                CODEC_HAP_Q_ALPHA: _ClassVar[Recording.Stream.Encoder.Codec]
                CODEC_NOTCH: _ClassVar[Recording.Stream.Encoder.Codec]
                CODEC_H264_SOFTWARE: _ClassVar[Recording.Stream.Encoder.Codec]
                CODEC_H265_SOFTWARE: _ClassVar[Recording.Stream.Encoder.Codec]
            CODEC_AUTOMATIC: Recording.Stream.Encoder.Codec
            CODEC_H264: Recording.Stream.Encoder.Codec
            CODEC_H265: Recording.Stream.Encoder.Codec
            CODEC_PRORES_422_PROXY: Recording.Stream.Encoder.Codec
            CODEC_PRORES_422_LT: Recording.Stream.Encoder.Codec
            CODEC_PRORES_422: Recording.Stream.Encoder.Codec
            CODEC_PRORES_422_HQ: Recording.Stream.Encoder.Codec
            CODEC_PRORES_4444: Recording.Stream.Encoder.Codec
            CODEC_PRORES_4444_XQ: Recording.Stream.Encoder.Codec
            CODEC_HAP: Recording.Stream.Encoder.Codec
            CODEC_HAP_ALPHA: Recording.Stream.Encoder.Codec
            CODEC_HAP_Q: Recording.Stream.Encoder.Codec
            CODEC_HAP_Q_ALPHA: Recording.Stream.Encoder.Codec
            CODEC_NOTCH: Recording.Stream.Encoder.Codec
            CODEC_H264_SOFTWARE: Recording.Stream.Encoder.Codec
            CODEC_H265_SOFTWARE: Recording.Stream.Encoder.Codec
            class FrameRate(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                FRAME_RATE_UNKNOWN: _ClassVar[Recording.Stream.Encoder.FrameRate]
                FRAME_RATE_24: _ClassVar[Recording.Stream.Encoder.FrameRate]
                FRAME_RATE_25: _ClassVar[Recording.Stream.Encoder.FrameRate]
                FRAME_RATE_29_97: _ClassVar[Recording.Stream.Encoder.FrameRate]
                FRAME_RATE_30: _ClassVar[Recording.Stream.Encoder.FrameRate]
                FRAME_RATE_50: _ClassVar[Recording.Stream.Encoder.FrameRate]
                FRAME_RATE_59_94: _ClassVar[Recording.Stream.Encoder.FrameRate]
                FRAME_RATE_60: _ClassVar[Recording.Stream.Encoder.FrameRate]
            FRAME_RATE_UNKNOWN: Recording.Stream.Encoder.FrameRate
            FRAME_RATE_24: Recording.Stream.Encoder.FrameRate
            FRAME_RATE_25: Recording.Stream.Encoder.FrameRate
            FRAME_RATE_29_97: Recording.Stream.Encoder.FrameRate
            FRAME_RATE_30: Recording.Stream.Encoder.FrameRate
            FRAME_RATE_50: Recording.Stream.Encoder.FrameRate
            FRAME_RATE_59_94: Recording.Stream.Encoder.FrameRate
            FRAME_RATE_60: Recording.Stream.Encoder.FrameRate
            CODEC_FIELD_NUMBER: _ClassVar[int]
            VIDEO_WIDTH_FIELD_NUMBER: _ClassVar[int]
            VIDEO_HEIGHT_FIELD_NUMBER: _ClassVar[int]
            IS_INTERLACED_FIELD_NUMBER: _ClassVar[int]
            FRAMERATE_FIELD_NUMBER: _ClassVar[int]
            VIDEO_BITRATE_FIELD_NUMBER: _ClassVar[int]
            codec: Recording.Stream.Encoder.Codec
            video_width: int
            video_height: int
            is_interlaced: bool
            frameRate: Recording.Stream.Encoder.FrameRate
            video_bitrate: int
            def __init__(self, codec: _Optional[_Union[Recording.Stream.Encoder.Codec, str]] = ..., video_width: _Optional[int] = ..., video_height: _Optional[int] = ..., is_interlaced: bool = ..., frameRate: _Optional[_Union[Recording.Stream.Encoder.FrameRate, str]] = ..., video_bitrate: _Optional[int] = ...) -> None: ...
        class OutputScreenSource(_message.Message):
            __slots__ = ("screen_id", "screen_name")
            SCREEN_ID_FIELD_NUMBER: _ClassVar[int]
            SCREEN_NAME_FIELD_NUMBER: _ClassVar[int]
            screen_id: _basicTypes_pb2.UUID
            screen_name: str
            def __init__(self, screen_id: _Optional[_Union[_basicTypes_pb2.UUID, _Mapping]] = ..., screen_name: _Optional[str] = ...) -> None: ...
        class DiskDestination(_message.Message):
            __slots__ = ("location", "container")
            class Container(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                CONTAINER_UNKNOWN: _ClassVar[Recording.Stream.DiskDestination.Container]
                CONTAINER_MOV: _ClassVar[Recording.Stream.DiskDestination.Container]
                CONTAINER_MP4: _ClassVar[Recording.Stream.DiskDestination.Container]
            CONTAINER_UNKNOWN: Recording.Stream.DiskDestination.Container
            CONTAINER_MOV: Recording.Stream.DiskDestination.Container
            CONTAINER_MP4: Recording.Stream.DiskDestination.Container
            LOCATION_FIELD_NUMBER: _ClassVar[int]
            CONTAINER_FIELD_NUMBER: _ClassVar[int]
            location: _basicTypes_pb2.URL
            container: Recording.Stream.DiskDestination.Container
            def __init__(self, location: _Optional[_Union[_basicTypes_pb2.URL, _Mapping]] = ..., container: _Optional[_Union[Recording.Stream.DiskDestination.Container, str]] = ...) -> None: ...
        class RTMPDestination(_message.Message):
            __slots__ = ("address", "key")
            ADDRESS_FIELD_NUMBER: _ClassVar[int]
            KEY_FIELD_NUMBER: _ClassVar[int]
            address: str
            key: str
            def __init__(self, address: _Optional[str] = ..., key: _Optional[str] = ...) -> None: ...
        class Destination(_message.Message):
            __slots__ = ("disk", "rtmp", "resi")
            class Resi(_message.Message):
                __slots__ = ("destination_group_id", "encoder_profile_id")
                DESTINATION_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
                ENCODER_PROFILE_ID_FIELD_NUMBER: _ClassVar[int]
                destination_group_id: _basicTypes_pb2.UUID
                encoder_profile_id: _basicTypes_pb2.UUID
                def __init__(self, destination_group_id: _Optional[_Union[_basicTypes_pb2.UUID, _Mapping]] = ..., encoder_profile_id: _Optional[_Union[_basicTypes_pb2.UUID, _Mapping]] = ...) -> None: ...
            DISK_FIELD_NUMBER: _ClassVar[int]
            RTMP_FIELD_NUMBER: _ClassVar[int]
            RESI_FIELD_NUMBER: _ClassVar[int]
            disk: Recording.Stream.DiskDestination
            rtmp: Recording.Stream.RTMPDestination
            resi: Recording.Stream.Destination.Resi
            def __init__(self, disk: _Optional[_Union[Recording.Stream.DiskDestination, _Mapping]] = ..., rtmp: _Optional[_Union[Recording.Stream.RTMPDestination, _Mapping]] = ..., resi: _Optional[_Union[Recording.Stream.Destination.Resi, _Mapping]] = ...) -> None: ...
        ID_FIELD_NUMBER: _ClassVar[int]
        ENCODER_FIELD_NUMBER: _ClassVar[int]
        DESTINATIONS_FIELD_NUMBER: _ClassVar[int]
        AUDIO_MAP_FIELD_NUMBER: _ClassVar[int]
        ISAUDIOCUSTOMMAPPED_FIELD_NUMBER: _ClassVar[int]
        OUTPUT_SCREEN_FIELD_NUMBER: _ClassVar[int]
        id: _basicTypes_pb2.UUID
        encoder: Recording.Stream.Encoder
        destinations: _containers.RepeatedCompositeFieldContainer[Recording.Stream.Destination]
        audio_map: _containers.RepeatedCompositeFieldContainer[_digitalAudio_pb2.DigitalAudio.Device.Map]
        isAudioCustomMapped: bool
        output_screen: Recording.Stream.OutputScreenSource
        def __init__(self, id: _Optional[_Union[_basicTypes_pb2.UUID, _Mapping]] = ..., encoder: _Optional[_Union[Recording.Stream.Encoder, _Mapping]] = ..., destinations: _Optional[_Iterable[_Union[Recording.Stream.Destination, _Mapping]]] = ..., audio_map: _Optional[_Iterable[_Union[_digitalAudio_pb2.DigitalAudio.Device.Map, _Mapping]]] = ..., isAudioCustomMapped: bool = ..., output_screen: _Optional[_Union[Recording.Stream.OutputScreenSource, _Mapping]] = ...) -> None: ...
    def __init__(self) -> None: ...
