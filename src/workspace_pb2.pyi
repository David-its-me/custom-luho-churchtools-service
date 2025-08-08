import effects_pb2 as _effects_pb2
import masks_pb2 as _masks_pb2
import screens_pb2 as _screens_pb2
import layers_pb2 as _layers_pb2
import targets_pb2 as _targets_pb2
import playlist_pb2 as _playlist_pb2
import hotKey_pb2 as _hotKey_pb2
import basicTypes_pb2 as _basicTypes_pb2
import calendar_pb2 as _calendar_pb2
import alignmentGuide_pb2 as _alignmentGuide_pb2
import liveVideoPlaylist_pb2 as _liveVideoPlaylist_pb2
import graphicsData_pb2 as _graphicsData_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Workspace(_message.Message):
    __slots__ = ("uuid", "muted", "hidden", "editor_background", "effect_preset_uuid", "effect_build_duration", "transition", "active_mask_uuid", "playlist", "unit_scaling", "effects", "masks", "screens", "edge_blends", "layers", "target_sets", "hot_keys", "calendar", "alignment_guides", "live_video_playlist", "output_preview_display")
    class EditorBackground(_message.Message):
        __slots__ = ("enabled", "frame", "url", "opacity")
        ENABLED_FIELD_NUMBER: _ClassVar[int]
        FRAME_FIELD_NUMBER: _ClassVar[int]
        URL_FIELD_NUMBER: _ClassVar[int]
        OPACITY_FIELD_NUMBER: _ClassVar[int]
        enabled: bool
        frame: _graphicsData_pb2.Graphics.Rect
        url: _basicTypes_pb2.URL
        opacity: float
        def __init__(self, enabled: bool = ..., frame: _Optional[_Union[_graphicsData_pb2.Graphics.Rect, _Mapping]] = ..., url: _Optional[_Union[_basicTypes_pb2.URL, _Mapping]] = ..., opacity: _Optional[float] = ...) -> None: ...
    class UnitScaling(_message.Message):
        __slots__ = ("length", "unit", "points")
        class UnitType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            UNIT_TYPE_POINTS: _ClassVar[Workspace.UnitScaling.UnitType]
            UNIT_TYPE_MILLIMETERS: _ClassVar[Workspace.UnitScaling.UnitType]
            UNIT_TYPE_CENTIMETERS: _ClassVar[Workspace.UnitScaling.UnitType]
            UNIT_TYPE_METERS: _ClassVar[Workspace.UnitScaling.UnitType]
            UNIT_TYPE_INCHES: _ClassVar[Workspace.UnitScaling.UnitType]
            UNIT_TYPE_FEET: _ClassVar[Workspace.UnitScaling.UnitType]
        UNIT_TYPE_POINTS: Workspace.UnitScaling.UnitType
        UNIT_TYPE_MILLIMETERS: Workspace.UnitScaling.UnitType
        UNIT_TYPE_CENTIMETERS: Workspace.UnitScaling.UnitType
        UNIT_TYPE_METERS: Workspace.UnitScaling.UnitType
        UNIT_TYPE_INCHES: Workspace.UnitScaling.UnitType
        UNIT_TYPE_FEET: Workspace.UnitScaling.UnitType
        LENGTH_FIELD_NUMBER: _ClassVar[int]
        UNIT_FIELD_NUMBER: _ClassVar[int]
        POINTS_FIELD_NUMBER: _ClassVar[int]
        length: float
        unit: Workspace.UnitScaling.UnitType
        points: float
        def __init__(self, length: _Optional[float] = ..., unit: _Optional[_Union[Workspace.UnitScaling.UnitType, str]] = ..., points: _Optional[float] = ...) -> None: ...
    UUID_FIELD_NUMBER: _ClassVar[int]
    MUTED_FIELD_NUMBER: _ClassVar[int]
    HIDDEN_FIELD_NUMBER: _ClassVar[int]
    EDITOR_BACKGROUND_FIELD_NUMBER: _ClassVar[int]
    EFFECT_PRESET_UUID_FIELD_NUMBER: _ClassVar[int]
    EFFECT_BUILD_DURATION_FIELD_NUMBER: _ClassVar[int]
    TRANSITION_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_MASK_UUID_FIELD_NUMBER: _ClassVar[int]
    PLAYLIST_FIELD_NUMBER: _ClassVar[int]
    UNIT_SCALING_FIELD_NUMBER: _ClassVar[int]
    EFFECTS_FIELD_NUMBER: _ClassVar[int]
    MASKS_FIELD_NUMBER: _ClassVar[int]
    SCREENS_FIELD_NUMBER: _ClassVar[int]
    EDGE_BLENDS_FIELD_NUMBER: _ClassVar[int]
    LAYERS_FIELD_NUMBER: _ClassVar[int]
    TARGET_SETS_FIELD_NUMBER: _ClassVar[int]
    HOT_KEYS_FIELD_NUMBER: _ClassVar[int]
    CALENDAR_FIELD_NUMBER: _ClassVar[int]
    ALIGNMENT_GUIDES_FIELD_NUMBER: _ClassVar[int]
    LIVE_VIDEO_PLAYLIST_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_PREVIEW_DISPLAY_FIELD_NUMBER: _ClassVar[int]
    uuid: _basicTypes_pb2.UUID
    muted: bool
    hidden: bool
    editor_background: Workspace.EditorBackground
    effect_preset_uuid: _basicTypes_pb2.UUID
    effect_build_duration: float
    transition: _effects_pb2.Transition
    active_mask_uuid: _basicTypes_pb2.UUID
    playlist: _playlist_pb2.Playlist
    unit_scaling: Workspace.UnitScaling
    effects: _containers.RepeatedCompositeFieldContainer[_effects_pb2.Effect]
    masks: _containers.RepeatedCompositeFieldContainer[_masks_pb2.Mask]
    screens: _containers.RepeatedCompositeFieldContainer[_screens_pb2.Screen]
    edge_blends: _containers.RepeatedCompositeFieldContainer[_screens_pb2.EdgeBlend]
    layers: _containers.RepeatedCompositeFieldContainer[_layers_pb2.Layer]
    target_sets: _containers.RepeatedCompositeFieldContainer[_targets_pb2.TargetSet]
    hot_keys: _containers.RepeatedCompositeFieldContainer[_hotKey_pb2.HotKey]
    calendar: _calendar_pb2.Calendar
    alignment_guides: _containers.RepeatedCompositeFieldContainer[_alignmentGuide_pb2.AlignmentGuide]
    live_video_playlist: _liveVideoPlaylist_pb2.LiveVideoPlaylist
    output_preview_display: _screens_pb2.OutputDisplay
    def __init__(self, uuid: _Optional[_Union[_basicTypes_pb2.UUID, _Mapping]] = ..., muted: bool = ..., hidden: bool = ..., editor_background: _Optional[_Union[Workspace.EditorBackground, _Mapping]] = ..., effect_preset_uuid: _Optional[_Union[_basicTypes_pb2.UUID, _Mapping]] = ..., effect_build_duration: _Optional[float] = ..., transition: _Optional[_Union[_effects_pb2.Transition, _Mapping]] = ..., active_mask_uuid: _Optional[_Union[_basicTypes_pb2.UUID, _Mapping]] = ..., playlist: _Optional[_Union[_playlist_pb2.Playlist, _Mapping]] = ..., unit_scaling: _Optional[_Union[Workspace.UnitScaling, _Mapping]] = ..., effects: _Optional[_Iterable[_Union[_effects_pb2.Effect, _Mapping]]] = ..., masks: _Optional[_Iterable[_Union[_masks_pb2.Mask, _Mapping]]] = ..., screens: _Optional[_Iterable[_Union[_screens_pb2.Screen, _Mapping]]] = ..., edge_blends: _Optional[_Iterable[_Union[_screens_pb2.EdgeBlend, _Mapping]]] = ..., layers: _Optional[_Iterable[_Union[_layers_pb2.Layer, _Mapping]]] = ..., target_sets: _Optional[_Iterable[_Union[_targets_pb2.TargetSet, _Mapping]]] = ..., hot_keys: _Optional[_Iterable[_Union[_hotKey_pb2.HotKey, _Mapping]]] = ..., calendar: _Optional[_Union[_calendar_pb2.Calendar, _Mapping]] = ..., alignment_guides: _Optional[_Iterable[_Union[_alignmentGuide_pb2.AlignmentGuide, _Mapping]]] = ..., live_video_playlist: _Optional[_Union[_liveVideoPlaylist_pb2.LiveVideoPlaylist, _Mapping]] = ..., output_preview_display: _Optional[_Union[_screens_pb2.OutputDisplay, _Mapping]] = ...) -> None: ...
