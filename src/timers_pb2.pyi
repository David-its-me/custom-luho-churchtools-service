import basicTypes_pb2 as _basicTypes_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Clock(_message.Message):
    __slots__ = ("format",)
    class Format(_message.Message):
        __slots__ = ("date_type", "time_format", "military_time_enabled")
        class DateFormatterStyle(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            DATE_FORMATTER_STYLE_NONE: _ClassVar[Clock.Format.DateFormatterStyle]
            DATE_FORMATTER_STYLE_SHORT: _ClassVar[Clock.Format.DateFormatterStyle]
            DATE_FORMATTER_STYLE_MEDIUM: _ClassVar[Clock.Format.DateFormatterStyle]
            DATE_FORMATTER_STYLE_LONG: _ClassVar[Clock.Format.DateFormatterStyle]
            DATE_FORMATTER_STYLE_FULL: _ClassVar[Clock.Format.DateFormatterStyle]
        DATE_FORMATTER_STYLE_NONE: Clock.Format.DateFormatterStyle
        DATE_FORMATTER_STYLE_SHORT: Clock.Format.DateFormatterStyle
        DATE_FORMATTER_STYLE_MEDIUM: Clock.Format.DateFormatterStyle
        DATE_FORMATTER_STYLE_LONG: Clock.Format.DateFormatterStyle
        DATE_FORMATTER_STYLE_FULL: Clock.Format.DateFormatterStyle
        DATE_TYPE_FIELD_NUMBER: _ClassVar[int]
        TIME_FORMAT_FIELD_NUMBER: _ClassVar[int]
        MILITARY_TIME_ENABLED_FIELD_NUMBER: _ClassVar[int]
        date_type: Clock.Format.DateFormatterStyle
        time_format: Clock.Format.DateFormatterStyle
        military_time_enabled: bool
        def __init__(self, date_type: _Optional[_Union[Clock.Format.DateFormatterStyle, str]] = ..., time_format: _Optional[_Union[Clock.Format.DateFormatterStyle, str]] = ..., military_time_enabled: bool = ...) -> None: ...
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    format: str
    def __init__(self, format: _Optional[str] = ...) -> None: ...

class Timer(_message.Message):
    __slots__ = ("uuid", "name", "configuration")
    class Format(_message.Message):
        __slots__ = ("hour", "minute", "second", "millisecond", "is_wall_clock_time", "is_24_hour_time", "show_milliseconds_under_minute_only")
        class Style(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            STYE_NONE: _ClassVar[Timer.Format.Style]
            STYLE_SHORT: _ClassVar[Timer.Format.Style]
            STYLE_LONG: _ClassVar[Timer.Format.Style]
            STYLE_REMOVE_SHORT: _ClassVar[Timer.Format.Style]
            STYLE_REMOVE_LONG: _ClassVar[Timer.Format.Style]
        STYE_NONE: Timer.Format.Style
        STYLE_SHORT: Timer.Format.Style
        STYLE_LONG: Timer.Format.Style
        STYLE_REMOVE_SHORT: Timer.Format.Style
        STYLE_REMOVE_LONG: Timer.Format.Style
        HOUR_FIELD_NUMBER: _ClassVar[int]
        MINUTE_FIELD_NUMBER: _ClassVar[int]
        SECOND_FIELD_NUMBER: _ClassVar[int]
        MILLISECOND_FIELD_NUMBER: _ClassVar[int]
        IS_WALL_CLOCK_TIME_FIELD_NUMBER: _ClassVar[int]
        IS_24_HOUR_TIME_FIELD_NUMBER: _ClassVar[int]
        SHOW_MILLISECONDS_UNDER_MINUTE_ONLY_FIELD_NUMBER: _ClassVar[int]
        hour: Timer.Format.Style
        minute: Timer.Format.Style
        second: Timer.Format.Style
        millisecond: Timer.Format.Style
        is_wall_clock_time: bool
        is_24_hour_time: bool
        show_milliseconds_under_minute_only: bool
        def __init__(self, hour: _Optional[_Union[Timer.Format.Style, str]] = ..., minute: _Optional[_Union[Timer.Format.Style, str]] = ..., second: _Optional[_Union[Timer.Format.Style, str]] = ..., millisecond: _Optional[_Union[Timer.Format.Style, str]] = ..., is_wall_clock_time: bool = ..., is_24_hour_time: bool = ..., show_milliseconds_under_minute_only: bool = ...) -> None: ...
    class Configuration(_message.Message):
        __slots__ = ("allows_overrun", "countdown", "countdown_to_time", "elapsed_time")
        class TimerTypeCountdown(_message.Message):
            __slots__ = ("duration",)
            DURATION_FIELD_NUMBER: _ClassVar[int]
            duration: float
            def __init__(self, duration: _Optional[float] = ...) -> None: ...
        class TimerTypeCountdownToTime(_message.Message):
            __slots__ = ("time_of_day", "period")
            class TimePeriod(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                TIME_PERIOD_AM: _ClassVar[Timer.Configuration.TimerTypeCountdownToTime.TimePeriod]
                TIME_PERIOD_PM: _ClassVar[Timer.Configuration.TimerTypeCountdownToTime.TimePeriod]
                TIME_PERIOD_24: _ClassVar[Timer.Configuration.TimerTypeCountdownToTime.TimePeriod]
            TIME_PERIOD_AM: Timer.Configuration.TimerTypeCountdownToTime.TimePeriod
            TIME_PERIOD_PM: Timer.Configuration.TimerTypeCountdownToTime.TimePeriod
            TIME_PERIOD_24: Timer.Configuration.TimerTypeCountdownToTime.TimePeriod
            TIME_OF_DAY_FIELD_NUMBER: _ClassVar[int]
            PERIOD_FIELD_NUMBER: _ClassVar[int]
            time_of_day: float
            period: Timer.Configuration.TimerTypeCountdownToTime.TimePeriod
            def __init__(self, time_of_day: _Optional[float] = ..., period: _Optional[_Union[Timer.Configuration.TimerTypeCountdownToTime.TimePeriod, str]] = ...) -> None: ...
        class TimerTypeElapsedTime(_message.Message):
            __slots__ = ("start_time", "end_time", "has_end_time")
            START_TIME_FIELD_NUMBER: _ClassVar[int]
            END_TIME_FIELD_NUMBER: _ClassVar[int]
            HAS_END_TIME_FIELD_NUMBER: _ClassVar[int]
            start_time: float
            end_time: float
            has_end_time: bool
            def __init__(self, start_time: _Optional[float] = ..., end_time: _Optional[float] = ..., has_end_time: bool = ...) -> None: ...
        ALLOWS_OVERRUN_FIELD_NUMBER: _ClassVar[int]
        COUNTDOWN_FIELD_NUMBER: _ClassVar[int]
        COUNTDOWN_TO_TIME_FIELD_NUMBER: _ClassVar[int]
        ELAPSED_TIME_FIELD_NUMBER: _ClassVar[int]
        allows_overrun: bool
        countdown: Timer.Configuration.TimerTypeCountdown
        countdown_to_time: Timer.Configuration.TimerTypeCountdownToTime
        elapsed_time: Timer.Configuration.TimerTypeElapsedTime
        def __init__(self, allows_overrun: bool = ..., countdown: _Optional[_Union[Timer.Configuration.TimerTypeCountdown, _Mapping]] = ..., countdown_to_time: _Optional[_Union[Timer.Configuration.TimerTypeCountdownToTime, _Mapping]] = ..., elapsed_time: _Optional[_Union[Timer.Configuration.TimerTypeElapsedTime, _Mapping]] = ...) -> None: ...
    UUID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    uuid: _basicTypes_pb2.UUID
    name: str
    configuration: Timer.Configuration
    def __init__(self, uuid: _Optional[_Union[_basicTypes_pb2.UUID, _Mapping]] = ..., name: _Optional[str] = ..., configuration: _Optional[_Union[Timer.Configuration, _Mapping]] = ...) -> None: ...

class TimersDocument(_message.Message):
    __slots__ = ("application_info", "clock", "timers")
    APPLICATION_INFO_FIELD_NUMBER: _ClassVar[int]
    CLOCK_FIELD_NUMBER: _ClassVar[int]
    TIMERS_FIELD_NUMBER: _ClassVar[int]
    application_info: _basicTypes_pb2.ApplicationInfo
    clock: Clock
    timers: _containers.RepeatedCompositeFieldContainer[Timer]
    def __init__(self, application_info: _Optional[_Union[_basicTypes_pb2.ApplicationInfo, _Mapping]] = ..., clock: _Optional[_Union[Clock, _Mapping]] = ..., timers: _Optional[_Iterable[_Union[Timer, _Mapping]]] = ...) -> None: ...
