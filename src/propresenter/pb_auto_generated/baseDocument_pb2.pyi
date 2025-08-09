import propresenter.pb_auto_generated.workspace_pb2 as _workspace_pb2
import propresenter.pb_auto_generated.basicTypes_pb2 as _basicTypes_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Document(_message.Message):
    __slots__ = ("application_info", "uuid", "uses_relative_urls", "workspace")
    APPLICATION_INFO_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    USES_RELATIVE_URLS_FIELD_NUMBER: _ClassVar[int]
    WORKSPACE_FIELD_NUMBER: _ClassVar[int]
    application_info: _basicTypes_pb2.ApplicationInfo
    uuid: _basicTypes_pb2.UUID
    uses_relative_urls: bool
    workspace: _workspace_pb2.Workspace
    def __init__(self, application_info: _Optional[_Union[_basicTypes_pb2.ApplicationInfo, _Mapping]] = ..., uuid: _Optional[_Union[_basicTypes_pb2.UUID, _Mapping]] = ..., uses_relative_urls: bool = ..., workspace: _Optional[_Union[_workspace_pb2.Workspace, _Mapping]] = ...) -> None: ...

class CacheInfo(_message.Message):
    __slots__ = ("uuid", "application_version", "url", "last_modified_date")
    UUID_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_VERSION_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    LAST_MODIFIED_DATE_FIELD_NUMBER: _ClassVar[int]
    uuid: _basicTypes_pb2.UUID
    application_version: _basicTypes_pb2.Version
    url: _basicTypes_pb2.URL
    last_modified_date: float
    def __init__(self, uuid: _Optional[_Union[_basicTypes_pb2.UUID, _Mapping]] = ..., application_version: _Optional[_Union[_basicTypes_pb2.Version, _Mapping]] = ..., url: _Optional[_Union[_basicTypes_pb2.URL, _Mapping]] = ..., last_modified_date: _Optional[float] = ...) -> None: ...

class PVPDocumentState(_message.Message):
    __slots__ = ("primary_playlist", "alternate_playlist", "playlist_split_is_vertical", "targeted_layer", "selected_layer", "locked_layer", "live_video_playlist_scale", "split_view_divider_position")
    class PlaylistState(_message.Message):
        __slots__ = ("uuid", "layout", "item_scale")
        class LayoutType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            LAYOUT_TYPE_CUE: _ClassVar[PVPDocumentState.PlaylistState.LayoutType]
            LAYOUT_TYPE_ACTION: _ClassVar[PVPDocumentState.PlaylistState.LayoutType]
            LAYOUT_TYPE_LIVE_VIDEO: _ClassVar[PVPDocumentState.PlaylistState.LayoutType]
        LAYOUT_TYPE_CUE: PVPDocumentState.PlaylistState.LayoutType
        LAYOUT_TYPE_ACTION: PVPDocumentState.PlaylistState.LayoutType
        LAYOUT_TYPE_LIVE_VIDEO: PVPDocumentState.PlaylistState.LayoutType
        UUID_FIELD_NUMBER: _ClassVar[int]
        LAYOUT_FIELD_NUMBER: _ClassVar[int]
        ITEM_SCALE_FIELD_NUMBER: _ClassVar[int]
        uuid: _basicTypes_pb2.UUID
        layout: PVPDocumentState.PlaylistState.LayoutType
        item_scale: float
        def __init__(self, uuid: _Optional[_Union[_basicTypes_pb2.UUID, _Mapping]] = ..., layout: _Optional[_Union[PVPDocumentState.PlaylistState.LayoutType, str]] = ..., item_scale: _Optional[float] = ...) -> None: ...
    PRIMARY_PLAYLIST_FIELD_NUMBER: _ClassVar[int]
    ALTERNATE_PLAYLIST_FIELD_NUMBER: _ClassVar[int]
    PLAYLIST_SPLIT_IS_VERTICAL_FIELD_NUMBER: _ClassVar[int]
    TARGETED_LAYER_FIELD_NUMBER: _ClassVar[int]
    SELECTED_LAYER_FIELD_NUMBER: _ClassVar[int]
    LOCKED_LAYER_FIELD_NUMBER: _ClassVar[int]
    LIVE_VIDEO_PLAYLIST_SCALE_FIELD_NUMBER: _ClassVar[int]
    SPLIT_VIEW_DIVIDER_POSITION_FIELD_NUMBER: _ClassVar[int]
    primary_playlist: PVPDocumentState.PlaylistState
    alternate_playlist: PVPDocumentState.PlaylistState
    playlist_split_is_vertical: bool
    targeted_layer: _basicTypes_pb2.UUID
    selected_layer: _basicTypes_pb2.UUID
    locked_layer: _basicTypes_pb2.UUID
    live_video_playlist_scale: float
    split_view_divider_position: float
    def __init__(self, primary_playlist: _Optional[_Union[PVPDocumentState.PlaylistState, _Mapping]] = ..., alternate_playlist: _Optional[_Union[PVPDocumentState.PlaylistState, _Mapping]] = ..., playlist_split_is_vertical: bool = ..., targeted_layer: _Optional[_Union[_basicTypes_pb2.UUID, _Mapping]] = ..., selected_layer: _Optional[_Union[_basicTypes_pb2.UUID, _Mapping]] = ..., locked_layer: _Optional[_Union[_basicTypes_pb2.UUID, _Mapping]] = ..., live_video_playlist_scale: _Optional[float] = ..., split_view_divider_position: _Optional[float] = ...) -> None: ...
