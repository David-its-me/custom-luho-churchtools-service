import basicTypes_pb2 as _basicTypes_pb2
import action_pb2 as _action_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ClearGroupsDocument(_message.Message):
    __slots__ = ("application_info", "groups")
    class ClearGroup(_message.Message):
        __slots__ = ("uuid", "name", "layer_targets", "is_hidden_in_preview", "image_data", "image_type", "is_icon_tinted", "icon_tint_color", "timeline_targets", "clear_presentation_next_slide")
        class ImageType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            ImageTypeCustom: _ClassVar[ClearGroupsDocument.ClearGroup.ImageType]
            ImageTypeOne: _ClassVar[ClearGroupsDocument.ClearGroup.ImageType]
            ImageTypeTwo: _ClassVar[ClearGroupsDocument.ClearGroup.ImageType]
            ImageTypeThree: _ClassVar[ClearGroupsDocument.ClearGroup.ImageType]
            ImageTypeFour: _ClassVar[ClearGroupsDocument.ClearGroup.ImageType]
            ImageTypeFive: _ClassVar[ClearGroupsDocument.ClearGroup.ImageType]
            ImageTypeSix: _ClassVar[ClearGroupsDocument.ClearGroup.ImageType]
            ImageTypeSeven: _ClassVar[ClearGroupsDocument.ClearGroup.ImageType]
            ImageTypeEight: _ClassVar[ClearGroupsDocument.ClearGroup.ImageType]
            ImageTypeNine: _ClassVar[ClearGroupsDocument.ClearGroup.ImageType]
            ImageTypeZero: _ClassVar[ClearGroupsDocument.ClearGroup.ImageType]
            ImageTypeAll: _ClassVar[ClearGroupsDocument.ClearGroup.ImageType]
            ImageTypeMegahorn: _ClassVar[ClearGroupsDocument.ClearGroup.ImageType]
            ImageTypePlay: _ClassVar[ClearGroupsDocument.ClearGroup.ImageType]
            ImageTypeBulb: _ClassVar[ClearGroupsDocument.ClearGroup.ImageType]
            ImageTypeSunglasses: _ClassVar[ClearGroupsDocument.ClearGroup.ImageType]
            ImageTypeArrow: _ClassVar[ClearGroupsDocument.ClearGroup.ImageType]
            ImageTypeTarget: _ClassVar[ClearGroupsDocument.ClearGroup.ImageType]
            ImageTypeStar: _ClassVar[ClearGroupsDocument.ClearGroup.ImageType]
            ImageTypeSun: _ClassVar[ClearGroupsDocument.ClearGroup.ImageType]
            ImageTypeBell: _ClassVar[ClearGroupsDocument.ClearGroup.ImageType]
            ImageTypePaperclip: _ClassVar[ClearGroupsDocument.ClearGroup.ImageType]
            ImageTypeFlask: _ClassVar[ClearGroupsDocument.ClearGroup.ImageType]
            ImageTypeEyeglasses: _ClassVar[ClearGroupsDocument.ClearGroup.ImageType]
            ImageTypeCupcake: _ClassVar[ClearGroupsDocument.ClearGroup.ImageType]
            ImageTypeSlide: _ClassVar[ClearGroupsDocument.ClearGroup.ImageType]
            ImageTypeHat: _ClassVar[ClearGroupsDocument.ClearGroup.ImageType]
            ImageTypeFlower: _ClassVar[ClearGroupsDocument.ClearGroup.ImageType]
            ImageTypeHeart: _ClassVar[ClearGroupsDocument.ClearGroup.ImageType]
            ImageTypeMessage: _ClassVar[ClearGroupsDocument.ClearGroup.ImageType]
            ImageTypeAudio: _ClassVar[ClearGroupsDocument.ClearGroup.ImageType]
            ImageTypeCloud: _ClassVar[ClearGroupsDocument.ClearGroup.ImageType]
            ImageTypeExclamation: _ClassVar[ClearGroupsDocument.ClearGroup.ImageType]
        ImageTypeCustom: ClearGroupsDocument.ClearGroup.ImageType
        ImageTypeOne: ClearGroupsDocument.ClearGroup.ImageType
        ImageTypeTwo: ClearGroupsDocument.ClearGroup.ImageType
        ImageTypeThree: ClearGroupsDocument.ClearGroup.ImageType
        ImageTypeFour: ClearGroupsDocument.ClearGroup.ImageType
        ImageTypeFive: ClearGroupsDocument.ClearGroup.ImageType
        ImageTypeSix: ClearGroupsDocument.ClearGroup.ImageType
        ImageTypeSeven: ClearGroupsDocument.ClearGroup.ImageType
        ImageTypeEight: ClearGroupsDocument.ClearGroup.ImageType
        ImageTypeNine: ClearGroupsDocument.ClearGroup.ImageType
        ImageTypeZero: ClearGroupsDocument.ClearGroup.ImageType
        ImageTypeAll: ClearGroupsDocument.ClearGroup.ImageType
        ImageTypeMegahorn: ClearGroupsDocument.ClearGroup.ImageType
        ImageTypePlay: ClearGroupsDocument.ClearGroup.ImageType
        ImageTypeBulb: ClearGroupsDocument.ClearGroup.ImageType
        ImageTypeSunglasses: ClearGroupsDocument.ClearGroup.ImageType
        ImageTypeArrow: ClearGroupsDocument.ClearGroup.ImageType
        ImageTypeTarget: ClearGroupsDocument.ClearGroup.ImageType
        ImageTypeStar: ClearGroupsDocument.ClearGroup.ImageType
        ImageTypeSun: ClearGroupsDocument.ClearGroup.ImageType
        ImageTypeBell: ClearGroupsDocument.ClearGroup.ImageType
        ImageTypePaperclip: ClearGroupsDocument.ClearGroup.ImageType
        ImageTypeFlask: ClearGroupsDocument.ClearGroup.ImageType
        ImageTypeEyeglasses: ClearGroupsDocument.ClearGroup.ImageType
        ImageTypeCupcake: ClearGroupsDocument.ClearGroup.ImageType
        ImageTypeSlide: ClearGroupsDocument.ClearGroup.ImageType
        ImageTypeHat: ClearGroupsDocument.ClearGroup.ImageType
        ImageTypeFlower: ClearGroupsDocument.ClearGroup.ImageType
        ImageTypeHeart: ClearGroupsDocument.ClearGroup.ImageType
        ImageTypeMessage: ClearGroupsDocument.ClearGroup.ImageType
        ImageTypeAudio: ClearGroupsDocument.ClearGroup.ImageType
        ImageTypeCloud: ClearGroupsDocument.ClearGroup.ImageType
        ImageTypeExclamation: ClearGroupsDocument.ClearGroup.ImageType
        class ContentDestination(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            CONTENT_DESTINATION_GLOBAL: _ClassVar[ClearGroupsDocument.ClearGroup.ContentDestination]
            CONTENT_DESTINATION_ANNOUNCEMENTS: _ClassVar[ClearGroupsDocument.ClearGroup.ContentDestination]
        CONTENT_DESTINATION_GLOBAL: ClearGroupsDocument.ClearGroup.ContentDestination
        CONTENT_DESTINATION_ANNOUNCEMENTS: ClearGroupsDocument.ClearGroup.ContentDestination
        UUID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        LAYER_TARGETS_FIELD_NUMBER: _ClassVar[int]
        IS_HIDDEN_IN_PREVIEW_FIELD_NUMBER: _ClassVar[int]
        IMAGE_DATA_FIELD_NUMBER: _ClassVar[int]
        IMAGE_TYPE_FIELD_NUMBER: _ClassVar[int]
        IS_ICON_TINTED_FIELD_NUMBER: _ClassVar[int]
        ICON_TINT_COLOR_FIELD_NUMBER: _ClassVar[int]
        TIMELINE_TARGETS_FIELD_NUMBER: _ClassVar[int]
        CLEAR_PRESENTATION_NEXT_SLIDE_FIELD_NUMBER: _ClassVar[int]
        uuid: _basicTypes_pb2.UUID
        name: str
        layer_targets: _containers.RepeatedCompositeFieldContainer[_action_pb2.Action.ClearType]
        is_hidden_in_preview: bool
        image_data: bytes
        image_type: ClearGroupsDocument.ClearGroup.ImageType
        is_icon_tinted: bool
        icon_tint_color: _basicTypes_pb2.Color
        timeline_targets: _containers.RepeatedScalarFieldContainer[ClearGroupsDocument.ClearGroup.ContentDestination]
        clear_presentation_next_slide: bool
        def __init__(self, uuid: _Optional[_Union[_basicTypes_pb2.UUID, _Mapping]] = ..., name: _Optional[str] = ..., layer_targets: _Optional[_Iterable[_Union[_action_pb2.Action.ClearType, _Mapping]]] = ..., is_hidden_in_preview: bool = ..., image_data: _Optional[bytes] = ..., image_type: _Optional[_Union[ClearGroupsDocument.ClearGroup.ImageType, str]] = ..., is_icon_tinted: bool = ..., icon_tint_color: _Optional[_Union[_basicTypes_pb2.Color, _Mapping]] = ..., timeline_targets: _Optional[_Iterable[_Union[ClearGroupsDocument.ClearGroup.ContentDestination, str]]] = ..., clear_presentation_next_slide: bool = ...) -> None: ...
    APPLICATION_INFO_FIELD_NUMBER: _ClassVar[int]
    GROUPS_FIELD_NUMBER: _ClassVar[int]
    application_info: _basicTypes_pb2.ApplicationInfo
    groups: _containers.RepeatedCompositeFieldContainer[ClearGroupsDocument.ClearGroup]
    def __init__(self, application_info: _Optional[_Union[_basicTypes_pb2.ApplicationInfo, _Mapping]] = ..., groups: _Optional[_Iterable[_Union[ClearGroupsDocument.ClearGroup, _Mapping]]] = ...) -> None: ...
