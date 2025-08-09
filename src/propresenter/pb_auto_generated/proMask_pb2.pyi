import propresenter.pb_auto_generated.slide_pb2 as _slide_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ProMask(_message.Message):
    __slots__ = ("base_slide", "name")
    BASE_SLIDE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    base_slide: _slide_pb2.Slide
    name: str
    def __init__(self, base_slide: _Optional[_Union[_slide_pb2.Slide, _Mapping]] = ..., name: _Optional[str] = ...) -> None: ...
