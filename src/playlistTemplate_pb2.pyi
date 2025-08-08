import playlist_pb2 as _playlist_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PlaylistTemplate(_message.Message):
    __slots__ = ("templates",)
    class Template(_message.Message):
        __slots__ = ("name", "playlist_items")
        NAME_FIELD_NUMBER: _ClassVar[int]
        PLAYLIST_ITEMS_FIELD_NUMBER: _ClassVar[int]
        name: str
        playlist_items: _containers.RepeatedCompositeFieldContainer[_playlist_pb2.PlaylistItem]
        def __init__(self, name: _Optional[str] = ..., playlist_items: _Optional[_Iterable[_Union[_playlist_pb2.PlaylistItem, _Mapping]]] = ...) -> None: ...
    TEMPLATES_FIELD_NUMBER: _ClassVar[int]
    templates: _containers.RepeatedCompositeFieldContainer[PlaylistTemplate.Template]
    def __init__(self, templates: _Optional[_Iterable[_Union[PlaylistTemplate.Template, _Mapping]]] = ...) -> None: ...
