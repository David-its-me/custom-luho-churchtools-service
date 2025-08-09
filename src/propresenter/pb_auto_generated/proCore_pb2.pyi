import propresenter.pb_auto_generated.effects_pb2 as _effects_pb2
import propresenter.pb_auto_generated.action_pb2 as _action_pb2
import propresenter.pb_auto_generated.graphicsData_pb2 as _graphicsData_pb2
import propresenter.pb_auto_generated.input_pb2 as _input_pb2
import propresenter.pb_auto_generated.recording_pb2 as _recording_pb2
import propresenter.pb_auto_generated.basicTypes_pb2 as _basicTypes_pb2
import propresenter.pb_auto_generated.cue_pb2 as _cue_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MediaMetadataRequestInfo(_message.Message):
    __slots__ = ("file_path", "time", "width", "height", "effects", "crop_insets", "native_rotation", "flipped_horizontally", "flipped_vertically")
    class NativeRotationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NATIVE_ROTATION_TYPE_ROTATE_STANDARD: _ClassVar[MediaMetadataRequestInfo.NativeRotationType]
        NATIVE_ROTATION_TYPE_ROTATE_90: _ClassVar[MediaMetadataRequestInfo.NativeRotationType]
        NATIVE_ROTATION_TYPE_ROTATE_180: _ClassVar[MediaMetadataRequestInfo.NativeRotationType]
        NATIVE_ROTATION_TYPE_ROTATE_270: _ClassVar[MediaMetadataRequestInfo.NativeRotationType]
    NATIVE_ROTATION_TYPE_ROTATE_STANDARD: MediaMetadataRequestInfo.NativeRotationType
    NATIVE_ROTATION_TYPE_ROTATE_90: MediaMetadataRequestInfo.NativeRotationType
    NATIVE_ROTATION_TYPE_ROTATE_180: MediaMetadataRequestInfo.NativeRotationType
    NATIVE_ROTATION_TYPE_ROTATE_270: MediaMetadataRequestInfo.NativeRotationType
    FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    EFFECTS_FIELD_NUMBER: _ClassVar[int]
    CROP_INSETS_FIELD_NUMBER: _ClassVar[int]
    NATIVE_ROTATION_FIELD_NUMBER: _ClassVar[int]
    FLIPPED_HORIZONTALLY_FIELD_NUMBER: _ClassVar[int]
    FLIPPED_VERTICALLY_FIELD_NUMBER: _ClassVar[int]
    file_path: str
    time: float
    width: int
    height: int
    effects: _containers.RepeatedCompositeFieldContainer[_effects_pb2.Effect]
    crop_insets: _graphicsData_pb2.Graphics.EdgeInsets
    native_rotation: MediaMetadataRequestInfo.NativeRotationType
    flipped_horizontally: bool
    flipped_vertically: bool
    def __init__(self, file_path: _Optional[str] = ..., time: _Optional[float] = ..., width: _Optional[int] = ..., height: _Optional[int] = ..., effects: _Optional[_Iterable[_Union[_effects_pb2.Effect, _Mapping]]] = ..., crop_insets: _Optional[_Union[_graphicsData_pb2.Graphics.EdgeInsets, _Mapping]] = ..., native_rotation: _Optional[_Union[MediaMetadataRequestInfo.NativeRotationType, str]] = ..., flipped_horizontally: bool = ..., flipped_vertically: bool = ...) -> None: ...

class MediaMetadataRequestResponse(_message.Message):
    __slots__ = ("metadata", "generated_bitmap_info")
    class Metadata(_message.Message):
        __slots__ = ("width", "height", "fps", "duration", "number_audio_channels", "codec", "artist", "title", "rotation", "content_type")
        class ContentType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            CONTENT_TYPE_UNKNOWN: _ClassVar[MediaMetadataRequestResponse.Metadata.ContentType]
            CONTENT_TYPE_AUDIO: _ClassVar[MediaMetadataRequestResponse.Metadata.ContentType]
            CONTENT_TYPE_IMAGE: _ClassVar[MediaMetadataRequestResponse.Metadata.ContentType]
            CONTENT_TYPE_VIDEO: _ClassVar[MediaMetadataRequestResponse.Metadata.ContentType]
        CONTENT_TYPE_UNKNOWN: MediaMetadataRequestResponse.Metadata.ContentType
        CONTENT_TYPE_AUDIO: MediaMetadataRequestResponse.Metadata.ContentType
        CONTENT_TYPE_IMAGE: MediaMetadataRequestResponse.Metadata.ContentType
        CONTENT_TYPE_VIDEO: MediaMetadataRequestResponse.Metadata.ContentType
        WIDTH_FIELD_NUMBER: _ClassVar[int]
        HEIGHT_FIELD_NUMBER: _ClassVar[int]
        FPS_FIELD_NUMBER: _ClassVar[int]
        DURATION_FIELD_NUMBER: _ClassVar[int]
        NUMBER_AUDIO_CHANNELS_FIELD_NUMBER: _ClassVar[int]
        CODEC_FIELD_NUMBER: _ClassVar[int]
        ARTIST_FIELD_NUMBER: _ClassVar[int]
        TITLE_FIELD_NUMBER: _ClassVar[int]
        ROTATION_FIELD_NUMBER: _ClassVar[int]
        CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
        width: int
        height: int
        fps: float
        duration: float
        number_audio_channels: int
        codec: str
        artist: str
        title: str
        rotation: float
        content_type: MediaMetadataRequestResponse.Metadata.ContentType
        def __init__(self, width: _Optional[int] = ..., height: _Optional[int] = ..., fps: _Optional[float] = ..., duration: _Optional[float] = ..., number_audio_channels: _Optional[int] = ..., codec: _Optional[str] = ..., artist: _Optional[str] = ..., title: _Optional[str] = ..., rotation: _Optional[float] = ..., content_type: _Optional[_Union[MediaMetadataRequestResponse.Metadata.ContentType, str]] = ...) -> None: ...
    class BitmapInfo(_message.Message):
        __slots__ = ("width", "height")
        WIDTH_FIELD_NUMBER: _ClassVar[int]
        HEIGHT_FIELD_NUMBER: _ClassVar[int]
        width: int
        height: int
        def __init__(self, width: _Optional[int] = ..., height: _Optional[int] = ...) -> None: ...
    METADATA_FIELD_NUMBER: _ClassVar[int]
    GENERATED_BITMAP_INFO_FIELD_NUMBER: _ClassVar[int]
    metadata: MediaMetadataRequestResponse.Metadata
    generated_bitmap_info: MediaMetadataRequestResponse.BitmapInfo
    def __init__(self, metadata: _Optional[_Union[MediaMetadataRequestResponse.Metadata, _Mapping]] = ..., generated_bitmap_info: _Optional[_Union[MediaMetadataRequestResponse.BitmapInfo, _Mapping]] = ...) -> None: ...

class TriggerSource(_message.Message):
    __slots__ = ("library_location", "playlist_location")
    class Library(_message.Message):
        __slots__ = ("path", "presentation_name")
        PATH_FIELD_NUMBER: _ClassVar[int]
        PRESENTATION_NAME_FIELD_NUMBER: _ClassVar[int]
        path: str
        presentation_name: str
        def __init__(self, path: _Optional[str] = ..., presentation_name: _Optional[str] = ...) -> None: ...
    class Playlist(_message.Message):
        __slots__ = ("identifier", "item_identifier")
        IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
        ITEM_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
        identifier: _basicTypes_pb2.UUID
        item_identifier: _basicTypes_pb2.UUID
        def __init__(self, identifier: _Optional[_Union[_basicTypes_pb2.UUID, _Mapping]] = ..., item_identifier: _Optional[_Union[_basicTypes_pb2.UUID, _Mapping]] = ...) -> None: ...
    LIBRARY_LOCATION_FIELD_NUMBER: _ClassVar[int]
    PLAYLIST_LOCATION_FIELD_NUMBER: _ClassVar[int]
    library_location: TriggerSource.Library
    playlist_location: TriggerSource.Playlist
    def __init__(self, library_location: _Optional[_Union[TriggerSource.Library, _Mapping]] = ..., playlist_location: _Optional[_Union[TriggerSource.Playlist, _Mapping]] = ...) -> None: ...

class NetworkIdentifier(_message.Message):
    __slots__ = ("identifiers",)
    class IndexOrName(_message.Message):
        __slots__ = ("index", "name")
        INDEX_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        index: int
        name: str
        def __init__(self, index: _Optional[int] = ..., name: _Optional[str] = ...) -> None: ...
    IDENTIFIERS_FIELD_NUMBER: _ClassVar[int]
    identifiers: _containers.RepeatedCompositeFieldContainer[NetworkIdentifier.IndexOrName]
    def __init__(self, identifiers: _Optional[_Iterable[_Union[NetworkIdentifier.IndexOrName, _Mapping]]] = ...) -> None: ...

class TriggerOptions(_message.Message):
    __slots__ = ("content_destination", "suppress_auto_start_video", "suppress_media_background", "force_retrigger", "reset_chord_chart", "from_playlist_library", "from_timeline", "ignore_analytics", "start_position", "trigger_source", "network_identifier")
    class ContentDestination(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CONTENT_DESTINATION_GLOBAL: _ClassVar[TriggerOptions.ContentDestination]
        CONTENT_DESTINATION_ANNOUNCEMENTS: _ClassVar[TriggerOptions.ContentDestination]
    CONTENT_DESTINATION_GLOBAL: TriggerOptions.ContentDestination
    CONTENT_DESTINATION_ANNOUNCEMENTS: TriggerOptions.ContentDestination
    CONTENT_DESTINATION_FIELD_NUMBER: _ClassVar[int]
    SUPPRESS_AUTO_START_VIDEO_FIELD_NUMBER: _ClassVar[int]
    SUPPRESS_MEDIA_BACKGROUND_FIELD_NUMBER: _ClassVar[int]
    FORCE_RETRIGGER_FIELD_NUMBER: _ClassVar[int]
    RESET_CHORD_CHART_FIELD_NUMBER: _ClassVar[int]
    FROM_PLAYLIST_LIBRARY_FIELD_NUMBER: _ClassVar[int]
    FROM_TIMELINE_FIELD_NUMBER: _ClassVar[int]
    IGNORE_ANALYTICS_FIELD_NUMBER: _ClassVar[int]
    START_POSITION_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_SOURCE_FIELD_NUMBER: _ClassVar[int]
    NETWORK_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    content_destination: TriggerOptions.ContentDestination
    suppress_auto_start_video: bool
    suppress_media_background: bool
    force_retrigger: bool
    reset_chord_chart: bool
    from_playlist_library: bool
    from_timeline: bool
    ignore_analytics: bool
    start_position: float
    trigger_source: TriggerSource
    network_identifier: NetworkIdentifier
    def __init__(self, content_destination: _Optional[_Union[TriggerOptions.ContentDestination, str]] = ..., suppress_auto_start_video: bool = ..., suppress_media_background: bool = ..., force_retrigger: bool = ..., reset_chord_chart: bool = ..., from_playlist_library: bool = ..., from_timeline: bool = ..., ignore_analytics: bool = ..., start_position: _Optional[float] = ..., trigger_source: _Optional[_Union[TriggerSource, _Mapping]] = ..., network_identifier: _Optional[_Union[NetworkIdentifier, _Mapping]] = ...) -> None: ...

class ControlTransport(_message.Message):
    __slots__ = ("play", "pause", "rewind", "fastforward", "skip_back", "skip_forward", "step_back", "step_forward", "go_to_start", "go_to_end", "jump_to_time", "jump_to_percent", "mark_in", "mark_out", "set_scale_mode", "set_flipped_mode", "set_play_rate", "set_rotation", "toggle_playback", "set_effects", "update_effect", "begin_scrub", "end_scrub", "scrub_to_time", "scrub_to_percent", "set_audio_fade", "set_audio_properties")
    class PlayControlType(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class PauseControlType(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class RewindControlType(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class FastForwardControlType(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class SkipBackControlType(_message.Message):
        __slots__ = ("offset",)
        OFFSET_FIELD_NUMBER: _ClassVar[int]
        offset: float
        def __init__(self, offset: _Optional[float] = ...) -> None: ...
    class SkipForwardControlType(_message.Message):
        __slots__ = ("offset",)
        OFFSET_FIELD_NUMBER: _ClassVar[int]
        offset: float
        def __init__(self, offset: _Optional[float] = ...) -> None: ...
    class StepBackControlType(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class StepForwardControlType(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class GoToStartControlType(_message.Message):
        __slots__ = ("offset",)
        OFFSET_FIELD_NUMBER: _ClassVar[int]
        offset: float
        def __init__(self, offset: _Optional[float] = ...) -> None: ...
    class GoToEndControlType(_message.Message):
        __slots__ = ("offset",)
        OFFSET_FIELD_NUMBER: _ClassVar[int]
        offset: float
        def __init__(self, offset: _Optional[float] = ...) -> None: ...
    class JumpToTimeControlType(_message.Message):
        __slots__ = ("time",)
        TIME_FIELD_NUMBER: _ClassVar[int]
        time: float
        def __init__(self, time: _Optional[float] = ...) -> None: ...
    class JumpToPercentControlType(_message.Message):
        __slots__ = ("percent",)
        PERCENT_FIELD_NUMBER: _ClassVar[int]
        percent: float
        def __init__(self, percent: _Optional[float] = ...) -> None: ...
    class MarkInPointControlType(_message.Message):
        __slots__ = ("time",)
        TIME_FIELD_NUMBER: _ClassVar[int]
        time: float
        def __init__(self, time: _Optional[float] = ...) -> None: ...
    class MarkOutPointControlType(_message.Message):
        __slots__ = ("time",)
        TIME_FIELD_NUMBER: _ClassVar[int]
        time: float
        def __init__(self, time: _Optional[float] = ...) -> None: ...
    class SetScaleModeControlType(_message.Message):
        __slots__ = ("mode", "alignment")
        class ScaleBehavior(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            SCALE_BEHAVIOR_FIT: _ClassVar[ControlTransport.SetScaleModeControlType.ScaleBehavior]
            SCALE_BEHAVIOR_FILL: _ClassVar[ControlTransport.SetScaleModeControlType.ScaleBehavior]
            SCALE_BEHAVIOR_STRETCH: _ClassVar[ControlTransport.SetScaleModeControlType.ScaleBehavior]
            SCALE_BEHAVIOR_CUSTOM: _ClassVar[ControlTransport.SetScaleModeControlType.ScaleBehavior]
        SCALE_BEHAVIOR_FIT: ControlTransport.SetScaleModeControlType.ScaleBehavior
        SCALE_BEHAVIOR_FILL: ControlTransport.SetScaleModeControlType.ScaleBehavior
        SCALE_BEHAVIOR_STRETCH: ControlTransport.SetScaleModeControlType.ScaleBehavior
        SCALE_BEHAVIOR_CUSTOM: ControlTransport.SetScaleModeControlType.ScaleBehavior
        class ScaleAlignment(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            SCALE_ALIGNMENT_MIDDLE_CENTER: _ClassVar[ControlTransport.SetScaleModeControlType.ScaleAlignment]
            SCALE_ALIGNMENT_TOP_LEFT: _ClassVar[ControlTransport.SetScaleModeControlType.ScaleAlignment]
            SCALE_ALIGNMENT_TOP_CENTER: _ClassVar[ControlTransport.SetScaleModeControlType.ScaleAlignment]
            SCALE_ALIGNMENT_TOP_RIGHT: _ClassVar[ControlTransport.SetScaleModeControlType.ScaleAlignment]
            SCALE_ALIGNMENT_MIDDLE_RIGHT: _ClassVar[ControlTransport.SetScaleModeControlType.ScaleAlignment]
            SCALE_ALIGNMENT_BOTTOM_RIGHT: _ClassVar[ControlTransport.SetScaleModeControlType.ScaleAlignment]
            SCALE_ALIGNMENT_BOTTOM_CENTER: _ClassVar[ControlTransport.SetScaleModeControlType.ScaleAlignment]
            SCALE_ALIGNMENT_BOTTOM_LEFT: _ClassVar[ControlTransport.SetScaleModeControlType.ScaleAlignment]
            SCALE_ALIGNMENT_MIDDLE_LEFT: _ClassVar[ControlTransport.SetScaleModeControlType.ScaleAlignment]
        SCALE_ALIGNMENT_MIDDLE_CENTER: ControlTransport.SetScaleModeControlType.ScaleAlignment
        SCALE_ALIGNMENT_TOP_LEFT: ControlTransport.SetScaleModeControlType.ScaleAlignment
        SCALE_ALIGNMENT_TOP_CENTER: ControlTransport.SetScaleModeControlType.ScaleAlignment
        SCALE_ALIGNMENT_TOP_RIGHT: ControlTransport.SetScaleModeControlType.ScaleAlignment
        SCALE_ALIGNMENT_MIDDLE_RIGHT: ControlTransport.SetScaleModeControlType.ScaleAlignment
        SCALE_ALIGNMENT_BOTTOM_RIGHT: ControlTransport.SetScaleModeControlType.ScaleAlignment
        SCALE_ALIGNMENT_BOTTOM_CENTER: ControlTransport.SetScaleModeControlType.ScaleAlignment
        SCALE_ALIGNMENT_BOTTOM_LEFT: ControlTransport.SetScaleModeControlType.ScaleAlignment
        SCALE_ALIGNMENT_MIDDLE_LEFT: ControlTransport.SetScaleModeControlType.ScaleAlignment
        MODE_FIELD_NUMBER: _ClassVar[int]
        ALIGNMENT_FIELD_NUMBER: _ClassVar[int]
        mode: ControlTransport.SetScaleModeControlType.ScaleBehavior
        alignment: ControlTransport.SetScaleModeControlType.ScaleAlignment
        def __init__(self, mode: _Optional[_Union[ControlTransport.SetScaleModeControlType.ScaleBehavior, str]] = ..., alignment: _Optional[_Union[ControlTransport.SetScaleModeControlType.ScaleAlignment, str]] = ...) -> None: ...
    class SetFlippedModeControlType(_message.Message):
        __slots__ = ("horizontal", "vertical")
        HORIZONTAL_FIELD_NUMBER: _ClassVar[int]
        VERTICAL_FIELD_NUMBER: _ClassVar[int]
        horizontal: bool
        vertical: bool
        def __init__(self, horizontal: bool = ..., vertical: bool = ...) -> None: ...
    class SetPlayRateControlType(_message.Message):
        __slots__ = ("play_rate",)
        PLAY_RATE_FIELD_NUMBER: _ClassVar[int]
        play_rate: float
        def __init__(self, play_rate: _Optional[float] = ...) -> None: ...
    class SetNativeRotationControlType(_message.Message):
        __slots__ = ("rotation",)
        class NativeRotationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            NATIVE_ROTATION_TYPE_ROTATE_STANDARD: _ClassVar[ControlTransport.SetNativeRotationControlType.NativeRotationType]
            NATIVE_ROTATION_TYPE_ROTATE_90: _ClassVar[ControlTransport.SetNativeRotationControlType.NativeRotationType]
            NATIVE_ROTATION_TYPE_ROTATE_180: _ClassVar[ControlTransport.SetNativeRotationControlType.NativeRotationType]
            NATIVE_ROTATION_TYPE_ROTATE_270: _ClassVar[ControlTransport.SetNativeRotationControlType.NativeRotationType]
        NATIVE_ROTATION_TYPE_ROTATE_STANDARD: ControlTransport.SetNativeRotationControlType.NativeRotationType
        NATIVE_ROTATION_TYPE_ROTATE_90: ControlTransport.SetNativeRotationControlType.NativeRotationType
        NATIVE_ROTATION_TYPE_ROTATE_180: ControlTransport.SetNativeRotationControlType.NativeRotationType
        NATIVE_ROTATION_TYPE_ROTATE_270: ControlTransport.SetNativeRotationControlType.NativeRotationType
        ROTATION_FIELD_NUMBER: _ClassVar[int]
        rotation: ControlTransport.SetNativeRotationControlType.NativeRotationType
        def __init__(self, rotation: _Optional[_Union[ControlTransport.SetNativeRotationControlType.NativeRotationType, str]] = ...) -> None: ...
    class TogglePlaybackControlType(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class SetEffectsControlType(_message.Message):
        __slots__ = ("effects",)
        EFFECTS_FIELD_NUMBER: _ClassVar[int]
        effects: _containers.RepeatedCompositeFieldContainer[_effects_pb2.Effect]
        def __init__(self, effects: _Optional[_Iterable[_Union[_effects_pb2.Effect, _Mapping]]] = ...) -> None: ...
    class UpdateEffectControlType(_message.Message):
        __slots__ = ("effect",)
        EFFECT_FIELD_NUMBER: _ClassVar[int]
        effect: _effects_pb2.Effect
        def __init__(self, effect: _Optional[_Union[_effects_pb2.Effect, _Mapping]] = ...) -> None: ...
    class BeginScrubControlType(_message.Message):
        __slots__ = ("time",)
        TIME_FIELD_NUMBER: _ClassVar[int]
        time: float
        def __init__(self, time: _Optional[float] = ...) -> None: ...
    class EndScrubControlType(_message.Message):
        __slots__ = ("time",)
        TIME_FIELD_NUMBER: _ClassVar[int]
        time: float
        def __init__(self, time: _Optional[float] = ...) -> None: ...
    class ScrubToTimeControlType(_message.Message):
        __slots__ = ("time",)
        TIME_FIELD_NUMBER: _ClassVar[int]
        time: float
        def __init__(self, time: _Optional[float] = ...) -> None: ...
    class ScrubToPercentControlType(_message.Message):
        __slots__ = ("percent",)
        PERCENT_FIELD_NUMBER: _ClassVar[int]
        percent: float
        def __init__(self, percent: _Optional[float] = ...) -> None: ...
    class SetAudioFadeType(_message.Message):
        __slots__ = ("fade_in_duration", "fade_out_duration", "should_fade_in", "should_fade_out")
        FADE_IN_DURATION_FIELD_NUMBER: _ClassVar[int]
        FADE_OUT_DURATION_FIELD_NUMBER: _ClassVar[int]
        SHOULD_FADE_IN_FIELD_NUMBER: _ClassVar[int]
        SHOULD_FADE_OUT_FIELD_NUMBER: _ClassVar[int]
        fade_in_duration: float
        fade_out_duration: float
        should_fade_in: bool
        should_fade_out: bool
        def __init__(self, fade_in_duration: _Optional[float] = ..., fade_out_duration: _Optional[float] = ..., should_fade_in: bool = ..., should_fade_out: bool = ...) -> None: ...
    class SetAudioPropertiesType(_message.Message):
        __slots__ = ("audio_properties", "solo")
        AUDIO_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
        SOLO_FIELD_NUMBER: _ClassVar[int]
        audio_properties: _graphicsData_pb2.Media.AudioProperties
        solo: _containers.RepeatedScalarFieldContainer[bool]
        def __init__(self, audio_properties: _Optional[_Union[_graphicsData_pb2.Media.AudioProperties, _Mapping]] = ..., solo: _Optional[_Iterable[bool]] = ...) -> None: ...
    PLAY_FIELD_NUMBER: _ClassVar[int]
    PAUSE_FIELD_NUMBER: _ClassVar[int]
    REWIND_FIELD_NUMBER: _ClassVar[int]
    FASTFORWARD_FIELD_NUMBER: _ClassVar[int]
    SKIP_BACK_FIELD_NUMBER: _ClassVar[int]
    SKIP_FORWARD_FIELD_NUMBER: _ClassVar[int]
    STEP_BACK_FIELD_NUMBER: _ClassVar[int]
    STEP_FORWARD_FIELD_NUMBER: _ClassVar[int]
    GO_TO_START_FIELD_NUMBER: _ClassVar[int]
    GO_TO_END_FIELD_NUMBER: _ClassVar[int]
    JUMP_TO_TIME_FIELD_NUMBER: _ClassVar[int]
    JUMP_TO_PERCENT_FIELD_NUMBER: _ClassVar[int]
    MARK_IN_FIELD_NUMBER: _ClassVar[int]
    MARK_OUT_FIELD_NUMBER: _ClassVar[int]
    SET_SCALE_MODE_FIELD_NUMBER: _ClassVar[int]
    SET_FLIPPED_MODE_FIELD_NUMBER: _ClassVar[int]
    SET_PLAY_RATE_FIELD_NUMBER: _ClassVar[int]
    SET_ROTATION_FIELD_NUMBER: _ClassVar[int]
    TOGGLE_PLAYBACK_FIELD_NUMBER: _ClassVar[int]
    SET_EFFECTS_FIELD_NUMBER: _ClassVar[int]
    UPDATE_EFFECT_FIELD_NUMBER: _ClassVar[int]
    BEGIN_SCRUB_FIELD_NUMBER: _ClassVar[int]
    END_SCRUB_FIELD_NUMBER: _ClassVar[int]
    SCRUB_TO_TIME_FIELD_NUMBER: _ClassVar[int]
    SCRUB_TO_PERCENT_FIELD_NUMBER: _ClassVar[int]
    SET_AUDIO_FADE_FIELD_NUMBER: _ClassVar[int]
    SET_AUDIO_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    play: ControlTransport.PlayControlType
    pause: ControlTransport.PauseControlType
    rewind: ControlTransport.RewindControlType
    fastforward: ControlTransport.FastForwardControlType
    skip_back: ControlTransport.SkipBackControlType
    skip_forward: ControlTransport.SkipForwardControlType
    step_back: ControlTransport.StepBackControlType
    step_forward: ControlTransport.StepForwardControlType
    go_to_start: ControlTransport.GoToStartControlType
    go_to_end: ControlTransport.GoToEndControlType
    jump_to_time: ControlTransport.JumpToTimeControlType
    jump_to_percent: ControlTransport.JumpToPercentControlType
    mark_in: ControlTransport.MarkInPointControlType
    mark_out: ControlTransport.MarkOutPointControlType
    set_scale_mode: ControlTransport.SetScaleModeControlType
    set_flipped_mode: ControlTransport.SetFlippedModeControlType
    set_play_rate: ControlTransport.SetPlayRateControlType
    set_rotation: ControlTransport.SetNativeRotationControlType
    toggle_playback: ControlTransport.TogglePlaybackControlType
    set_effects: ControlTransport.SetEffectsControlType
    update_effect: ControlTransport.UpdateEffectControlType
    begin_scrub: ControlTransport.BeginScrubControlType
    end_scrub: ControlTransport.EndScrubControlType
    scrub_to_time: ControlTransport.ScrubToTimeControlType
    scrub_to_percent: ControlTransport.ScrubToPercentControlType
    set_audio_fade: ControlTransport.SetAudioFadeType
    set_audio_properties: ControlTransport.SetAudioPropertiesType
    def __init__(self, play: _Optional[_Union[ControlTransport.PlayControlType, _Mapping]] = ..., pause: _Optional[_Union[ControlTransport.PauseControlType, _Mapping]] = ..., rewind: _Optional[_Union[ControlTransport.RewindControlType, _Mapping]] = ..., fastforward: _Optional[_Union[ControlTransport.FastForwardControlType, _Mapping]] = ..., skip_back: _Optional[_Union[ControlTransport.SkipBackControlType, _Mapping]] = ..., skip_forward: _Optional[_Union[ControlTransport.SkipForwardControlType, _Mapping]] = ..., step_back: _Optional[_Union[ControlTransport.StepBackControlType, _Mapping]] = ..., step_forward: _Optional[_Union[ControlTransport.StepForwardControlType, _Mapping]] = ..., go_to_start: _Optional[_Union[ControlTransport.GoToStartControlType, _Mapping]] = ..., go_to_end: _Optional[_Union[ControlTransport.GoToEndControlType, _Mapping]] = ..., jump_to_time: _Optional[_Union[ControlTransport.JumpToTimeControlType, _Mapping]] = ..., jump_to_percent: _Optional[_Union[ControlTransport.JumpToPercentControlType, _Mapping]] = ..., mark_in: _Optional[_Union[ControlTransport.MarkInPointControlType, _Mapping]] = ..., mark_out: _Optional[_Union[ControlTransport.MarkOutPointControlType, _Mapping]] = ..., set_scale_mode: _Optional[_Union[ControlTransport.SetScaleModeControlType, _Mapping]] = ..., set_flipped_mode: _Optional[_Union[ControlTransport.SetFlippedModeControlType, _Mapping]] = ..., set_play_rate: _Optional[_Union[ControlTransport.SetPlayRateControlType, _Mapping]] = ..., set_rotation: _Optional[_Union[ControlTransport.SetNativeRotationControlType, _Mapping]] = ..., toggle_playback: _Optional[_Union[ControlTransport.TogglePlaybackControlType, _Mapping]] = ..., set_effects: _Optional[_Union[ControlTransport.SetEffectsControlType, _Mapping]] = ..., update_effect: _Optional[_Union[ControlTransport.UpdateEffectControlType, _Mapping]] = ..., begin_scrub: _Optional[_Union[ControlTransport.BeginScrubControlType, _Mapping]] = ..., end_scrub: _Optional[_Union[ControlTransport.EndScrubControlType, _Mapping]] = ..., scrub_to_time: _Optional[_Union[ControlTransport.ScrubToTimeControlType, _Mapping]] = ..., scrub_to_percent: _Optional[_Union[ControlTransport.ScrubToPercentControlType, _Mapping]] = ..., set_audio_fade: _Optional[_Union[ControlTransport.SetAudioFadeType, _Mapping]] = ..., set_audio_properties: _Optional[_Union[ControlTransport.SetAudioPropertiesType, _Mapping]] = ...) -> None: ...

class AudioInputSettings(_message.Message):
    __slots__ = ("inputs", "transitionTime")
    INPUTS_FIELD_NUMBER: _ClassVar[int]
    TRANSITIONTIME_FIELD_NUMBER: _ClassVar[int]
    inputs: _containers.RepeatedCompositeFieldContainer[_input_pb2.AudioInput]
    transitionTime: float
    def __init__(self, inputs: _Optional[_Iterable[_Union[_input_pb2.AudioInput, _Mapping]]] = ..., transitionTime: _Optional[float] = ...) -> None: ...

class VideoInputSettings(_message.Message):
    __slots__ = ("inputs",)
    INPUTS_FIELD_NUMBER: _ClassVar[int]
    inputs: _containers.RepeatedCompositeFieldContainer[_input_pb2.VideoInput]
    def __init__(self, inputs: _Optional[_Iterable[_Union[_input_pb2.VideoInput, _Mapping]]] = ...) -> None: ...

class RecordRequest(_message.Message):
    __slots__ = ("stream", "working_directory", "resi")
    class Resi(_message.Message):
        __slots__ = ("gop", "segmentSize", "destinationGroupId", "bufSize", "minRate", "maxRate", "eventName", "social_description")
        GOP_FIELD_NUMBER: _ClassVar[int]
        SEGMENTSIZE_FIELD_NUMBER: _ClassVar[int]
        DESTINATIONGROUPID_FIELD_NUMBER: _ClassVar[int]
        BUFSIZE_FIELD_NUMBER: _ClassVar[int]
        MINRATE_FIELD_NUMBER: _ClassVar[int]
        MAXRATE_FIELD_NUMBER: _ClassVar[int]
        EVENTNAME_FIELD_NUMBER: _ClassVar[int]
        SOCIAL_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        gop: int
        segmentSize: float
        destinationGroupId: str
        bufSize: int
        minRate: int
        maxRate: int
        eventName: str
        social_description: str
        def __init__(self, gop: _Optional[int] = ..., segmentSize: _Optional[float] = ..., destinationGroupId: _Optional[str] = ..., bufSize: _Optional[int] = ..., minRate: _Optional[int] = ..., maxRate: _Optional[int] = ..., eventName: _Optional[str] = ..., social_description: _Optional[str] = ...) -> None: ...
    STREAM_FIELD_NUMBER: _ClassVar[int]
    WORKING_DIRECTORY_FIELD_NUMBER: _ClassVar[int]
    RESI_FIELD_NUMBER: _ClassVar[int]
    stream: _recording_pb2.Recording.Stream
    working_directory: _basicTypes_pb2.URL
    resi: RecordRequest.Resi
    def __init__(self, stream: _Optional[_Union[_recording_pb2.Recording.Stream, _Mapping]] = ..., working_directory: _Optional[_Union[_basicTypes_pb2.URL, _Mapping]] = ..., resi: _Optional[_Union[RecordRequest.Resi, _Mapping]] = ...) -> None: ...

class TextSegmentRequest(_message.Message):
    __slots__ = ("segments", "start_position")
    class Segment(_message.Message):
        __slots__ = ("index", "size")
        INDEX_FIELD_NUMBER: _ClassVar[int]
        SIZE_FIELD_NUMBER: _ClassVar[int]
        index: int
        size: float
        def __init__(self, index: _Optional[int] = ..., size: _Optional[float] = ...) -> None: ...
    SEGMENTS_FIELD_NUMBER: _ClassVar[int]
    START_POSITION_FIELD_NUMBER: _ClassVar[int]
    segments: _containers.RepeatedCompositeFieldContainer[TextSegmentRequest.Segment]
    start_position: float
    def __init__(self, segments: _Optional[_Iterable[_Union[TextSegmentRequest.Segment, _Mapping]]] = ..., start_position: _Optional[float] = ...) -> None: ...

class ProClockSource(_message.Message):
    __slots__ = ("uuid", "name", "connected", "active", "type")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_UNKOWN: _ClassVar[ProClockSource.Type]
        TYPE_INPUT: _ClassVar[ProClockSource.Type]
        TYPE_OUTPUT: _ClassVar[ProClockSource.Type]
    TYPE_UNKOWN: ProClockSource.Type
    TYPE_INPUT: ProClockSource.Type
    TYPE_OUTPUT: ProClockSource.Type
    UUID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CONNECTED_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    uuid: str
    name: str
    connected: bool
    active: bool
    type: ProClockSource.Type
    def __init__(self, uuid: _Optional[str] = ..., name: _Optional[str] = ..., connected: bool = ..., active: bool = ..., type: _Optional[_Union[ProClockSource.Type, str]] = ...) -> None: ...

class TimedPlayback(_message.Message):
    __slots__ = ("sequence", "timing")
    class Sequence(_message.Message):
        __slots__ = ("sequence", "content_destination")
        class ContentDestination(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            CONTENT_DESTINATION_GLOBAL: _ClassVar[TimedPlayback.Sequence.ContentDestination]
            CONTENT_DESTINATION_ANNOUNCEMENTS: _ClassVar[TimedPlayback.Sequence.ContentDestination]
        CONTENT_DESTINATION_GLOBAL: TimedPlayback.Sequence.ContentDestination
        CONTENT_DESTINATION_ANNOUNCEMENTS: TimedPlayback.Sequence.ContentDestination
        class SequenceItem(_message.Message):
            __slots__ = ("identifier", "time", "trigger_source", "content_destination", "cue", "action")
            class ContentDestination(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                CONTENT_DESTINATION_GLOBAL: _ClassVar[TimedPlayback.Sequence.SequenceItem.ContentDestination]
                CONTENT_DESTINATION_ANNOUNCEMENTS: _ClassVar[TimedPlayback.Sequence.SequenceItem.ContentDestination]
            CONTENT_DESTINATION_GLOBAL: TimedPlayback.Sequence.SequenceItem.ContentDestination
            CONTENT_DESTINATION_ANNOUNCEMENTS: TimedPlayback.Sequence.SequenceItem.ContentDestination
            IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
            TIME_FIELD_NUMBER: _ClassVar[int]
            TRIGGER_SOURCE_FIELD_NUMBER: _ClassVar[int]
            CONTENT_DESTINATION_FIELD_NUMBER: _ClassVar[int]
            CUE_FIELD_NUMBER: _ClassVar[int]
            ACTION_FIELD_NUMBER: _ClassVar[int]
            identifier: _basicTypes_pb2.UUID
            time: float
            trigger_source: TriggerSource
            content_destination: TimedPlayback.Sequence.SequenceItem.ContentDestination
            cue: _cue_pb2.Cue
            action: _action_pb2.Action
            def __init__(self, identifier: _Optional[_Union[_basicTypes_pb2.UUID, _Mapping]] = ..., time: _Optional[float] = ..., trigger_source: _Optional[_Union[TriggerSource, _Mapping]] = ..., content_destination: _Optional[_Union[TimedPlayback.Sequence.SequenceItem.ContentDestination, str]] = ..., cue: _Optional[_Union[_cue_pb2.Cue, _Mapping]] = ..., action: _Optional[_Union[_action_pb2.Action, _Mapping]] = ...) -> None: ...
        SEQUENCE_FIELD_NUMBER: _ClassVar[int]
        CONTENT_DESTINATION_FIELD_NUMBER: _ClassVar[int]
        sequence: _containers.RepeatedCompositeFieldContainer[TimedPlayback.Sequence.SequenceItem]
        content_destination: TimedPlayback.Sequence.ContentDestination
        def __init__(self, sequence: _Optional[_Iterable[_Union[TimedPlayback.Sequence.SequenceItem, _Mapping]]] = ..., content_destination: _Optional[_Union[TimedPlayback.Sequence.ContentDestination, str]] = ...) -> None: ...
    class Timing(_message.Message):
        __slots__ = ("layer_transport", "smpte_timecode", "internal")
        class LayerTransport(_message.Message):
            __slots__ = ("layer",)
            LAYER_FIELD_NUMBER: _ClassVar[int]
            layer: int
            def __init__(self, layer: _Optional[int] = ...) -> None: ...
        class SMPTETimecode(_message.Message):
            __slots__ = ("device_identifier", "channel", "format")
            class Format(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                FORMAT_24_FPS: _ClassVar[TimedPlayback.Timing.SMPTETimecode.Format]
                FORMAT_25_FPS: _ClassVar[TimedPlayback.Timing.SMPTETimecode.Format]
                FORMAT_29_97_FPS: _ClassVar[TimedPlayback.Timing.SMPTETimecode.Format]
                FORMAT_30_FPS: _ClassVar[TimedPlayback.Timing.SMPTETimecode.Format]
            FORMAT_24_FPS: TimedPlayback.Timing.SMPTETimecode.Format
            FORMAT_25_FPS: TimedPlayback.Timing.SMPTETimecode.Format
            FORMAT_29_97_FPS: TimedPlayback.Timing.SMPTETimecode.Format
            FORMAT_30_FPS: TimedPlayback.Timing.SMPTETimecode.Format
            DEVICE_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
            CHANNEL_FIELD_NUMBER: _ClassVar[int]
            FORMAT_FIELD_NUMBER: _ClassVar[int]
            device_identifier: str
            channel: int
            format: TimedPlayback.Timing.SMPTETimecode.Format
            def __init__(self, device_identifier: _Optional[str] = ..., channel: _Optional[int] = ..., format: _Optional[_Union[TimedPlayback.Timing.SMPTETimecode.Format, str]] = ...) -> None: ...
        class Internal(_message.Message):
            __slots__ = ("duration", "should_loop")
            DURATION_FIELD_NUMBER: _ClassVar[int]
            SHOULD_LOOP_FIELD_NUMBER: _ClassVar[int]
            duration: float
            should_loop: bool
            def __init__(self, duration: _Optional[float] = ..., should_loop: bool = ...) -> None: ...
        LAYER_TRANSPORT_FIELD_NUMBER: _ClassVar[int]
        SMPTE_TIMECODE_FIELD_NUMBER: _ClassVar[int]
        INTERNAL_FIELD_NUMBER: _ClassVar[int]
        layer_transport: TimedPlayback.Timing.LayerTransport
        smpte_timecode: TimedPlayback.Timing.SMPTETimecode
        internal: TimedPlayback.Timing.Internal
        def __init__(self, layer_transport: _Optional[_Union[TimedPlayback.Timing.LayerTransport, _Mapping]] = ..., smpte_timecode: _Optional[_Union[TimedPlayback.Timing.SMPTETimecode, _Mapping]] = ..., internal: _Optional[_Union[TimedPlayback.Timing.Internal, _Mapping]] = ...) -> None: ...
    class Update(_message.Message):
        __slots__ = ("play", "record", "pause", "reset", "jump_to_time", "start_scrub", "end_scrub", "duration", "loop", "update_sequence", "monitor_source")
        class Play(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class Record(_message.Message):
            __slots__ = ("is_recording",)
            IS_RECORDING_FIELD_NUMBER: _ClassVar[int]
            is_recording: bool
            def __init__(self, is_recording: bool = ...) -> None: ...
        class Pause(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class Reset(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class JumpToTime(_message.Message):
            __slots__ = ("time",)
            TIME_FIELD_NUMBER: _ClassVar[int]
            time: float
            def __init__(self, time: _Optional[float] = ...) -> None: ...
        class StartScrub(_message.Message):
            __slots__ = ("time",)
            TIME_FIELD_NUMBER: _ClassVar[int]
            time: float
            def __init__(self, time: _Optional[float] = ...) -> None: ...
        class EndScrub(_message.Message):
            __slots__ = ("time",)
            TIME_FIELD_NUMBER: _ClassVar[int]
            time: float
            def __init__(self, time: _Optional[float] = ...) -> None: ...
        class Duration(_message.Message):
            __slots__ = ("duration",)
            DURATION_FIELD_NUMBER: _ClassVar[int]
            duration: float
            def __init__(self, duration: _Optional[float] = ...) -> None: ...
        class Loop(_message.Message):
            __slots__ = ("loop",)
            LOOP_FIELD_NUMBER: _ClassVar[int]
            loop: bool
            def __init__(self, loop: bool = ...) -> None: ...
        class MonitorSource(_message.Message):
            __slots__ = ("enable",)
            ENABLE_FIELD_NUMBER: _ClassVar[int]
            enable: bool
            def __init__(self, enable: bool = ...) -> None: ...
        PLAY_FIELD_NUMBER: _ClassVar[int]
        RECORD_FIELD_NUMBER: _ClassVar[int]
        PAUSE_FIELD_NUMBER: _ClassVar[int]
        RESET_FIELD_NUMBER: _ClassVar[int]
        JUMP_TO_TIME_FIELD_NUMBER: _ClassVar[int]
        START_SCRUB_FIELD_NUMBER: _ClassVar[int]
        END_SCRUB_FIELD_NUMBER: _ClassVar[int]
        DURATION_FIELD_NUMBER: _ClassVar[int]
        LOOP_FIELD_NUMBER: _ClassVar[int]
        UPDATE_SEQUENCE_FIELD_NUMBER: _ClassVar[int]
        MONITOR_SOURCE_FIELD_NUMBER: _ClassVar[int]
        play: TimedPlayback.Update.Play
        record: TimedPlayback.Update.Record
        pause: TimedPlayback.Update.Pause
        reset: TimedPlayback.Update.Reset
        jump_to_time: TimedPlayback.Update.JumpToTime
        start_scrub: TimedPlayback.Update.StartScrub
        end_scrub: TimedPlayback.Update.EndScrub
        duration: TimedPlayback.Update.Duration
        loop: TimedPlayback.Update.Loop
        update_sequence: TimedPlayback.Sequence
        monitor_source: TimedPlayback.Update.MonitorSource
        def __init__(self, play: _Optional[_Union[TimedPlayback.Update.Play, _Mapping]] = ..., record: _Optional[_Union[TimedPlayback.Update.Record, _Mapping]] = ..., pause: _Optional[_Union[TimedPlayback.Update.Pause, _Mapping]] = ..., reset: _Optional[_Union[TimedPlayback.Update.Reset, _Mapping]] = ..., jump_to_time: _Optional[_Union[TimedPlayback.Update.JumpToTime, _Mapping]] = ..., start_scrub: _Optional[_Union[TimedPlayback.Update.StartScrub, _Mapping]] = ..., end_scrub: _Optional[_Union[TimedPlayback.Update.EndScrub, _Mapping]] = ..., duration: _Optional[_Union[TimedPlayback.Update.Duration, _Mapping]] = ..., loop: _Optional[_Union[TimedPlayback.Update.Loop, _Mapping]] = ..., update_sequence: _Optional[_Union[TimedPlayback.Sequence, _Mapping]] = ..., monitor_source: _Optional[_Union[TimedPlayback.Update.MonitorSource, _Mapping]] = ...) -> None: ...
    SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    TIMING_FIELD_NUMBER: _ClassVar[int]
    sequence: TimedPlayback.Sequence
    timing: TimedPlayback.Timing
    def __init__(self, sequence: _Optional[_Union[TimedPlayback.Sequence, _Mapping]] = ..., timing: _Optional[_Union[TimedPlayback.Timing, _Mapping]] = ...) -> None: ...

class NetworkTriggerDataItem(_message.Message):
    __slots__ = ("action", "cue")
    ACTION_FIELD_NUMBER: _ClassVar[int]
    CUE_FIELD_NUMBER: _ClassVar[int]
    action: _action_pb2.Action
    cue: _cue_pb2.Cue
    def __init__(self, action: _Optional[_Union[_action_pb2.Action, _Mapping]] = ..., cue: _Optional[_Union[_cue_pb2.Cue, _Mapping]] = ...) -> None: ...

class SlideElementTextRenderInfo(_message.Message):
    __slots__ = ("layers",)
    class Layer(_message.Message):
        __slots__ = ("layer_type", "text_build_index", "cut_out_fill", "media_fill", "background_effect")
        class LayerType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            LAYER_TYPE_COMPOSITE: _ClassVar[SlideElementTextRenderInfo.Layer.LayerType]
            LAYER_TYPE_MASK: _ClassVar[SlideElementTextRenderInfo.Layer.LayerType]
            LAYER_TYPE_OVER: _ClassVar[SlideElementTextRenderInfo.Layer.LayerType]
            LAYER_TYPE_UNDER: _ClassVar[SlideElementTextRenderInfo.Layer.LayerType]
        LAYER_TYPE_COMPOSITE: SlideElementTextRenderInfo.Layer.LayerType
        LAYER_TYPE_MASK: SlideElementTextRenderInfo.Layer.LayerType
        LAYER_TYPE_OVER: SlideElementTextRenderInfo.Layer.LayerType
        LAYER_TYPE_UNDER: SlideElementTextRenderInfo.Layer.LayerType
        LAYER_TYPE_FIELD_NUMBER: _ClassVar[int]
        TEXT_BUILD_INDEX_FIELD_NUMBER: _ClassVar[int]
        CUT_OUT_FILL_FIELD_NUMBER: _ClassVar[int]
        MEDIA_FILL_FIELD_NUMBER: _ClassVar[int]
        BACKGROUND_EFFECT_FIELD_NUMBER: _ClassVar[int]
        layer_type: SlideElementTextRenderInfo.Layer.LayerType
        text_build_index: int
        cut_out_fill: _graphicsData_pb2.Graphics.Text.CutOutFill
        media_fill: _graphicsData_pb2.Graphics.Text.MediaFill
        background_effect: _graphicsData_pb2.Graphics.BackgroundEffect
        def __init__(self, layer_type: _Optional[_Union[SlideElementTextRenderInfo.Layer.LayerType, str]] = ..., text_build_index: _Optional[int] = ..., cut_out_fill: _Optional[_Union[_graphicsData_pb2.Graphics.Text.CutOutFill, _Mapping]] = ..., media_fill: _Optional[_Union[_graphicsData_pb2.Graphics.Text.MediaFill, _Mapping]] = ..., background_effect: _Optional[_Union[_graphicsData_pb2.Graphics.BackgroundEffect, _Mapping]] = ...) -> None: ...
    LAYERS_FIELD_NUMBER: _ClassVar[int]
    layers: _containers.RepeatedCompositeFieldContainer[SlideElementTextRenderInfo.Layer]
    def __init__(self, layers: _Optional[_Iterable[_Union[SlideElementTextRenderInfo.Layer, _Mapping]]] = ...) -> None: ...
