import basicTypes_pb2 as _basicTypes_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TemplateIdentification(_message.Message):
    __slots__ = ("uuid", "name", "slide_uuid", "slide_name", "slide_index")
    UUID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SLIDE_UUID_FIELD_NUMBER: _ClassVar[int]
    SLIDE_NAME_FIELD_NUMBER: _ClassVar[int]
    SLIDE_INDEX_FIELD_NUMBER: _ClassVar[int]
    uuid: _basicTypes_pb2.UUID
    name: str
    slide_uuid: _basicTypes_pb2.UUID
    slide_name: str
    slide_index: int
    def __init__(self, uuid: _Optional[_Union[_basicTypes_pb2.UUID, _Mapping]] = ..., name: _Optional[str] = ..., slide_uuid: _Optional[_Union[_basicTypes_pb2.UUID, _Mapping]] = ..., slide_name: _Optional[str] = ..., slide_index: _Optional[int] = ...) -> None: ...
