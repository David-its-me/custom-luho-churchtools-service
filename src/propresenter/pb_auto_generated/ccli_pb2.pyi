import propresenter.pb_auto_generated.basicTypes_pb2 as _basicTypes_pb2
import propresenter.pb_auto_generated.template_pb2 as _template_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CCLIDocument(_message.Message):
    __slots__ = ("application_info", "enable_ccli_display", "ccli_license", "display_type", "template")
    class DisplayType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DISPLAY_TYPE_FIRST_SLIDE: _ClassVar[CCLIDocument.DisplayType]
        DISPLAY_TYPE_LAST_SLIDE: _ClassVar[CCLIDocument.DisplayType]
        DISPLAY_TYPE_FIRST_AND_LAST_SLIDE: _ClassVar[CCLIDocument.DisplayType]
        DISPLAY_TYPE_ALL_SLIDES: _ClassVar[CCLIDocument.DisplayType]
    DISPLAY_TYPE_FIRST_SLIDE: CCLIDocument.DisplayType
    DISPLAY_TYPE_LAST_SLIDE: CCLIDocument.DisplayType
    DISPLAY_TYPE_FIRST_AND_LAST_SLIDE: CCLIDocument.DisplayType
    DISPLAY_TYPE_ALL_SLIDES: CCLIDocument.DisplayType
    APPLICATION_INFO_FIELD_NUMBER: _ClassVar[int]
    ENABLE_CCLI_DISPLAY_FIELD_NUMBER: _ClassVar[int]
    CCLI_LICENSE_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_TYPE_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    application_info: _basicTypes_pb2.ApplicationInfo
    enable_ccli_display: bool
    ccli_license: str
    display_type: CCLIDocument.DisplayType
    template: _template_pb2.Template.Slide
    def __init__(self, application_info: _Optional[_Union[_basicTypes_pb2.ApplicationInfo, _Mapping]] = ..., enable_ccli_display: bool = ..., ccli_license: _Optional[str] = ..., display_type: _Optional[_Union[CCLIDocument.DisplayType, str]] = ..., template: _Optional[_Union[_template_pb2.Template.Slide, _Mapping]] = ...) -> None: ...
