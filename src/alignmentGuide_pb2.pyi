import basicTypes_pb2 as _basicTypes_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AlignmentGuide(_message.Message):
    __slots__ = ("uuid", "orientation", "location")
    class GuidelineOrientation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        GUIDELINE_ORIENTATION_HORIZONTAL: _ClassVar[AlignmentGuide.GuidelineOrientation]
        GUIDELINE_ORIENTATION_VERTICAL: _ClassVar[AlignmentGuide.GuidelineOrientation]
    GUIDELINE_ORIENTATION_HORIZONTAL: AlignmentGuide.GuidelineOrientation
    GUIDELINE_ORIENTATION_VERTICAL: AlignmentGuide.GuidelineOrientation
    UUID_FIELD_NUMBER: _ClassVar[int]
    ORIENTATION_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    uuid: _basicTypes_pb2.UUID
    orientation: AlignmentGuide.GuidelineOrientation
    location: float
    def __init__(self, uuid: _Optional[_Union[_basicTypes_pb2.UUID, _Mapping]] = ..., orientation: _Optional[_Union[AlignmentGuide.GuidelineOrientation, str]] = ..., location: _Optional[float] = ...) -> None: ...
