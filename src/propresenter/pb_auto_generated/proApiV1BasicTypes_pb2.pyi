import propresenter.pb_auto_generated.basicTypes_pb2 as _basicTypes_pb2
import propresenter.pb_auto_generated.rvtimestamp_pb2 as _rvtimestamp_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class API_v1_Identifier(_message.Message):
    __slots__ = ("uuid", "name", "index")
    UUID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    uuid: str
    name: str
    index: int
    def __init__(self, uuid: _Optional[str] = ..., name: _Optional[str] = ..., index: _Optional[int] = ...) -> None: ...

class API_v1_SlideIndex(_message.Message):
    __slots__ = ("index", "presentation_id")
    INDEX_FIELD_NUMBER: _ClassVar[int]
    PRESENTATION_ID_FIELD_NUMBER: _ClassVar[int]
    index: int
    presentation_id: API_v1_Identifier
    def __init__(self, index: _Optional[int] = ..., presentation_id: _Optional[_Union[API_v1_Identifier, _Mapping]] = ...) -> None: ...

class API_v1_Playlist(_message.Message):
    __slots__ = ("id", "type", "children")
    class API_v1_PlaylistType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        group: _ClassVar[API_v1_Playlist.API_v1_PlaylistType]
        playlist: _ClassVar[API_v1_Playlist.API_v1_PlaylistType]
    group: API_v1_Playlist.API_v1_PlaylistType
    playlist: API_v1_Playlist.API_v1_PlaylistType
    ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    CHILDREN_FIELD_NUMBER: _ClassVar[int]
    id: API_v1_Identifier
    type: API_v1_Playlist.API_v1_PlaylistType
    children: _containers.RepeatedCompositeFieldContainer[API_v1_Playlist]
    def __init__(self, id: _Optional[_Union[API_v1_Identifier, _Mapping]] = ..., type: _Optional[_Union[API_v1_Playlist.API_v1_PlaylistType, str]] = ..., children: _Optional[_Iterable[_Union[API_v1_Playlist, _Mapping]]] = ...) -> None: ...

class API_v1_PlaylistAndItem(_message.Message):
    __slots__ = ("playlist", "item")
    PLAYLIST_FIELD_NUMBER: _ClassVar[int]
    ITEM_FIELD_NUMBER: _ClassVar[int]
    playlist: API_v1_Identifier
    item: API_v1_Identifier
    def __init__(self, playlist: _Optional[_Union[API_v1_Identifier, _Mapping]] = ..., item: _Optional[_Union[API_v1_Identifier, _Mapping]] = ...) -> None: ...

class API_v1_MediaPlaylistItem(_message.Message):
    __slots__ = ("id", "type", "artist", "duration")
    class API_v1_MediaPlaylistItemType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        audio: _ClassVar[API_v1_MediaPlaylistItem.API_v1_MediaPlaylistItemType]
        image: _ClassVar[API_v1_MediaPlaylistItem.API_v1_MediaPlaylistItemType]
        video: _ClassVar[API_v1_MediaPlaylistItem.API_v1_MediaPlaylistItemType]
    audio: API_v1_MediaPlaylistItem.API_v1_MediaPlaylistItemType
    image: API_v1_MediaPlaylistItem.API_v1_MediaPlaylistItemType
    video: API_v1_MediaPlaylistItem.API_v1_MediaPlaylistItemType
    ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ARTIST_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    id: API_v1_Identifier
    type: API_v1_MediaPlaylistItem.API_v1_MediaPlaylistItemType
    artist: str
    duration: int
    def __init__(self, id: _Optional[_Union[API_v1_Identifier, _Mapping]] = ..., type: _Optional[_Union[API_v1_MediaPlaylistItem.API_v1_MediaPlaylistItemType, str]] = ..., artist: _Optional[str] = ..., duration: _Optional[int] = ...) -> None: ...

class API_v1_PlaylistItem(_message.Message):
    __slots__ = ("id", "type", "is_hidden", "is_pco", "header_color", "duration")
    class API_v1_PlaylistItemType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        presentation: _ClassVar[API_v1_PlaylistItem.API_v1_PlaylistItemType]
        placeholder: _ClassVar[API_v1_PlaylistItem.API_v1_PlaylistItemType]
        header: _ClassVar[API_v1_PlaylistItem.API_v1_PlaylistItemType]
        media: _ClassVar[API_v1_PlaylistItem.API_v1_PlaylistItemType]
        audio: _ClassVar[API_v1_PlaylistItem.API_v1_PlaylistItemType]
        livevideo: _ClassVar[API_v1_PlaylistItem.API_v1_PlaylistItemType]
    presentation: API_v1_PlaylistItem.API_v1_PlaylistItemType
    placeholder: API_v1_PlaylistItem.API_v1_PlaylistItemType
    header: API_v1_PlaylistItem.API_v1_PlaylistItemType
    media: API_v1_PlaylistItem.API_v1_PlaylistItemType
    audio: API_v1_PlaylistItem.API_v1_PlaylistItemType
    livevideo: API_v1_PlaylistItem.API_v1_PlaylistItemType
    ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    IS_HIDDEN_FIELD_NUMBER: _ClassVar[int]
    IS_PCO_FIELD_NUMBER: _ClassVar[int]
    HEADER_COLOR_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    id: API_v1_Identifier
    type: API_v1_PlaylistItem.API_v1_PlaylistItemType
    is_hidden: bool
    is_pco: bool
    header_color: API_v1_Color
    duration: _wrappers_pb2.UInt32Value
    def __init__(self, id: _Optional[_Union[API_v1_Identifier, _Mapping]] = ..., type: _Optional[_Union[API_v1_PlaylistItem.API_v1_PlaylistItemType, str]] = ..., is_hidden: bool = ..., is_pco: bool = ..., header_color: _Optional[_Union[API_v1_Color, _Mapping]] = ..., duration: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ...) -> None: ...

class API_v1_ClearGroup(_message.Message):
    __slots__ = ("id", "icon", "tint", "layers", "stop_timeline_announcements", "stop_timeline_presentation", "clear_next_presentation")
    class API_v1_ClearGroupLayerType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        music: _ClassVar[API_v1_ClearGroup.API_v1_ClearGroupLayerType]
        audio_effects: _ClassVar[API_v1_ClearGroup.API_v1_ClearGroupLayerType]
        props: _ClassVar[API_v1_ClearGroup.API_v1_ClearGroupLayerType]
        messages: _ClassVar[API_v1_ClearGroup.API_v1_ClearGroupLayerType]
        announcements: _ClassVar[API_v1_ClearGroup.API_v1_ClearGroupLayerType]
        presentation: _ClassVar[API_v1_ClearGroup.API_v1_ClearGroupLayerType]
        presentation_media: _ClassVar[API_v1_ClearGroup.API_v1_ClearGroupLayerType]
        video_input: _ClassVar[API_v1_ClearGroup.API_v1_ClearGroupLayerType]
    music: API_v1_ClearGroup.API_v1_ClearGroupLayerType
    audio_effects: API_v1_ClearGroup.API_v1_ClearGroupLayerType
    props: API_v1_ClearGroup.API_v1_ClearGroupLayerType
    messages: API_v1_ClearGroup.API_v1_ClearGroupLayerType
    announcements: API_v1_ClearGroup.API_v1_ClearGroupLayerType
    presentation: API_v1_ClearGroup.API_v1_ClearGroupLayerType
    presentation_media: API_v1_ClearGroup.API_v1_ClearGroupLayerType
    video_input: API_v1_ClearGroup.API_v1_ClearGroupLayerType
    ID_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    TINT_FIELD_NUMBER: _ClassVar[int]
    LAYERS_FIELD_NUMBER: _ClassVar[int]
    STOP_TIMELINE_ANNOUNCEMENTS_FIELD_NUMBER: _ClassVar[int]
    STOP_TIMELINE_PRESENTATION_FIELD_NUMBER: _ClassVar[int]
    CLEAR_NEXT_PRESENTATION_FIELD_NUMBER: _ClassVar[int]
    id: API_v1_Identifier
    icon: str
    tint: API_v1_Color
    layers: _containers.RepeatedScalarFieldContainer[API_v1_ClearGroup.API_v1_ClearGroupLayerType]
    stop_timeline_announcements: bool
    stop_timeline_presentation: bool
    clear_next_presentation: bool
    def __init__(self, id: _Optional[_Union[API_v1_Identifier, _Mapping]] = ..., icon: _Optional[str] = ..., tint: _Optional[_Union[API_v1_Color, _Mapping]] = ..., layers: _Optional[_Iterable[_Union[API_v1_ClearGroup.API_v1_ClearGroupLayerType, str]]] = ..., stop_timeline_announcements: bool = ..., stop_timeline_presentation: bool = ..., clear_next_presentation: bool = ...) -> None: ...

class API_v1_Message(_message.Message):
    __slots__ = ("id", "message", "tokens", "theme")
    class API_v1_MessageToken(_message.Message):
        __slots__ = ("name", "text", "timer", "clock")
        class API_v1_TextToken(_message.Message):
            __slots__ = ("text",)
            TEXT_FIELD_NUMBER: _ClassVar[int]
            text: str
            def __init__(self, text: _Optional[str] = ...) -> None: ...
        class API_v1_TimerToken(_message.Message):
            __slots__ = ("id", "allows_overrun", "format", "countdown", "count_down_to_time", "elapsed")
            ID_FIELD_NUMBER: _ClassVar[int]
            ALLOWS_OVERRUN_FIELD_NUMBER: _ClassVar[int]
            FORMAT_FIELD_NUMBER: _ClassVar[int]
            COUNTDOWN_FIELD_NUMBER: _ClassVar[int]
            COUNT_DOWN_TO_TIME_FIELD_NUMBER: _ClassVar[int]
            ELAPSED_FIELD_NUMBER: _ClassVar[int]
            id: API_v1_Identifier
            allows_overrun: bool
            format: API_v1_TimerFormat
            countdown: API_v1_Timer.API_v1_Timer_Countdown
            count_down_to_time: API_v1_Timer.API_v1_Timer_CountdownToTime
            elapsed: API_v1_Timer.API_v1_Timer_Elapsed
            def __init__(self, id: _Optional[_Union[API_v1_Identifier, _Mapping]] = ..., allows_overrun: bool = ..., format: _Optional[_Union[API_v1_TimerFormat, _Mapping]] = ..., countdown: _Optional[_Union[API_v1_Timer.API_v1_Timer_Countdown, _Mapping]] = ..., count_down_to_time: _Optional[_Union[API_v1_Timer.API_v1_Timer_CountdownToTime, _Mapping]] = ..., elapsed: _Optional[_Union[API_v1_Timer.API_v1_Timer_Elapsed, _Mapping]] = ...) -> None: ...
        class API_v1_ClockToken(_message.Message):
            __slots__ = ("date", "time", "is_24_hours")
            class API_v1_ClockTokenFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                none: _ClassVar[API_v1_Message.API_v1_MessageToken.API_v1_ClockToken.API_v1_ClockTokenFormat]
                short: _ClassVar[API_v1_Message.API_v1_MessageToken.API_v1_ClockToken.API_v1_ClockTokenFormat]
                medium: _ClassVar[API_v1_Message.API_v1_MessageToken.API_v1_ClockToken.API_v1_ClockTokenFormat]
                long: _ClassVar[API_v1_Message.API_v1_MessageToken.API_v1_ClockToken.API_v1_ClockTokenFormat]
                full: _ClassVar[API_v1_Message.API_v1_MessageToken.API_v1_ClockToken.API_v1_ClockTokenFormat]
            none: API_v1_Message.API_v1_MessageToken.API_v1_ClockToken.API_v1_ClockTokenFormat
            short: API_v1_Message.API_v1_MessageToken.API_v1_ClockToken.API_v1_ClockTokenFormat
            medium: API_v1_Message.API_v1_MessageToken.API_v1_ClockToken.API_v1_ClockTokenFormat
            long: API_v1_Message.API_v1_MessageToken.API_v1_ClockToken.API_v1_ClockTokenFormat
            full: API_v1_Message.API_v1_MessageToken.API_v1_ClockToken.API_v1_ClockTokenFormat
            DATE_FIELD_NUMBER: _ClassVar[int]
            TIME_FIELD_NUMBER: _ClassVar[int]
            IS_24_HOURS_FIELD_NUMBER: _ClassVar[int]
            date: API_v1_Message.API_v1_MessageToken.API_v1_ClockToken.API_v1_ClockTokenFormat
            time: API_v1_Message.API_v1_MessageToken.API_v1_ClockToken.API_v1_ClockTokenFormat
            is_24_hours: bool
            def __init__(self, date: _Optional[_Union[API_v1_Message.API_v1_MessageToken.API_v1_ClockToken.API_v1_ClockTokenFormat, str]] = ..., time: _Optional[_Union[API_v1_Message.API_v1_MessageToken.API_v1_ClockToken.API_v1_ClockTokenFormat, str]] = ..., is_24_hours: bool = ...) -> None: ...
        NAME_FIELD_NUMBER: _ClassVar[int]
        TEXT_FIELD_NUMBER: _ClassVar[int]
        TIMER_FIELD_NUMBER: _ClassVar[int]
        CLOCK_FIELD_NUMBER: _ClassVar[int]
        name: str
        text: API_v1_Message.API_v1_MessageToken.API_v1_TextToken
        timer: API_v1_Message.API_v1_MessageToken.API_v1_TimerToken
        clock: API_v1_Message.API_v1_MessageToken.API_v1_ClockToken
        def __init__(self, name: _Optional[str] = ..., text: _Optional[_Union[API_v1_Message.API_v1_MessageToken.API_v1_TextToken, _Mapping]] = ..., timer: _Optional[_Union[API_v1_Message.API_v1_MessageToken.API_v1_TimerToken, _Mapping]] = ..., clock: _Optional[_Union[API_v1_Message.API_v1_MessageToken.API_v1_ClockToken, _Mapping]] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    TOKENS_FIELD_NUMBER: _ClassVar[int]
    THEME_FIELD_NUMBER: _ClassVar[int]
    id: API_v1_Identifier
    message: str
    tokens: _containers.RepeatedCompositeFieldContainer[API_v1_Message.API_v1_MessageToken]
    theme: API_v1_Identifier
    def __init__(self, id: _Optional[_Union[API_v1_Identifier, _Mapping]] = ..., message: _Optional[str] = ..., tokens: _Optional[_Iterable[_Union[API_v1_Message.API_v1_MessageToken, _Mapping]]] = ..., theme: _Optional[_Union[API_v1_Identifier, _Mapping]] = ...) -> None: ...

class API_v1_Timer(_message.Message):
    __slots__ = ("id", "allows_overrun", "countdown", "count_down_to_time", "elapsed")
    class API_v1_Timer_Countdown(_message.Message):
        __slots__ = ("duration",)
        DURATION_FIELD_NUMBER: _ClassVar[int]
        duration: int
        def __init__(self, duration: _Optional[int] = ...) -> None: ...
    class API_v1_Timer_CountdownToTime(_message.Message):
        __slots__ = ("time_of_day", "period")
        class API_v1_TimePeriod(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            am: _ClassVar[API_v1_Timer.API_v1_Timer_CountdownToTime.API_v1_TimePeriod]
            pm: _ClassVar[API_v1_Timer.API_v1_Timer_CountdownToTime.API_v1_TimePeriod]
            is_24_hour: _ClassVar[API_v1_Timer.API_v1_Timer_CountdownToTime.API_v1_TimePeriod]
        am: API_v1_Timer.API_v1_Timer_CountdownToTime.API_v1_TimePeriod
        pm: API_v1_Timer.API_v1_Timer_CountdownToTime.API_v1_TimePeriod
        is_24_hour: API_v1_Timer.API_v1_Timer_CountdownToTime.API_v1_TimePeriod
        TIME_OF_DAY_FIELD_NUMBER: _ClassVar[int]
        PERIOD_FIELD_NUMBER: _ClassVar[int]
        time_of_day: int
        period: API_v1_Timer.API_v1_Timer_CountdownToTime.API_v1_TimePeriod
        def __init__(self, time_of_day: _Optional[int] = ..., period: _Optional[_Union[API_v1_Timer.API_v1_Timer_CountdownToTime.API_v1_TimePeriod, str]] = ...) -> None: ...
    class API_v1_Timer_Elapsed(_message.Message):
        __slots__ = ("start_time", "end_time", "has_end_time")
        START_TIME_FIELD_NUMBER: _ClassVar[int]
        END_TIME_FIELD_NUMBER: _ClassVar[int]
        HAS_END_TIME_FIELD_NUMBER: _ClassVar[int]
        start_time: int
        end_time: int
        has_end_time: bool
        def __init__(self, start_time: _Optional[int] = ..., end_time: _Optional[int] = ..., has_end_time: bool = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    ALLOWS_OVERRUN_FIELD_NUMBER: _ClassVar[int]
    COUNTDOWN_FIELD_NUMBER: _ClassVar[int]
    COUNT_DOWN_TO_TIME_FIELD_NUMBER: _ClassVar[int]
    ELAPSED_FIELD_NUMBER: _ClassVar[int]
    id: API_v1_Identifier
    allows_overrun: bool
    countdown: API_v1_Timer.API_v1_Timer_Countdown
    count_down_to_time: API_v1_Timer.API_v1_Timer_CountdownToTime
    elapsed: API_v1_Timer.API_v1_Timer_Elapsed
    def __init__(self, id: _Optional[_Union[API_v1_Identifier, _Mapping]] = ..., allows_overrun: bool = ..., countdown: _Optional[_Union[API_v1_Timer.API_v1_Timer_Countdown, _Mapping]] = ..., count_down_to_time: _Optional[_Union[API_v1_Timer.API_v1_Timer_CountdownToTime, _Mapping]] = ..., elapsed: _Optional[_Union[API_v1_Timer.API_v1_Timer_Elapsed, _Mapping]] = ...) -> None: ...

class API_v1_TimerFormat(_message.Message):
    __slots__ = ("hour", "minute", "second", "millisecond")
    class API_v1_TimerUnitDisplayFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        none: _ClassVar[API_v1_TimerFormat.API_v1_TimerUnitDisplayFormat]
        short: _ClassVar[API_v1_TimerFormat.API_v1_TimerUnitDisplayFormat]
        long: _ClassVar[API_v1_TimerFormat.API_v1_TimerUnitDisplayFormat]
        remove_short: _ClassVar[API_v1_TimerFormat.API_v1_TimerUnitDisplayFormat]
        remove_long: _ClassVar[API_v1_TimerFormat.API_v1_TimerUnitDisplayFormat]
    none: API_v1_TimerFormat.API_v1_TimerUnitDisplayFormat
    short: API_v1_TimerFormat.API_v1_TimerUnitDisplayFormat
    long: API_v1_TimerFormat.API_v1_TimerUnitDisplayFormat
    remove_short: API_v1_TimerFormat.API_v1_TimerUnitDisplayFormat
    remove_long: API_v1_TimerFormat.API_v1_TimerUnitDisplayFormat
    HOUR_FIELD_NUMBER: _ClassVar[int]
    MINUTE_FIELD_NUMBER: _ClassVar[int]
    SECOND_FIELD_NUMBER: _ClassVar[int]
    MILLISECOND_FIELD_NUMBER: _ClassVar[int]
    hour: API_v1_TimerFormat.API_v1_TimerUnitDisplayFormat
    minute: API_v1_TimerFormat.API_v1_TimerUnitDisplayFormat
    second: API_v1_TimerFormat.API_v1_TimerUnitDisplayFormat
    millisecond: API_v1_TimerFormat.API_v1_TimerUnitDisplayFormat
    def __init__(self, hour: _Optional[_Union[API_v1_TimerFormat.API_v1_TimerUnitDisplayFormat, str]] = ..., minute: _Optional[_Union[API_v1_TimerFormat.API_v1_TimerUnitDisplayFormat, str]] = ..., second: _Optional[_Union[API_v1_TimerFormat.API_v1_TimerUnitDisplayFormat, str]] = ..., millisecond: _Optional[_Union[API_v1_TimerFormat.API_v1_TimerUnitDisplayFormat, str]] = ...) -> None: ...

class API_v1_TimerValue(_message.Message):
    __slots__ = ("id", "time", "state")
    class API_v1_TimerState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        stopped: _ClassVar[API_v1_TimerValue.API_v1_TimerState]
        running: _ClassVar[API_v1_TimerValue.API_v1_TimerState]
        complete: _ClassVar[API_v1_TimerValue.API_v1_TimerState]
        overrunning: _ClassVar[API_v1_TimerValue.API_v1_TimerState]
        overran: _ClassVar[API_v1_TimerValue.API_v1_TimerState]
    stopped: API_v1_TimerValue.API_v1_TimerState
    running: API_v1_TimerValue.API_v1_TimerState
    complete: API_v1_TimerValue.API_v1_TimerState
    overrunning: API_v1_TimerValue.API_v1_TimerState
    overran: API_v1_TimerValue.API_v1_TimerState
    ID_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    id: API_v1_Identifier
    time: str
    state: API_v1_TimerValue.API_v1_TimerState
    def __init__(self, id: _Optional[_Union[API_v1_Identifier, _Mapping]] = ..., time: _Optional[str] = ..., state: _Optional[_Union[API_v1_TimerValue.API_v1_TimerState, str]] = ...) -> None: ...

class API_v1_Color(_message.Message):
    __slots__ = ("red", "green", "blue", "alpha")
    RED_FIELD_NUMBER: _ClassVar[int]
    GREEN_FIELD_NUMBER: _ClassVar[int]
    BLUE_FIELD_NUMBER: _ClassVar[int]
    ALPHA_FIELD_NUMBER: _ClassVar[int]
    red: float
    green: float
    blue: float
    alpha: float
    def __init__(self, red: _Optional[float] = ..., green: _Optional[float] = ..., blue: _Optional[float] = ..., alpha: _Optional[float] = ...) -> None: ...

class API_v1_Look(_message.Message):
    __slots__ = ("id", "screens")
    ID_FIELD_NUMBER: _ClassVar[int]
    SCREENS_FIELD_NUMBER: _ClassVar[int]
    id: API_v1_Identifier
    screens: _containers.RepeatedCompositeFieldContainer[API_v1_Screen]
    def __init__(self, id: _Optional[_Union[API_v1_Identifier, _Mapping]] = ..., screens: _Optional[_Iterable[_Union[API_v1_Screen, _Mapping]]] = ...) -> None: ...

class API_v1_Screen(_message.Message):
    __slots__ = ("video_input", "media", "slide", "announcements", "props", "messages", "presentation", "mask")
    VIDEO_INPUT_FIELD_NUMBER: _ClassVar[int]
    MEDIA_FIELD_NUMBER: _ClassVar[int]
    SLIDE_FIELD_NUMBER: _ClassVar[int]
    ANNOUNCEMENTS_FIELD_NUMBER: _ClassVar[int]
    PROPS_FIELD_NUMBER: _ClassVar[int]
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    PRESENTATION_FIELD_NUMBER: _ClassVar[int]
    MASK_FIELD_NUMBER: _ClassVar[int]
    video_input: bool
    media: bool
    slide: bool
    announcements: bool
    props: bool
    messages: bool
    presentation: str
    mask: str
    def __init__(self, video_input: bool = ..., media: bool = ..., slide: bool = ..., announcements: bool = ..., props: bool = ..., messages: bool = ..., presentation: _Optional[str] = ..., mask: _Optional[str] = ...) -> None: ...

class API_v1_Macro(_message.Message):
    __slots__ = ("id", "color")
    ID_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    id: API_v1_Identifier
    color: API_v1_Color
    def __init__(self, id: _Optional[_Union[API_v1_Identifier, _Mapping]] = ..., color: _Optional[_Union[API_v1_Color, _Mapping]] = ...) -> None: ...

class API_v1_GroupMember(_message.Message):
    __slots__ = ("ip", "port")
    IP_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    ip: str
    port: int
    def __init__(self, ip: _Optional[str] = ..., port: _Optional[int] = ...) -> None: ...

class API_v1_GroupMemberStatus(_message.Message):
    __slots__ = ("ip", "port", "name", "platform", "os_version", "host_description", "api_version", "connection_status")
    class API_v1_GroupMemberStatus_Platform(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PLATFORM_UNKNOWN: _ClassVar[API_v1_GroupMemberStatus.API_v1_GroupMemberStatus_Platform]
        PLATFORM_MACOS: _ClassVar[API_v1_GroupMemberStatus.API_v1_GroupMemberStatus_Platform]
        PLATFORM_WIN32: _ClassVar[API_v1_GroupMemberStatus.API_v1_GroupMemberStatus_Platform]
        PLATFORM_WEB: _ClassVar[API_v1_GroupMemberStatus.API_v1_GroupMemberStatus_Platform]
    PLATFORM_UNKNOWN: API_v1_GroupMemberStatus.API_v1_GroupMemberStatus_Platform
    PLATFORM_MACOS: API_v1_GroupMemberStatus.API_v1_GroupMemberStatus_Platform
    PLATFORM_WIN32: API_v1_GroupMemberStatus.API_v1_GroupMemberStatus_Platform
    PLATFORM_WEB: API_v1_GroupMemberStatus.API_v1_GroupMemberStatus_Platform
    class API_v1_GroupMemberStatus_ConnectionStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CONNECTION_STATUS_UNKNOWN: _ClassVar[API_v1_GroupMemberStatus.API_v1_GroupMemberStatus_ConnectionStatus]
        CONNECTION_STATUS_CONNECTED: _ClassVar[API_v1_GroupMemberStatus.API_v1_GroupMemberStatus_ConnectionStatus]
        CONNECTION_STATUS_DISCONNECTED: _ClassVar[API_v1_GroupMemberStatus.API_v1_GroupMemberStatus_ConnectionStatus]
    CONNECTION_STATUS_UNKNOWN: API_v1_GroupMemberStatus.API_v1_GroupMemberStatus_ConnectionStatus
    CONNECTION_STATUS_CONNECTED: API_v1_GroupMemberStatus.API_v1_GroupMemberStatus_ConnectionStatus
    CONNECTION_STATUS_DISCONNECTED: API_v1_GroupMemberStatus.API_v1_GroupMemberStatus_ConnectionStatus
    IP_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_FIELD_NUMBER: _ClassVar[int]
    OS_VERSION_FIELD_NUMBER: _ClassVar[int]
    HOST_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_STATUS_FIELD_NUMBER: _ClassVar[int]
    ip: str
    port: int
    name: str
    platform: API_v1_GroupMemberStatus.API_v1_GroupMemberStatus_Platform
    os_version: str
    host_description: str
    api_version: str
    connection_status: API_v1_GroupMemberStatus.API_v1_GroupMemberStatus_ConnectionStatus
    def __init__(self, ip: _Optional[str] = ..., port: _Optional[int] = ..., name: _Optional[str] = ..., platform: _Optional[_Union[API_v1_GroupMemberStatus.API_v1_GroupMemberStatus_Platform, str]] = ..., os_version: _Optional[str] = ..., host_description: _Optional[str] = ..., api_version: _Optional[str] = ..., connection_status: _Optional[_Union[API_v1_GroupMemberStatus.API_v1_GroupMemberStatus_ConnectionStatus, str]] = ...) -> None: ...

class API_v1_GroupDefinition(_message.Message):
    __slots__ = ("timestamp", "secret", "name", "members", "group_identifier")
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    SECRET_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    MEMBERS_FIELD_NUMBER: _ClassVar[int]
    GROUP_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    timestamp: _rvtimestamp_pb2.Timestamp
    secret: str
    name: str
    members: _containers.RepeatedCompositeFieldContainer[API_v1_GroupMember]
    group_identifier: _basicTypes_pb2.UUID
    def __init__(self, timestamp: _Optional[_Union[_rvtimestamp_pb2.Timestamp, _Mapping]] = ..., secret: _Optional[str] = ..., name: _Optional[str] = ..., members: _Optional[_Iterable[_Union[API_v1_GroupMember, _Mapping]]] = ..., group_identifier: _Optional[_Union[_basicTypes_pb2.UUID, _Mapping]] = ...) -> None: ...

class API_v1_Error_Response(_message.Message):
    __slots__ = ("error",)
    class API_v1_Error_Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NOT_FOUND: _ClassVar[API_v1_Error_Response.API_v1_Error_Type]
        BAD_REQUEST: _ClassVar[API_v1_Error_Response.API_v1_Error_Type]
        INTERNAL_ERROR: _ClassVar[API_v1_Error_Response.API_v1_Error_Type]
        UNAUTHORIZED: _ClassVar[API_v1_Error_Response.API_v1_Error_Type]
    NOT_FOUND: API_v1_Error_Response.API_v1_Error_Type
    BAD_REQUEST: API_v1_Error_Response.API_v1_Error_Type
    INTERNAL_ERROR: API_v1_Error_Response.API_v1_Error_Type
    UNAUTHORIZED: API_v1_Error_Response.API_v1_Error_Type
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: API_v1_Error_Response.API_v1_Error_Type
    def __init__(self, error: _Optional[_Union[API_v1_Error_Response.API_v1_Error_Type, str]] = ...) -> None: ...

class API_v1_CaptureSettings(_message.Message):
    __slots__ = ("source", "audio_routing", "disk", "rtmp", "resi")
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    AUDIO_ROUTING_FIELD_NUMBER: _ClassVar[int]
    DISK_FIELD_NUMBER: _ClassVar[int]
    RTMP_FIELD_NUMBER: _ClassVar[int]
    RESI_FIELD_NUMBER: _ClassVar[int]
    source: _basicTypes_pb2.UUID
    audio_routing: _containers.RepeatedCompositeFieldContainer[API_v1_AudioRouting]
    disk: API_v1_DiskCapture
    rtmp: API_v1_RTMPCapture
    resi: API_v1_ResiCapture
    def __init__(self, source: _Optional[_Union[_basicTypes_pb2.UUID, _Mapping]] = ..., audio_routing: _Optional[_Iterable[_Union[API_v1_AudioRouting, _Mapping]]] = ..., disk: _Optional[_Union[API_v1_DiskCapture, _Mapping]] = ..., rtmp: _Optional[_Union[API_v1_RTMPCapture, _Mapping]] = ..., resi: _Optional[_Union[API_v1_ResiCapture, _Mapping]] = ...) -> None: ...

class API_v1_Size(_message.Message):
    __slots__ = ("width", "height")
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    width: int
    height: int
    def __init__(self, width: _Optional[int] = ..., height: _Optional[int] = ...) -> None: ...

class API_v1_AudioRouting(_message.Message):
    __slots__ = ("map",)
    MAP_FIELD_NUMBER: _ClassVar[int]
    map: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, map: _Optional[_Iterable[int]] = ...) -> None: ...

class API_v1_DiskCapture(_message.Message):
    __slots__ = ("file_location", "codec", "resolution", "frame_rate")
    FILE_LOCATION_FIELD_NUMBER: _ClassVar[int]
    CODEC_FIELD_NUMBER: _ClassVar[int]
    RESOLUTION_FIELD_NUMBER: _ClassVar[int]
    FRAME_RATE_FIELD_NUMBER: _ClassVar[int]
    file_location: str
    codec: str
    resolution: API_v1_Size
    frame_rate: float
    def __init__(self, file_location: _Optional[str] = ..., codec: _Optional[str] = ..., resolution: _Optional[_Union[API_v1_Size, _Mapping]] = ..., frame_rate: _Optional[float] = ...) -> None: ...

class API_v1_RTMPCapture(_message.Message):
    __slots__ = ("server", "key", "encoding", "save_local", "file_location")
    SERVER_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    ENCODING_FIELD_NUMBER: _ClassVar[int]
    SAVE_LOCAL_FIELD_NUMBER: _ClassVar[int]
    FILE_LOCATION_FIELD_NUMBER: _ClassVar[int]
    server: str
    key: str
    encoding: str
    save_local: bool
    file_location: str
    def __init__(self, server: _Optional[str] = ..., key: _Optional[str] = ..., encoding: _Optional[str] = ..., save_local: bool = ..., file_location: _Optional[str] = ...) -> None: ...

class API_v1_ResiCapture(_message.Message):
    __slots__ = ("event_name", "event_description", "destination_group", "encoding")
    EVENT_NAME_FIELD_NUMBER: _ClassVar[int]
    EVENT_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_GROUP_FIELD_NUMBER: _ClassVar[int]
    ENCODING_FIELD_NUMBER: _ClassVar[int]
    event_name: str
    event_description: str
    destination_group: str
    encoding: str
    def __init__(self, event_name: _Optional[str] = ..., event_description: _Optional[str] = ..., destination_group: _Optional[str] = ..., encoding: _Optional[str] = ...) -> None: ...

class API_v1_Presentation(_message.Message):
    __slots__ = ("id", "groups", "has_timeline", "presentation_path", "destination")
    class Destination(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        presentation: _ClassVar[API_v1_Presentation.Destination]
        announcements: _ClassVar[API_v1_Presentation.Destination]
    presentation: API_v1_Presentation.Destination
    announcements: API_v1_Presentation.Destination
    class SlideGroup(_message.Message):
        __slots__ = ("name", "color", "slides")
        class Slide(_message.Message):
            __slots__ = ("enabled", "notes", "text", "label", "size")
            ENABLED_FIELD_NUMBER: _ClassVar[int]
            NOTES_FIELD_NUMBER: _ClassVar[int]
            TEXT_FIELD_NUMBER: _ClassVar[int]
            LABEL_FIELD_NUMBER: _ClassVar[int]
            SIZE_FIELD_NUMBER: _ClassVar[int]
            enabled: bool
            notes: str
            text: str
            label: str
            size: API_v1_Size
            def __init__(self, enabled: bool = ..., notes: _Optional[str] = ..., text: _Optional[str] = ..., label: _Optional[str] = ..., size: _Optional[_Union[API_v1_Size, _Mapping]] = ...) -> None: ...
        NAME_FIELD_NUMBER: _ClassVar[int]
        COLOR_FIELD_NUMBER: _ClassVar[int]
        SLIDES_FIELD_NUMBER: _ClassVar[int]
        name: str
        color: API_v1_Color
        slides: _containers.RepeatedCompositeFieldContainer[API_v1_Presentation.SlideGroup.Slide]
        def __init__(self, name: _Optional[str] = ..., color: _Optional[_Union[API_v1_Color, _Mapping]] = ..., slides: _Optional[_Iterable[_Union[API_v1_Presentation.SlideGroup.Slide, _Mapping]]] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    GROUPS_FIELD_NUMBER: _ClassVar[int]
    HAS_TIMELINE_FIELD_NUMBER: _ClassVar[int]
    PRESENTATION_PATH_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_FIELD_NUMBER: _ClassVar[int]
    id: API_v1_Identifier
    groups: _containers.RepeatedCompositeFieldContainer[API_v1_Presentation.SlideGroup]
    has_timeline: bool
    presentation_path: str
    destination: API_v1_Presentation.Destination
    def __init__(self, id: _Optional[_Union[API_v1_Identifier, _Mapping]] = ..., groups: _Optional[_Iterable[_Union[API_v1_Presentation.SlideGroup, _Mapping]]] = ..., has_timeline: bool = ..., presentation_path: _Optional[str] = ..., destination: _Optional[_Union[API_v1_Presentation.Destination, str]] = ...) -> None: ...

class API_v1_StageLayoutMap(_message.Message):
    __slots__ = ("entries",)
    class Entry(_message.Message):
        __slots__ = ("screen", "layout")
        SCREEN_FIELD_NUMBER: _ClassVar[int]
        LAYOUT_FIELD_NUMBER: _ClassVar[int]
        screen: API_v1_Identifier
        layout: API_v1_Identifier
        def __init__(self, screen: _Optional[_Union[API_v1_Identifier, _Mapping]] = ..., layout: _Optional[_Union[API_v1_Identifier, _Mapping]] = ...) -> None: ...
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    entries: _containers.RepeatedCompositeFieldContainer[API_v1_StageLayoutMap.Entry]
    def __init__(self, entries: _Optional[_Iterable[_Union[API_v1_StageLayoutMap.Entry, _Mapping]]] = ...) -> None: ...

class API_v1_ThemeGroup(_message.Message):
    __slots__ = ("id", "groups", "themes")
    ID_FIELD_NUMBER: _ClassVar[int]
    GROUPS_FIELD_NUMBER: _ClassVar[int]
    THEMES_FIELD_NUMBER: _ClassVar[int]
    id: API_v1_Identifier
    groups: _containers.RepeatedCompositeFieldContainer[API_v1_ThemeGroup]
    themes: _containers.RepeatedCompositeFieldContainer[API_v1_Theme]
    def __init__(self, id: _Optional[_Union[API_v1_Identifier, _Mapping]] = ..., groups: _Optional[_Iterable[_Union[API_v1_ThemeGroup, _Mapping]]] = ..., themes: _Optional[_Iterable[_Union[API_v1_Theme, _Mapping]]] = ...) -> None: ...

class API_v1_Theme(_message.Message):
    __slots__ = ("id", "slides")
    ID_FIELD_NUMBER: _ClassVar[int]
    SLIDES_FIELD_NUMBER: _ClassVar[int]
    id: API_v1_Identifier
    slides: _containers.RepeatedCompositeFieldContainer[API_v1_ThemeSlide]
    def __init__(self, id: _Optional[_Union[API_v1_Identifier, _Mapping]] = ..., slides: _Optional[_Iterable[_Union[API_v1_ThemeSlide, _Mapping]]] = ...) -> None: ...

class API_v1_ThemeSlide(_message.Message):
    __slots__ = ("id", "size", "background")
    ID_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    BACKGROUND_FIELD_NUMBER: _ClassVar[int]
    id: API_v1_Identifier
    size: API_v1_Size
    background: API_v1_Color
    def __init__(self, id: _Optional[_Union[API_v1_Identifier, _Mapping]] = ..., size: _Optional[_Union[API_v1_Size, _Mapping]] = ..., background: _Optional[_Union[API_v1_Color, _Mapping]] = ...) -> None: ...

class API_v1_SlideDisplayDetails(_message.Message):
    __slots__ = ("text", "notes", "uuid")
    TEXT_FIELD_NUMBER: _ClassVar[int]
    NOTES_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    text: str
    notes: str
    uuid: str
    def __init__(self, text: _Optional[str] = ..., notes: _Optional[str] = ..., uuid: _Optional[str] = ...) -> None: ...

class API_v1_ScreenConfig(_message.Message):
    __slots__ = ("id", "size", "screen_type")
    class API_v1_ScreenType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        audience: _ClassVar[API_v1_ScreenConfig.API_v1_ScreenType]
        stage: _ClassVar[API_v1_ScreenConfig.API_v1_ScreenType]
    audience: API_v1_ScreenConfig.API_v1_ScreenType
    stage: API_v1_ScreenConfig.API_v1_ScreenType
    ID_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    SCREEN_TYPE_FIELD_NUMBER: _ClassVar[int]
    id: API_v1_Identifier
    size: API_v1_Size
    screen_type: API_v1_ScreenConfig.API_v1_ScreenType
    def __init__(self, id: _Optional[_Union[API_v1_Identifier, _Mapping]] = ..., size: _Optional[_Union[API_v1_Size, _Mapping]] = ..., screen_type: _Optional[_Union[API_v1_ScreenConfig.API_v1_ScreenType, str]] = ...) -> None: ...

class API_v1_PropData(_message.Message):
    __slots__ = ("id", "is_active")
    ID_FIELD_NUMBER: _ClassVar[int]
    IS_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    id: API_v1_Identifier
    is_active: bool
    def __init__(self, id: _Optional[_Union[API_v1_Identifier, _Mapping]] = ..., is_active: bool = ...) -> None: ...
