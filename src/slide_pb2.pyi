import graphicsData_pb2 as _graphicsData_pb2
import basicTypes_pb2 as _basicTypes_pb2
import alignmentGuide_pb2 as _alignmentGuide_pb2
import effects_pb2 as _effects_pb2
import timers_pb2 as _timers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Slide(_message.Message):
    __slots__ = ("elements", "element_build_order", "guidelines", "draws_background_color", "background_color", "size", "uuid")
    class Element(_message.Message):
        __slots__ = ("element", "build_in", "build_out", "info", "reveal_type", "data_links", "childBuilds", "reveal_from_index", "text_scroller")
        class TextRevealType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            TEXT_REVEAL_TYPE_NONE: _ClassVar[Slide.Element.TextRevealType]
            TEXT_REVEAL_TYPE_BULLET: _ClassVar[Slide.Element.TextRevealType]
            TEXT_REVEAL_TYPE_UNDERLINE: _ClassVar[Slide.Element.TextRevealType]
        TEXT_REVEAL_TYPE_NONE: Slide.Element.TextRevealType
        TEXT_REVEAL_TYPE_BULLET: Slide.Element.TextRevealType
        TEXT_REVEAL_TYPE_UNDERLINE: Slide.Element.TextRevealType
        class Build(_message.Message):
            __slots__ = ("uuid", "elementUUID", "start", "delayTime", "transition")
            class Start(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                START_ON_CLICK: _ClassVar[Slide.Element.Build.Start]
                START_WITH_PREVIOUS: _ClassVar[Slide.Element.Build.Start]
                START_AFTER_PREVIOUS: _ClassVar[Slide.Element.Build.Start]
                START_WITH_SLIDE: _ClassVar[Slide.Element.Build.Start]
            START_ON_CLICK: Slide.Element.Build.Start
            START_WITH_PREVIOUS: Slide.Element.Build.Start
            START_AFTER_PREVIOUS: Slide.Element.Build.Start
            START_WITH_SLIDE: Slide.Element.Build.Start
            UUID_FIELD_NUMBER: _ClassVar[int]
            ELEMENTUUID_FIELD_NUMBER: _ClassVar[int]
            START_FIELD_NUMBER: _ClassVar[int]
            DELAYTIME_FIELD_NUMBER: _ClassVar[int]
            TRANSITION_FIELD_NUMBER: _ClassVar[int]
            uuid: _basicTypes_pb2.UUID
            elementUUID: _basicTypes_pb2.UUID
            start: Slide.Element.Build.Start
            delayTime: float
            transition: _effects_pb2.Transition
            def __init__(self, uuid: _Optional[_Union[_basicTypes_pb2.UUID, _Mapping]] = ..., elementUUID: _Optional[_Union[_basicTypes_pb2.UUID, _Mapping]] = ..., start: _Optional[_Union[Slide.Element.Build.Start, str]] = ..., delayTime: _Optional[float] = ..., transition: _Optional[_Union[_effects_pb2.Transition, _Mapping]] = ...) -> None: ...
        class ChildBuild(_message.Message):
            __slots__ = ("uuid", "start", "delayTime", "index")
            class Start(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                START_ON_CLICK: _ClassVar[Slide.Element.ChildBuild.Start]
                START_WITH_PREVIOUS: _ClassVar[Slide.Element.ChildBuild.Start]
                START_AFTER_PREVIOUS: _ClassVar[Slide.Element.ChildBuild.Start]
                START_WITH_SLIDE: _ClassVar[Slide.Element.ChildBuild.Start]
            START_ON_CLICK: Slide.Element.ChildBuild.Start
            START_WITH_PREVIOUS: Slide.Element.ChildBuild.Start
            START_AFTER_PREVIOUS: Slide.Element.ChildBuild.Start
            START_WITH_SLIDE: Slide.Element.ChildBuild.Start
            UUID_FIELD_NUMBER: _ClassVar[int]
            START_FIELD_NUMBER: _ClassVar[int]
            DELAYTIME_FIELD_NUMBER: _ClassVar[int]
            INDEX_FIELD_NUMBER: _ClassVar[int]
            uuid: _basicTypes_pb2.UUID
            start: Slide.Element.ChildBuild.Start
            delayTime: float
            index: int
            def __init__(self, uuid: _Optional[_Union[_basicTypes_pb2.UUID, _Mapping]] = ..., start: _Optional[_Union[Slide.Element.ChildBuild.Start, str]] = ..., delayTime: _Optional[float] = ..., index: _Optional[int] = ...) -> None: ...
        class DataLink(_message.Message):
            __slots__ = ("ticker", "alternate_text", "timer_text", "clock_text", "chord_chart", "output_screen", "pco_live", "alternate_fill", "visibility_link", "slide_text", "stage_message", "video_countdown", "slide_image", "ccli_text", "group_name", "group_color", "presentation_notes", "playlist_item", "auto_advance_time_remaining", "capture_status_text", "capture_status_color", "slide_count", "audio_countdown", "presentation", "slide_Label_Text", "slide_Label_Color", "rss_feed", "file_feed", "chord_pro_chart", "playback_marker_text", "playback_marker_color", "timecode_text", "timecode_status")
            class RSSFeed(_message.Message):
                __slots__ = ("url", "content", "text_delimiter")
                class ContentType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                    __slots__ = ()
                    CONTENT_TYPE_TITLE_ONLY: _ClassVar[Slide.Element.DataLink.RSSFeed.ContentType]
                    CONTENT_TYPE_TITLE_AND_DESCRIPTION: _ClassVar[Slide.Element.DataLink.RSSFeed.ContentType]
                CONTENT_TYPE_TITLE_ONLY: Slide.Element.DataLink.RSSFeed.ContentType
                CONTENT_TYPE_TITLE_AND_DESCRIPTION: Slide.Element.DataLink.RSSFeed.ContentType
                URL_FIELD_NUMBER: _ClassVar[int]
                CONTENT_FIELD_NUMBER: _ClassVar[int]
                TEXT_DELIMITER_FIELD_NUMBER: _ClassVar[int]
                url: _basicTypes_pb2.URL
                content: Slide.Element.DataLink.RSSFeed.ContentType
                text_delimiter: str
                def __init__(self, url: _Optional[_Union[_basicTypes_pb2.URL, _Mapping]] = ..., content: _Optional[_Union[Slide.Element.DataLink.RSSFeed.ContentType, str]] = ..., text_delimiter: _Optional[str] = ...) -> None: ...
            class FileFeed(_message.Message):
                __slots__ = ("url",)
                URL_FIELD_NUMBER: _ClassVar[int]
                url: _basicTypes_pb2.URL
                def __init__(self, url: _Optional[_Union[_basicTypes_pb2.URL, _Mapping]] = ...) -> None: ...
            class Ticker(_message.Message):
                __slots__ = ("play_rate", "should_loop", "loop_delay", "text_delimiter", "text_type", "rss_type", "file_type")
                class TextType(_message.Message):
                    __slots__ = ("text",)
                    TEXT_FIELD_NUMBER: _ClassVar[int]
                    text: str
                    def __init__(self, text: _Optional[str] = ...) -> None: ...
                class RSSType(_message.Message):
                    __slots__ = ("url", "content")
                    class ContentType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                        __slots__ = ()
                        CONTENT_TYPE_TITLE_ONLY: _ClassVar[Slide.Element.DataLink.Ticker.RSSType.ContentType]
                        CONTENT_TYPE_TITLE_AND_DESCRIPTION: _ClassVar[Slide.Element.DataLink.Ticker.RSSType.ContentType]
                    CONTENT_TYPE_TITLE_ONLY: Slide.Element.DataLink.Ticker.RSSType.ContentType
                    CONTENT_TYPE_TITLE_AND_DESCRIPTION: Slide.Element.DataLink.Ticker.RSSType.ContentType
                    URL_FIELD_NUMBER: _ClassVar[int]
                    CONTENT_FIELD_NUMBER: _ClassVar[int]
                    url: _basicTypes_pb2.URL
                    content: Slide.Element.DataLink.Ticker.RSSType.ContentType
                    def __init__(self, url: _Optional[_Union[_basicTypes_pb2.URL, _Mapping]] = ..., content: _Optional[_Union[Slide.Element.DataLink.Ticker.RSSType.ContentType, str]] = ...) -> None: ...
                class FileType(_message.Message):
                    __slots__ = ("url",)
                    URL_FIELD_NUMBER: _ClassVar[int]
                    url: _basicTypes_pb2.URL
                    def __init__(self, url: _Optional[_Union[_basicTypes_pb2.URL, _Mapping]] = ...) -> None: ...
                PLAY_RATE_FIELD_NUMBER: _ClassVar[int]
                SHOULD_LOOP_FIELD_NUMBER: _ClassVar[int]
                LOOP_DELAY_FIELD_NUMBER: _ClassVar[int]
                TEXT_DELIMITER_FIELD_NUMBER: _ClassVar[int]
                TEXT_TYPE_FIELD_NUMBER: _ClassVar[int]
                RSS_TYPE_FIELD_NUMBER: _ClassVar[int]
                FILE_TYPE_FIELD_NUMBER: _ClassVar[int]
                play_rate: float
                should_loop: bool
                loop_delay: float
                text_delimiter: str
                text_type: Slide.Element.DataLink.Ticker.TextType
                rss_type: Slide.Element.DataLink.Ticker.RSSType
                file_type: Slide.Element.DataLink.Ticker.FileType
                def __init__(self, play_rate: _Optional[float] = ..., should_loop: bool = ..., loop_delay: _Optional[float] = ..., text_delimiter: _Optional[str] = ..., text_type: _Optional[_Union[Slide.Element.DataLink.Ticker.TextType, _Mapping]] = ..., rss_type: _Optional[_Union[Slide.Element.DataLink.Ticker.RSSType, _Mapping]] = ..., file_type: _Optional[_Union[Slide.Element.DataLink.Ticker.FileType, _Mapping]] = ...) -> None: ...
            class AlternateElementText(_message.Message):
                __slots__ = ("other_element_uuid", "other_element_name", "text_transform_options", "text_transform")
                class TextTransformOption(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                    __slots__ = ()
                    TEXT_TRANSFORM_OPTION_NONE: _ClassVar[Slide.Element.DataLink.AlternateElementText.TextTransformOption]
                    TEXT_TRANSFORM_OPTION_REMOVE_LINE_RETURNS: _ClassVar[Slide.Element.DataLink.AlternateElementText.TextTransformOption]
                    TEXT_TRANSFORM_OPTION_ONE_WORD_PER_LINE: _ClassVar[Slide.Element.DataLink.AlternateElementText.TextTransformOption]
                    TEXT_TRANSFORM_OPTION_ONE_CHARACTER_PER_LINE: _ClassVar[Slide.Element.DataLink.AlternateElementText.TextTransformOption]
                TEXT_TRANSFORM_OPTION_NONE: Slide.Element.DataLink.AlternateElementText.TextTransformOption
                TEXT_TRANSFORM_OPTION_REMOVE_LINE_RETURNS: Slide.Element.DataLink.AlternateElementText.TextTransformOption
                TEXT_TRANSFORM_OPTION_ONE_WORD_PER_LINE: Slide.Element.DataLink.AlternateElementText.TextTransformOption
                TEXT_TRANSFORM_OPTION_ONE_CHARACTER_PER_LINE: Slide.Element.DataLink.AlternateElementText.TextTransformOption
                OTHER_ELEMENT_UUID_FIELD_NUMBER: _ClassVar[int]
                OTHER_ELEMENT_NAME_FIELD_NUMBER: _ClassVar[int]
                TEXT_TRANSFORM_OPTIONS_FIELD_NUMBER: _ClassVar[int]
                TEXT_TRANSFORM_FIELD_NUMBER: _ClassVar[int]
                other_element_uuid: _basicTypes_pb2.UUID
                other_element_name: str
                text_transform_options: int
                text_transform: Slide.Element.DataLink.AlternateElementText.TextTransformOption
                def __init__(self, other_element_uuid: _Optional[_Union[_basicTypes_pb2.UUID, _Mapping]] = ..., other_element_name: _Optional[str] = ..., text_transform_options: _Optional[int] = ..., text_transform: _Optional[_Union[Slide.Element.DataLink.AlternateElementText.TextTransformOption, str]] = ...) -> None: ...
            class CCLIText(_message.Message):
                __slots__ = ()
                def __init__(self) -> None: ...
            class ColorTrigger(_message.Message):
                __slots__ = ("time", "color")
                TIME_FIELD_NUMBER: _ClassVar[int]
                COLOR_FIELD_NUMBER: _ClassVar[int]
                time: float
                color: _basicTypes_pb2.Color
                def __init__(self, time: _Optional[float] = ..., color: _Optional[_Union[_basicTypes_pb2.Color, _Mapping]] = ...) -> None: ...
            class TimerText(_message.Message):
                __slots__ = ("timer_uuid", "timer_name", "timer_format", "timer_format_string", "color_triggers")
                TIMER_UUID_FIELD_NUMBER: _ClassVar[int]
                TIMER_NAME_FIELD_NUMBER: _ClassVar[int]
                TIMER_FORMAT_FIELD_NUMBER: _ClassVar[int]
                TIMER_FORMAT_STRING_FIELD_NUMBER: _ClassVar[int]
                COLOR_TRIGGERS_FIELD_NUMBER: _ClassVar[int]
                timer_uuid: _basicTypes_pb2.UUID
                timer_name: str
                timer_format: _timers_pb2.Timer.Format
                timer_format_string: str
                color_triggers: _containers.RepeatedCompositeFieldContainer[Slide.Element.DataLink.ColorTrigger]
                def __init__(self, timer_uuid: _Optional[_Union[_basicTypes_pb2.UUID, _Mapping]] = ..., timer_name: _Optional[str] = ..., timer_format: _Optional[_Union[_timers_pb2.Timer.Format, _Mapping]] = ..., timer_format_string: _Optional[str] = ..., color_triggers: _Optional[_Iterable[_Union[Slide.Element.DataLink.ColorTrigger, _Mapping]]] = ...) -> None: ...
            class ClockText(_message.Message):
                __slots__ = ("clock_format_string", "format")
                CLOCK_FORMAT_STRING_FIELD_NUMBER: _ClassVar[int]
                FORMAT_FIELD_NUMBER: _ClassVar[int]
                clock_format_string: str
                format: _timers_pb2.Clock.Format
                def __init__(self, clock_format_string: _Optional[str] = ..., format: _Optional[_Union[_timers_pb2.Clock.Format, _Mapping]] = ...) -> None: ...
            class ChordChart(_message.Message):
                __slots__ = ()
                def __init__(self) -> None: ...
            class OutputScreen(_message.Message):
                __slots__ = ("screen_id", "screen_name")
                SCREEN_ID_FIELD_NUMBER: _ClassVar[int]
                SCREEN_NAME_FIELD_NUMBER: _ClassVar[int]
                screen_id: _basicTypes_pb2.UUID
                screen_name: str
                def __init__(self, screen_id: _Optional[_Union[_basicTypes_pb2.UUID, _Mapping]] = ..., screen_name: _Optional[str] = ...) -> None: ...
            class PCOLive(_message.Message):
                __slots__ = ("theme", "countdown_type")
                class Theme(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                    __slots__ = ()
                    PCOLIVE_THEME_LIGHT: _ClassVar[Slide.Element.DataLink.PCOLive.Theme]
                    PCOLIVE_THEME_DARK: _ClassVar[Slide.Element.DataLink.PCOLive.Theme]
                PCOLIVE_THEME_LIGHT: Slide.Element.DataLink.PCOLive.Theme
                PCOLIVE_THEME_DARK: Slide.Element.DataLink.PCOLive.Theme
                class CountdownType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                    __slots__ = ()
                    COUNTDOWN_TYPE_FULL_ITEM_LENGTH: _ClassVar[Slide.Element.DataLink.PCOLive.CountdownType]
                    COUNTDOWN_TYPE_END_ITEM_ON_TIME: _ClassVar[Slide.Element.DataLink.PCOLive.CountdownType]
                    COUNTDOWN_TYPE_END_SERVICE_ON_TIME: _ClassVar[Slide.Element.DataLink.PCOLive.CountdownType]
                COUNTDOWN_TYPE_FULL_ITEM_LENGTH: Slide.Element.DataLink.PCOLive.CountdownType
                COUNTDOWN_TYPE_END_ITEM_ON_TIME: Slide.Element.DataLink.PCOLive.CountdownType
                COUNTDOWN_TYPE_END_SERVICE_ON_TIME: Slide.Element.DataLink.PCOLive.CountdownType
                THEME_FIELD_NUMBER: _ClassVar[int]
                COUNTDOWN_TYPE_FIELD_NUMBER: _ClassVar[int]
                theme: Slide.Element.DataLink.PCOLive.Theme
                countdown_type: Slide.Element.DataLink.PCOLive.CountdownType
                def __init__(self, theme: _Optional[_Union[Slide.Element.DataLink.PCOLive.Theme, str]] = ..., countdown_type: _Optional[_Union[Slide.Element.DataLink.PCOLive.CountdownType, str]] = ...) -> None: ...
            class AlternateElementFill(_message.Message):
                __slots__ = ("other_element_uuid", "other_element_name")
                OTHER_ELEMENT_UUID_FIELD_NUMBER: _ClassVar[int]
                OTHER_ELEMENT_NAME_FIELD_NUMBER: _ClassVar[int]
                other_element_uuid: _basicTypes_pb2.UUID
                other_element_name: str
                def __init__(self, other_element_uuid: _Optional[_Union[_basicTypes_pb2.UUID, _Mapping]] = ..., other_element_name: _Optional[str] = ...) -> None: ...
            class VisibilityLink(_message.Message):
                __slots__ = ("visibility_criterion", "conditions")
                class VisibilityCriterion(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                    __slots__ = ()
                    VISIBILITY_CRITERION_ALL: _ClassVar[Slide.Element.DataLink.VisibilityLink.VisibilityCriterion]
                    VISIBILITY_CRITERION_ANY: _ClassVar[Slide.Element.DataLink.VisibilityLink.VisibilityCriterion]
                    VISIBILITY_CRITERION_NONE: _ClassVar[Slide.Element.DataLink.VisibilityLink.VisibilityCriterion]
                VISIBILITY_CRITERION_ALL: Slide.Element.DataLink.VisibilityLink.VisibilityCriterion
                VISIBILITY_CRITERION_ANY: Slide.Element.DataLink.VisibilityLink.VisibilityCriterion
                VISIBILITY_CRITERION_NONE: Slide.Element.DataLink.VisibilityLink.VisibilityCriterion
                class Condition(_message.Message):
                    __slots__ = ("element_visibility", "timer_visibility", "video_countdown_visibility", "capture_session_visibility", "video_input_visibility", "audio_countdown_visibility")
                    class ElementVisibility(_message.Message):
                        __slots__ = ("other_element_uuid", "other_element_name", "visibility_criterion")
                        class ElementVisibilityCriterion(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                            __slots__ = ()
                            ELEMENT_VISIBILITY_CRITERION_HAS_TEXT: _ClassVar[Slide.Element.DataLink.VisibilityLink.Condition.ElementVisibility.ElementVisibilityCriterion]
                            ELEMENT_VISIBILITY_CRITERION_HAS_NO_TEXT: _ClassVar[Slide.Element.DataLink.VisibilityLink.Condition.ElementVisibility.ElementVisibilityCriterion]
                        ELEMENT_VISIBILITY_CRITERION_HAS_TEXT: Slide.Element.DataLink.VisibilityLink.Condition.ElementVisibility.ElementVisibilityCriterion
                        ELEMENT_VISIBILITY_CRITERION_HAS_NO_TEXT: Slide.Element.DataLink.VisibilityLink.Condition.ElementVisibility.ElementVisibilityCriterion
                        OTHER_ELEMENT_UUID_FIELD_NUMBER: _ClassVar[int]
                        OTHER_ELEMENT_NAME_FIELD_NUMBER: _ClassVar[int]
                        VISIBILITY_CRITERION_FIELD_NUMBER: _ClassVar[int]
                        other_element_uuid: _basicTypes_pb2.UUID
                        other_element_name: str
                        visibility_criterion: Slide.Element.DataLink.VisibilityLink.Condition.ElementVisibility.ElementVisibilityCriterion
                        def __init__(self, other_element_uuid: _Optional[_Union[_basicTypes_pb2.UUID, _Mapping]] = ..., other_element_name: _Optional[str] = ..., visibility_criterion: _Optional[_Union[Slide.Element.DataLink.VisibilityLink.Condition.ElementVisibility.ElementVisibilityCriterion, str]] = ...) -> None: ...
                    class TimerVisibility(_message.Message):
                        __slots__ = ("timer_uuid", "timer_name", "visibility_criterion")
                        class TimerVisibilityCriterion(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                            __slots__ = ()
                            TIMER_VISIBILITY_CRITERION_HAS_TIME_REMAINING: _ClassVar[Slide.Element.DataLink.VisibilityLink.Condition.TimerVisibility.TimerVisibilityCriterion]
                            TIMER_VISIBILITY_CRITERION_HAS_EXPIRED: _ClassVar[Slide.Element.DataLink.VisibilityLink.Condition.TimerVisibility.TimerVisibilityCriterion]
                            TIMER_VISIBILITY_CRITERION_IS_RUNNING: _ClassVar[Slide.Element.DataLink.VisibilityLink.Condition.TimerVisibility.TimerVisibilityCriterion]
                            TIMER_VISIBILITY_CRITERION_NOT_RUNNING: _ClassVar[Slide.Element.DataLink.VisibilityLink.Condition.TimerVisibility.TimerVisibilityCriterion]
                        TIMER_VISIBILITY_CRITERION_HAS_TIME_REMAINING: Slide.Element.DataLink.VisibilityLink.Condition.TimerVisibility.TimerVisibilityCriterion
                        TIMER_VISIBILITY_CRITERION_HAS_EXPIRED: Slide.Element.DataLink.VisibilityLink.Condition.TimerVisibility.TimerVisibilityCriterion
                        TIMER_VISIBILITY_CRITERION_IS_RUNNING: Slide.Element.DataLink.VisibilityLink.Condition.TimerVisibility.TimerVisibilityCriterion
                        TIMER_VISIBILITY_CRITERION_NOT_RUNNING: Slide.Element.DataLink.VisibilityLink.Condition.TimerVisibility.TimerVisibilityCriterion
                        TIMER_UUID_FIELD_NUMBER: _ClassVar[int]
                        TIMER_NAME_FIELD_NUMBER: _ClassVar[int]
                        VISIBILITY_CRITERION_FIELD_NUMBER: _ClassVar[int]
                        timer_uuid: _basicTypes_pb2.UUID
                        timer_name: str
                        visibility_criterion: Slide.Element.DataLink.VisibilityLink.Condition.TimerVisibility.TimerVisibilityCriterion
                        def __init__(self, timer_uuid: _Optional[_Union[_basicTypes_pb2.UUID, _Mapping]] = ..., timer_name: _Optional[str] = ..., visibility_criterion: _Optional[_Union[Slide.Element.DataLink.VisibilityLink.Condition.TimerVisibility.TimerVisibilityCriterion, str]] = ...) -> None: ...
                    class VideoCountdownVisibility(_message.Message):
                        __slots__ = ("visibility_criterion",)
                        class VideoCountdownVisibilityCriterion(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                            __slots__ = ()
                            VIDEO_COUNTDOWN_VISIBILITY_CRITERION_HAS_TIME_REMAINING: _ClassVar[Slide.Element.DataLink.VisibilityLink.Condition.VideoCountdownVisibility.VideoCountdownVisibilityCriterion]
                            VIDEO_COUNTDOWN_VISIBILITY_CRITERION_HAS_EXPIRED: _ClassVar[Slide.Element.DataLink.VisibilityLink.Condition.VideoCountdownVisibility.VideoCountdownVisibilityCriterion]
                            VIDEO_COUNTDOWN_VISIBILITY_CRITERION_IS_RUNNING: _ClassVar[Slide.Element.DataLink.VisibilityLink.Condition.VideoCountdownVisibility.VideoCountdownVisibilityCriterion]
                            VIDEO_COUNTDOWN_VISIBILITY_CRITERION_NOT_RUNNING: _ClassVar[Slide.Element.DataLink.VisibilityLink.Condition.VideoCountdownVisibility.VideoCountdownVisibilityCriterion]
                            VIDEO_COUNTDOWN_VISIBILITY_CRITERION_LOOPING: _ClassVar[Slide.Element.DataLink.VisibilityLink.Condition.VideoCountdownVisibility.VideoCountdownVisibilityCriterion]
                            VIDEO_COUNTDOWN_VISIBILITY_CRITERION_NOT_LOOPING: _ClassVar[Slide.Element.DataLink.VisibilityLink.Condition.VideoCountdownVisibility.VideoCountdownVisibilityCriterion]
                        VIDEO_COUNTDOWN_VISIBILITY_CRITERION_HAS_TIME_REMAINING: Slide.Element.DataLink.VisibilityLink.Condition.VideoCountdownVisibility.VideoCountdownVisibilityCriterion
                        VIDEO_COUNTDOWN_VISIBILITY_CRITERION_HAS_EXPIRED: Slide.Element.DataLink.VisibilityLink.Condition.VideoCountdownVisibility.VideoCountdownVisibilityCriterion
                        VIDEO_COUNTDOWN_VISIBILITY_CRITERION_IS_RUNNING: Slide.Element.DataLink.VisibilityLink.Condition.VideoCountdownVisibility.VideoCountdownVisibilityCriterion
                        VIDEO_COUNTDOWN_VISIBILITY_CRITERION_NOT_RUNNING: Slide.Element.DataLink.VisibilityLink.Condition.VideoCountdownVisibility.VideoCountdownVisibilityCriterion
                        VIDEO_COUNTDOWN_VISIBILITY_CRITERION_LOOPING: Slide.Element.DataLink.VisibilityLink.Condition.VideoCountdownVisibility.VideoCountdownVisibilityCriterion
                        VIDEO_COUNTDOWN_VISIBILITY_CRITERION_NOT_LOOPING: Slide.Element.DataLink.VisibilityLink.Condition.VideoCountdownVisibility.VideoCountdownVisibilityCriterion
                        VISIBILITY_CRITERION_FIELD_NUMBER: _ClassVar[int]
                        visibility_criterion: Slide.Element.DataLink.VisibilityLink.Condition.VideoCountdownVisibility.VideoCountdownVisibilityCriterion
                        def __init__(self, visibility_criterion: _Optional[_Union[Slide.Element.DataLink.VisibilityLink.Condition.VideoCountdownVisibility.VideoCountdownVisibilityCriterion, str]] = ...) -> None: ...
                    class AudioCountdownVisibility(_message.Message):
                        __slots__ = ("visibility_criterion",)
                        class AudioCountdownVisibilityCriterion(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                            __slots__ = ()
                            AUDIO_COUNTDOWN_VISIBILITY_CRITERION_HAS_TIME_REMAINING: _ClassVar[Slide.Element.DataLink.VisibilityLink.Condition.AudioCountdownVisibility.AudioCountdownVisibilityCriterion]
                            AUDIO_COUNTDOWN_VISIBILITY_CRITERION_HAS_EXPIRED: _ClassVar[Slide.Element.DataLink.VisibilityLink.Condition.AudioCountdownVisibility.AudioCountdownVisibilityCriterion]
                            AUDIO_COUNTDOWN_VISIBILITY_CRITERION_IS_RUNNING: _ClassVar[Slide.Element.DataLink.VisibilityLink.Condition.AudioCountdownVisibility.AudioCountdownVisibilityCriterion]
                            AUDIO_COUNTDOWN_VISIBILITY_CRITERION_NOT_RUNNING: _ClassVar[Slide.Element.DataLink.VisibilityLink.Condition.AudioCountdownVisibility.AudioCountdownVisibilityCriterion]
                            AUDIO_COUNTDOWN_VISIBILITY_CRITERION_LOOPING: _ClassVar[Slide.Element.DataLink.VisibilityLink.Condition.AudioCountdownVisibility.AudioCountdownVisibilityCriterion]
                            AUDIO_COUNTDOWN_VISIBILITY_CRITERION_NOT_LOOPING: _ClassVar[Slide.Element.DataLink.VisibilityLink.Condition.AudioCountdownVisibility.AudioCountdownVisibilityCriterion]
                        AUDIO_COUNTDOWN_VISIBILITY_CRITERION_HAS_TIME_REMAINING: Slide.Element.DataLink.VisibilityLink.Condition.AudioCountdownVisibility.AudioCountdownVisibilityCriterion
                        AUDIO_COUNTDOWN_VISIBILITY_CRITERION_HAS_EXPIRED: Slide.Element.DataLink.VisibilityLink.Condition.AudioCountdownVisibility.AudioCountdownVisibilityCriterion
                        AUDIO_COUNTDOWN_VISIBILITY_CRITERION_IS_RUNNING: Slide.Element.DataLink.VisibilityLink.Condition.AudioCountdownVisibility.AudioCountdownVisibilityCriterion
                        AUDIO_COUNTDOWN_VISIBILITY_CRITERION_NOT_RUNNING: Slide.Element.DataLink.VisibilityLink.Condition.AudioCountdownVisibility.AudioCountdownVisibilityCriterion
                        AUDIO_COUNTDOWN_VISIBILITY_CRITERION_LOOPING: Slide.Element.DataLink.VisibilityLink.Condition.AudioCountdownVisibility.AudioCountdownVisibilityCriterion
                        AUDIO_COUNTDOWN_VISIBILITY_CRITERION_NOT_LOOPING: Slide.Element.DataLink.VisibilityLink.Condition.AudioCountdownVisibility.AudioCountdownVisibilityCriterion
                        VISIBILITY_CRITERION_FIELD_NUMBER: _ClassVar[int]
                        visibility_criterion: Slide.Element.DataLink.VisibilityLink.Condition.AudioCountdownVisibility.AudioCountdownVisibilityCriterion
                        def __init__(self, visibility_criterion: _Optional[_Union[Slide.Element.DataLink.VisibilityLink.Condition.AudioCountdownVisibility.AudioCountdownVisibilityCriterion, str]] = ...) -> None: ...
                    class CaptureSessionVisibility(_message.Message):
                        __slots__ = ("visibility_criterion",)
                        class CaptureSessionVisibilityCriterion(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                            __slots__ = ()
                            CAPTURE_SESSION_VISIBILITY_CRITERION_ACTIVE: _ClassVar[Slide.Element.DataLink.VisibilityLink.Condition.CaptureSessionVisibility.CaptureSessionVisibilityCriterion]
                            CAPTURE_SESSION_VISIBILITY_CRITERION_INACTIVE: _ClassVar[Slide.Element.DataLink.VisibilityLink.Condition.CaptureSessionVisibility.CaptureSessionVisibilityCriterion]
                        CAPTURE_SESSION_VISIBILITY_CRITERION_ACTIVE: Slide.Element.DataLink.VisibilityLink.Condition.CaptureSessionVisibility.CaptureSessionVisibilityCriterion
                        CAPTURE_SESSION_VISIBILITY_CRITERION_INACTIVE: Slide.Element.DataLink.VisibilityLink.Condition.CaptureSessionVisibility.CaptureSessionVisibilityCriterion
                        VISIBILITY_CRITERION_FIELD_NUMBER: _ClassVar[int]
                        visibility_criterion: Slide.Element.DataLink.VisibilityLink.Condition.CaptureSessionVisibility.CaptureSessionVisibilityCriterion
                        def __init__(self, visibility_criterion: _Optional[_Union[Slide.Element.DataLink.VisibilityLink.Condition.CaptureSessionVisibility.CaptureSessionVisibilityCriterion, str]] = ...) -> None: ...
                    class VideoInputVisibility(_message.Message):
                        __slots__ = ("video_input_index", "visibility_criterion")
                        class VideoInputVisibilityCriterion(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                            __slots__ = ()
                            VIDEO_INPUT_VISIBILITY_CRITERION_ACTIVE: _ClassVar[Slide.Element.DataLink.VisibilityLink.Condition.VideoInputVisibility.VideoInputVisibilityCriterion]
                            VIDEO_INPUT_VISIBILITY_CRITERION_INACTIVE: _ClassVar[Slide.Element.DataLink.VisibilityLink.Condition.VideoInputVisibility.VideoInputVisibilityCriterion]
                        VIDEO_INPUT_VISIBILITY_CRITERION_ACTIVE: Slide.Element.DataLink.VisibilityLink.Condition.VideoInputVisibility.VideoInputVisibilityCriterion
                        VIDEO_INPUT_VISIBILITY_CRITERION_INACTIVE: Slide.Element.DataLink.VisibilityLink.Condition.VideoInputVisibility.VideoInputVisibilityCriterion
                        VIDEO_INPUT_INDEX_FIELD_NUMBER: _ClassVar[int]
                        VISIBILITY_CRITERION_FIELD_NUMBER: _ClassVar[int]
                        video_input_index: int
                        visibility_criterion: Slide.Element.DataLink.VisibilityLink.Condition.VideoInputVisibility.VideoInputVisibilityCriterion
                        def __init__(self, video_input_index: _Optional[int] = ..., visibility_criterion: _Optional[_Union[Slide.Element.DataLink.VisibilityLink.Condition.VideoInputVisibility.VideoInputVisibilityCriterion, str]] = ...) -> None: ...
                    ELEMENT_VISIBILITY_FIELD_NUMBER: _ClassVar[int]
                    TIMER_VISIBILITY_FIELD_NUMBER: _ClassVar[int]
                    VIDEO_COUNTDOWN_VISIBILITY_FIELD_NUMBER: _ClassVar[int]
                    CAPTURE_SESSION_VISIBILITY_FIELD_NUMBER: _ClassVar[int]
                    VIDEO_INPUT_VISIBILITY_FIELD_NUMBER: _ClassVar[int]
                    AUDIO_COUNTDOWN_VISIBILITY_FIELD_NUMBER: _ClassVar[int]
                    element_visibility: Slide.Element.DataLink.VisibilityLink.Condition.ElementVisibility
                    timer_visibility: Slide.Element.DataLink.VisibilityLink.Condition.TimerVisibility
                    video_countdown_visibility: Slide.Element.DataLink.VisibilityLink.Condition.VideoCountdownVisibility
                    capture_session_visibility: Slide.Element.DataLink.VisibilityLink.Condition.CaptureSessionVisibility
                    video_input_visibility: Slide.Element.DataLink.VisibilityLink.Condition.VideoInputVisibility
                    audio_countdown_visibility: Slide.Element.DataLink.VisibilityLink.Condition.AudioCountdownVisibility
                    def __init__(self, element_visibility: _Optional[_Union[Slide.Element.DataLink.VisibilityLink.Condition.ElementVisibility, _Mapping]] = ..., timer_visibility: _Optional[_Union[Slide.Element.DataLink.VisibilityLink.Condition.TimerVisibility, _Mapping]] = ..., video_countdown_visibility: _Optional[_Union[Slide.Element.DataLink.VisibilityLink.Condition.VideoCountdownVisibility, _Mapping]] = ..., capture_session_visibility: _Optional[_Union[Slide.Element.DataLink.VisibilityLink.Condition.CaptureSessionVisibility, _Mapping]] = ..., video_input_visibility: _Optional[_Union[Slide.Element.DataLink.VisibilityLink.Condition.VideoInputVisibility, _Mapping]] = ..., audio_countdown_visibility: _Optional[_Union[Slide.Element.DataLink.VisibilityLink.Condition.AudioCountdownVisibility, _Mapping]] = ...) -> None: ...
                VISIBILITY_CRITERION_FIELD_NUMBER: _ClassVar[int]
                CONDITIONS_FIELD_NUMBER: _ClassVar[int]
                visibility_criterion: Slide.Element.DataLink.VisibilityLink.VisibilityCriterion
                conditions: _containers.RepeatedCompositeFieldContainer[Slide.Element.DataLink.VisibilityLink.Condition]
                def __init__(self, visibility_criterion: _Optional[_Union[Slide.Element.DataLink.VisibilityLink.VisibilityCriterion, str]] = ..., conditions: _Optional[_Iterable[_Union[Slide.Element.DataLink.VisibilityLink.Condition, _Mapping]]] = ...) -> None: ...
            class SlideText(_message.Message):
                __slots__ = ("source_slide", "source_option", "preserve_notes_format", "name_to_match", "element_text_transform")
                class SlideSourceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                    __slots__ = ()
                    SLIDE_SOURCE_TYPE_CURRENT_SLIDE: _ClassVar[Slide.Element.DataLink.SlideText.SlideSourceType]
                    SLIDE_SOURCE_TYPE_NEXT_SLIDE: _ClassVar[Slide.Element.DataLink.SlideText.SlideSourceType]
                SLIDE_SOURCE_TYPE_CURRENT_SLIDE: Slide.Element.DataLink.SlideText.SlideSourceType
                SLIDE_SOURCE_TYPE_NEXT_SLIDE: Slide.Element.DataLink.SlideText.SlideSourceType
                class TextSourceOption(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                    __slots__ = ()
                    TEXT_SOURCE_OPTION_TEXT: _ClassVar[Slide.Element.DataLink.SlideText.TextSourceOption]
                    TEXT_SOURCE_OPTION_NOTES: _ClassVar[Slide.Element.DataLink.SlideText.TextSourceOption]
                    TEXT_SOURCE_OPTION_ELEMENT_MATCHING_NAME: _ClassVar[Slide.Element.DataLink.SlideText.TextSourceOption]
                TEXT_SOURCE_OPTION_TEXT: Slide.Element.DataLink.SlideText.TextSourceOption
                TEXT_SOURCE_OPTION_NOTES: Slide.Element.DataLink.SlideText.TextSourceOption
                TEXT_SOURCE_OPTION_ELEMENT_MATCHING_NAME: Slide.Element.DataLink.SlideText.TextSourceOption
                class TextTransformOption(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                    __slots__ = ()
                    TEXT_TRANSFORM_OPTION_NONE: _ClassVar[Slide.Element.DataLink.SlideText.TextTransformOption]
                    TEXT_TRANSFORM_OPTION_REMOVE_LINE_RETURNS: _ClassVar[Slide.Element.DataLink.SlideText.TextTransformOption]
                    TEXT_TRANSFORM_OPTION_ONE_WORD_PER_LINE: _ClassVar[Slide.Element.DataLink.SlideText.TextTransformOption]
                    TEXT_TRANSFORM_OPTION_ONE_CHARACTER_PER_LINE: _ClassVar[Slide.Element.DataLink.SlideText.TextTransformOption]
                TEXT_TRANSFORM_OPTION_NONE: Slide.Element.DataLink.SlideText.TextTransformOption
                TEXT_TRANSFORM_OPTION_REMOVE_LINE_RETURNS: Slide.Element.DataLink.SlideText.TextTransformOption
                TEXT_TRANSFORM_OPTION_ONE_WORD_PER_LINE: Slide.Element.DataLink.SlideText.TextTransformOption
                TEXT_TRANSFORM_OPTION_ONE_CHARACTER_PER_LINE: Slide.Element.DataLink.SlideText.TextTransformOption
                SOURCE_SLIDE_FIELD_NUMBER: _ClassVar[int]
                SOURCE_OPTION_FIELD_NUMBER: _ClassVar[int]
                PRESERVE_NOTES_FORMAT_FIELD_NUMBER: _ClassVar[int]
                NAME_TO_MATCH_FIELD_NUMBER: _ClassVar[int]
                ELEMENT_TEXT_TRANSFORM_FIELD_NUMBER: _ClassVar[int]
                source_slide: Slide.Element.DataLink.SlideText.SlideSourceType
                source_option: Slide.Element.DataLink.SlideText.TextSourceOption
                preserve_notes_format: bool
                name_to_match: str
                element_text_transform: Slide.Element.DataLink.SlideText.TextTransformOption
                def __init__(self, source_slide: _Optional[_Union[Slide.Element.DataLink.SlideText.SlideSourceType, str]] = ..., source_option: _Optional[_Union[Slide.Element.DataLink.SlideText.TextSourceOption, str]] = ..., preserve_notes_format: bool = ..., name_to_match: _Optional[str] = ..., element_text_transform: _Optional[_Union[Slide.Element.DataLink.SlideText.TextTransformOption, str]] = ...) -> None: ...
            class SlideImage(_message.Message):
                __slots__ = ("source_slide",)
                class SlideSourceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                    __slots__ = ()
                    SLIDE_SOURCE_TYPE_CURRENT_SLIDE: _ClassVar[Slide.Element.DataLink.SlideImage.SlideSourceType]
                    SLIDE_SOURCE_TYPE_NEXT_SLIDE: _ClassVar[Slide.Element.DataLink.SlideImage.SlideSourceType]
                SLIDE_SOURCE_TYPE_CURRENT_SLIDE: Slide.Element.DataLink.SlideImage.SlideSourceType
                SLIDE_SOURCE_TYPE_NEXT_SLIDE: Slide.Element.DataLink.SlideImage.SlideSourceType
                SOURCE_SLIDE_FIELD_NUMBER: _ClassVar[int]
                source_slide: Slide.Element.DataLink.SlideImage.SlideSourceType
                def __init__(self, source_slide: _Optional[_Union[Slide.Element.DataLink.SlideImage.SlideSourceType, str]] = ...) -> None: ...
            class StageMessage(_message.Message):
                __slots__ = ("should_flash", "flash_color")
                SHOULD_FLASH_FIELD_NUMBER: _ClassVar[int]
                FLASH_COLOR_FIELD_NUMBER: _ClassVar[int]
                should_flash: bool
                flash_color: _basicTypes_pb2.Color
                def __init__(self, should_flash: bool = ..., flash_color: _Optional[_Union[_basicTypes_pb2.Color, _Mapping]] = ...) -> None: ...
            class VideoCountdown(_message.Message):
                __slots__ = ("timer_format", "timer_format_string", "color_triggers", "ignore_looping_videos", "video_countdown_source")
                class VideoCountdownSource(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                    __slots__ = ()
                    VIDEO_COUNTDOWN_SOURCE_PRESENTATION: _ClassVar[Slide.Element.DataLink.VideoCountdown.VideoCountdownSource]
                    VIDEO_COUNTDOWN_SOURCE_ANNOUNCEMENT: _ClassVar[Slide.Element.DataLink.VideoCountdown.VideoCountdownSource]
                VIDEO_COUNTDOWN_SOURCE_PRESENTATION: Slide.Element.DataLink.VideoCountdown.VideoCountdownSource
                VIDEO_COUNTDOWN_SOURCE_ANNOUNCEMENT: Slide.Element.DataLink.VideoCountdown.VideoCountdownSource
                TIMER_FORMAT_FIELD_NUMBER: _ClassVar[int]
                TIMER_FORMAT_STRING_FIELD_NUMBER: _ClassVar[int]
                COLOR_TRIGGERS_FIELD_NUMBER: _ClassVar[int]
                IGNORE_LOOPING_VIDEOS_FIELD_NUMBER: _ClassVar[int]
                VIDEO_COUNTDOWN_SOURCE_FIELD_NUMBER: _ClassVar[int]
                timer_format: _timers_pb2.Timer.Format
                timer_format_string: str
                color_triggers: _containers.RepeatedCompositeFieldContainer[Slide.Element.DataLink.ColorTrigger]
                ignore_looping_videos: bool
                video_countdown_source: Slide.Element.DataLink.VideoCountdown.VideoCountdownSource
                def __init__(self, timer_format: _Optional[_Union[_timers_pb2.Timer.Format, _Mapping]] = ..., timer_format_string: _Optional[str] = ..., color_triggers: _Optional[_Iterable[_Union[Slide.Element.DataLink.ColorTrigger, _Mapping]]] = ..., ignore_looping_videos: bool = ..., video_countdown_source: _Optional[_Union[Slide.Element.DataLink.VideoCountdown.VideoCountdownSource, str]] = ...) -> None: ...
            class AudioCountdown(_message.Message):
                __slots__ = ("timer_format", "timer_format_string", "color_triggers", "ignore_looping_audio")
                TIMER_FORMAT_FIELD_NUMBER: _ClassVar[int]
                TIMER_FORMAT_STRING_FIELD_NUMBER: _ClassVar[int]
                COLOR_TRIGGERS_FIELD_NUMBER: _ClassVar[int]
                IGNORE_LOOPING_AUDIO_FIELD_NUMBER: _ClassVar[int]
                timer_format: _timers_pb2.Timer.Format
                timer_format_string: str
                color_triggers: _containers.RepeatedCompositeFieldContainer[Slide.Element.DataLink.ColorTrigger]
                ignore_looping_audio: bool
                def __init__(self, timer_format: _Optional[_Union[_timers_pb2.Timer.Format, _Mapping]] = ..., timer_format_string: _Optional[str] = ..., color_triggers: _Optional[_Iterable[_Union[Slide.Element.DataLink.ColorTrigger, _Mapping]]] = ..., ignore_looping_audio: bool = ...) -> None: ...
            class GroupName(_message.Message):
                __slots__ = ("groupSource",)
                class GroupSourceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                    __slots__ = ()
                    GROUP_SOURCE_TYPE_CURRENT_SLIDE: _ClassVar[Slide.Element.DataLink.GroupName.GroupSourceType]
                    GROUP_SOURCE_TYPE_NEXT_SLIDE: _ClassVar[Slide.Element.DataLink.GroupName.GroupSourceType]
                    GROUP_SOURCE_TYPE_NEXT_GROUP: _ClassVar[Slide.Element.DataLink.GroupName.GroupSourceType]
                GROUP_SOURCE_TYPE_CURRENT_SLIDE: Slide.Element.DataLink.GroupName.GroupSourceType
                GROUP_SOURCE_TYPE_NEXT_SLIDE: Slide.Element.DataLink.GroupName.GroupSourceType
                GROUP_SOURCE_TYPE_NEXT_GROUP: Slide.Element.DataLink.GroupName.GroupSourceType
                GROUPSOURCE_FIELD_NUMBER: _ClassVar[int]
                groupSource: Slide.Element.DataLink.GroupName.GroupSourceType
                def __init__(self, groupSource: _Optional[_Union[Slide.Element.DataLink.GroupName.GroupSourceType, str]] = ...) -> None: ...
            class GroupColor(_message.Message):
                __slots__ = ("groupSource",)
                class GroupSourceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                    __slots__ = ()
                    GROUP_SOURCE_TYPE_CURRENT_SLIDE: _ClassVar[Slide.Element.DataLink.GroupColor.GroupSourceType]
                    GROUP_SOURCE_TYPE_NEXT_SLIDE: _ClassVar[Slide.Element.DataLink.GroupColor.GroupSourceType]
                    GROUP_SOURCE_TYPE_NEXT_GROUP: _ClassVar[Slide.Element.DataLink.GroupColor.GroupSourceType]
                GROUP_SOURCE_TYPE_CURRENT_SLIDE: Slide.Element.DataLink.GroupColor.GroupSourceType
                GROUP_SOURCE_TYPE_NEXT_SLIDE: Slide.Element.DataLink.GroupColor.GroupSourceType
                GROUP_SOURCE_TYPE_NEXT_GROUP: Slide.Element.DataLink.GroupColor.GroupSourceType
                GROUPSOURCE_FIELD_NUMBER: _ClassVar[int]
                groupSource: Slide.Element.DataLink.GroupColor.GroupSourceType
                def __init__(self, groupSource: _Optional[_Union[Slide.Element.DataLink.GroupColor.GroupSourceType, str]] = ...) -> None: ...
            class SlideLabelText(_message.Message):
                __slots__ = ("slide_label_source",)
                class SlideLabelSource(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                    __slots__ = ()
                    SLIDE_LABEL_SOURCE_CURRENT_SLIDE: _ClassVar[Slide.Element.DataLink.SlideLabelText.SlideLabelSource]
                    SLIDE_LABEL_SOURCE_NEXT_SLIDE: _ClassVar[Slide.Element.DataLink.SlideLabelText.SlideLabelSource]
                SLIDE_LABEL_SOURCE_CURRENT_SLIDE: Slide.Element.DataLink.SlideLabelText.SlideLabelSource
                SLIDE_LABEL_SOURCE_NEXT_SLIDE: Slide.Element.DataLink.SlideLabelText.SlideLabelSource
                SLIDE_LABEL_SOURCE_FIELD_NUMBER: _ClassVar[int]
                slide_label_source: Slide.Element.DataLink.SlideLabelText.SlideLabelSource
                def __init__(self, slide_label_source: _Optional[_Union[Slide.Element.DataLink.SlideLabelText.SlideLabelSource, str]] = ...) -> None: ...
            class SlideLabelColor(_message.Message):
                __slots__ = ("slide_label_source",)
                class SlideLabelSource(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                    __slots__ = ()
                    SLIDE_LABEL_SOURCE_CURRENT_SLIDE: _ClassVar[Slide.Element.DataLink.SlideLabelColor.SlideLabelSource]
                    SLIDE_LABEL_SOURCE_NEXT_SLIDE: _ClassVar[Slide.Element.DataLink.SlideLabelColor.SlideLabelSource]
                SLIDE_LABEL_SOURCE_CURRENT_SLIDE: Slide.Element.DataLink.SlideLabelColor.SlideLabelSource
                SLIDE_LABEL_SOURCE_NEXT_SLIDE: Slide.Element.DataLink.SlideLabelColor.SlideLabelSource
                SLIDE_LABEL_SOURCE_FIELD_NUMBER: _ClassVar[int]
                slide_label_source: Slide.Element.DataLink.SlideLabelColor.SlideLabelSource
                def __init__(self, slide_label_source: _Optional[_Union[Slide.Element.DataLink.SlideLabelColor.SlideLabelSource, str]] = ...) -> None: ...
            class PresentationNotes(_message.Message):
                __slots__ = ()
                def __init__(self) -> None: ...
            class Presentation(_message.Message):
                __slots__ = ("presentation_source",)
                class PresentationSource(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                    __slots__ = ()
                    PRESENTATION_SOURCE_PRESENTATION: _ClassVar[Slide.Element.DataLink.Presentation.PresentationSource]
                    PRESENTATION_SOURCE_ANNOUNCEMENT: _ClassVar[Slide.Element.DataLink.Presentation.PresentationSource]
                PRESENTATION_SOURCE_PRESENTATION: Slide.Element.DataLink.Presentation.PresentationSource
                PRESENTATION_SOURCE_ANNOUNCEMENT: Slide.Element.DataLink.Presentation.PresentationSource
                PRESENTATION_SOURCE_FIELD_NUMBER: _ClassVar[int]
                presentation_source: Slide.Element.DataLink.Presentation.PresentationSource
                def __init__(self, presentation_source: _Optional[_Union[Slide.Element.DataLink.Presentation.PresentationSource, str]] = ...) -> None: ...
            class PlaylistItem(_message.Message):
                __slots__ = ("playlistItemSource", "showArrangement")
                class PlaylistItemSourceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                    __slots__ = ()
                    PLAYLIST_ITEM_SOURCE_TYPE_CURRENT: _ClassVar[Slide.Element.DataLink.PlaylistItem.PlaylistItemSourceType]
                    PLAYLIST_ITEM_SOURCE_TYPE_NEXT: _ClassVar[Slide.Element.DataLink.PlaylistItem.PlaylistItemSourceType]
                    PLAYLIST_ITEM_SOURCE_TYPE_CURRENT_HEADER: _ClassVar[Slide.Element.DataLink.PlaylistItem.PlaylistItemSourceType]
                    PLAYLIST_ITEM_SOURCE_TYPE_NEXT_HEADER: _ClassVar[Slide.Element.DataLink.PlaylistItem.PlaylistItemSourceType]
                    PLAYLIST_ITEM_SOURCE_TYPE_PARENT_PLAYLIST: _ClassVar[Slide.Element.DataLink.PlaylistItem.PlaylistItemSourceType]
                PLAYLIST_ITEM_SOURCE_TYPE_CURRENT: Slide.Element.DataLink.PlaylistItem.PlaylistItemSourceType
                PLAYLIST_ITEM_SOURCE_TYPE_NEXT: Slide.Element.DataLink.PlaylistItem.PlaylistItemSourceType
                PLAYLIST_ITEM_SOURCE_TYPE_CURRENT_HEADER: Slide.Element.DataLink.PlaylistItem.PlaylistItemSourceType
                PLAYLIST_ITEM_SOURCE_TYPE_NEXT_HEADER: Slide.Element.DataLink.PlaylistItem.PlaylistItemSourceType
                PLAYLIST_ITEM_SOURCE_TYPE_PARENT_PLAYLIST: Slide.Element.DataLink.PlaylistItem.PlaylistItemSourceType
                PLAYLISTITEMSOURCE_FIELD_NUMBER: _ClassVar[int]
                SHOWARRANGEMENT_FIELD_NUMBER: _ClassVar[int]
                playlistItemSource: Slide.Element.DataLink.PlaylistItem.PlaylistItemSourceType
                showArrangement: bool
                def __init__(self, playlistItemSource: _Optional[_Union[Slide.Element.DataLink.PlaylistItem.PlaylistItemSourceType, str]] = ..., showArrangement: bool = ...) -> None: ...
            class AutoAdvanceTimeRemaining(_message.Message):
                __slots__ = ("auto_advance_source", "timer_format")
                class AutoAdvanceSource(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                    __slots__ = ()
                    AUTO_ADVANCE_SOURCE_PRESENTATION: _ClassVar[Slide.Element.DataLink.AutoAdvanceTimeRemaining.AutoAdvanceSource]
                    AUTO_ADVANCE_SOURCE_ANNOUNCEMENT: _ClassVar[Slide.Element.DataLink.AutoAdvanceTimeRemaining.AutoAdvanceSource]
                AUTO_ADVANCE_SOURCE_PRESENTATION: Slide.Element.DataLink.AutoAdvanceTimeRemaining.AutoAdvanceSource
                AUTO_ADVANCE_SOURCE_ANNOUNCEMENT: Slide.Element.DataLink.AutoAdvanceTimeRemaining.AutoAdvanceSource
                AUTO_ADVANCE_SOURCE_FIELD_NUMBER: _ClassVar[int]
                TIMER_FORMAT_FIELD_NUMBER: _ClassVar[int]
                auto_advance_source: Slide.Element.DataLink.AutoAdvanceTimeRemaining.AutoAdvanceSource
                timer_format: _timers_pb2.Timer.Format
                def __init__(self, auto_advance_source: _Optional[_Union[Slide.Element.DataLink.AutoAdvanceTimeRemaining.AutoAdvanceSource, str]] = ..., timer_format: _Optional[_Union[_timers_pb2.Timer.Format, _Mapping]] = ...) -> None: ...
            class CaptureStatusText(_message.Message):
                __slots__ = ("status_text", "elapsed_time")
                class StatusText(_message.Message):
                    __slots__ = ()
                    def __init__(self) -> None: ...
                class ElapsedTime(_message.Message):
                    __slots__ = ("timer_format",)
                    TIMER_FORMAT_FIELD_NUMBER: _ClassVar[int]
                    timer_format: _timers_pb2.Timer.Format
                    def __init__(self, timer_format: _Optional[_Union[_timers_pb2.Timer.Format, _Mapping]] = ...) -> None: ...
                STATUS_TEXT_FIELD_NUMBER: _ClassVar[int]
                ELAPSED_TIME_FIELD_NUMBER: _ClassVar[int]
                status_text: Slide.Element.DataLink.CaptureStatusText.StatusText
                elapsed_time: Slide.Element.DataLink.CaptureStatusText.ElapsedTime
                def __init__(self, status_text: _Optional[_Union[Slide.Element.DataLink.CaptureStatusText.StatusText, _Mapping]] = ..., elapsed_time: _Optional[_Union[Slide.Element.DataLink.CaptureStatusText.ElapsedTime, _Mapping]] = ...) -> None: ...
            class CaptureStatusColor(_message.Message):
                __slots__ = ()
                def __init__(self) -> None: ...
            class SlideCount(_message.Message):
                __slots__ = ("slideCountSourceType",)
                class SlideCountSourceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                    __slots__ = ()
                    SLIDE_COUNT_SOURCE_TYPE_CURRENT: _ClassVar[Slide.Element.DataLink.SlideCount.SlideCountSourceType]
                    SLIDE_COUNT_SOURCE_TYPE_REMAINING: _ClassVar[Slide.Element.DataLink.SlideCount.SlideCountSourceType]
                    SLIDE_COUNT_SOURCE_TYPE_TOTAL: _ClassVar[Slide.Element.DataLink.SlideCount.SlideCountSourceType]
                SLIDE_COUNT_SOURCE_TYPE_CURRENT: Slide.Element.DataLink.SlideCount.SlideCountSourceType
                SLIDE_COUNT_SOURCE_TYPE_REMAINING: Slide.Element.DataLink.SlideCount.SlideCountSourceType
                SLIDE_COUNT_SOURCE_TYPE_TOTAL: Slide.Element.DataLink.SlideCount.SlideCountSourceType
                SLIDECOUNTSOURCETYPE_FIELD_NUMBER: _ClassVar[int]
                slideCountSourceType: Slide.Element.DataLink.SlideCount.SlideCountSourceType
                def __init__(self, slideCountSourceType: _Optional[_Union[Slide.Element.DataLink.SlideCount.SlideCountSourceType, str]] = ...) -> None: ...
            class PlaybackMarkerIdentifier(_message.Message):
                __slots__ = ("destination", "type", "name")
                class Destination(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                    __slots__ = ()
                    PLAYBACK_MARKER_DESTINATION_PRESENTATION: _ClassVar[Slide.Element.DataLink.PlaybackMarkerIdentifier.Destination]
                    PLAYBACK_MARKER_DESTINATION_ANNOUNCEMENT: _ClassVar[Slide.Element.DataLink.PlaybackMarkerIdentifier.Destination]
                    PLAYBACK_MARKER_DESTINATION_AUDIO: _ClassVar[Slide.Element.DataLink.PlaybackMarkerIdentifier.Destination]
                PLAYBACK_MARKER_DESTINATION_PRESENTATION: Slide.Element.DataLink.PlaybackMarkerIdentifier.Destination
                PLAYBACK_MARKER_DESTINATION_ANNOUNCEMENT: Slide.Element.DataLink.PlaybackMarkerIdentifier.Destination
                PLAYBACK_MARKER_DESTINATION_AUDIO: Slide.Element.DataLink.PlaybackMarkerIdentifier.Destination
                class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                    __slots__ = ()
                    PLAYBACK_MARKER_IDENTIFIER_FIRST: _ClassVar[Slide.Element.DataLink.PlaybackMarkerIdentifier.Type]
                    PLAYBACK_MARKER_IDENTIFIER_PREVIOUS: _ClassVar[Slide.Element.DataLink.PlaybackMarkerIdentifier.Type]
                    PLAYBACK_MARKER_IDENTIFIER_NEXT: _ClassVar[Slide.Element.DataLink.PlaybackMarkerIdentifier.Type]
                    PLAYBACK_MARKER_IDENTIFIER_LAST: _ClassVar[Slide.Element.DataLink.PlaybackMarkerIdentifier.Type]
                    PLAYBACK_MARKER_IDENTIFIER_NAME: _ClassVar[Slide.Element.DataLink.PlaybackMarkerIdentifier.Type]
                PLAYBACK_MARKER_IDENTIFIER_FIRST: Slide.Element.DataLink.PlaybackMarkerIdentifier.Type
                PLAYBACK_MARKER_IDENTIFIER_PREVIOUS: Slide.Element.DataLink.PlaybackMarkerIdentifier.Type
                PLAYBACK_MARKER_IDENTIFIER_NEXT: Slide.Element.DataLink.PlaybackMarkerIdentifier.Type
                PLAYBACK_MARKER_IDENTIFIER_LAST: Slide.Element.DataLink.PlaybackMarkerIdentifier.Type
                PLAYBACK_MARKER_IDENTIFIER_NAME: Slide.Element.DataLink.PlaybackMarkerIdentifier.Type
                DESTINATION_FIELD_NUMBER: _ClassVar[int]
                TYPE_FIELD_NUMBER: _ClassVar[int]
                NAME_FIELD_NUMBER: _ClassVar[int]
                destination: Slide.Element.DataLink.PlaybackMarkerIdentifier.Destination
                type: Slide.Element.DataLink.PlaybackMarkerIdentifier.Type
                name: str
                def __init__(self, destination: _Optional[_Union[Slide.Element.DataLink.PlaybackMarkerIdentifier.Destination, str]] = ..., type: _Optional[_Union[Slide.Element.DataLink.PlaybackMarkerIdentifier.Type, str]] = ..., name: _Optional[str] = ...) -> None: ...
            class PlaybackMarkerText(_message.Message):
                __slots__ = ("identifier", "should_use_marker_color", "name", "time")
                class Name(_message.Message):
                    __slots__ = ()
                    def __init__(self) -> None: ...
                class Time(_message.Message):
                    __slots__ = ("format",)
                    FORMAT_FIELD_NUMBER: _ClassVar[int]
                    format: _timers_pb2.Timer.Format
                    def __init__(self, format: _Optional[_Union[_timers_pb2.Timer.Format, _Mapping]] = ...) -> None: ...
                IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
                SHOULD_USE_MARKER_COLOR_FIELD_NUMBER: _ClassVar[int]
                NAME_FIELD_NUMBER: _ClassVar[int]
                TIME_FIELD_NUMBER: _ClassVar[int]
                identifier: Slide.Element.DataLink.PlaybackMarkerIdentifier
                should_use_marker_color: bool
                name: Slide.Element.DataLink.PlaybackMarkerText.Name
                time: Slide.Element.DataLink.PlaybackMarkerText.Time
                def __init__(self, identifier: _Optional[_Union[Slide.Element.DataLink.PlaybackMarkerIdentifier, _Mapping]] = ..., should_use_marker_color: bool = ..., name: _Optional[_Union[Slide.Element.DataLink.PlaybackMarkerText.Name, _Mapping]] = ..., time: _Optional[_Union[Slide.Element.DataLink.PlaybackMarkerText.Time, _Mapping]] = ...) -> None: ...
            class ChordProChart(_message.Message):
                __slots__ = ()
                def __init__(self) -> None: ...
            class TimecodeText(_message.Message):
                __slots__ = ()
                def __init__(self) -> None: ...
            class TimecodeStatus(_message.Message):
                __slots__ = ()
                def __init__(self) -> None: ...
            TICKER_FIELD_NUMBER: _ClassVar[int]
            ALTERNATE_TEXT_FIELD_NUMBER: _ClassVar[int]
            TIMER_TEXT_FIELD_NUMBER: _ClassVar[int]
            CLOCK_TEXT_FIELD_NUMBER: _ClassVar[int]
            CHORD_CHART_FIELD_NUMBER: _ClassVar[int]
            OUTPUT_SCREEN_FIELD_NUMBER: _ClassVar[int]
            PCO_LIVE_FIELD_NUMBER: _ClassVar[int]
            ALTERNATE_FILL_FIELD_NUMBER: _ClassVar[int]
            VISIBILITY_LINK_FIELD_NUMBER: _ClassVar[int]
            SLIDE_TEXT_FIELD_NUMBER: _ClassVar[int]
            STAGE_MESSAGE_FIELD_NUMBER: _ClassVar[int]
            VIDEO_COUNTDOWN_FIELD_NUMBER: _ClassVar[int]
            SLIDE_IMAGE_FIELD_NUMBER: _ClassVar[int]
            CCLI_TEXT_FIELD_NUMBER: _ClassVar[int]
            GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
            GROUP_COLOR_FIELD_NUMBER: _ClassVar[int]
            PRESENTATION_NOTES_FIELD_NUMBER: _ClassVar[int]
            PLAYLIST_ITEM_FIELD_NUMBER: _ClassVar[int]
            AUTO_ADVANCE_TIME_REMAINING_FIELD_NUMBER: _ClassVar[int]
            CAPTURE_STATUS_TEXT_FIELD_NUMBER: _ClassVar[int]
            CAPTURE_STATUS_COLOR_FIELD_NUMBER: _ClassVar[int]
            SLIDE_COUNT_FIELD_NUMBER: _ClassVar[int]
            AUDIO_COUNTDOWN_FIELD_NUMBER: _ClassVar[int]
            PRESENTATION_FIELD_NUMBER: _ClassVar[int]
            SLIDE_LABEL_TEXT_FIELD_NUMBER: _ClassVar[int]
            SLIDE_LABEL_COLOR_FIELD_NUMBER: _ClassVar[int]
            RSS_FEED_FIELD_NUMBER: _ClassVar[int]
            FILE_FEED_FIELD_NUMBER: _ClassVar[int]
            CHORD_PRO_CHART_FIELD_NUMBER: _ClassVar[int]
            PLAYBACK_MARKER_TEXT_FIELD_NUMBER: _ClassVar[int]
            PLAYBACK_MARKER_COLOR_FIELD_NUMBER: _ClassVar[int]
            TIMECODE_TEXT_FIELD_NUMBER: _ClassVar[int]
            TIMECODE_STATUS_FIELD_NUMBER: _ClassVar[int]
            ticker: Slide.Element.DataLink.Ticker
            alternate_text: Slide.Element.DataLink.AlternateElementText
            timer_text: Slide.Element.DataLink.TimerText
            clock_text: Slide.Element.DataLink.ClockText
            chord_chart: Slide.Element.DataLink.ChordChart
            output_screen: Slide.Element.DataLink.OutputScreen
            pco_live: Slide.Element.DataLink.PCOLive
            alternate_fill: Slide.Element.DataLink.AlternateElementFill
            visibility_link: Slide.Element.DataLink.VisibilityLink
            slide_text: Slide.Element.DataLink.SlideText
            stage_message: Slide.Element.DataLink.StageMessage
            video_countdown: Slide.Element.DataLink.VideoCountdown
            slide_image: Slide.Element.DataLink.SlideImage
            ccli_text: Slide.Element.DataLink.CCLIText
            group_name: Slide.Element.DataLink.GroupName
            group_color: Slide.Element.DataLink.GroupColor
            presentation_notes: Slide.Element.DataLink.PresentationNotes
            playlist_item: Slide.Element.DataLink.PlaylistItem
            auto_advance_time_remaining: Slide.Element.DataLink.AutoAdvanceTimeRemaining
            capture_status_text: Slide.Element.DataLink.CaptureStatusText
            capture_status_color: Slide.Element.DataLink.CaptureStatusColor
            slide_count: Slide.Element.DataLink.SlideCount
            audio_countdown: Slide.Element.DataLink.AudioCountdown
            presentation: Slide.Element.DataLink.Presentation
            slide_Label_Text: Slide.Element.DataLink.SlideLabelText
            slide_Label_Color: Slide.Element.DataLink.SlideLabelColor
            rss_feed: Slide.Element.DataLink.RSSFeed
            file_feed: Slide.Element.DataLink.FileFeed
            chord_pro_chart: Slide.Element.DataLink.ChordProChart
            playback_marker_text: Slide.Element.DataLink.PlaybackMarkerText
            playback_marker_color: Slide.Element.DataLink.PlaybackMarkerIdentifier
            timecode_text: Slide.Element.DataLink.TimecodeText
            timecode_status: Slide.Element.DataLink.TimecodeStatus
            def __init__(self, ticker: _Optional[_Union[Slide.Element.DataLink.Ticker, _Mapping]] = ..., alternate_text: _Optional[_Union[Slide.Element.DataLink.AlternateElementText, _Mapping]] = ..., timer_text: _Optional[_Union[Slide.Element.DataLink.TimerText, _Mapping]] = ..., clock_text: _Optional[_Union[Slide.Element.DataLink.ClockText, _Mapping]] = ..., chord_chart: _Optional[_Union[Slide.Element.DataLink.ChordChart, _Mapping]] = ..., output_screen: _Optional[_Union[Slide.Element.DataLink.OutputScreen, _Mapping]] = ..., pco_live: _Optional[_Union[Slide.Element.DataLink.PCOLive, _Mapping]] = ..., alternate_fill: _Optional[_Union[Slide.Element.DataLink.AlternateElementFill, _Mapping]] = ..., visibility_link: _Optional[_Union[Slide.Element.DataLink.VisibilityLink, _Mapping]] = ..., slide_text: _Optional[_Union[Slide.Element.DataLink.SlideText, _Mapping]] = ..., stage_message: _Optional[_Union[Slide.Element.DataLink.StageMessage, _Mapping]] = ..., video_countdown: _Optional[_Union[Slide.Element.DataLink.VideoCountdown, _Mapping]] = ..., slide_image: _Optional[_Union[Slide.Element.DataLink.SlideImage, _Mapping]] = ..., ccli_text: _Optional[_Union[Slide.Element.DataLink.CCLIText, _Mapping]] = ..., group_name: _Optional[_Union[Slide.Element.DataLink.GroupName, _Mapping]] = ..., group_color: _Optional[_Union[Slide.Element.DataLink.GroupColor, _Mapping]] = ..., presentation_notes: _Optional[_Union[Slide.Element.DataLink.PresentationNotes, _Mapping]] = ..., playlist_item: _Optional[_Union[Slide.Element.DataLink.PlaylistItem, _Mapping]] = ..., auto_advance_time_remaining: _Optional[_Union[Slide.Element.DataLink.AutoAdvanceTimeRemaining, _Mapping]] = ..., capture_status_text: _Optional[_Union[Slide.Element.DataLink.CaptureStatusText, _Mapping]] = ..., capture_status_color: _Optional[_Union[Slide.Element.DataLink.CaptureStatusColor, _Mapping]] = ..., slide_count: _Optional[_Union[Slide.Element.DataLink.SlideCount, _Mapping]] = ..., audio_countdown: _Optional[_Union[Slide.Element.DataLink.AudioCountdown, _Mapping]] = ..., presentation: _Optional[_Union[Slide.Element.DataLink.Presentation, _Mapping]] = ..., slide_Label_Text: _Optional[_Union[Slide.Element.DataLink.SlideLabelText, _Mapping]] = ..., slide_Label_Color: _Optional[_Union[Slide.Element.DataLink.SlideLabelColor, _Mapping]] = ..., rss_feed: _Optional[_Union[Slide.Element.DataLink.RSSFeed, _Mapping]] = ..., file_feed: _Optional[_Union[Slide.Element.DataLink.FileFeed, _Mapping]] = ..., chord_pro_chart: _Optional[_Union[Slide.Element.DataLink.ChordProChart, _Mapping]] = ..., playback_marker_text: _Optional[_Union[Slide.Element.DataLink.PlaybackMarkerText, _Mapping]] = ..., playback_marker_color: _Optional[_Union[Slide.Element.DataLink.PlaybackMarkerIdentifier, _Mapping]] = ..., timecode_text: _Optional[_Union[Slide.Element.DataLink.TimecodeText, _Mapping]] = ..., timecode_status: _Optional[_Union[Slide.Element.DataLink.TimecodeStatus, _Mapping]] = ...) -> None: ...
        class TextScroller(_message.Message):
            __slots__ = ("should_scroll", "scroll_rate", "should_repeat", "repeat_distance", "scrolling_direction", "starts_off_screen", "fade_left", "fade_right")
            class Direction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                DIRECTION_LEFT: _ClassVar[Slide.Element.TextScroller.Direction]
                DIRECTION_RIGHT: _ClassVar[Slide.Element.TextScroller.Direction]
                DIRECTION_UP: _ClassVar[Slide.Element.TextScroller.Direction]
                DIRECTION_DOWN: _ClassVar[Slide.Element.TextScroller.Direction]
            DIRECTION_LEFT: Slide.Element.TextScroller.Direction
            DIRECTION_RIGHT: Slide.Element.TextScroller.Direction
            DIRECTION_UP: Slide.Element.TextScroller.Direction
            DIRECTION_DOWN: Slide.Element.TextScroller.Direction
            SHOULD_SCROLL_FIELD_NUMBER: _ClassVar[int]
            SCROLL_RATE_FIELD_NUMBER: _ClassVar[int]
            SHOULD_REPEAT_FIELD_NUMBER: _ClassVar[int]
            REPEAT_DISTANCE_FIELD_NUMBER: _ClassVar[int]
            SCROLLING_DIRECTION_FIELD_NUMBER: _ClassVar[int]
            STARTS_OFF_SCREEN_FIELD_NUMBER: _ClassVar[int]
            FADE_LEFT_FIELD_NUMBER: _ClassVar[int]
            FADE_RIGHT_FIELD_NUMBER: _ClassVar[int]
            should_scroll: bool
            scroll_rate: float
            should_repeat: bool
            repeat_distance: float
            scrolling_direction: Slide.Element.TextScroller.Direction
            starts_off_screen: bool
            fade_left: float
            fade_right: float
            def __init__(self, should_scroll: bool = ..., scroll_rate: _Optional[float] = ..., should_repeat: bool = ..., repeat_distance: _Optional[float] = ..., scrolling_direction: _Optional[_Union[Slide.Element.TextScroller.Direction, str]] = ..., starts_off_screen: bool = ..., fade_left: _Optional[float] = ..., fade_right: _Optional[float] = ...) -> None: ...
        ELEMENT_FIELD_NUMBER: _ClassVar[int]
        BUILD_IN_FIELD_NUMBER: _ClassVar[int]
        BUILD_OUT_FIELD_NUMBER: _ClassVar[int]
        INFO_FIELD_NUMBER: _ClassVar[int]
        REVEAL_TYPE_FIELD_NUMBER: _ClassVar[int]
        DATA_LINKS_FIELD_NUMBER: _ClassVar[int]
        CHILDBUILDS_FIELD_NUMBER: _ClassVar[int]
        REVEAL_FROM_INDEX_FIELD_NUMBER: _ClassVar[int]
        TEXT_SCROLLER_FIELD_NUMBER: _ClassVar[int]
        element: _graphicsData_pb2.Graphics.Element
        build_in: Slide.Element.Build
        build_out: Slide.Element.Build
        info: int
        reveal_type: Slide.Element.TextRevealType
        data_links: _containers.RepeatedCompositeFieldContainer[Slide.Element.DataLink]
        childBuilds: _containers.RepeatedCompositeFieldContainer[Slide.Element.ChildBuild]
        reveal_from_index: int
        text_scroller: Slide.Element.TextScroller
        def __init__(self, element: _Optional[_Union[_graphicsData_pb2.Graphics.Element, _Mapping]] = ..., build_in: _Optional[_Union[Slide.Element.Build, _Mapping]] = ..., build_out: _Optional[_Union[Slide.Element.Build, _Mapping]] = ..., info: _Optional[int] = ..., reveal_type: _Optional[_Union[Slide.Element.TextRevealType, str]] = ..., data_links: _Optional[_Iterable[_Union[Slide.Element.DataLink, _Mapping]]] = ..., childBuilds: _Optional[_Iterable[_Union[Slide.Element.ChildBuild, _Mapping]]] = ..., reveal_from_index: _Optional[int] = ..., text_scroller: _Optional[_Union[Slide.Element.TextScroller, _Mapping]] = ...) -> None: ...
    ELEMENTS_FIELD_NUMBER: _ClassVar[int]
    ELEMENT_BUILD_ORDER_FIELD_NUMBER: _ClassVar[int]
    GUIDELINES_FIELD_NUMBER: _ClassVar[int]
    DRAWS_BACKGROUND_COLOR_FIELD_NUMBER: _ClassVar[int]
    BACKGROUND_COLOR_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    elements: _containers.RepeatedCompositeFieldContainer[Slide.Element]
    element_build_order: _containers.RepeatedCompositeFieldContainer[_basicTypes_pb2.UUID]
    guidelines: _containers.RepeatedCompositeFieldContainer[_alignmentGuide_pb2.AlignmentGuide]
    draws_background_color: bool
    background_color: _basicTypes_pb2.Color
    size: _graphicsData_pb2.Graphics.Size
    uuid: _basicTypes_pb2.UUID
    def __init__(self, elements: _Optional[_Iterable[_Union[Slide.Element, _Mapping]]] = ..., element_build_order: _Optional[_Iterable[_Union[_basicTypes_pb2.UUID, _Mapping]]] = ..., guidelines: _Optional[_Iterable[_Union[_alignmentGuide_pb2.AlignmentGuide, _Mapping]]] = ..., draws_background_color: bool = ..., background_color: _Optional[_Union[_basicTypes_pb2.Color, _Mapping]] = ..., size: _Optional[_Union[_graphicsData_pb2.Graphics.Size, _Mapping]] = ..., uuid: _Optional[_Union[_basicTypes_pb2.UUID, _Mapping]] = ...) -> None: ...
