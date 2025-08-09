import propresenter.pb_auto_generated.basicTypes_pb2 as _basicTypes_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ProAudienceLook(_message.Message):
    __slots__ = ("uuid", "name", "screen_looks", "original_look_uuid")
    class ProScreenLook(_message.Message):
        __slots__ = ("pro_screen_uuid", "props_enabled", "live_video_enabled", "presentation_background_enabled", "template_document_file_path", "template_slide_uuid", "presentation_foreground_enabled", "mask_uuid", "announcements_enabled", "props_layer_enabled", "messages_layer_enabled")
        PRO_SCREEN_UUID_FIELD_NUMBER: _ClassVar[int]
        PROPS_ENABLED_FIELD_NUMBER: _ClassVar[int]
        LIVE_VIDEO_ENABLED_FIELD_NUMBER: _ClassVar[int]
        PRESENTATION_BACKGROUND_ENABLED_FIELD_NUMBER: _ClassVar[int]
        TEMPLATE_DOCUMENT_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
        TEMPLATE_SLIDE_UUID_FIELD_NUMBER: _ClassVar[int]
        PRESENTATION_FOREGROUND_ENABLED_FIELD_NUMBER: _ClassVar[int]
        MASK_UUID_FIELD_NUMBER: _ClassVar[int]
        ANNOUNCEMENTS_ENABLED_FIELD_NUMBER: _ClassVar[int]
        PROPS_LAYER_ENABLED_FIELD_NUMBER: _ClassVar[int]
        MESSAGES_LAYER_ENABLED_FIELD_NUMBER: _ClassVar[int]
        pro_screen_uuid: _basicTypes_pb2.UUID
        props_enabled: bool
        live_video_enabled: bool
        presentation_background_enabled: bool
        template_document_file_path: _basicTypes_pb2.URL
        template_slide_uuid: _basicTypes_pb2.UUID
        presentation_foreground_enabled: bool
        mask_uuid: _basicTypes_pb2.UUID
        announcements_enabled: bool
        props_layer_enabled: bool
        messages_layer_enabled: bool
        def __init__(self, pro_screen_uuid: _Optional[_Union[_basicTypes_pb2.UUID, _Mapping]] = ..., props_enabled: bool = ..., live_video_enabled: bool = ..., presentation_background_enabled: bool = ..., template_document_file_path: _Optional[_Union[_basicTypes_pb2.URL, _Mapping]] = ..., template_slide_uuid: _Optional[_Union[_basicTypes_pb2.UUID, _Mapping]] = ..., presentation_foreground_enabled: bool = ..., mask_uuid: _Optional[_Union[_basicTypes_pb2.UUID, _Mapping]] = ..., announcements_enabled: bool = ..., props_layer_enabled: bool = ..., messages_layer_enabled: bool = ...) -> None: ...
    UUID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SCREEN_LOOKS_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_LOOK_UUID_FIELD_NUMBER: _ClassVar[int]
    uuid: _basicTypes_pb2.UUID
    name: str
    screen_looks: _containers.RepeatedCompositeFieldContainer[ProAudienceLook.ProScreenLook]
    original_look_uuid: _basicTypes_pb2.UUID
    def __init__(self, uuid: _Optional[_Union[_basicTypes_pb2.UUID, _Mapping]] = ..., name: _Optional[str] = ..., screen_looks: _Optional[_Iterable[_Union[ProAudienceLook.ProScreenLook, _Mapping]]] = ..., original_look_uuid: _Optional[_Union[_basicTypes_pb2.UUID, _Mapping]] = ...) -> None: ...
