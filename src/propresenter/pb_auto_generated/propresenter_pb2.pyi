import propresenter.pb_auto_generated.basicTypes_pb2 as _basicTypes_pb2
import propresenter.pb_auto_generated.playlist_pb2 as _playlist_pb2
import propresenter.pb_auto_generated.action_pb2 as _action_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PlaylistDocument(_message.Message):
    __slots__ = ("application_info", "type", "root_node", "tags", "live_video_playlist", "downloads_playlist")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_UNKNOWN: _ClassVar[PlaylistDocument.Type]
        TYPE_PRESENTATION: _ClassVar[PlaylistDocument.Type]
        TYPE_MEDIA: _ClassVar[PlaylistDocument.Type]
        TYPE_AUDIO: _ClassVar[PlaylistDocument.Type]
    TYPE_UNKNOWN: PlaylistDocument.Type
    TYPE_PRESENTATION: PlaylistDocument.Type
    TYPE_MEDIA: PlaylistDocument.Type
    TYPE_AUDIO: PlaylistDocument.Type
    APPLICATION_INFO_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ROOT_NODE_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    LIVE_VIDEO_PLAYLIST_FIELD_NUMBER: _ClassVar[int]
    DOWNLOADS_PLAYLIST_FIELD_NUMBER: _ClassVar[int]
    application_info: _basicTypes_pb2.ApplicationInfo
    type: PlaylistDocument.Type
    root_node: _playlist_pb2.Playlist
    tags: _containers.RepeatedCompositeFieldContainer[_playlist_pb2.Playlist.Tag]
    live_video_playlist: _playlist_pb2.Playlist
    downloads_playlist: _playlist_pb2.Playlist
    def __init__(self, application_info: _Optional[_Union[_basicTypes_pb2.ApplicationInfo, _Mapping]] = ..., type: _Optional[_Union[PlaylistDocument.Type, str]] = ..., root_node: _Optional[_Union[_playlist_pb2.Playlist, _Mapping]] = ..., tags: _Optional[_Iterable[_Union[_playlist_pb2.Playlist.Tag, _Mapping]]] = ..., live_video_playlist: _Optional[_Union[_playlist_pb2.Playlist, _Mapping]] = ..., downloads_playlist: _Optional[_Union[_playlist_pb2.Playlist, _Mapping]] = ...) -> None: ...

class SettingsDocument(_message.Message):
    __slots__ = ("labels",)
    LABELS_FIELD_NUMBER: _ClassVar[int]
    labels: _containers.RepeatedCompositeFieldContainer[_action_pb2.Action.Label]
    def __init__(self, labels: _Optional[_Iterable[_Union[_action_pb2.Action.Label, _Mapping]]] = ...) -> None: ...
