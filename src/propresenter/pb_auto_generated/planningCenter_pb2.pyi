import propresenter.pb_auto_generated.basicTypes_pb2 as _basicTypes_pb2
import propresenter.pb_auto_generated.rvtimestamp_pb2 as _rvtimestamp_pb2
import propresenter.pb_auto_generated.presentation_pb2 as _presentation_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PlanningCenterPlan(_message.Message):
    __slots__ = ("plan_id_num", "parent_id_num", "series_title", "plan_title", "date_list", "created_date", "update_date", "last_update_check_date", "plan_id_str", "parent_id_str")
    class PlanItem(_message.Message):
        __slots__ = ("item_type", "pco_id_num", "service_id_num", "parent_id_num", "name", "attachments", "update_date", "linked_song", "pco_id_str", "service_id_str", "parent_id_str")
        class PlanItemType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            PLAN_ITEM_TYPE_ITEM: _ClassVar[PlanningCenterPlan.PlanItem.PlanItemType]
            PLAN_ITEM_TYPE_SONG: _ClassVar[PlanningCenterPlan.PlanItem.PlanItemType]
            PLAN_ITEM_TYPE_MEDIA: _ClassVar[PlanningCenterPlan.PlanItem.PlanItemType]
            PLAN_ITEM_TYPE_HEADER: _ClassVar[PlanningCenterPlan.PlanItem.PlanItemType]
        PLAN_ITEM_TYPE_ITEM: PlanningCenterPlan.PlanItem.PlanItemType
        PLAN_ITEM_TYPE_SONG: PlanningCenterPlan.PlanItem.PlanItemType
        PLAN_ITEM_TYPE_MEDIA: PlanningCenterPlan.PlanItem.PlanItemType
        PLAN_ITEM_TYPE_HEADER: PlanningCenterPlan.PlanItem.PlanItemType
        class Attachment(_message.Message):
            __slots__ = ("name", "url", "created_date", "linked_path", "pco_id_num", "needs_update", "update_date", "pco_id_str")
            NAME_FIELD_NUMBER: _ClassVar[int]
            URL_FIELD_NUMBER: _ClassVar[int]
            CREATED_DATE_FIELD_NUMBER: _ClassVar[int]
            LINKED_PATH_FIELD_NUMBER: _ClassVar[int]
            PCO_ID_NUM_FIELD_NUMBER: _ClassVar[int]
            NEEDS_UPDATE_FIELD_NUMBER: _ClassVar[int]
            UPDATE_DATE_FIELD_NUMBER: _ClassVar[int]
            PCO_ID_STR_FIELD_NUMBER: _ClassVar[int]
            name: str
            url: _basicTypes_pb2.URL
            created_date: _rvtimestamp_pb2.Timestamp
            linked_path: _basicTypes_pb2.URL
            pco_id_num: int
            needs_update: bool
            update_date: _rvtimestamp_pb2.Timestamp
            pco_id_str: str
            def __init__(self, name: _Optional[str] = ..., url: _Optional[_Union[_basicTypes_pb2.URL, _Mapping]] = ..., created_date: _Optional[_Union[_rvtimestamp_pb2.Timestamp, _Mapping]] = ..., linked_path: _Optional[_Union[_basicTypes_pb2.URL, _Mapping]] = ..., pco_id_num: _Optional[int] = ..., needs_update: bool = ..., update_date: _Optional[_Union[_rvtimestamp_pb2.Timestamp, _Mapping]] = ..., pco_id_str: _Optional[str] = ...) -> None: ...
        class SongItem(_message.Message):
            __slots__ = ("pco_id_num", "arrangement_id_num", "ccli", "sequence", "pco_id_str", "arrangement_id_str")
            class Sequence(_message.Message):
                __slots__ = ("pco_id_num", "name", "group_names", "pco_id_str")
                PCO_ID_NUM_FIELD_NUMBER: _ClassVar[int]
                NAME_FIELD_NUMBER: _ClassVar[int]
                GROUP_NAMES_FIELD_NUMBER: _ClassVar[int]
                PCO_ID_STR_FIELD_NUMBER: _ClassVar[int]
                pco_id_num: int
                name: str
                group_names: _containers.RepeatedScalarFieldContainer[str]
                pco_id_str: str
                def __init__(self, pco_id_num: _Optional[int] = ..., name: _Optional[str] = ..., group_names: _Optional[_Iterable[str]] = ..., pco_id_str: _Optional[str] = ...) -> None: ...
            PCO_ID_NUM_FIELD_NUMBER: _ClassVar[int]
            ARRANGEMENT_ID_NUM_FIELD_NUMBER: _ClassVar[int]
            CCLI_FIELD_NUMBER: _ClassVar[int]
            SEQUENCE_FIELD_NUMBER: _ClassVar[int]
            PCO_ID_STR_FIELD_NUMBER: _ClassVar[int]
            ARRANGEMENT_ID_STR_FIELD_NUMBER: _ClassVar[int]
            pco_id_num: int
            arrangement_id_num: int
            ccli: _presentation_pb2.Presentation.CCLI
            sequence: PlanningCenterPlan.PlanItem.SongItem.Sequence
            pco_id_str: str
            arrangement_id_str: str
            def __init__(self, pco_id_num: _Optional[int] = ..., arrangement_id_num: _Optional[int] = ..., ccli: _Optional[_Union[_presentation_pb2.Presentation.CCLI, _Mapping]] = ..., sequence: _Optional[_Union[PlanningCenterPlan.PlanItem.SongItem.Sequence, _Mapping]] = ..., pco_id_str: _Optional[str] = ..., arrangement_id_str: _Optional[str] = ...) -> None: ...
        ITEM_TYPE_FIELD_NUMBER: _ClassVar[int]
        PCO_ID_NUM_FIELD_NUMBER: _ClassVar[int]
        SERVICE_ID_NUM_FIELD_NUMBER: _ClassVar[int]
        PARENT_ID_NUM_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        ATTACHMENTS_FIELD_NUMBER: _ClassVar[int]
        UPDATE_DATE_FIELD_NUMBER: _ClassVar[int]
        LINKED_SONG_FIELD_NUMBER: _ClassVar[int]
        PCO_ID_STR_FIELD_NUMBER: _ClassVar[int]
        SERVICE_ID_STR_FIELD_NUMBER: _ClassVar[int]
        PARENT_ID_STR_FIELD_NUMBER: _ClassVar[int]
        item_type: PlanningCenterPlan.PlanItem.PlanItemType
        pco_id_num: int
        service_id_num: int
        parent_id_num: int
        name: str
        attachments: _containers.RepeatedCompositeFieldContainer[PlanningCenterPlan.PlanItem.Attachment]
        update_date: _rvtimestamp_pb2.Timestamp
        linked_song: PlanningCenterPlan.PlanItem.SongItem
        pco_id_str: str
        service_id_str: str
        parent_id_str: str
        def __init__(self, item_type: _Optional[_Union[PlanningCenterPlan.PlanItem.PlanItemType, str]] = ..., pco_id_num: _Optional[int] = ..., service_id_num: _Optional[int] = ..., parent_id_num: _Optional[int] = ..., name: _Optional[str] = ..., attachments: _Optional[_Iterable[_Union[PlanningCenterPlan.PlanItem.Attachment, _Mapping]]] = ..., update_date: _Optional[_Union[_rvtimestamp_pb2.Timestamp, _Mapping]] = ..., linked_song: _Optional[_Union[PlanningCenterPlan.PlanItem.SongItem, _Mapping]] = ..., pco_id_str: _Optional[str] = ..., service_id_str: _Optional[str] = ..., parent_id_str: _Optional[str] = ...) -> None: ...
    PLAN_ID_NUM_FIELD_NUMBER: _ClassVar[int]
    PARENT_ID_NUM_FIELD_NUMBER: _ClassVar[int]
    SERIES_TITLE_FIELD_NUMBER: _ClassVar[int]
    PLAN_TITLE_FIELD_NUMBER: _ClassVar[int]
    DATE_LIST_FIELD_NUMBER: _ClassVar[int]
    CREATED_DATE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_DATE_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATE_CHECK_DATE_FIELD_NUMBER: _ClassVar[int]
    PLAN_ID_STR_FIELD_NUMBER: _ClassVar[int]
    PARENT_ID_STR_FIELD_NUMBER: _ClassVar[int]
    plan_id_num: int
    parent_id_num: int
    series_title: str
    plan_title: str
    date_list: str
    created_date: _rvtimestamp_pb2.Timestamp
    update_date: _rvtimestamp_pb2.Timestamp
    last_update_check_date: _rvtimestamp_pb2.Timestamp
    plan_id_str: str
    parent_id_str: str
    def __init__(self, plan_id_num: _Optional[int] = ..., parent_id_num: _Optional[int] = ..., series_title: _Optional[str] = ..., plan_title: _Optional[str] = ..., date_list: _Optional[str] = ..., created_date: _Optional[_Union[_rvtimestamp_pb2.Timestamp, _Mapping]] = ..., update_date: _Optional[_Union[_rvtimestamp_pb2.Timestamp, _Mapping]] = ..., last_update_check_date: _Optional[_Union[_rvtimestamp_pb2.Timestamp, _Mapping]] = ..., plan_id_str: _Optional[str] = ..., parent_id_str: _Optional[str] = ...) -> None: ...
