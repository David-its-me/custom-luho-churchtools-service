import action_pb2 as _action_pb2
import basicTypes_pb2 as _basicTypes_pb2
import cue_pb2 as _cue_pb2
import rvtimestamp_pb2 as _rvtimestamp_pb2
import background_pb2 as _background_pb2
import effects_pb2 as _effects_pb2
import groups_pb2 as _groups_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Presentation(_message.Message):
    __slots__ = ("application_info", "uuid", "name", "last_date_used", "last_modified_date", "category", "notes", "background", "chord_chart", "selected_arrangement", "arrangements", "cue_groups", "cues", "ccli", "bible_reference", "social_media", "timeline", "transition", "content_destination", "multi_tracks_licensing", "music_key", "music", "slide_show_duration")
    class ContentDestination(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CONTENT_DESTINATION_GLOBAL: _ClassVar[Presentation.ContentDestination]
        CONTENT_DESTINATION_ANNOUNCEMENTS: _ClassVar[Presentation.ContentDestination]
    CONTENT_DESTINATION_GLOBAL: Presentation.ContentDestination
    CONTENT_DESTINATION_ANNOUNCEMENTS: Presentation.ContentDestination
    class CCLI(_message.Message):
        __slots__ = ("author", "artist_credits", "song_title", "publisher", "copyright_year", "song_number", "display", "album", "artwork")
        AUTHOR_FIELD_NUMBER: _ClassVar[int]
        ARTIST_CREDITS_FIELD_NUMBER: _ClassVar[int]
        SONG_TITLE_FIELD_NUMBER: _ClassVar[int]
        PUBLISHER_FIELD_NUMBER: _ClassVar[int]
        COPYRIGHT_YEAR_FIELD_NUMBER: _ClassVar[int]
        SONG_NUMBER_FIELD_NUMBER: _ClassVar[int]
        DISPLAY_FIELD_NUMBER: _ClassVar[int]
        ALBUM_FIELD_NUMBER: _ClassVar[int]
        ARTWORK_FIELD_NUMBER: _ClassVar[int]
        author: str
        artist_credits: str
        song_title: str
        publisher: str
        copyright_year: int
        song_number: int
        display: bool
        album: str
        artwork: bytes
        def __init__(self, author: _Optional[str] = ..., artist_credits: _Optional[str] = ..., song_title: _Optional[str] = ..., publisher: _Optional[str] = ..., copyright_year: _Optional[int] = ..., song_number: _Optional[int] = ..., display: bool = ..., album: _Optional[str] = ..., artwork: _Optional[bytes] = ...) -> None: ...
    class BibleReference(_message.Message):
        __slots__ = ("book_index", "book_name", "chapter_range", "verse_range", "translation_name", "translation_display_abbreviation", "translation_internal_abbreviation", "book_key")
        BOOK_INDEX_FIELD_NUMBER: _ClassVar[int]
        BOOK_NAME_FIELD_NUMBER: _ClassVar[int]
        CHAPTER_RANGE_FIELD_NUMBER: _ClassVar[int]
        VERSE_RANGE_FIELD_NUMBER: _ClassVar[int]
        TRANSLATION_NAME_FIELD_NUMBER: _ClassVar[int]
        TRANSLATION_DISPLAY_ABBREVIATION_FIELD_NUMBER: _ClassVar[int]
        TRANSLATION_INTERNAL_ABBREVIATION_FIELD_NUMBER: _ClassVar[int]
        BOOK_KEY_FIELD_NUMBER: _ClassVar[int]
        book_index: int
        book_name: str
        chapter_range: _basicTypes_pb2.IntRange
        verse_range: _basicTypes_pb2.IntRange
        translation_name: str
        translation_display_abbreviation: str
        translation_internal_abbreviation: str
        book_key: str
        def __init__(self, book_index: _Optional[int] = ..., book_name: _Optional[str] = ..., chapter_range: _Optional[_Union[_basicTypes_pb2.IntRange, _Mapping]] = ..., verse_range: _Optional[_Union[_basicTypes_pb2.IntRange, _Mapping]] = ..., translation_name: _Optional[str] = ..., translation_display_abbreviation: _Optional[str] = ..., translation_internal_abbreviation: _Optional[str] = ..., book_key: _Optional[str] = ...) -> None: ...
    class SocialMedia(_message.Message):
        __slots__ = ("term", "time")
        TERM_FIELD_NUMBER: _ClassVar[int]
        TIME_FIELD_NUMBER: _ClassVar[int]
        term: str
        time: _rvtimestamp_pb2.Timestamp
        def __init__(self, term: _Optional[str] = ..., time: _Optional[_Union[_rvtimestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
    class Timeline(_message.Message):
        __slots__ = ("cues", "duration", "loop", "audio_action", "timecode_enable", "timecode_offset", "cues_v2")
        class Cue(_message.Message):
            __slots__ = ("trigger_time", "name", "cue_id", "action")
            TRIGGER_TIME_FIELD_NUMBER: _ClassVar[int]
            NAME_FIELD_NUMBER: _ClassVar[int]
            CUE_ID_FIELD_NUMBER: _ClassVar[int]
            ACTION_FIELD_NUMBER: _ClassVar[int]
            trigger_time: float
            name: str
            cue_id: _basicTypes_pb2.UUID
            action: _action_pb2.Action
            def __init__(self, trigger_time: _Optional[float] = ..., name: _Optional[str] = ..., cue_id: _Optional[_Union[_basicTypes_pb2.UUID, _Mapping]] = ..., action: _Optional[_Union[_action_pb2.Action, _Mapping]] = ...) -> None: ...
        CUES_FIELD_NUMBER: _ClassVar[int]
        DURATION_FIELD_NUMBER: _ClassVar[int]
        LOOP_FIELD_NUMBER: _ClassVar[int]
        AUDIO_ACTION_FIELD_NUMBER: _ClassVar[int]
        TIMECODE_ENABLE_FIELD_NUMBER: _ClassVar[int]
        TIMECODE_OFFSET_FIELD_NUMBER: _ClassVar[int]
        CUES_V2_FIELD_NUMBER: _ClassVar[int]
        cues: _containers.RepeatedCompositeFieldContainer[Presentation.Timeline.Cue]
        duration: float
        loop: bool
        audio_action: _action_pb2.Action
        timecode_enable: bool
        timecode_offset: float
        cues_v2: _containers.RepeatedCompositeFieldContainer[Presentation.Timeline.Cue]
        def __init__(self, cues: _Optional[_Iterable[_Union[Presentation.Timeline.Cue, _Mapping]]] = ..., duration: _Optional[float] = ..., loop: bool = ..., audio_action: _Optional[_Union[_action_pb2.Action, _Mapping]] = ..., timecode_enable: bool = ..., timecode_offset: _Optional[float] = ..., cues_v2: _Optional[_Iterable[_Union[Presentation.Timeline.Cue, _Mapping]]] = ...) -> None: ...
    class Arrangement(_message.Message):
        __slots__ = ("uuid", "name", "group_identifiers")
        UUID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        GROUP_IDENTIFIERS_FIELD_NUMBER: _ClassVar[int]
        uuid: _basicTypes_pb2.UUID
        name: str
        group_identifiers: _containers.RepeatedCompositeFieldContainer[_basicTypes_pb2.UUID]
        def __init__(self, uuid: _Optional[_Union[_basicTypes_pb2.UUID, _Mapping]] = ..., name: _Optional[str] = ..., group_identifiers: _Optional[_Iterable[_Union[_basicTypes_pb2.UUID, _Mapping]]] = ...) -> None: ...
    class CueGroup(_message.Message):
        __slots__ = ("group", "cue_identifiers")
        GROUP_FIELD_NUMBER: _ClassVar[int]
        CUE_IDENTIFIERS_FIELD_NUMBER: _ClassVar[int]
        group: _groups_pb2.Group
        cue_identifiers: _containers.RepeatedCompositeFieldContainer[_basicTypes_pb2.UUID]
        def __init__(self, group: _Optional[_Union[_groups_pb2.Group, _Mapping]] = ..., cue_identifiers: _Optional[_Iterable[_Union[_basicTypes_pb2.UUID, _Mapping]]] = ...) -> None: ...
    class MultiTracksLicensing(_message.Message):
        __slots__ = ("song_identifier", "customer_identifier", "expiration_date", "license_expiration", "subscription")
        class Subscription(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            SUBSCRIPTION_CHART_PRO: _ClassVar[Presentation.MultiTracksLicensing.Subscription]
            SUBSCRIPTION_SLIDE_PRO: _ClassVar[Presentation.MultiTracksLicensing.Subscription]
        SUBSCRIPTION_CHART_PRO: Presentation.MultiTracksLicensing.Subscription
        SUBSCRIPTION_SLIDE_PRO: Presentation.MultiTracksLicensing.Subscription
        SONG_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
        CUSTOMER_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
        EXPIRATION_DATE_FIELD_NUMBER: _ClassVar[int]
        LICENSE_EXPIRATION_FIELD_NUMBER: _ClassVar[int]
        SUBSCRIPTION_FIELD_NUMBER: _ClassVar[int]
        song_identifier: int
        customer_identifier: str
        expiration_date: _rvtimestamp_pb2.Timestamp
        license_expiration: _rvtimestamp_pb2.Timestamp
        subscription: Presentation.MultiTracksLicensing.Subscription
        def __init__(self, song_identifier: _Optional[int] = ..., customer_identifier: _Optional[str] = ..., expiration_date: _Optional[_Union[_rvtimestamp_pb2.Timestamp, _Mapping]] = ..., license_expiration: _Optional[_Union[_rvtimestamp_pb2.Timestamp, _Mapping]] = ..., subscription: _Optional[_Union[Presentation.MultiTracksLicensing.Subscription, str]] = ...) -> None: ...
    class Music(_message.Message):
        __slots__ = ("original_music_key", "user_music_key", "original", "user")
        ORIGINAL_MUSIC_KEY_FIELD_NUMBER: _ClassVar[int]
        USER_MUSIC_KEY_FIELD_NUMBER: _ClassVar[int]
        ORIGINAL_FIELD_NUMBER: _ClassVar[int]
        USER_FIELD_NUMBER: _ClassVar[int]
        original_music_key: str
        user_music_key: str
        original: _basicTypes_pb2.MusicKeyScale
        user: _basicTypes_pb2.MusicKeyScale
        def __init__(self, original_music_key: _Optional[str] = ..., user_music_key: _Optional[str] = ..., original: _Optional[_Union[_basicTypes_pb2.MusicKeyScale, _Mapping]] = ..., user: _Optional[_Union[_basicTypes_pb2.MusicKeyScale, _Mapping]] = ...) -> None: ...
    APPLICATION_INFO_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    LAST_DATE_USED_FIELD_NUMBER: _ClassVar[int]
    LAST_MODIFIED_DATE_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    NOTES_FIELD_NUMBER: _ClassVar[int]
    BACKGROUND_FIELD_NUMBER: _ClassVar[int]
    CHORD_CHART_FIELD_NUMBER: _ClassVar[int]
    SELECTED_ARRANGEMENT_FIELD_NUMBER: _ClassVar[int]
    ARRANGEMENTS_FIELD_NUMBER: _ClassVar[int]
    CUE_GROUPS_FIELD_NUMBER: _ClassVar[int]
    CUES_FIELD_NUMBER: _ClassVar[int]
    CCLI_FIELD_NUMBER: _ClassVar[int]
    BIBLE_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    SOCIAL_MEDIA_FIELD_NUMBER: _ClassVar[int]
    TIMELINE_FIELD_NUMBER: _ClassVar[int]
    TRANSITION_FIELD_NUMBER: _ClassVar[int]
    CONTENT_DESTINATION_FIELD_NUMBER: _ClassVar[int]
    MULTI_TRACKS_LICENSING_FIELD_NUMBER: _ClassVar[int]
    MUSIC_KEY_FIELD_NUMBER: _ClassVar[int]
    MUSIC_FIELD_NUMBER: _ClassVar[int]
    SLIDE_SHOW_DURATION_FIELD_NUMBER: _ClassVar[int]
    application_info: _basicTypes_pb2.ApplicationInfo
    uuid: _basicTypes_pb2.UUID
    name: str
    last_date_used: _rvtimestamp_pb2.Timestamp
    last_modified_date: _rvtimestamp_pb2.Timestamp
    category: str
    notes: str
    background: _background_pb2.Background
    chord_chart: _basicTypes_pb2.URL
    selected_arrangement: _basicTypes_pb2.UUID
    arrangements: _containers.RepeatedCompositeFieldContainer[Presentation.Arrangement]
    cue_groups: _containers.RepeatedCompositeFieldContainer[Presentation.CueGroup]
    cues: _containers.RepeatedCompositeFieldContainer[_cue_pb2.Cue]
    ccli: Presentation.CCLI
    bible_reference: Presentation.BibleReference
    social_media: Presentation.SocialMedia
    timeline: Presentation.Timeline
    transition: _effects_pb2.Transition
    content_destination: Presentation.ContentDestination
    multi_tracks_licensing: Presentation.MultiTracksLicensing
    music_key: str
    music: Presentation.Music
    slide_show_duration: float
    def __init__(self, application_info: _Optional[_Union[_basicTypes_pb2.ApplicationInfo, _Mapping]] = ..., uuid: _Optional[_Union[_basicTypes_pb2.UUID, _Mapping]] = ..., name: _Optional[str] = ..., last_date_used: _Optional[_Union[_rvtimestamp_pb2.Timestamp, _Mapping]] = ..., last_modified_date: _Optional[_Union[_rvtimestamp_pb2.Timestamp, _Mapping]] = ..., category: _Optional[str] = ..., notes: _Optional[str] = ..., background: _Optional[_Union[_background_pb2.Background, _Mapping]] = ..., chord_chart: _Optional[_Union[_basicTypes_pb2.URL, _Mapping]] = ..., selected_arrangement: _Optional[_Union[_basicTypes_pb2.UUID, _Mapping]] = ..., arrangements: _Optional[_Iterable[_Union[Presentation.Arrangement, _Mapping]]] = ..., cue_groups: _Optional[_Iterable[_Union[Presentation.CueGroup, _Mapping]]] = ..., cues: _Optional[_Iterable[_Union[_cue_pb2.Cue, _Mapping]]] = ..., ccli: _Optional[_Union[Presentation.CCLI, _Mapping]] = ..., bible_reference: _Optional[_Union[Presentation.BibleReference, _Mapping]] = ..., social_media: _Optional[_Union[Presentation.SocialMedia, _Mapping]] = ..., timeline: _Optional[_Union[Presentation.Timeline, _Mapping]] = ..., transition: _Optional[_Union[_effects_pb2.Transition, _Mapping]] = ..., content_destination: _Optional[_Union[Presentation.ContentDestination, str]] = ..., multi_tracks_licensing: _Optional[_Union[Presentation.MultiTracksLicensing, _Mapping]] = ..., music_key: _Optional[str] = ..., music: _Optional[_Union[Presentation.Music, _Mapping]] = ..., slide_show_duration: _Optional[float] = ...) -> None: ...
