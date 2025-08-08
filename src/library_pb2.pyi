import basicTypes_pb2 as _basicTypes_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Library(_message.Message):
    __slots__ = ("url", "libraryChildren", "libraryItems")
    class LibraryArray(_message.Message):
        __slots__ = ("libraries",)
        LIBRARIES_FIELD_NUMBER: _ClassVar[int]
        libraries: _containers.RepeatedCompositeFieldContainer[Library]
        def __init__(self, libraries: _Optional[_Iterable[_Union[Library, _Mapping]]] = ...) -> None: ...
    class LibraryItems(_message.Message):
        __slots__ = ("items",)
        ITEMS_FIELD_NUMBER: _ClassVar[int]
        items: _containers.RepeatedCompositeFieldContainer[LibraryItem]
        def __init__(self, items: _Optional[_Iterable[_Union[LibraryItem, _Mapping]]] = ...) -> None: ...
    URL_FIELD_NUMBER: _ClassVar[int]
    LIBRARYCHILDREN_FIELD_NUMBER: _ClassVar[int]
    LIBRARYITEMS_FIELD_NUMBER: _ClassVar[int]
    url: _basicTypes_pb2.URL
    libraryChildren: Library.LibraryArray
    libraryItems: Library.LibraryItems
    def __init__(self, url: _Optional[_Union[_basicTypes_pb2.URL, _Mapping]] = ..., libraryChildren: _Optional[_Union[Library.LibraryArray, _Mapping]] = ..., libraryItems: _Optional[_Union[Library.LibraryItems, _Mapping]] = ...) -> None: ...

class LibraryItem(_message.Message):
    __slots__ = ("url",)
    URL_FIELD_NUMBER: _ClassVar[int]
    url: _basicTypes_pb2.URL
    def __init__(self, url: _Optional[_Union[_basicTypes_pb2.URL, _Mapping]] = ...) -> None: ...
