import propresenter.pb_auto_generated.hotKey_pb2 as _hotKey_pb2
import propresenter.pb_auto_generated.cue_pb2 as _cue_pb2
import propresenter.pb_auto_generated.basicTypes_pb2 as _basicTypes_pb2
import propresenter.pb_auto_generated.action_pb2 as _action_pb2
import propresenter.pb_auto_generated.planningCenter_pb2 as _planningCenter_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Playlist(_message.Message):
    __slots__ = ("uuid", "name", "type", "expanded", "targeted_layer_uuid", "smart_directory_path", "hot_key", "cues", "children", "timecode_enabled", "timing", "startup_info", "playlists", "items", "smart_directory", "pco_plan")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_UNKNOWN: _ClassVar[Playlist.Type]
        TYPE_PLAYLIST: _ClassVar[Playlist.Type]
        TYPE_GROUP: _ClassVar[Playlist.Type]
        TYPE_SMART: _ClassVar[Playlist.Type]
        TYPE_ROOT: _ClassVar[Playlist.Type]
    TYPE_UNKNOWN: Playlist.Type
    TYPE_PLAYLIST: Playlist.Type
    TYPE_GROUP: Playlist.Type
    TYPE_SMART: Playlist.Type
    TYPE_ROOT: Playlist.Type
    class TimingType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TIMING_TYPE_NONE: _ClassVar[Playlist.TimingType]
        TIMING_TYPE_TIMECODE: _ClassVar[Playlist.TimingType]
        TIMING_TYPE_TIME_OF_DAY: _ClassVar[Playlist.TimingType]
    TIMING_TYPE_NONE: Playlist.TimingType
    TIMING_TYPE_TIMECODE: Playlist.TimingType
    TIMING_TYPE_TIME_OF_DAY: Playlist.TimingType
    class PlaylistArray(_message.Message):
        __slots__ = ("playlists",)
        PLAYLISTS_FIELD_NUMBER: _ClassVar[int]
        playlists: _containers.RepeatedCompositeFieldContainer[Playlist]
        def __init__(self, playlists: _Optional[_Iterable[_Union[Playlist, _Mapping]]] = ...) -> None: ...
    class PlaylistItems(_message.Message):
        __slots__ = ("items",)
        ITEMS_FIELD_NUMBER: _ClassVar[int]
        items: _containers.RepeatedCompositeFieldContainer[PlaylistItem]
        def __init__(self, items: _Optional[_Iterable[_Union[PlaylistItem, _Mapping]]] = ...) -> None: ...
    class FolderDirectory(_message.Message):
        __slots__ = ("smart_directory", "import_behavior")
        class ImportBehavior(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            IMPORT_BEHAVIOR_BACKGROUND: _ClassVar[Playlist.FolderDirectory.ImportBehavior]
            IMPORT_BEHAVIOR_FOREGROUND: _ClassVar[Playlist.FolderDirectory.ImportBehavior]
        IMPORT_BEHAVIOR_BACKGROUND: Playlist.FolderDirectory.ImportBehavior
        IMPORT_BEHAVIOR_FOREGROUND: Playlist.FolderDirectory.ImportBehavior
        SMART_DIRECTORY_FIELD_NUMBER: _ClassVar[int]
        IMPORT_BEHAVIOR_FIELD_NUMBER: _ClassVar[int]
        smart_directory: _basicTypes_pb2.URL
        import_behavior: Playlist.FolderDirectory.ImportBehavior
        def __init__(self, smart_directory: _Optional[_Union[_basicTypes_pb2.URL, _Mapping]] = ..., import_behavior: _Optional[_Union[Playlist.FolderDirectory.ImportBehavior, str]] = ...) -> None: ...
    class Tag(_message.Message):
        __slots__ = ("color", "name", "uuid")
        COLOR_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        UUID_FIELD_NUMBER: _ClassVar[int]
        color: _basicTypes_pb2.Color
        name: str
        uuid: _basicTypes_pb2.UUID
        def __init__(self, color: _Optional[_Union[_basicTypes_pb2.Color, _Mapping]] = ..., name: _Optional[str] = ..., uuid: _Optional[_Union[_basicTypes_pb2.UUID, _Mapping]] = ...) -> None: ...
    class StartupInfo(_message.Message):
        __slots__ = ("trigger_on_startup",)
        TRIGGER_ON_STARTUP_FIELD_NUMBER: _ClassVar[int]
        trigger_on_startup: bool
        def __init__(self, trigger_on_startup: bool = ...) -> None: ...
    UUID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    EXPANDED_FIELD_NUMBER: _ClassVar[int]
    TARGETED_LAYER_UUID_FIELD_NUMBER: _ClassVar[int]
    SMART_DIRECTORY_PATH_FIELD_NUMBER: _ClassVar[int]
    HOT_KEY_FIELD_NUMBER: _ClassVar[int]
    CUES_FIELD_NUMBER: _ClassVar[int]
    CHILDREN_FIELD_NUMBER: _ClassVar[int]
    TIMECODE_ENABLED_FIELD_NUMBER: _ClassVar[int]
    TIMING_FIELD_NUMBER: _ClassVar[int]
    STARTUP_INFO_FIELD_NUMBER: _ClassVar[int]
    PLAYLISTS_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    SMART_DIRECTORY_FIELD_NUMBER: _ClassVar[int]
    PCO_PLAN_FIELD_NUMBER: _ClassVar[int]
    uuid: _basicTypes_pb2.UUID
    name: str
    type: Playlist.Type
    expanded: bool
    targeted_layer_uuid: _basicTypes_pb2.UUID
    smart_directory_path: _basicTypes_pb2.URL
    hot_key: _hotKey_pb2.HotKey
    cues: _containers.RepeatedCompositeFieldContainer[_cue_pb2.Cue]
    children: _containers.RepeatedCompositeFieldContainer[Playlist]
    timecode_enabled: bool
    timing: Playlist.TimingType
    startup_info: Playlist.StartupInfo
    playlists: Playlist.PlaylistArray
    items: Playlist.PlaylistItems
    smart_directory: Playlist.FolderDirectory
    pco_plan: _planningCenter_pb2.PlanningCenterPlan
    def __init__(self, uuid: _Optional[_Union[_basicTypes_pb2.UUID, _Mapping]] = ..., name: _Optional[str] = ..., type: _Optional[_Union[Playlist.Type, str]] = ..., expanded: bool = ..., targeted_layer_uuid: _Optional[_Union[_basicTypes_pb2.UUID, _Mapping]] = ..., smart_directory_path: _Optional[_Union[_basicTypes_pb2.URL, _Mapping]] = ..., hot_key: _Optional[_Union[_hotKey_pb2.HotKey, _Mapping]] = ..., cues: _Optional[_Iterable[_Union[_cue_pb2.Cue, _Mapping]]] = ..., children: _Optional[_Iterable[_Union[Playlist, _Mapping]]] = ..., timecode_enabled: bool = ..., timing: _Optional[_Union[Playlist.TimingType, str]] = ..., startup_info: _Optional[_Union[Playlist.StartupInfo, _Mapping]] = ..., playlists: _Optional[_Union[Playlist.PlaylistArray, _Mapping]] = ..., items: _Optional[_Union[Playlist.PlaylistItems, _Mapping]] = ..., smart_directory: _Optional[_Union[Playlist.FolderDirectory, _Mapping]] = ..., pco_plan: _Optional[_Union[_planningCenter_pb2.PlanningCenterPlan, _Mapping]] = ...) -> None: ...

class PlaylistItem(_message.Message):
    __slots__ = ("uuid", "name", "tags", "is_hidden", "header", "presentation", "cue", "planning_center", "placeholder")
    class Header(_message.Message):
        __slots__ = ("color", "actions")
        COLOR_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        color: _basicTypes_pb2.Color
        actions: _containers.RepeatedCompositeFieldContainer[_action_pb2.Action]
        def __init__(self, color: _Optional[_Union[_basicTypes_pb2.Color, _Mapping]] = ..., actions: _Optional[_Iterable[_Union[_action_pb2.Action, _Mapping]]] = ...) -> None: ...
    class Presentation(_message.Message):
        __slots__ = ("document_path", "arrangement", "content_destination", "user_music_key")
        class ContentDestination(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            CONTENT_DESTINATION_GLOBAL: _ClassVar[PlaylistItem.Presentation.ContentDestination]
            CONTENT_DESTINATION_ANNOUNCEMENTS: _ClassVar[PlaylistItem.Presentation.ContentDestination]
        CONTENT_DESTINATION_GLOBAL: PlaylistItem.Presentation.ContentDestination
        CONTENT_DESTINATION_ANNOUNCEMENTS: PlaylistItem.Presentation.ContentDestination
        DOCUMENT_PATH_FIELD_NUMBER: _ClassVar[int]
        ARRANGEMENT_FIELD_NUMBER: _ClassVar[int]
        CONTENT_DESTINATION_FIELD_NUMBER: _ClassVar[int]
        USER_MUSIC_KEY_FIELD_NUMBER: _ClassVar[int]
        document_path: _basicTypes_pb2.URL
        arrangement: _basicTypes_pb2.UUID
        content_destination: PlaylistItem.Presentation.ContentDestination
        user_music_key: _basicTypes_pb2.MusicKeyScale
        def __init__(self, document_path: _Optional[_Union[_basicTypes_pb2.URL, _Mapping]] = ..., arrangement: _Optional[_Union[_basicTypes_pb2.UUID, _Mapping]] = ..., content_destination: _Optional[_Union[PlaylistItem.Presentation.ContentDestination, str]] = ..., user_music_key: _Optional[_Union[_basicTypes_pb2.MusicKeyScale, _Mapping]] = ...) -> None: ...
    class PlanningCenter(_message.Message):
        __slots__ = ("item", "linked_data")
        ITEM_FIELD_NUMBER: _ClassVar[int]
        LINKED_DATA_FIELD_NUMBER: _ClassVar[int]
        item: _planningCenter_pb2.PlanningCenterPlan.PlanItem
        linked_data: PlaylistItem
        def __init__(self, item: _Optional[_Union[_planningCenter_pb2.PlanningCenterPlan.PlanItem, _Mapping]] = ..., linked_data: _Optional[_Union[PlaylistItem, _Mapping]] = ...) -> None: ...
    class Placeholder(_message.Message):
        __slots__ = ("linked_data",)
        LINKED_DATA_FIELD_NUMBER: _ClassVar[int]
        linked_data: PlaylistItem
        def __init__(self, linked_data: _Optional[_Union[PlaylistItem, _Mapping]] = ...) -> None: ...
    UUID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    IS_HIDDEN_FIELD_NUMBER: _ClassVar[int]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    PRESENTATION_FIELD_NUMBER: _ClassVar[int]
    CUE_FIELD_NUMBER: _ClassVar[int]
    PLANNING_CENTER_FIELD_NUMBER: _ClassVar[int]
    PLACEHOLDER_FIELD_NUMBER: _ClassVar[int]
    uuid: _basicTypes_pb2.UUID
    name: str
    tags: _containers.RepeatedCompositeFieldContainer[_basicTypes_pb2.UUID]
    is_hidden: bool
    header: PlaylistItem.Header
    presentation: PlaylistItem.Presentation
    cue: _cue_pb2.Cue
    planning_center: PlaylistItem.PlanningCenter
    placeholder: PlaylistItem.Placeholder
    def __init__(self, uuid: _Optional[_Union[_basicTypes_pb2.UUID, _Mapping]] = ..., name: _Optional[str] = ..., tags: _Optional[_Iterable[_Union[_basicTypes_pb2.UUID, _Mapping]]] = ..., is_hidden: bool = ..., header: _Optional[_Union[PlaylistItem.Header, _Mapping]] = ..., presentation: _Optional[_Union[PlaylistItem.Presentation, _Mapping]] = ..., cue: _Optional[_Union[_cue_pb2.Cue, _Mapping]] = ..., planning_center: _Optional[_Union[PlaylistItem.PlanningCenter, _Mapping]] = ..., placeholder: _Optional[_Union[PlaylistItem.Placeholder, _Mapping]] = ...) -> None: ...
