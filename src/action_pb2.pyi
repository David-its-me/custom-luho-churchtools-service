import basicTypes_pb2 as _basicTypes_pb2
import layers_pb2 as _layers_pb2
import effects_pb2 as _effects_pb2
import graphicsData_pb2 as _graphicsData_pb2
import background_pb2 as _background_pb2
import presentationSlide_pb2 as _presentationSlide_pb2
import propSlide_pb2 as _propSlide_pb2
import timers_pb2 as _timers_pb2
import messages_pb2 as _messages_pb2
import stage_pb2 as _stage_pb2
import input_pb2 as _input_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Action(_message.Message):
    __slots__ = ("uuid", "name", "label", "delay_time", "old_type", "isEnabled", "layer_identification", "duration", "type", "collection_element", "playlist_item", "blend_mode", "transition", "media", "double_item", "effects", "slide", "background", "timer", "clear", "stage", "prop", "mask", "message", "social_media", "communication", "multi_screen", "presentation_document", "external_presentation", "audience_look", "audio_input", "slide_destination", "macro", "clear_group", "transport_control")
    class ActionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ACTION_TYPE_UNKNOWN: _ClassVar[Action.ActionType]
        ACTION_TYPE_STAGE_LAYOUT: _ClassVar[Action.ActionType]
        ACTION_TYPE_MEDIA: _ClassVar[Action.ActionType]
        ACTION_TYPE_TIMER: _ClassVar[Action.ActionType]
        ACTION_TYPE_COMMUNICATION: _ClassVar[Action.ActionType]
        ACTION_TYPE_CLEAR: _ClassVar[Action.ActionType]
        ACTION_TYPE_PROP: _ClassVar[Action.ActionType]
        ACTION_TYPE_MASK: _ClassVar[Action.ActionType]
        ACTION_TYPE_MESSAGE: _ClassVar[Action.ActionType]
        ACTION_TYPE_SOCIAL_MEDIA: _ClassVar[Action.ActionType]
        ACTION_TYPE_MULTISCREEN: _ClassVar[Action.ActionType]
        ACTION_TYPE_PRESENTATION_SLIDE: _ClassVar[Action.ActionType]
        ACTION_TYPE_FOREGROUND_MEDIA: _ClassVar[Action.ActionType]
        ACTION_TYPE_BACKGROUND_MEDIA: _ClassVar[Action.ActionType]
        ACTION_TYPE_PRESENTATION_DOCUMENT: _ClassVar[Action.ActionType]
        ACTION_TYPE_PROP_SLIDE: _ClassVar[Action.ActionType]
        ACTION_TYPE_EXTERNAL_PRESENTATION: _ClassVar[Action.ActionType]
        ACTION_TYPE_AUDIENCE_LOOK: _ClassVar[Action.ActionType]
        ACTION_TYPE_AUDIO_INPUT: _ClassVar[Action.ActionType]
        ACTION_TYPE_AUDIO_BIN_PLAYLIST: _ClassVar[Action.ActionType]
        ACTION_TYPE_MEDIA_BIN_PLAYLIST: _ClassVar[Action.ActionType]
        ACTION_TYPE_SLIDE_DESTINATION: _ClassVar[Action.ActionType]
        ACTION_TYPE_MACRO: _ClassVar[Action.ActionType]
        ACTION_TYPE_CLEAR_GROUP: _ClassVar[Action.ActionType]
    ACTION_TYPE_UNKNOWN: Action.ActionType
    ACTION_TYPE_STAGE_LAYOUT: Action.ActionType
    ACTION_TYPE_MEDIA: Action.ActionType
    ACTION_TYPE_TIMER: Action.ActionType
    ACTION_TYPE_COMMUNICATION: Action.ActionType
    ACTION_TYPE_CLEAR: Action.ActionType
    ACTION_TYPE_PROP: Action.ActionType
    ACTION_TYPE_MASK: Action.ActionType
    ACTION_TYPE_MESSAGE: Action.ActionType
    ACTION_TYPE_SOCIAL_MEDIA: Action.ActionType
    ACTION_TYPE_MULTISCREEN: Action.ActionType
    ACTION_TYPE_PRESENTATION_SLIDE: Action.ActionType
    ACTION_TYPE_FOREGROUND_MEDIA: Action.ActionType
    ACTION_TYPE_BACKGROUND_MEDIA: Action.ActionType
    ACTION_TYPE_PRESENTATION_DOCUMENT: Action.ActionType
    ACTION_TYPE_PROP_SLIDE: Action.ActionType
    ACTION_TYPE_EXTERNAL_PRESENTATION: Action.ActionType
    ACTION_TYPE_AUDIENCE_LOOK: Action.ActionType
    ACTION_TYPE_AUDIO_INPUT: Action.ActionType
    ACTION_TYPE_AUDIO_BIN_PLAYLIST: Action.ActionType
    ACTION_TYPE_MEDIA_BIN_PLAYLIST: Action.ActionType
    ACTION_TYPE_SLIDE_DESTINATION: Action.ActionType
    ACTION_TYPE_MACRO: Action.ActionType
    ACTION_TYPE_CLEAR_GROUP: Action.ActionType
    class OldType(_message.Message):
        __slots__ = ("category", "application_type")
        class Category(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            CATEGORY_UNKNOWN: _ClassVar[Action.OldType.Category]
            CATEGORY_MEDIA: _ClassVar[Action.OldType.Category]
            CATEGORY_APPLICATION: _ClassVar[Action.OldType.Category]
        CATEGORY_UNKNOWN: Action.OldType.Category
        CATEGORY_MEDIA: Action.OldType.Category
        CATEGORY_APPLICATION: Action.OldType.Category
        CATEGORY_FIELD_NUMBER: _ClassVar[int]
        APPLICATION_TYPE_FIELD_NUMBER: _ClassVar[int]
        category: Action.OldType.Category
        application_type: int
        def __init__(self, category: _Optional[_Union[Action.OldType.Category, str]] = ..., application_type: _Optional[int] = ...) -> None: ...
    class Label(_message.Message):
        __slots__ = ("text", "color")
        TEXT_FIELD_NUMBER: _ClassVar[int]
        COLOR_FIELD_NUMBER: _ClassVar[int]
        text: str
        color: _basicTypes_pb2.Color
        def __init__(self, text: _Optional[str] = ..., color: _Optional[_Union[_basicTypes_pb2.Color, _Mapping]] = ...) -> None: ...
    class LayerIdentification(_message.Message):
        __slots__ = ("uuid", "name")
        UUID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        uuid: _basicTypes_pb2.UUID
        name: str
        def __init__(self, uuid: _Optional[_Union[_basicTypes_pb2.UUID, _Mapping]] = ..., name: _Optional[str] = ...) -> None: ...
    class PlaylistItemType(_message.Message):
        __slots__ = ("playlist_uuid", "playlist_name", "item_uuid", "item_name", "select_playlist", "always_retrigger")
        PLAYLIST_UUID_FIELD_NUMBER: _ClassVar[int]
        PLAYLIST_NAME_FIELD_NUMBER: _ClassVar[int]
        ITEM_UUID_FIELD_NUMBER: _ClassVar[int]
        ITEM_NAME_FIELD_NUMBER: _ClassVar[int]
        SELECT_PLAYLIST_FIELD_NUMBER: _ClassVar[int]
        ALWAYS_RETRIGGER_FIELD_NUMBER: _ClassVar[int]
        playlist_uuid: _basicTypes_pb2.UUID
        playlist_name: str
        item_uuid: _basicTypes_pb2.UUID
        item_name: str
        select_playlist: bool
        always_retrigger: bool
        def __init__(self, playlist_uuid: _Optional[_Union[_basicTypes_pb2.UUID, _Mapping]] = ..., playlist_name: _Optional[str] = ..., item_uuid: _Optional[_Union[_basicTypes_pb2.UUID, _Mapping]] = ..., item_name: _Optional[str] = ..., select_playlist: bool = ..., always_retrigger: bool = ...) -> None: ...
    class BlendModeType(_message.Message):
        __slots__ = ("blend_mode", "blend")
        class BlendMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            BLEND_MODE_NORMAL: _ClassVar[Action.BlendModeType.BlendMode]
            BLEND_MODE_DISSOLVE: _ClassVar[Action.BlendModeType.BlendMode]
            BLEND_MODE_DARKEN: _ClassVar[Action.BlendModeType.BlendMode]
            BLEND_MODE_MULTIPLY: _ClassVar[Action.BlendModeType.BlendMode]
            BLEND_MODE_COLOR_BURN: _ClassVar[Action.BlendModeType.BlendMode]
            BLEND_MODE_LINEAR_BURN: _ClassVar[Action.BlendModeType.BlendMode]
            BLEND_MODE_DARKER_COLOR: _ClassVar[Action.BlendModeType.BlendMode]
            BLEND_MODE_LIGHTEN: _ClassVar[Action.BlendModeType.BlendMode]
            BLEND_MODE_SCREEN: _ClassVar[Action.BlendModeType.BlendMode]
            BLEND_MODE_COLOR_DODGE: _ClassVar[Action.BlendModeType.BlendMode]
            BLEND_MODE_LINEAR_DODGE: _ClassVar[Action.BlendModeType.BlendMode]
            BLEND_MODE_LIGHTER_COLOR: _ClassVar[Action.BlendModeType.BlendMode]
            BLEND_MODE_OVERLAY: _ClassVar[Action.BlendModeType.BlendMode]
            BLEND_MODE_SOFT_LIGHT: _ClassVar[Action.BlendModeType.BlendMode]
            BLEND_MODE_HARD_LIGHT: _ClassVar[Action.BlendModeType.BlendMode]
            BLEND_MODE_VIVID_LIGHT: _ClassVar[Action.BlendModeType.BlendMode]
            BLEND_MODE_LINEAR_LIGHT: _ClassVar[Action.BlendModeType.BlendMode]
            BLEND_MODE_PIN_LIGHT: _ClassVar[Action.BlendModeType.BlendMode]
            BLEND_MODE_HARD_MIX: _ClassVar[Action.BlendModeType.BlendMode]
            BLEND_MODE_DIFFERENCE: _ClassVar[Action.BlendModeType.BlendMode]
            BLEND_MODE_EXCLUSION: _ClassVar[Action.BlendModeType.BlendMode]
            BLEND_MODE_SUBTRACT: _ClassVar[Action.BlendModeType.BlendMode]
            BLEND_MODE_DIVIDE: _ClassVar[Action.BlendModeType.BlendMode]
            BLEND_MODE_HUE: _ClassVar[Action.BlendModeType.BlendMode]
            BLEND_MODE_SATURATION: _ClassVar[Action.BlendModeType.BlendMode]
            BLEND_MODE_COLOR: _ClassVar[Action.BlendModeType.BlendMode]
            BLEND_MODE_LUMINOSITY: _ClassVar[Action.BlendModeType.BlendMode]
        BLEND_MODE_NORMAL: Action.BlendModeType.BlendMode
        BLEND_MODE_DISSOLVE: Action.BlendModeType.BlendMode
        BLEND_MODE_DARKEN: Action.BlendModeType.BlendMode
        BLEND_MODE_MULTIPLY: Action.BlendModeType.BlendMode
        BLEND_MODE_COLOR_BURN: Action.BlendModeType.BlendMode
        BLEND_MODE_LINEAR_BURN: Action.BlendModeType.BlendMode
        BLEND_MODE_DARKER_COLOR: Action.BlendModeType.BlendMode
        BLEND_MODE_LIGHTEN: Action.BlendModeType.BlendMode
        BLEND_MODE_SCREEN: Action.BlendModeType.BlendMode
        BLEND_MODE_COLOR_DODGE: Action.BlendModeType.BlendMode
        BLEND_MODE_LINEAR_DODGE: Action.BlendModeType.BlendMode
        BLEND_MODE_LIGHTER_COLOR: Action.BlendModeType.BlendMode
        BLEND_MODE_OVERLAY: Action.BlendModeType.BlendMode
        BLEND_MODE_SOFT_LIGHT: Action.BlendModeType.BlendMode
        BLEND_MODE_HARD_LIGHT: Action.BlendModeType.BlendMode
        BLEND_MODE_VIVID_LIGHT: Action.BlendModeType.BlendMode
        BLEND_MODE_LINEAR_LIGHT: Action.BlendModeType.BlendMode
        BLEND_MODE_PIN_LIGHT: Action.BlendModeType.BlendMode
        BLEND_MODE_HARD_MIX: Action.BlendModeType.BlendMode
        BLEND_MODE_DIFFERENCE: Action.BlendModeType.BlendMode
        BLEND_MODE_EXCLUSION: Action.BlendModeType.BlendMode
        BLEND_MODE_SUBTRACT: Action.BlendModeType.BlendMode
        BLEND_MODE_DIVIDE: Action.BlendModeType.BlendMode
        BLEND_MODE_HUE: Action.BlendModeType.BlendMode
        BLEND_MODE_SATURATION: Action.BlendModeType.BlendMode
        BLEND_MODE_COLOR: Action.BlendModeType.BlendMode
        BLEND_MODE_LUMINOSITY: Action.BlendModeType.BlendMode
        BLEND_MODE_FIELD_NUMBER: _ClassVar[int]
        BLEND_FIELD_NUMBER: _ClassVar[int]
        blend_mode: Action.BlendModeType.BlendMode
        blend: _layers_pb2.Layer.Blending
        def __init__(self, blend_mode: _Optional[_Union[Action.BlendModeType.BlendMode, str]] = ..., blend: _Optional[_Union[_layers_pb2.Layer.Blending, _Mapping]] = ...) -> None: ...
    class TransitionType(_message.Message):
        __slots__ = ("transition_name", "transition")
        TRANSITION_NAME_FIELD_NUMBER: _ClassVar[int]
        TRANSITION_FIELD_NUMBER: _ClassVar[int]
        transition_name: str
        transition: _effects_pb2.Transition
        def __init__(self, transition_name: _Optional[str] = ..., transition: _Optional[_Union[_effects_pb2.Transition, _Mapping]] = ...) -> None: ...
    class DoubleType(_message.Message):
        __slots__ = ("value",)
        VALUE_FIELD_NUMBER: _ClassVar[int]
        value: float
        def __init__(self, value: _Optional[float] = ...) -> None: ...
    class EffectsType(_message.Message):
        __slots__ = ("effects",)
        EFFECTS_FIELD_NUMBER: _ClassVar[int]
        effects: _containers.RepeatedCompositeFieldContainer[_effects_pb2.Effect]
        def __init__(self, effects: _Optional[_Iterable[_Union[_effects_pb2.Effect, _Mapping]]] = ...) -> None: ...
    class MediaType(_message.Message):
        __slots__ = ("transition_duration", "selected_effect_preset_uuid", "transition", "effects", "element", "layer_type", "always_retrigger", "markers", "image", "video", "audio", "live_video")
        class LayerType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            LAYER_TYPE_BACKGROUND: _ClassVar[Action.MediaType.LayerType]
            LAYER_TYPE_FOREGROUND: _ClassVar[Action.MediaType.LayerType]
            LAYER_TYPE_FILL: _ClassVar[Action.MediaType.LayerType]
            LAYER_TYPE_INPUT: _ClassVar[Action.MediaType.LayerType]
        LAYER_TYPE_BACKGROUND: Action.MediaType.LayerType
        LAYER_TYPE_FOREGROUND: Action.MediaType.LayerType
        LAYER_TYPE_FILL: Action.MediaType.LayerType
        LAYER_TYPE_INPUT: Action.MediaType.LayerType
        class Image(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class Video(_message.Message):
            __slots__ = ("playback_behavior", "end_behavior", "loop_time", "times_to_loop", "soft_loop", "soft_loop_duration")
            class PlaybackBehavior(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                PLAYBACK_BEHAVIOR_STOP: _ClassVar[Action.MediaType.Video.PlaybackBehavior]
                PLAYBACK_BEHAVIOR_LOOP: _ClassVar[Action.MediaType.Video.PlaybackBehavior]
                PLAYBACK_BEHAVIOR_LOOP_FOR_COUNT: _ClassVar[Action.MediaType.Video.PlaybackBehavior]
                PLAYBACK_BEHAVIOR_LOOP_FOR_TIME: _ClassVar[Action.MediaType.Video.PlaybackBehavior]
            PLAYBACK_BEHAVIOR_STOP: Action.MediaType.Video.PlaybackBehavior
            PLAYBACK_BEHAVIOR_LOOP: Action.MediaType.Video.PlaybackBehavior
            PLAYBACK_BEHAVIOR_LOOP_FOR_COUNT: Action.MediaType.Video.PlaybackBehavior
            PLAYBACK_BEHAVIOR_LOOP_FOR_TIME: Action.MediaType.Video.PlaybackBehavior
            class EndBehavior(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                END_BEHAVIOR_STOP: _ClassVar[Action.MediaType.Video.EndBehavior]
                END_BEHAVIOR_STOP_ON_BLACK: _ClassVar[Action.MediaType.Video.EndBehavior]
                END_BEHAVIOR_STOP_ON_CLEAR: _ClassVar[Action.MediaType.Video.EndBehavior]
                END_BEHAVIOR_FADE_TO_BLACK: _ClassVar[Action.MediaType.Video.EndBehavior]
                END_BEHAVIOR_FADE_TO_CLEAR: _ClassVar[Action.MediaType.Video.EndBehavior]
            END_BEHAVIOR_STOP: Action.MediaType.Video.EndBehavior
            END_BEHAVIOR_STOP_ON_BLACK: Action.MediaType.Video.EndBehavior
            END_BEHAVIOR_STOP_ON_CLEAR: Action.MediaType.Video.EndBehavior
            END_BEHAVIOR_FADE_TO_BLACK: Action.MediaType.Video.EndBehavior
            END_BEHAVIOR_FADE_TO_CLEAR: Action.MediaType.Video.EndBehavior
            PLAYBACK_BEHAVIOR_FIELD_NUMBER: _ClassVar[int]
            END_BEHAVIOR_FIELD_NUMBER: _ClassVar[int]
            LOOP_TIME_FIELD_NUMBER: _ClassVar[int]
            TIMES_TO_LOOP_FIELD_NUMBER: _ClassVar[int]
            SOFT_LOOP_FIELD_NUMBER: _ClassVar[int]
            SOFT_LOOP_DURATION_FIELD_NUMBER: _ClassVar[int]
            playback_behavior: Action.MediaType.Video.PlaybackBehavior
            end_behavior: Action.MediaType.Video.EndBehavior
            loop_time: float
            times_to_loop: int
            soft_loop: bool
            soft_loop_duration: float
            def __init__(self, playback_behavior: _Optional[_Union[Action.MediaType.Video.PlaybackBehavior, str]] = ..., end_behavior: _Optional[_Union[Action.MediaType.Video.EndBehavior, str]] = ..., loop_time: _Optional[float] = ..., times_to_loop: _Optional[int] = ..., soft_loop: bool = ..., soft_loop_duration: _Optional[float] = ...) -> None: ...
        class Audio(_message.Message):
            __slots__ = ("playback_behavior", "loop_time", "times_to_loop", "audio_type")
            class PlaybackBehavior(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                PLAYBACK_BEHAVIOR_STOP: _ClassVar[Action.MediaType.Audio.PlaybackBehavior]
                PLAYBACK_BEHAVIOR_LOOP: _ClassVar[Action.MediaType.Audio.PlaybackBehavior]
                PLAYBACK_BEHAVIOR_LOOP_FOR_COUNT: _ClassVar[Action.MediaType.Audio.PlaybackBehavior]
                PLAYBACK_BEHAVIOR_LOOP_FOR_TIME: _ClassVar[Action.MediaType.Audio.PlaybackBehavior]
            PLAYBACK_BEHAVIOR_STOP: Action.MediaType.Audio.PlaybackBehavior
            PLAYBACK_BEHAVIOR_LOOP: Action.MediaType.Audio.PlaybackBehavior
            PLAYBACK_BEHAVIOR_LOOP_FOR_COUNT: Action.MediaType.Audio.PlaybackBehavior
            PLAYBACK_BEHAVIOR_LOOP_FOR_TIME: Action.MediaType.Audio.PlaybackBehavior
            class MediaActionAudioType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                MEDIA_ACTION_AUDIO_TYPE_TUNE: _ClassVar[Action.MediaType.Audio.MediaActionAudioType]
                MEDIA_ACTION_AUDIO_TYPE_SOUND: _ClassVar[Action.MediaType.Audio.MediaActionAudioType]
            MEDIA_ACTION_AUDIO_TYPE_TUNE: Action.MediaType.Audio.MediaActionAudioType
            MEDIA_ACTION_AUDIO_TYPE_SOUND: Action.MediaType.Audio.MediaActionAudioType
            PLAYBACK_BEHAVIOR_FIELD_NUMBER: _ClassVar[int]
            LOOP_TIME_FIELD_NUMBER: _ClassVar[int]
            TIMES_TO_LOOP_FIELD_NUMBER: _ClassVar[int]
            AUDIO_TYPE_FIELD_NUMBER: _ClassVar[int]
            playback_behavior: Action.MediaType.Audio.PlaybackBehavior
            loop_time: float
            times_to_loop: int
            audio_type: Action.MediaType.Audio.MediaActionAudioType
            def __init__(self, playback_behavior: _Optional[_Union[Action.MediaType.Audio.PlaybackBehavior, str]] = ..., loop_time: _Optional[float] = ..., times_to_loop: _Optional[int] = ..., audio_type: _Optional[_Union[Action.MediaType.Audio.MediaActionAudioType, str]] = ...) -> None: ...
        class LiveVideo(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class PlaybackMarker(_message.Message):
            __slots__ = ("uuid", "time", "color", "name", "actions")
            UUID_FIELD_NUMBER: _ClassVar[int]
            TIME_FIELD_NUMBER: _ClassVar[int]
            COLOR_FIELD_NUMBER: _ClassVar[int]
            NAME_FIELD_NUMBER: _ClassVar[int]
            ACTIONS_FIELD_NUMBER: _ClassVar[int]
            uuid: _basicTypes_pb2.UUID
            time: float
            color: _basicTypes_pb2.Color
            name: str
            actions: _containers.RepeatedCompositeFieldContainer[Action]
            def __init__(self, uuid: _Optional[_Union[_basicTypes_pb2.UUID, _Mapping]] = ..., time: _Optional[float] = ..., color: _Optional[_Union[_basicTypes_pb2.Color, _Mapping]] = ..., name: _Optional[str] = ..., actions: _Optional[_Iterable[_Union[Action, _Mapping]]] = ...) -> None: ...
        TRANSITION_DURATION_FIELD_NUMBER: _ClassVar[int]
        SELECTED_EFFECT_PRESET_UUID_FIELD_NUMBER: _ClassVar[int]
        TRANSITION_FIELD_NUMBER: _ClassVar[int]
        EFFECTS_FIELD_NUMBER: _ClassVar[int]
        ELEMENT_FIELD_NUMBER: _ClassVar[int]
        LAYER_TYPE_FIELD_NUMBER: _ClassVar[int]
        ALWAYS_RETRIGGER_FIELD_NUMBER: _ClassVar[int]
        MARKERS_FIELD_NUMBER: _ClassVar[int]
        IMAGE_FIELD_NUMBER: _ClassVar[int]
        VIDEO_FIELD_NUMBER: _ClassVar[int]
        AUDIO_FIELD_NUMBER: _ClassVar[int]
        LIVE_VIDEO_FIELD_NUMBER: _ClassVar[int]
        transition_duration: float
        selected_effect_preset_uuid: _basicTypes_pb2.UUID
        transition: _effects_pb2.Transition
        effects: _containers.RepeatedCompositeFieldContainer[_effects_pb2.Effect]
        element: _graphicsData_pb2.Media
        layer_type: Action.MediaType.LayerType
        always_retrigger: bool
        markers: _containers.RepeatedCompositeFieldContainer[Action.MediaType.PlaybackMarker]
        image: Action.MediaType.Image
        video: Action.MediaType.Video
        audio: Action.MediaType.Audio
        live_video: Action.MediaType.LiveVideo
        def __init__(self, transition_duration: _Optional[float] = ..., selected_effect_preset_uuid: _Optional[_Union[_basicTypes_pb2.UUID, _Mapping]] = ..., transition: _Optional[_Union[_effects_pb2.Transition, _Mapping]] = ..., effects: _Optional[_Iterable[_Union[_effects_pb2.Effect, _Mapping]]] = ..., element: _Optional[_Union[_graphicsData_pb2.Media, _Mapping]] = ..., layer_type: _Optional[_Union[Action.MediaType.LayerType, str]] = ..., always_retrigger: bool = ..., markers: _Optional[_Iterable[_Union[Action.MediaType.PlaybackMarker, _Mapping]]] = ..., image: _Optional[_Union[Action.MediaType.Image, _Mapping]] = ..., video: _Optional[_Union[Action.MediaType.Video, _Mapping]] = ..., audio: _Optional[_Union[Action.MediaType.Audio, _Mapping]] = ..., live_video: _Optional[_Union[Action.MediaType.LiveVideo, _Mapping]] = ...) -> None: ...
    class SlideType(_message.Message):
        __slots__ = ("presentation", "prop")
        PRESENTATION_FIELD_NUMBER: _ClassVar[int]
        PROP_FIELD_NUMBER: _ClassVar[int]
        presentation: _presentationSlide_pb2.PresentationSlide
        prop: _propSlide_pb2.PropSlide
        def __init__(self, presentation: _Optional[_Union[_presentationSlide_pb2.PresentationSlide, _Mapping]] = ..., prop: _Optional[_Union[_propSlide_pb2.PropSlide, _Mapping]] = ...) -> None: ...
    class BackgroundType(_message.Message):
        __slots__ = ("element",)
        ELEMENT_FIELD_NUMBER: _ClassVar[int]
        element: _background_pb2.Background
        def __init__(self, element: _Optional[_Union[_background_pb2.Background, _Mapping]] = ...) -> None: ...
    class TimerType(_message.Message):
        __slots__ = ("action_type", "timer_identification", "timer_configuration")
        class TimerAction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            ACTION_START: _ClassVar[Action.TimerType.TimerAction]
            ACTION_STOP: _ClassVar[Action.TimerType.TimerAction]
            ACTION_RESET: _ClassVar[Action.TimerType.TimerAction]
            ACTION_RESET_AND_START: _ClassVar[Action.TimerType.TimerAction]
            ACTION_STOP_AND_RESET: _ClassVar[Action.TimerType.TimerAction]
        ACTION_START: Action.TimerType.TimerAction
        ACTION_STOP: Action.TimerType.TimerAction
        ACTION_RESET: Action.TimerType.TimerAction
        ACTION_RESET_AND_START: Action.TimerType.TimerAction
        ACTION_STOP_AND_RESET: Action.TimerType.TimerAction
        ACTION_TYPE_FIELD_NUMBER: _ClassVar[int]
        TIMER_IDENTIFICATION_FIELD_NUMBER: _ClassVar[int]
        TIMER_CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
        action_type: Action.TimerType.TimerAction
        timer_identification: _basicTypes_pb2.CollectionElementType
        timer_configuration: _timers_pb2.Timer.Configuration
        def __init__(self, action_type: _Optional[_Union[Action.TimerType.TimerAction, str]] = ..., timer_identification: _Optional[_Union[_basicTypes_pb2.CollectionElementType, _Mapping]] = ..., timer_configuration: _Optional[_Union[_timers_pb2.Timer.Configuration, _Mapping]] = ...) -> None: ...
    class ClearType(_message.Message):
        __slots__ = ("target_layer", "content_destination")
        class ClearTargetLayer(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            CLEAR_TARGET_LAYER_ALL: _ClassVar[Action.ClearType.ClearTargetLayer]
            CLEAR_TARGET_LAYER_AUDIO: _ClassVar[Action.ClearType.ClearTargetLayer]
            CLEAR_TARGET_LAYER_BACKGROUND: _ClassVar[Action.ClearType.ClearTargetLayer]
            CLEAR_TARGET_LAYER_LIVE_VIDEO: _ClassVar[Action.ClearType.ClearTargetLayer]
            CLEAR_TARGET_LAYER_PROP: _ClassVar[Action.ClearType.ClearTargetLayer]
            CLEAR_TARGET_LAYER_SLIDE: _ClassVar[Action.ClearType.ClearTargetLayer]
            CLEAR_TARGET_LAYER_LOGO: _ClassVar[Action.ClearType.ClearTargetLayer]
            CLEAR_TARGET_LAYER_MESSAGES: _ClassVar[Action.ClearType.ClearTargetLayer]
            CLEAR_TARGET_LAYER_AUDIO_EFFECTS: _ClassVar[Action.ClearType.ClearTargetLayer]
        CLEAR_TARGET_LAYER_ALL: Action.ClearType.ClearTargetLayer
        CLEAR_TARGET_LAYER_AUDIO: Action.ClearType.ClearTargetLayer
        CLEAR_TARGET_LAYER_BACKGROUND: Action.ClearType.ClearTargetLayer
        CLEAR_TARGET_LAYER_LIVE_VIDEO: Action.ClearType.ClearTargetLayer
        CLEAR_TARGET_LAYER_PROP: Action.ClearType.ClearTargetLayer
        CLEAR_TARGET_LAYER_SLIDE: Action.ClearType.ClearTargetLayer
        CLEAR_TARGET_LAYER_LOGO: Action.ClearType.ClearTargetLayer
        CLEAR_TARGET_LAYER_MESSAGES: Action.ClearType.ClearTargetLayer
        CLEAR_TARGET_LAYER_AUDIO_EFFECTS: Action.ClearType.ClearTargetLayer
        class ContentDestination(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            CONTENT_DESTINATION_GLOBAL: _ClassVar[Action.ClearType.ContentDestination]
            CONTENT_DESTINATION_ANNOUNCEMENTS: _ClassVar[Action.ClearType.ContentDestination]
        CONTENT_DESTINATION_GLOBAL: Action.ClearType.ContentDestination
        CONTENT_DESTINATION_ANNOUNCEMENTS: Action.ClearType.ContentDestination
        TARGET_LAYER_FIELD_NUMBER: _ClassVar[int]
        CONTENT_DESTINATION_FIELD_NUMBER: _ClassVar[int]
        target_layer: Action.ClearType.ClearTargetLayer
        content_destination: Action.ClearType.ContentDestination
        def __init__(self, target_layer: _Optional[_Union[Action.ClearType.ClearTargetLayer, str]] = ..., content_destination: _Optional[_Union[Action.ClearType.ContentDestination, str]] = ...) -> None: ...
    class ClearGroupType(_message.Message):
        __slots__ = ("identification",)
        IDENTIFICATION_FIELD_NUMBER: _ClassVar[int]
        identification: _basicTypes_pb2.CollectionElementType
        def __init__(self, identification: _Optional[_Union[_basicTypes_pb2.CollectionElementType, _Mapping]] = ...) -> None: ...
    class TransportControlType(_message.Message):
        __slots__ = ("play", "pause", "jumpToTime")
        class Play(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class Pause(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class JumpToTime(_message.Message):
            __slots__ = ("time",)
            TIME_FIELD_NUMBER: _ClassVar[int]
            time: float
            def __init__(self, time: _Optional[float] = ...) -> None: ...
        PLAY_FIELD_NUMBER: _ClassVar[int]
        PAUSE_FIELD_NUMBER: _ClassVar[int]
        JUMPTOTIME_FIELD_NUMBER: _ClassVar[int]
        play: Action.TransportControlType.Play
        pause: Action.TransportControlType.Pause
        jumpToTime: Action.TransportControlType.JumpToTime
        def __init__(self, play: _Optional[_Union[Action.TransportControlType.Play, _Mapping]] = ..., pause: _Optional[_Union[Action.TransportControlType.Pause, _Mapping]] = ..., jumpToTime: _Optional[_Union[Action.TransportControlType.JumpToTime, _Mapping]] = ...) -> None: ...
    class StageLayoutType(_message.Message):
        __slots__ = ("stage_screen_assignments", "slide_target")
        class SlideTarget(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            SLIDE_TARGET_NO_CHANGE: _ClassVar[Action.StageLayoutType.SlideTarget]
            SLIDE_TARGET_STAGE_ONLY: _ClassVar[Action.StageLayoutType.SlideTarget]
            SLIDE_TARGET_ALL: _ClassVar[Action.StageLayoutType.SlideTarget]
        SLIDE_TARGET_NO_CHANGE: Action.StageLayoutType.SlideTarget
        SLIDE_TARGET_STAGE_ONLY: Action.StageLayoutType.SlideTarget
        SLIDE_TARGET_ALL: Action.StageLayoutType.SlideTarget
        STAGE_SCREEN_ASSIGNMENTS_FIELD_NUMBER: _ClassVar[int]
        SLIDE_TARGET_FIELD_NUMBER: _ClassVar[int]
        stage_screen_assignments: _containers.RepeatedCompositeFieldContainer[_stage_pb2.Stage.ScreenAssignment]
        slide_target: Action.StageLayoutType.SlideTarget
        def __init__(self, stage_screen_assignments: _Optional[_Iterable[_Union[_stage_pb2.Stage.ScreenAssignment, _Mapping]]] = ..., slide_target: _Optional[_Union[Action.StageLayoutType.SlideTarget, str]] = ...) -> None: ...
    class SlideDestinationType(_message.Message):
        __slots__ = ("slide_target",)
        class SlideTarget(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            SLIDE_TARGET_NO_CHANGE: _ClassVar[Action.SlideDestinationType.SlideTarget]
            SLIDE_TARGET_STAGE_ONLY: _ClassVar[Action.SlideDestinationType.SlideTarget]
            SLIDE_TARGET_ALL: _ClassVar[Action.SlideDestinationType.SlideTarget]
        SLIDE_TARGET_NO_CHANGE: Action.SlideDestinationType.SlideTarget
        SLIDE_TARGET_STAGE_ONLY: Action.SlideDestinationType.SlideTarget
        SLIDE_TARGET_ALL: Action.SlideDestinationType.SlideTarget
        SLIDE_TARGET_FIELD_NUMBER: _ClassVar[int]
        slide_target: Action.SlideDestinationType.SlideTarget
        def __init__(self, slide_target: _Optional[_Union[Action.SlideDestinationType.SlideTarget, str]] = ...) -> None: ...
    class PropType(_message.Message):
        __slots__ = ("identification",)
        IDENTIFICATION_FIELD_NUMBER: _ClassVar[int]
        identification: _basicTypes_pb2.CollectionElementType
        def __init__(self, identification: _Optional[_Union[_basicTypes_pb2.CollectionElementType, _Mapping]] = ...) -> None: ...
    class MaskType(_message.Message):
        __slots__ = ("identification",)
        IDENTIFICATION_FIELD_NUMBER: _ClassVar[int]
        identification: _basicTypes_pb2.CollectionElementType
        def __init__(self, identification: _Optional[_Union[_basicTypes_pb2.CollectionElementType, _Mapping]] = ...) -> None: ...
    class MessageType(_message.Message):
        __slots__ = ("message_identificaton", "content")
        MESSAGE_IDENTIFICATON_FIELD_NUMBER: _ClassVar[int]
        CONTENT_FIELD_NUMBER: _ClassVar[int]
        message_identificaton: _basicTypes_pb2.CollectionElementType
        content: _containers.RepeatedCompositeFieldContainer[_messages_pb2.Message.TokenValue]
        def __init__(self, message_identificaton: _Optional[_Union[_basicTypes_pb2.CollectionElementType, _Mapping]] = ..., content: _Optional[_Iterable[_Union[_messages_pb2.Message.TokenValue, _Mapping]]] = ...) -> None: ...
    class SocialMediaType(_message.Message):
        __slots__ = ("action_type", "duration")
        class SocialMediaAction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            SOCIAL_MEDIA_ACTION_LENGTH_OF_GOTO_NEXT_TIMER: _ClassVar[Action.SocialMediaType.SocialMediaAction]
            SOCIAL_MEDIA_ACTION_SPECIFIED_TIME: _ClassVar[Action.SocialMediaType.SocialMediaAction]
        SOCIAL_MEDIA_ACTION_LENGTH_OF_GOTO_NEXT_TIMER: Action.SocialMediaType.SocialMediaAction
        SOCIAL_MEDIA_ACTION_SPECIFIED_TIME: Action.SocialMediaType.SocialMediaAction
        ACTION_TYPE_FIELD_NUMBER: _ClassVar[int]
        DURATION_FIELD_NUMBER: _ClassVar[int]
        action_type: Action.SocialMediaType.SocialMediaAction
        duration: float
        def __init__(self, action_type: _Optional[_Union[Action.SocialMediaType.SocialMediaAction, str]] = ..., duration: _Optional[float] = ...) -> None: ...
    class CommunicationType(_message.Message):
        __slots__ = ("device_identification", "format", "description", "commands", "midi_command", "global_cache_command", "gvg100_command", "sony_BVS_command")
        class Command(_message.Message):
            __slots__ = ("name", "value", "replacement_range", "possible_values")
            NAME_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            REPLACEMENT_RANGE_FIELD_NUMBER: _ClassVar[int]
            POSSIBLE_VALUES_FIELD_NUMBER: _ClassVar[int]
            name: str
            value: str
            replacement_range: _basicTypes_pb2.IntRange
            possible_values: _containers.RepeatedScalarFieldContainer[str]
            def __init__(self, name: _Optional[str] = ..., value: _Optional[str] = ..., replacement_range: _Optional[_Union[_basicTypes_pb2.IntRange, _Mapping]] = ..., possible_values: _Optional[_Iterable[str]] = ...) -> None: ...
        class MIDICommand(_message.Message):
            __slots__ = ("state", "channel", "note", "intensity")
            class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                STATE_ON: _ClassVar[Action.CommunicationType.MIDICommand.State]
                STATE_OFF: _ClassVar[Action.CommunicationType.MIDICommand.State]
            STATE_ON: Action.CommunicationType.MIDICommand.State
            STATE_OFF: Action.CommunicationType.MIDICommand.State
            STATE_FIELD_NUMBER: _ClassVar[int]
            CHANNEL_FIELD_NUMBER: _ClassVar[int]
            NOTE_FIELD_NUMBER: _ClassVar[int]
            INTENSITY_FIELD_NUMBER: _ClassVar[int]
            state: Action.CommunicationType.MIDICommand.State
            channel: int
            note: int
            intensity: int
            def __init__(self, state: _Optional[_Union[Action.CommunicationType.MIDICommand.State, str]] = ..., channel: _Optional[int] = ..., note: _Optional[int] = ..., intensity: _Optional[int] = ...) -> None: ...
        class GlobalCacheCommand(_message.Message):
            __slots__ = ("command_action", "output", "interval")
            class CommandAction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                COMMAND_ACTION_ON: _ClassVar[Action.CommunicationType.GlobalCacheCommand.CommandAction]
                COMMAND_ACTION_OFF: _ClassVar[Action.CommunicationType.GlobalCacheCommand.CommandAction]
                COMMAND_ACTION_ON_OFF_WITH_INTERVAL: _ClassVar[Action.CommunicationType.GlobalCacheCommand.CommandAction]
                COMMAND_ACTION_OFF_ON_WITH_INTERVAL: _ClassVar[Action.CommunicationType.GlobalCacheCommand.CommandAction]
            COMMAND_ACTION_ON: Action.CommunicationType.GlobalCacheCommand.CommandAction
            COMMAND_ACTION_OFF: Action.CommunicationType.GlobalCacheCommand.CommandAction
            COMMAND_ACTION_ON_OFF_WITH_INTERVAL: Action.CommunicationType.GlobalCacheCommand.CommandAction
            COMMAND_ACTION_OFF_ON_WITH_INTERVAL: Action.CommunicationType.GlobalCacheCommand.CommandAction
            COMMAND_ACTION_FIELD_NUMBER: _ClassVar[int]
            OUTPUT_FIELD_NUMBER: _ClassVar[int]
            INTERVAL_FIELD_NUMBER: _ClassVar[int]
            command_action: Action.CommunicationType.GlobalCacheCommand.CommandAction
            output: int
            interval: int
            def __init__(self, command_action: _Optional[_Union[Action.CommunicationType.GlobalCacheCommand.CommandAction, str]] = ..., output: _Optional[int] = ..., interval: _Optional[int] = ...) -> None: ...
        class GVG100Command(_message.Message):
            __slots__ = ("command_action",)
            class CommandAction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                COMMAND_ACTION_FADE_TO_BLACK: _ClassVar[Action.CommunicationType.GVG100Command.CommandAction]
                COMMAND_ACTION_DSK_TOGGLE: _ClassVar[Action.CommunicationType.GVG100Command.CommandAction]
            COMMAND_ACTION_FADE_TO_BLACK: Action.CommunicationType.GVG100Command.CommandAction
            COMMAND_ACTION_DSK_TOGGLE: Action.CommunicationType.GVG100Command.CommandAction
            COMMAND_ACTION_FIELD_NUMBER: _ClassVar[int]
            command_action: Action.CommunicationType.GVG100Command.CommandAction
            def __init__(self, command_action: _Optional[_Union[Action.CommunicationType.GVG100Command.CommandAction, str]] = ...) -> None: ...
        class SonyBVSCommand(_message.Message):
            __slots__ = ("command_action",)
            class CommandAction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                COMMAND_ACTION_FADE_TO_BLACK: _ClassVar[Action.CommunicationType.SonyBVSCommand.CommandAction]
                COMMAND_ACTION_KEY_ON: _ClassVar[Action.CommunicationType.SonyBVSCommand.CommandAction]
                COMMAND_ACTION_KEY_OFF: _ClassVar[Action.CommunicationType.SonyBVSCommand.CommandAction]
                COMMAND_ACTION_DSK_ON: _ClassVar[Action.CommunicationType.SonyBVSCommand.CommandAction]
                COMMAND_ACTION_DSK_OFF: _ClassVar[Action.CommunicationType.SonyBVSCommand.CommandAction]
            COMMAND_ACTION_FADE_TO_BLACK: Action.CommunicationType.SonyBVSCommand.CommandAction
            COMMAND_ACTION_KEY_ON: Action.CommunicationType.SonyBVSCommand.CommandAction
            COMMAND_ACTION_KEY_OFF: Action.CommunicationType.SonyBVSCommand.CommandAction
            COMMAND_ACTION_DSK_ON: Action.CommunicationType.SonyBVSCommand.CommandAction
            COMMAND_ACTION_DSK_OFF: Action.CommunicationType.SonyBVSCommand.CommandAction
            COMMAND_ACTION_FIELD_NUMBER: _ClassVar[int]
            command_action: Action.CommunicationType.SonyBVSCommand.CommandAction
            def __init__(self, command_action: _Optional[_Union[Action.CommunicationType.SonyBVSCommand.CommandAction, str]] = ...) -> None: ...
        DEVICE_IDENTIFICATION_FIELD_NUMBER: _ClassVar[int]
        FORMAT_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        COMMANDS_FIELD_NUMBER: _ClassVar[int]
        MIDI_COMMAND_FIELD_NUMBER: _ClassVar[int]
        GLOBAL_CACHE_COMMAND_FIELD_NUMBER: _ClassVar[int]
        GVG100_COMMAND_FIELD_NUMBER: _ClassVar[int]
        SONY_BVS_COMMAND_FIELD_NUMBER: _ClassVar[int]
        device_identification: _basicTypes_pb2.CollectionElementType
        format: str
        description: str
        commands: _containers.RepeatedCompositeFieldContainer[Action.CommunicationType.Command]
        midi_command: Action.CommunicationType.MIDICommand
        global_cache_command: Action.CommunicationType.GlobalCacheCommand
        gvg100_command: Action.CommunicationType.GVG100Command
        sony_BVS_command: Action.CommunicationType.SonyBVSCommand
        def __init__(self, device_identification: _Optional[_Union[_basicTypes_pb2.CollectionElementType, _Mapping]] = ..., format: _Optional[str] = ..., description: _Optional[str] = ..., commands: _Optional[_Iterable[_Union[Action.CommunicationType.Command, _Mapping]]] = ..., midi_command: _Optional[_Union[Action.CommunicationType.MIDICommand, _Mapping]] = ..., global_cache_command: _Optional[_Union[Action.CommunicationType.GlobalCacheCommand, _Mapping]] = ..., gvg100_command: _Optional[_Union[Action.CommunicationType.GVG100Command, _Mapping]] = ..., sony_BVS_command: _Optional[_Union[Action.CommunicationType.SonyBVSCommand, _Mapping]] = ...) -> None: ...
    class MultiScreenType(_message.Message):
        __slots__ = ("identification",)
        IDENTIFICATION_FIELD_NUMBER: _ClassVar[int]
        identification: _basicTypes_pb2.CollectionElementType
        def __init__(self, identification: _Optional[_Union[_basicTypes_pb2.CollectionElementType, _Mapping]] = ...) -> None: ...
    class DocumentType(_message.Message):
        __slots__ = ("identification", "selected_arrangement", "content_destination")
        class ContentDestination(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            CONTENT_DESTINATION_GLOBAL: _ClassVar[Action.DocumentType.ContentDestination]
            CONTENT_DESTINATION_ANNOUNCEMENTS: _ClassVar[Action.DocumentType.ContentDestination]
        CONTENT_DESTINATION_GLOBAL: Action.DocumentType.ContentDestination
        CONTENT_DESTINATION_ANNOUNCEMENTS: Action.DocumentType.ContentDestination
        IDENTIFICATION_FIELD_NUMBER: _ClassVar[int]
        SELECTED_ARRANGEMENT_FIELD_NUMBER: _ClassVar[int]
        CONTENT_DESTINATION_FIELD_NUMBER: _ClassVar[int]
        identification: _basicTypes_pb2.CollectionElementType
        selected_arrangement: _basicTypes_pb2.UUID
        content_destination: Action.DocumentType.ContentDestination
        def __init__(self, identification: _Optional[_Union[_basicTypes_pb2.CollectionElementType, _Mapping]] = ..., selected_arrangement: _Optional[_Union[_basicTypes_pb2.UUID, _Mapping]] = ..., content_destination: _Optional[_Union[Action.DocumentType.ContentDestination, str]] = ...) -> None: ...
    class ExternalPresentationType(_message.Message):
        __slots__ = ("url",)
        URL_FIELD_NUMBER: _ClassVar[int]
        url: _basicTypes_pb2.URL
        def __init__(self, url: _Optional[_Union[_basicTypes_pb2.URL, _Mapping]] = ...) -> None: ...
    class AudienceLookType(_message.Message):
        __slots__ = ("identification",)
        IDENTIFICATION_FIELD_NUMBER: _ClassVar[int]
        identification: _basicTypes_pb2.CollectionElementType
        def __init__(self, identification: _Optional[_Union[_basicTypes_pb2.CollectionElementType, _Mapping]] = ...) -> None: ...
    class AudioInputType(_message.Message):
        __slots__ = ("index", "override_mode", "behavior_mode", "override_volume", "volume")
        INDEX_FIELD_NUMBER: _ClassVar[int]
        OVERRIDE_MODE_FIELD_NUMBER: _ClassVar[int]
        BEHAVIOR_MODE_FIELD_NUMBER: _ClassVar[int]
        OVERRIDE_VOLUME_FIELD_NUMBER: _ClassVar[int]
        VOLUME_FIELD_NUMBER: _ClassVar[int]
        index: int
        override_mode: bool
        behavior_mode: _input_pb2.AudioInput.BehaviorMode
        override_volume: bool
        volume: float
        def __init__(self, index: _Optional[int] = ..., override_mode: bool = ..., behavior_mode: _Optional[_Union[_input_pb2.AudioInput.BehaviorMode, _Mapping]] = ..., override_volume: bool = ..., volume: _Optional[float] = ...) -> None: ...
    class MacroType(_message.Message):
        __slots__ = ("identification",)
        IDENTIFICATION_FIELD_NUMBER: _ClassVar[int]
        identification: _basicTypes_pb2.CollectionElementType
        def __init__(self, identification: _Optional[_Union[_basicTypes_pb2.CollectionElementType, _Mapping]] = ...) -> None: ...
    UUID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    DELAY_TIME_FIELD_NUMBER: _ClassVar[int]
    OLD_TYPE_FIELD_NUMBER: _ClassVar[int]
    ISENABLED_FIELD_NUMBER: _ClassVar[int]
    LAYER_IDENTIFICATION_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_ELEMENT_FIELD_NUMBER: _ClassVar[int]
    PLAYLIST_ITEM_FIELD_NUMBER: _ClassVar[int]
    BLEND_MODE_FIELD_NUMBER: _ClassVar[int]
    TRANSITION_FIELD_NUMBER: _ClassVar[int]
    MEDIA_FIELD_NUMBER: _ClassVar[int]
    DOUBLE_ITEM_FIELD_NUMBER: _ClassVar[int]
    EFFECTS_FIELD_NUMBER: _ClassVar[int]
    SLIDE_FIELD_NUMBER: _ClassVar[int]
    BACKGROUND_FIELD_NUMBER: _ClassVar[int]
    TIMER_FIELD_NUMBER: _ClassVar[int]
    CLEAR_FIELD_NUMBER: _ClassVar[int]
    STAGE_FIELD_NUMBER: _ClassVar[int]
    PROP_FIELD_NUMBER: _ClassVar[int]
    MASK_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    SOCIAL_MEDIA_FIELD_NUMBER: _ClassVar[int]
    COMMUNICATION_FIELD_NUMBER: _ClassVar[int]
    MULTI_SCREEN_FIELD_NUMBER: _ClassVar[int]
    PRESENTATION_DOCUMENT_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_PRESENTATION_FIELD_NUMBER: _ClassVar[int]
    AUDIENCE_LOOK_FIELD_NUMBER: _ClassVar[int]
    AUDIO_INPUT_FIELD_NUMBER: _ClassVar[int]
    SLIDE_DESTINATION_FIELD_NUMBER: _ClassVar[int]
    MACRO_FIELD_NUMBER: _ClassVar[int]
    CLEAR_GROUP_FIELD_NUMBER: _ClassVar[int]
    TRANSPORT_CONTROL_FIELD_NUMBER: _ClassVar[int]
    uuid: _basicTypes_pb2.UUID
    name: str
    label: Action.Label
    delay_time: float
    old_type: Action.OldType
    isEnabled: bool
    layer_identification: Action.LayerIdentification
    duration: float
    type: Action.ActionType
    collection_element: _basicTypes_pb2.CollectionElementType
    playlist_item: Action.PlaylistItemType
    blend_mode: Action.BlendModeType
    transition: Action.TransitionType
    media: Action.MediaType
    double_item: Action.DoubleType
    effects: Action.EffectsType
    slide: Action.SlideType
    background: Action.BackgroundType
    timer: Action.TimerType
    clear: Action.ClearType
    stage: Action.StageLayoutType
    prop: Action.PropType
    mask: Action.MaskType
    message: Action.MessageType
    social_media: Action.SocialMediaType
    communication: Action.CommunicationType
    multi_screen: Action.MultiScreenType
    presentation_document: Action.DocumentType
    external_presentation: Action.ExternalPresentationType
    audience_look: Action.AudienceLookType
    audio_input: Action.AudioInputType
    slide_destination: Action.SlideDestinationType
    macro: Action.MacroType
    clear_group: Action.ClearGroupType
    transport_control: Action.TransportControlType
    def __init__(self, uuid: _Optional[_Union[_basicTypes_pb2.UUID, _Mapping]] = ..., name: _Optional[str] = ..., label: _Optional[_Union[Action.Label, _Mapping]] = ..., delay_time: _Optional[float] = ..., old_type: _Optional[_Union[Action.OldType, _Mapping]] = ..., isEnabled: bool = ..., layer_identification: _Optional[_Union[Action.LayerIdentification, _Mapping]] = ..., duration: _Optional[float] = ..., type: _Optional[_Union[Action.ActionType, str]] = ..., collection_element: _Optional[_Union[_basicTypes_pb2.CollectionElementType, _Mapping]] = ..., playlist_item: _Optional[_Union[Action.PlaylistItemType, _Mapping]] = ..., blend_mode: _Optional[_Union[Action.BlendModeType, _Mapping]] = ..., transition: _Optional[_Union[Action.TransitionType, _Mapping]] = ..., media: _Optional[_Union[Action.MediaType, _Mapping]] = ..., double_item: _Optional[_Union[Action.DoubleType, _Mapping]] = ..., effects: _Optional[_Union[Action.EffectsType, _Mapping]] = ..., slide: _Optional[_Union[Action.SlideType, _Mapping]] = ..., background: _Optional[_Union[Action.BackgroundType, _Mapping]] = ..., timer: _Optional[_Union[Action.TimerType, _Mapping]] = ..., clear: _Optional[_Union[Action.ClearType, _Mapping]] = ..., stage: _Optional[_Union[Action.StageLayoutType, _Mapping]] = ..., prop: _Optional[_Union[Action.PropType, _Mapping]] = ..., mask: _Optional[_Union[Action.MaskType, _Mapping]] = ..., message: _Optional[_Union[Action.MessageType, _Mapping]] = ..., social_media: _Optional[_Union[Action.SocialMediaType, _Mapping]] = ..., communication: _Optional[_Union[Action.CommunicationType, _Mapping]] = ..., multi_screen: _Optional[_Union[Action.MultiScreenType, _Mapping]] = ..., presentation_document: _Optional[_Union[Action.DocumentType, _Mapping]] = ..., external_presentation: _Optional[_Union[Action.ExternalPresentationType, _Mapping]] = ..., audience_look: _Optional[_Union[Action.AudienceLookType, _Mapping]] = ..., audio_input: _Optional[_Union[Action.AudioInputType, _Mapping]] = ..., slide_destination: _Optional[_Union[Action.SlideDestinationType, _Mapping]] = ..., macro: _Optional[_Union[Action.MacroType, _Mapping]] = ..., clear_group: _Optional[_Union[Action.ClearGroupType, _Mapping]] = ..., transport_control: _Optional[_Union[Action.TransportControlType, _Mapping]] = ...) -> None: ...
