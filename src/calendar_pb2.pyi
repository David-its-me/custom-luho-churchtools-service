import basicTypes_pb2 as _basicTypes_pb2
import rvtimestamp_pb2 as _rvtimestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Calendar(_message.Message):
    __slots__ = ("events", "active")
    class Event(_message.Message):
        __slots__ = ("uuid", "name", "description", "date", "recurrence_days", "recurrence_limit_date", "recurrence_excluded_dates", "action")
        class DayOfWeek(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            DAY_OF_WEEK_UNKNOWN: _ClassVar[Calendar.Event.DayOfWeek]
            DAY_OF_WEEK_SUNDAY: _ClassVar[Calendar.Event.DayOfWeek]
            DAY_OF_WEEK_MONDAY: _ClassVar[Calendar.Event.DayOfWeek]
            DAY_OF_WEEK_TUESDAY: _ClassVar[Calendar.Event.DayOfWeek]
            DAY_OF_WEEK_WEDNESDAY: _ClassVar[Calendar.Event.DayOfWeek]
            DAY_OF_WEEK_THURSDAY: _ClassVar[Calendar.Event.DayOfWeek]
            DAY_OF_WEEK_FRIDAY: _ClassVar[Calendar.Event.DayOfWeek]
            DAY_OF_WEEK_SATURDAY: _ClassVar[Calendar.Event.DayOfWeek]
        DAY_OF_WEEK_UNKNOWN: Calendar.Event.DayOfWeek
        DAY_OF_WEEK_SUNDAY: Calendar.Event.DayOfWeek
        DAY_OF_WEEK_MONDAY: Calendar.Event.DayOfWeek
        DAY_OF_WEEK_TUESDAY: Calendar.Event.DayOfWeek
        DAY_OF_WEEK_WEDNESDAY: Calendar.Event.DayOfWeek
        DAY_OF_WEEK_THURSDAY: Calendar.Event.DayOfWeek
        DAY_OF_WEEK_FRIDAY: Calendar.Event.DayOfWeek
        DAY_OF_WEEK_SATURDAY: Calendar.Event.DayOfWeek
        class Action(_message.Message):
            __slots__ = ("type", "uuid", "playlist", "macro")
            class Playlist(_message.Message):
                __slots__ = ("playlist_uuid", "playlist_item_uuid")
                PLAYLIST_UUID_FIELD_NUMBER: _ClassVar[int]
                PLAYLIST_ITEM_UUID_FIELD_NUMBER: _ClassVar[int]
                playlist_uuid: _basicTypes_pb2.UUID
                playlist_item_uuid: _basicTypes_pb2.UUID
                def __init__(self, playlist_uuid: _Optional[_Union[_basicTypes_pb2.UUID, _Mapping]] = ..., playlist_item_uuid: _Optional[_Union[_basicTypes_pb2.UUID, _Mapping]] = ...) -> None: ...
            class Macro(_message.Message):
                __slots__ = ("identification",)
                IDENTIFICATION_FIELD_NUMBER: _ClassVar[int]
                identification: _basicTypes_pb2.CollectionElementType
                def __init__(self, identification: _Optional[_Union[_basicTypes_pb2.CollectionElementType, _Mapping]] = ...) -> None: ...
            TYPE_FIELD_NUMBER: _ClassVar[int]
            UUID_FIELD_NUMBER: _ClassVar[int]
            PLAYLIST_FIELD_NUMBER: _ClassVar[int]
            MACRO_FIELD_NUMBER: _ClassVar[int]
            type: int
            uuid: _basicTypes_pb2.UUID
            playlist: Calendar.Event.Action.Playlist
            macro: Calendar.Event.Action.Macro
            def __init__(self, type: _Optional[int] = ..., uuid: _Optional[_Union[_basicTypes_pb2.UUID, _Mapping]] = ..., playlist: _Optional[_Union[Calendar.Event.Action.Playlist, _Mapping]] = ..., macro: _Optional[_Union[Calendar.Event.Action.Macro, _Mapping]] = ...) -> None: ...
        UUID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        DATE_FIELD_NUMBER: _ClassVar[int]
        RECURRENCE_DAYS_FIELD_NUMBER: _ClassVar[int]
        RECURRENCE_LIMIT_DATE_FIELD_NUMBER: _ClassVar[int]
        RECURRENCE_EXCLUDED_DATES_FIELD_NUMBER: _ClassVar[int]
        ACTION_FIELD_NUMBER: _ClassVar[int]
        uuid: _basicTypes_pb2.UUID
        name: str
        description: str
        date: _rvtimestamp_pb2.Timestamp
        recurrence_days: _containers.RepeatedScalarFieldContainer[Calendar.Event.DayOfWeek]
        recurrence_limit_date: _rvtimestamp_pb2.Timestamp
        recurrence_excluded_dates: _containers.RepeatedCompositeFieldContainer[_rvtimestamp_pb2.Timestamp]
        action: Calendar.Event.Action
        def __init__(self, uuid: _Optional[_Union[_basicTypes_pb2.UUID, _Mapping]] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., date: _Optional[_Union[_rvtimestamp_pb2.Timestamp, _Mapping]] = ..., recurrence_days: _Optional[_Iterable[_Union[Calendar.Event.DayOfWeek, str]]] = ..., recurrence_limit_date: _Optional[_Union[_rvtimestamp_pb2.Timestamp, _Mapping]] = ..., recurrence_excluded_dates: _Optional[_Iterable[_Union[_rvtimestamp_pb2.Timestamp, _Mapping]]] = ..., action: _Optional[_Union[Calendar.Event.Action, _Mapping]] = ...) -> None: ...
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    events: _containers.RepeatedCompositeFieldContainer[Calendar.Event]
    active: bool
    def __init__(self, events: _Optional[_Iterable[_Union[Calendar.Event, _Mapping]]] = ..., active: bool = ...) -> None: ...
