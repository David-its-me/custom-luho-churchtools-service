import propresenter.pb_auto_generated.slide_pb2 as _slide_pb2
import propresenter.pb_auto_generated.effects_pb2 as _effects_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PropSlide(_message.Message):
    __slots__ = ("base_slide", "transition")
    BASE_SLIDE_FIELD_NUMBER: _ClassVar[int]
    TRANSITION_FIELD_NUMBER: _ClassVar[int]
    base_slide: _slide_pb2.Slide
    transition: _effects_pb2.Transition
    def __init__(self, base_slide: _Optional[_Union[_slide_pb2.Slide, _Mapping]] = ..., transition: _Optional[_Union[_effects_pb2.Transition, _Mapping]] = ...) -> None: ...
