import slide_pb2 as _slide_pb2
import basicTypes_pb2 as _basicTypes_pb2
import alignmentGuide_pb2 as _alignmentGuide_pb2
import effects_pb2 as _effects_pb2
import graphicsData_pb2 as _graphicsData_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PresentationSlide(_message.Message):
    __slots__ = ("base_slide", "notes", "template_guidelines", "chord_chart", "transition")
    class Notes(_message.Message):
        __slots__ = ("rtf_data", "attributes")
        RTF_DATA_FIELD_NUMBER: _ClassVar[int]
        ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
        rtf_data: bytes
        attributes: _graphicsData_pb2.Graphics.Text.Attributes
        def __init__(self, rtf_data: _Optional[bytes] = ..., attributes: _Optional[_Union[_graphicsData_pb2.Graphics.Text.Attributes, _Mapping]] = ...) -> None: ...
    BASE_SLIDE_FIELD_NUMBER: _ClassVar[int]
    NOTES_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_GUIDELINES_FIELD_NUMBER: _ClassVar[int]
    CHORD_CHART_FIELD_NUMBER: _ClassVar[int]
    TRANSITION_FIELD_NUMBER: _ClassVar[int]
    base_slide: _slide_pb2.Slide
    notes: PresentationSlide.Notes
    template_guidelines: _containers.RepeatedCompositeFieldContainer[_alignmentGuide_pb2.AlignmentGuide]
    chord_chart: _basicTypes_pb2.URL
    transition: _effects_pb2.Transition
    def __init__(self, base_slide: _Optional[_Union[_slide_pb2.Slide, _Mapping]] = ..., notes: _Optional[_Union[PresentationSlide.Notes, _Mapping]] = ..., template_guidelines: _Optional[_Iterable[_Union[_alignmentGuide_pb2.AlignmentGuide, _Mapping]]] = ..., chord_chart: _Optional[_Union[_basicTypes_pb2.URL, _Mapping]] = ..., transition: _Optional[_Union[_effects_pb2.Transition, _Mapping]] = ...) -> None: ...
