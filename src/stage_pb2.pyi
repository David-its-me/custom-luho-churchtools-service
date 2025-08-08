import basicTypes_pb2 as _basicTypes_pb2
import slide_pb2 as _slide_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Stage(_message.Message):
    __slots__ = ()
    class Layout(_message.Message):
        __slots__ = ("uuid", "name", "slide")
        UUID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        SLIDE_FIELD_NUMBER: _ClassVar[int]
        uuid: _basicTypes_pb2.UUID
        name: str
        slide: _slide_pb2.Slide
        def __init__(self, uuid: _Optional[_Union[_basicTypes_pb2.UUID, _Mapping]] = ..., name: _Optional[str] = ..., slide: _Optional[_Union[_slide_pb2.Slide, _Mapping]] = ...) -> None: ...
    class Document(_message.Message):
        __slots__ = ("application_info", "layouts")
        APPLICATION_INFO_FIELD_NUMBER: _ClassVar[int]
        LAYOUTS_FIELD_NUMBER: _ClassVar[int]
        application_info: _basicTypes_pb2.ApplicationInfo
        layouts: _containers.RepeatedCompositeFieldContainer[Stage.Layout]
        def __init__(self, application_info: _Optional[_Union[_basicTypes_pb2.ApplicationInfo, _Mapping]] = ..., layouts: _Optional[_Iterable[_Union[Stage.Layout, _Mapping]]] = ...) -> None: ...
    class ScreenAssignment(_message.Message):
        __slots__ = ("screen", "layout")
        SCREEN_FIELD_NUMBER: _ClassVar[int]
        LAYOUT_FIELD_NUMBER: _ClassVar[int]
        screen: _basicTypes_pb2.CollectionElementType
        layout: _basicTypes_pb2.CollectionElementType
        def __init__(self, screen: _Optional[_Union[_basicTypes_pb2.CollectionElementType, _Mapping]] = ..., layout: _Optional[_Union[_basicTypes_pb2.CollectionElementType, _Mapping]] = ...) -> None: ...
    def __init__(self) -> None: ...
