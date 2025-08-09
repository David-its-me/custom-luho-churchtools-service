import propresenter.pb_auto_generated.basicTypes_pb2 as _basicTypes_pb2
import propresenter.pb_auto_generated.proApiV1BasicTypes_pb2 as _proApiV1BasicTypes_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NetworkAPI_v1(_message.Message):
    __slots__ = ("action",)
    class Action(_message.Message):
        __slots__ = ("audio_request", "capture_request", "clearing_request", "groups_request", "link_request", "library_request", "looks_request", "macro_request", "masks_request", "media_request", "message_request", "miscellaneous_request", "playlist_request", "preroll_request", "presentation_request", "prop_request", "stage_request", "status_request", "theme_request", "timer_request", "transport_request", "trigger_request", "video_inputs_request", "announcement_request", "audio_response", "capture_response", "clearing_response", "groups_response", "link_response", "library_response", "looks_response", "macro_response", "masks_response", "media_response", "message_response", "miscellaneous_response", "playlist_response", "preroll_response", "presentation_response", "prop_response", "stage_response", "status_response", "theme_response", "timer_response", "transport_response", "trigger_response", "video_inputs_response", "announcement_response", "error_response", "update_identifier")
        AUDIO_REQUEST_FIELD_NUMBER: _ClassVar[int]
        CAPTURE_REQUEST_FIELD_NUMBER: _ClassVar[int]
        CLEARING_REQUEST_FIELD_NUMBER: _ClassVar[int]
        GROUPS_REQUEST_FIELD_NUMBER: _ClassVar[int]
        LINK_REQUEST_FIELD_NUMBER: _ClassVar[int]
        LIBRARY_REQUEST_FIELD_NUMBER: _ClassVar[int]
        LOOKS_REQUEST_FIELD_NUMBER: _ClassVar[int]
        MACRO_REQUEST_FIELD_NUMBER: _ClassVar[int]
        MASKS_REQUEST_FIELD_NUMBER: _ClassVar[int]
        MEDIA_REQUEST_FIELD_NUMBER: _ClassVar[int]
        MESSAGE_REQUEST_FIELD_NUMBER: _ClassVar[int]
        MISCELLANEOUS_REQUEST_FIELD_NUMBER: _ClassVar[int]
        PLAYLIST_REQUEST_FIELD_NUMBER: _ClassVar[int]
        PREROLL_REQUEST_FIELD_NUMBER: _ClassVar[int]
        PRESENTATION_REQUEST_FIELD_NUMBER: _ClassVar[int]
        PROP_REQUEST_FIELD_NUMBER: _ClassVar[int]
        STAGE_REQUEST_FIELD_NUMBER: _ClassVar[int]
        STATUS_REQUEST_FIELD_NUMBER: _ClassVar[int]
        THEME_REQUEST_FIELD_NUMBER: _ClassVar[int]
        TIMER_REQUEST_FIELD_NUMBER: _ClassVar[int]
        TRANSPORT_REQUEST_FIELD_NUMBER: _ClassVar[int]
        TRIGGER_REQUEST_FIELD_NUMBER: _ClassVar[int]
        VIDEO_INPUTS_REQUEST_FIELD_NUMBER: _ClassVar[int]
        ANNOUNCEMENT_REQUEST_FIELD_NUMBER: _ClassVar[int]
        AUDIO_RESPONSE_FIELD_NUMBER: _ClassVar[int]
        CAPTURE_RESPONSE_FIELD_NUMBER: _ClassVar[int]
        CLEARING_RESPONSE_FIELD_NUMBER: _ClassVar[int]
        GROUPS_RESPONSE_FIELD_NUMBER: _ClassVar[int]
        LINK_RESPONSE_FIELD_NUMBER: _ClassVar[int]
        LIBRARY_RESPONSE_FIELD_NUMBER: _ClassVar[int]
        LOOKS_RESPONSE_FIELD_NUMBER: _ClassVar[int]
        MACRO_RESPONSE_FIELD_NUMBER: _ClassVar[int]
        MASKS_RESPONSE_FIELD_NUMBER: _ClassVar[int]
        MEDIA_RESPONSE_FIELD_NUMBER: _ClassVar[int]
        MESSAGE_RESPONSE_FIELD_NUMBER: _ClassVar[int]
        MISCELLANEOUS_RESPONSE_FIELD_NUMBER: _ClassVar[int]
        PLAYLIST_RESPONSE_FIELD_NUMBER: _ClassVar[int]
        PREROLL_RESPONSE_FIELD_NUMBER: _ClassVar[int]
        PRESENTATION_RESPONSE_FIELD_NUMBER: _ClassVar[int]
        PROP_RESPONSE_FIELD_NUMBER: _ClassVar[int]
        STAGE_RESPONSE_FIELD_NUMBER: _ClassVar[int]
        STATUS_RESPONSE_FIELD_NUMBER: _ClassVar[int]
        THEME_RESPONSE_FIELD_NUMBER: _ClassVar[int]
        TIMER_RESPONSE_FIELD_NUMBER: _ClassVar[int]
        TRANSPORT_RESPONSE_FIELD_NUMBER: _ClassVar[int]
        TRIGGER_RESPONSE_FIELD_NUMBER: _ClassVar[int]
        VIDEO_INPUTS_RESPONSE_FIELD_NUMBER: _ClassVar[int]
        ANNOUNCEMENT_RESPONSE_FIELD_NUMBER: _ClassVar[int]
        ERROR_RESPONSE_FIELD_NUMBER: _ClassVar[int]
        UPDATE_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
        audio_request: NetworkAPI_v1.API_v1_Audio_Request
        capture_request: NetworkAPI_v1.API_v1_Capture_Request
        clearing_request: NetworkAPI_v1.API_v1_Clear_Request
        groups_request: NetworkAPI_v1.API_v1_Groups_Request
        link_request: NetworkAPI_v1.API_v1_Link_Request
        library_request: NetworkAPI_v1.API_v1_Library_Request
        looks_request: NetworkAPI_v1.API_v1_Looks_Request
        macro_request: NetworkAPI_v1.API_v1_Macro_Request
        masks_request: NetworkAPI_v1.API_v1_Masks_Request
        media_request: NetworkAPI_v1.API_v1_Media_Request
        message_request: NetworkAPI_v1.API_v1_Message_Request
        miscellaneous_request: NetworkAPI_v1.API_v1_Miscellaneous_Request
        playlist_request: NetworkAPI_v1.API_v1_Playlist_Request
        preroll_request: NetworkAPI_v1.API_v1_Preroll_Request
        presentation_request: NetworkAPI_v1.API_v1_Presentation_Request
        prop_request: NetworkAPI_v1.API_v1_Prop_Request
        stage_request: NetworkAPI_v1.API_v1_Stage_Request
        status_request: NetworkAPI_v1.API_v1_Status_Request
        theme_request: NetworkAPI_v1.API_v1_Theme_Request
        timer_request: NetworkAPI_v1.API_v1_Timer_Request
        transport_request: NetworkAPI_v1.API_v1_Transport_Request
        trigger_request: NetworkAPI_v1.API_v1_Trigger_Request
        video_inputs_request: NetworkAPI_v1.API_v1_Video_Inputs_Request
        announcement_request: NetworkAPI_v1.API_v1_Announcement_Request
        audio_response: NetworkAPI_v1.API_v1_Audio_Response
        capture_response: NetworkAPI_v1.API_v1_Capture_Response
        clearing_response: NetworkAPI_v1.API_v1_Clear_Response
        groups_response: NetworkAPI_v1.API_v1_Groups_Response
        link_response: NetworkAPI_v1.API_v1_Link_Response
        library_response: NetworkAPI_v1.API_v1_Library_Response
        looks_response: NetworkAPI_v1.API_v1_Looks_Response
        macro_response: NetworkAPI_v1.API_v1_Macro_Response
        masks_response: NetworkAPI_v1.API_v1_Masks_Response
        media_response: NetworkAPI_v1.API_v1_Media_Response
        message_response: NetworkAPI_v1.API_v1_Message_Response
        miscellaneous_response: NetworkAPI_v1.API_v1_Miscellaneous_Response
        playlist_response: NetworkAPI_v1.API_v1_Playlist_Response
        preroll_response: NetworkAPI_v1.API_v1_Preroll_Response
        presentation_response: NetworkAPI_v1.API_v1_Presentation_Response
        prop_response: NetworkAPI_v1.API_v1_Prop_Response
        stage_response: NetworkAPI_v1.API_v1_Stage_Response
        status_response: NetworkAPI_v1.API_v1_Status_Response
        theme_response: NetworkAPI_v1.API_v1_Theme_Response
        timer_response: NetworkAPI_v1.API_v1_Timer_Response
        transport_response: NetworkAPI_v1.API_v1_Transport_Response
        trigger_response: NetworkAPI_v1.API_v1_Trigger_Response
        video_inputs_response: NetworkAPI_v1.API_v1_Video_Inputs_Response
        announcement_response: NetworkAPI_v1.API_v1_Announcement_Response
        error_response: _proApiV1BasicTypes_pb2.API_v1_Error_Response
        update_identifier: str
        def __init__(self, audio_request: _Optional[_Union[NetworkAPI_v1.API_v1_Audio_Request, _Mapping]] = ..., capture_request: _Optional[_Union[NetworkAPI_v1.API_v1_Capture_Request, _Mapping]] = ..., clearing_request: _Optional[_Union[NetworkAPI_v1.API_v1_Clear_Request, _Mapping]] = ..., groups_request: _Optional[_Union[NetworkAPI_v1.API_v1_Groups_Request, _Mapping]] = ..., link_request: _Optional[_Union[NetworkAPI_v1.API_v1_Link_Request, _Mapping]] = ..., library_request: _Optional[_Union[NetworkAPI_v1.API_v1_Library_Request, _Mapping]] = ..., looks_request: _Optional[_Union[NetworkAPI_v1.API_v1_Looks_Request, _Mapping]] = ..., macro_request: _Optional[_Union[NetworkAPI_v1.API_v1_Macro_Request, _Mapping]] = ..., masks_request: _Optional[_Union[NetworkAPI_v1.API_v1_Masks_Request, _Mapping]] = ..., media_request: _Optional[_Union[NetworkAPI_v1.API_v1_Media_Request, _Mapping]] = ..., message_request: _Optional[_Union[NetworkAPI_v1.API_v1_Message_Request, _Mapping]] = ..., miscellaneous_request: _Optional[_Union[NetworkAPI_v1.API_v1_Miscellaneous_Request, _Mapping]] = ..., playlist_request: _Optional[_Union[NetworkAPI_v1.API_v1_Playlist_Request, _Mapping]] = ..., preroll_request: _Optional[_Union[NetworkAPI_v1.API_v1_Preroll_Request, _Mapping]] = ..., presentation_request: _Optional[_Union[NetworkAPI_v1.API_v1_Presentation_Request, _Mapping]] = ..., prop_request: _Optional[_Union[NetworkAPI_v1.API_v1_Prop_Request, _Mapping]] = ..., stage_request: _Optional[_Union[NetworkAPI_v1.API_v1_Stage_Request, _Mapping]] = ..., status_request: _Optional[_Union[NetworkAPI_v1.API_v1_Status_Request, _Mapping]] = ..., theme_request: _Optional[_Union[NetworkAPI_v1.API_v1_Theme_Request, _Mapping]] = ..., timer_request: _Optional[_Union[NetworkAPI_v1.API_v1_Timer_Request, _Mapping]] = ..., transport_request: _Optional[_Union[NetworkAPI_v1.API_v1_Transport_Request, _Mapping]] = ..., trigger_request: _Optional[_Union[NetworkAPI_v1.API_v1_Trigger_Request, _Mapping]] = ..., video_inputs_request: _Optional[_Union[NetworkAPI_v1.API_v1_Video_Inputs_Request, _Mapping]] = ..., announcement_request: _Optional[_Union[NetworkAPI_v1.API_v1_Announcement_Request, _Mapping]] = ..., audio_response: _Optional[_Union[NetworkAPI_v1.API_v1_Audio_Response, _Mapping]] = ..., capture_response: _Optional[_Union[NetworkAPI_v1.API_v1_Capture_Response, _Mapping]] = ..., clearing_response: _Optional[_Union[NetworkAPI_v1.API_v1_Clear_Response, _Mapping]] = ..., groups_response: _Optional[_Union[NetworkAPI_v1.API_v1_Groups_Response, _Mapping]] = ..., link_response: _Optional[_Union[NetworkAPI_v1.API_v1_Link_Response, _Mapping]] = ..., library_response: _Optional[_Union[NetworkAPI_v1.API_v1_Library_Response, _Mapping]] = ..., looks_response: _Optional[_Union[NetworkAPI_v1.API_v1_Looks_Response, _Mapping]] = ..., macro_response: _Optional[_Union[NetworkAPI_v1.API_v1_Macro_Response, _Mapping]] = ..., masks_response: _Optional[_Union[NetworkAPI_v1.API_v1_Masks_Response, _Mapping]] = ..., media_response: _Optional[_Union[NetworkAPI_v1.API_v1_Media_Response, _Mapping]] = ..., message_response: _Optional[_Union[NetworkAPI_v1.API_v1_Message_Response, _Mapping]] = ..., miscellaneous_response: _Optional[_Union[NetworkAPI_v1.API_v1_Miscellaneous_Response, _Mapping]] = ..., playlist_response: _Optional[_Union[NetworkAPI_v1.API_v1_Playlist_Response, _Mapping]] = ..., preroll_response: _Optional[_Union[NetworkAPI_v1.API_v1_Preroll_Response, _Mapping]] = ..., presentation_response: _Optional[_Union[NetworkAPI_v1.API_v1_Presentation_Response, _Mapping]] = ..., prop_response: _Optional[_Union[NetworkAPI_v1.API_v1_Prop_Response, _Mapping]] = ..., stage_response: _Optional[_Union[NetworkAPI_v1.API_v1_Stage_Response, _Mapping]] = ..., status_response: _Optional[_Union[NetworkAPI_v1.API_v1_Status_Response, _Mapping]] = ..., theme_response: _Optional[_Union[NetworkAPI_v1.API_v1_Theme_Response, _Mapping]] = ..., timer_response: _Optional[_Union[NetworkAPI_v1.API_v1_Timer_Response, _Mapping]] = ..., transport_response: _Optional[_Union[NetworkAPI_v1.API_v1_Transport_Response, _Mapping]] = ..., trigger_response: _Optional[_Union[NetworkAPI_v1.API_v1_Trigger_Response, _Mapping]] = ..., video_inputs_response: _Optional[_Union[NetworkAPI_v1.API_v1_Video_Inputs_Response, _Mapping]] = ..., announcement_response: _Optional[_Union[NetworkAPI_v1.API_v1_Announcement_Response, _Mapping]] = ..., error_response: _Optional[_Union[_proApiV1BasicTypes_pb2.API_v1_Error_Response, _Mapping]] = ..., update_identifier: _Optional[str] = ...) -> None: ...
    class API_v1_Announcement_Request(_message.Message):
        __slots__ = ("active_timeline_operation", "active_timeline_status", "active", "slide_index", "active_focus", "active_trigger", "active_next_trigger", "active_previous_trigger", "active_index_trigger")
        class ActiveTimelineOperation(_message.Message):
            __slots__ = ("operation",)
            class API_v1_TimelineOperation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                play: _ClassVar[NetworkAPI_v1.API_v1_Announcement_Request.ActiveTimelineOperation.API_v1_TimelineOperation]
                pause: _ClassVar[NetworkAPI_v1.API_v1_Announcement_Request.ActiveTimelineOperation.API_v1_TimelineOperation]
                rewind: _ClassVar[NetworkAPI_v1.API_v1_Announcement_Request.ActiveTimelineOperation.API_v1_TimelineOperation]
            play: NetworkAPI_v1.API_v1_Announcement_Request.ActiveTimelineOperation.API_v1_TimelineOperation
            pause: NetworkAPI_v1.API_v1_Announcement_Request.ActiveTimelineOperation.API_v1_TimelineOperation
            rewind: NetworkAPI_v1.API_v1_Announcement_Request.ActiveTimelineOperation.API_v1_TimelineOperation
            OPERATION_FIELD_NUMBER: _ClassVar[int]
            operation: NetworkAPI_v1.API_v1_Announcement_Request.ActiveTimelineOperation.API_v1_TimelineOperation
            def __init__(self, operation: _Optional[_Union[NetworkAPI_v1.API_v1_Announcement_Request.ActiveTimelineOperation.API_v1_TimelineOperation, str]] = ...) -> None: ...
        class ActiveTimelineStatus(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class Active(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class AnnouncementIndex(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class ActiveFocus(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class ActiveTrigger(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class ActiveNextTrigger(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class ActivePreviousTrigger(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class ActiveIndexTrigger(_message.Message):
            __slots__ = ("index",)
            INDEX_FIELD_NUMBER: _ClassVar[int]
            index: int
            def __init__(self, index: _Optional[int] = ...) -> None: ...
        ACTIVE_TIMELINE_OPERATION_FIELD_NUMBER: _ClassVar[int]
        ACTIVE_TIMELINE_STATUS_FIELD_NUMBER: _ClassVar[int]
        ACTIVE_FIELD_NUMBER: _ClassVar[int]
        SLIDE_INDEX_FIELD_NUMBER: _ClassVar[int]
        ACTIVE_FOCUS_FIELD_NUMBER: _ClassVar[int]
        ACTIVE_TRIGGER_FIELD_NUMBER: _ClassVar[int]
        ACTIVE_NEXT_TRIGGER_FIELD_NUMBER: _ClassVar[int]
        ACTIVE_PREVIOUS_TRIGGER_FIELD_NUMBER: _ClassVar[int]
        ACTIVE_INDEX_TRIGGER_FIELD_NUMBER: _ClassVar[int]
        active_timeline_operation: NetworkAPI_v1.API_v1_Announcement_Request.ActiveTimelineOperation
        active_timeline_status: NetworkAPI_v1.API_v1_Announcement_Request.ActiveTimelineStatus
        active: NetworkAPI_v1.API_v1_Announcement_Request.Active
        slide_index: NetworkAPI_v1.API_v1_Announcement_Request.AnnouncementIndex
        active_focus: NetworkAPI_v1.API_v1_Announcement_Request.ActiveFocus
        active_trigger: NetworkAPI_v1.API_v1_Announcement_Request.ActiveTrigger
        active_next_trigger: NetworkAPI_v1.API_v1_Announcement_Request.ActiveNextTrigger
        active_previous_trigger: NetworkAPI_v1.API_v1_Announcement_Request.ActivePreviousTrigger
        active_index_trigger: NetworkAPI_v1.API_v1_Announcement_Request.ActiveIndexTrigger
        def __init__(self, active_timeline_operation: _Optional[_Union[NetworkAPI_v1.API_v1_Announcement_Request.ActiveTimelineOperation, _Mapping]] = ..., active_timeline_status: _Optional[_Union[NetworkAPI_v1.API_v1_Announcement_Request.ActiveTimelineStatus, _Mapping]] = ..., active: _Optional[_Union[NetworkAPI_v1.API_v1_Announcement_Request.Active, _Mapping]] = ..., slide_index: _Optional[_Union[NetworkAPI_v1.API_v1_Announcement_Request.AnnouncementIndex, _Mapping]] = ..., active_focus: _Optional[_Union[NetworkAPI_v1.API_v1_Announcement_Request.ActiveFocus, _Mapping]] = ..., active_trigger: _Optional[_Union[NetworkAPI_v1.API_v1_Announcement_Request.ActiveTrigger, _Mapping]] = ..., active_next_trigger: _Optional[_Union[NetworkAPI_v1.API_v1_Announcement_Request.ActiveNextTrigger, _Mapping]] = ..., active_previous_trigger: _Optional[_Union[NetworkAPI_v1.API_v1_Announcement_Request.ActivePreviousTrigger, _Mapping]] = ..., active_index_trigger: _Optional[_Union[NetworkAPI_v1.API_v1_Announcement_Request.ActiveIndexTrigger, _Mapping]] = ...) -> None: ...
    class API_v1_Audio_Request(_message.Message):
        __slots__ = ("playlists", "playlist", "playlist_updates", "playlist_focused", "playlist_active", "playlist_next_focus", "playlist_previous_focus", "playlist_active_focus", "playlist_id_focus", "playlist_focused_trigger", "playlist_active_trigger", "playlist_id_trigger", "playlist_focused_next_trigger", "playlist_focused_previous_trigger", "playlist_focused_id_trigger", "playlist_active_next_trigger", "playlist_active_previous_trigger", "playlist_active_id_trigger", "playlist_id_next_trigger", "playlist_id_previous_trigger")
        class Playlists(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class Playlist(_message.Message):
            __slots__ = ("id", "start")
            ID_FIELD_NUMBER: _ClassVar[int]
            START_FIELD_NUMBER: _ClassVar[int]
            id: str
            start: int
            def __init__(self, id: _Optional[str] = ..., start: _Optional[int] = ...) -> None: ...
        class PlaylistUpdates(_message.Message):
            __slots__ = ("id",)
            ID_FIELD_NUMBER: _ClassVar[int]
            id: str
            def __init__(self, id: _Optional[str] = ...) -> None: ...
        class EmptyMessage(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class IdentifierMessage(_message.Message):
            __slots__ = ("id",)
            ID_FIELD_NUMBER: _ClassVar[int]
            id: str
            def __init__(self, id: _Optional[str] = ...) -> None: ...
        PLAYLISTS_FIELD_NUMBER: _ClassVar[int]
        PLAYLIST_FIELD_NUMBER: _ClassVar[int]
        PLAYLIST_UPDATES_FIELD_NUMBER: _ClassVar[int]
        PLAYLIST_FOCUSED_FIELD_NUMBER: _ClassVar[int]
        PLAYLIST_ACTIVE_FIELD_NUMBER: _ClassVar[int]
        PLAYLIST_NEXT_FOCUS_FIELD_NUMBER: _ClassVar[int]
        PLAYLIST_PREVIOUS_FOCUS_FIELD_NUMBER: _ClassVar[int]
        PLAYLIST_ACTIVE_FOCUS_FIELD_NUMBER: _ClassVar[int]
        PLAYLIST_ID_FOCUS_FIELD_NUMBER: _ClassVar[int]
        PLAYLIST_FOCUSED_TRIGGER_FIELD_NUMBER: _ClassVar[int]
        PLAYLIST_ACTIVE_TRIGGER_FIELD_NUMBER: _ClassVar[int]
        PLAYLIST_ID_TRIGGER_FIELD_NUMBER: _ClassVar[int]
        PLAYLIST_FOCUSED_NEXT_TRIGGER_FIELD_NUMBER: _ClassVar[int]
        PLAYLIST_FOCUSED_PREVIOUS_TRIGGER_FIELD_NUMBER: _ClassVar[int]
        PLAYLIST_FOCUSED_ID_TRIGGER_FIELD_NUMBER: _ClassVar[int]
        PLAYLIST_ACTIVE_NEXT_TRIGGER_FIELD_NUMBER: _ClassVar[int]
        PLAYLIST_ACTIVE_PREVIOUS_TRIGGER_FIELD_NUMBER: _ClassVar[int]
        PLAYLIST_ACTIVE_ID_TRIGGER_FIELD_NUMBER: _ClassVar[int]
        PLAYLIST_ID_NEXT_TRIGGER_FIELD_NUMBER: _ClassVar[int]
        PLAYLIST_ID_PREVIOUS_TRIGGER_FIELD_NUMBER: _ClassVar[int]
        playlists: NetworkAPI_v1.API_v1_Audio_Request.Playlists
        playlist: NetworkAPI_v1.API_v1_Audio_Request.Playlist
        playlist_updates: NetworkAPI_v1.API_v1_Audio_Request.PlaylistUpdates
        playlist_focused: NetworkAPI_v1.API_v1_Audio_Request.EmptyMessage
        playlist_active: NetworkAPI_v1.API_v1_Audio_Request.EmptyMessage
        playlist_next_focus: NetworkAPI_v1.API_v1_Audio_Request.EmptyMessage
        playlist_previous_focus: NetworkAPI_v1.API_v1_Audio_Request.EmptyMessage
        playlist_active_focus: NetworkAPI_v1.API_v1_Audio_Request.EmptyMessage
        playlist_id_focus: NetworkAPI_v1.API_v1_Audio_Request.IdentifierMessage
        playlist_focused_trigger: NetworkAPI_v1.API_v1_Audio_Request.EmptyMessage
        playlist_active_trigger: NetworkAPI_v1.API_v1_Audio_Request.EmptyMessage
        playlist_id_trigger: NetworkAPI_v1.API_v1_Audio_Request.IdentifierMessage
        playlist_focused_next_trigger: NetworkAPI_v1.API_v1_Audio_Request.EmptyMessage
        playlist_focused_previous_trigger: NetworkAPI_v1.API_v1_Audio_Request.EmptyMessage
        playlist_focused_id_trigger: NetworkAPI_v1.API_v1_Audio_Request.IdentifierMessage
        playlist_active_next_trigger: NetworkAPI_v1.API_v1_Audio_Request.EmptyMessage
        playlist_active_previous_trigger: NetworkAPI_v1.API_v1_Audio_Request.EmptyMessage
        playlist_active_id_trigger: NetworkAPI_v1.API_v1_Audio_Request.IdentifierMessage
        playlist_id_next_trigger: NetworkAPI_v1.API_v1_Audio_Request.IdentifierMessage
        playlist_id_previous_trigger: NetworkAPI_v1.API_v1_Audio_Request.IdentifierMessage
        def __init__(self, playlists: _Optional[_Union[NetworkAPI_v1.API_v1_Audio_Request.Playlists, _Mapping]] = ..., playlist: _Optional[_Union[NetworkAPI_v1.API_v1_Audio_Request.Playlist, _Mapping]] = ..., playlist_updates: _Optional[_Union[NetworkAPI_v1.API_v1_Audio_Request.PlaylistUpdates, _Mapping]] = ..., playlist_focused: _Optional[_Union[NetworkAPI_v1.API_v1_Audio_Request.EmptyMessage, _Mapping]] = ..., playlist_active: _Optional[_Union[NetworkAPI_v1.API_v1_Audio_Request.EmptyMessage, _Mapping]] = ..., playlist_next_focus: _Optional[_Union[NetworkAPI_v1.API_v1_Audio_Request.EmptyMessage, _Mapping]] = ..., playlist_previous_focus: _Optional[_Union[NetworkAPI_v1.API_v1_Audio_Request.EmptyMessage, _Mapping]] = ..., playlist_active_focus: _Optional[_Union[NetworkAPI_v1.API_v1_Audio_Request.EmptyMessage, _Mapping]] = ..., playlist_id_focus: _Optional[_Union[NetworkAPI_v1.API_v1_Audio_Request.IdentifierMessage, _Mapping]] = ..., playlist_focused_trigger: _Optional[_Union[NetworkAPI_v1.API_v1_Audio_Request.EmptyMessage, _Mapping]] = ..., playlist_active_trigger: _Optional[_Union[NetworkAPI_v1.API_v1_Audio_Request.EmptyMessage, _Mapping]] = ..., playlist_id_trigger: _Optional[_Union[NetworkAPI_v1.API_v1_Audio_Request.IdentifierMessage, _Mapping]] = ..., playlist_focused_next_trigger: _Optional[_Union[NetworkAPI_v1.API_v1_Audio_Request.EmptyMessage, _Mapping]] = ..., playlist_focused_previous_trigger: _Optional[_Union[NetworkAPI_v1.API_v1_Audio_Request.EmptyMessage, _Mapping]] = ..., playlist_focused_id_trigger: _Optional[_Union[NetworkAPI_v1.API_v1_Audio_Request.IdentifierMessage, _Mapping]] = ..., playlist_active_next_trigger: _Optional[_Union[NetworkAPI_v1.API_v1_Audio_Request.EmptyMessage, _Mapping]] = ..., playlist_active_previous_trigger: _Optional[_Union[NetworkAPI_v1.API_v1_Audio_Request.EmptyMessage, _Mapping]] = ..., playlist_active_id_trigger: _Optional[_Union[NetworkAPI_v1.API_v1_Audio_Request.IdentifierMessage, _Mapping]] = ..., playlist_id_next_trigger: _Optional[_Union[NetworkAPI_v1.API_v1_Audio_Request.IdentifierMessage, _Mapping]] = ..., playlist_id_previous_trigger: _Optional[_Union[NetworkAPI_v1.API_v1_Audio_Request.IdentifierMessage, _Mapping]] = ...) -> None: ...
    class API_v1_Capture_Request(_message.Message):
        __slots__ = ("get_status", "operation", "get_settings", "set_settings", "get_encodings")
        class Status(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class Operation(_message.Message):
            __slots__ = ("operation",)
            class CaptureOperation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                start: _ClassVar[NetworkAPI_v1.API_v1_Capture_Request.Operation.CaptureOperation]
                stop: _ClassVar[NetworkAPI_v1.API_v1_Capture_Request.Operation.CaptureOperation]
            start: NetworkAPI_v1.API_v1_Capture_Request.Operation.CaptureOperation
            stop: NetworkAPI_v1.API_v1_Capture_Request.Operation.CaptureOperation
            OPERATION_FIELD_NUMBER: _ClassVar[int]
            operation: NetworkAPI_v1.API_v1_Capture_Request.Operation.CaptureOperation
            def __init__(self, operation: _Optional[_Union[NetworkAPI_v1.API_v1_Capture_Request.Operation.CaptureOperation, str]] = ...) -> None: ...
        class GetSettings(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class SetSettings(_message.Message):
            __slots__ = ("settings",)
            SETTINGS_FIELD_NUMBER: _ClassVar[int]
            settings: _proApiV1BasicTypes_pb2.API_v1_CaptureSettings
            def __init__(self, settings: _Optional[_Union[_proApiV1BasicTypes_pb2.API_v1_CaptureSettings, _Mapping]] = ...) -> None: ...
        class Encodings(_message.Message):
            __slots__ = ("type",)
            class API_v1_CaptureDestination(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                disk: _ClassVar[NetworkAPI_v1.API_v1_Capture_Request.Encodings.API_v1_CaptureDestination]
                rtmp: _ClassVar[NetworkAPI_v1.API_v1_Capture_Request.Encodings.API_v1_CaptureDestination]
                resi: _ClassVar[NetworkAPI_v1.API_v1_Capture_Request.Encodings.API_v1_CaptureDestination]
            disk: NetworkAPI_v1.API_v1_Capture_Request.Encodings.API_v1_CaptureDestination
            rtmp: NetworkAPI_v1.API_v1_Capture_Request.Encodings.API_v1_CaptureDestination
            resi: NetworkAPI_v1.API_v1_Capture_Request.Encodings.API_v1_CaptureDestination
            TYPE_FIELD_NUMBER: _ClassVar[int]
            type: NetworkAPI_v1.API_v1_Capture_Request.Encodings.API_v1_CaptureDestination
            def __init__(self, type: _Optional[_Union[NetworkAPI_v1.API_v1_Capture_Request.Encodings.API_v1_CaptureDestination, str]] = ...) -> None: ...
        GET_STATUS_FIELD_NUMBER: _ClassVar[int]
        OPERATION_FIELD_NUMBER: _ClassVar[int]
        GET_SETTINGS_FIELD_NUMBER: _ClassVar[int]
        SET_SETTINGS_FIELD_NUMBER: _ClassVar[int]
        GET_ENCODINGS_FIELD_NUMBER: _ClassVar[int]
        get_status: NetworkAPI_v1.API_v1_Capture_Request.Status
        operation: NetworkAPI_v1.API_v1_Capture_Request.Operation
        get_settings: NetworkAPI_v1.API_v1_Capture_Request.GetSettings
        set_settings: NetworkAPI_v1.API_v1_Capture_Request.SetSettings
        get_encodings: NetworkAPI_v1.API_v1_Capture_Request.Encodings
        def __init__(self, get_status: _Optional[_Union[NetworkAPI_v1.API_v1_Capture_Request.Status, _Mapping]] = ..., operation: _Optional[_Union[NetworkAPI_v1.API_v1_Capture_Request.Operation, _Mapping]] = ..., get_settings: _Optional[_Union[NetworkAPI_v1.API_v1_Capture_Request.GetSettings, _Mapping]] = ..., set_settings: _Optional[_Union[NetworkAPI_v1.API_v1_Capture_Request.SetSettings, _Mapping]] = ..., get_encodings: _Optional[_Union[NetworkAPI_v1.API_v1_Capture_Request.Encodings, _Mapping]] = ...) -> None: ...
    class API_v1_Clear_Request(_message.Message):
        __slots__ = ("clear_layer", "create_group", "get_group", "put_group", "get_group_icon", "put_group_icon", "delete_group", "trigger_group", "get_groups")
        class ClearLayer(_message.Message):
            __slots__ = ("layer",)
            class API_v1_LayerType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                audio: _ClassVar[NetworkAPI_v1.API_v1_Clear_Request.ClearLayer.API_v1_LayerType]
                props: _ClassVar[NetworkAPI_v1.API_v1_Clear_Request.ClearLayer.API_v1_LayerType]
                messages: _ClassVar[NetworkAPI_v1.API_v1_Clear_Request.ClearLayer.API_v1_LayerType]
                announcements: _ClassVar[NetworkAPI_v1.API_v1_Clear_Request.ClearLayer.API_v1_LayerType]
                slide: _ClassVar[NetworkAPI_v1.API_v1_Clear_Request.ClearLayer.API_v1_LayerType]
                media: _ClassVar[NetworkAPI_v1.API_v1_Clear_Request.ClearLayer.API_v1_LayerType]
                video_input: _ClassVar[NetworkAPI_v1.API_v1_Clear_Request.ClearLayer.API_v1_LayerType]
            audio: NetworkAPI_v1.API_v1_Clear_Request.ClearLayer.API_v1_LayerType
            props: NetworkAPI_v1.API_v1_Clear_Request.ClearLayer.API_v1_LayerType
            messages: NetworkAPI_v1.API_v1_Clear_Request.ClearLayer.API_v1_LayerType
            announcements: NetworkAPI_v1.API_v1_Clear_Request.ClearLayer.API_v1_LayerType
            slide: NetworkAPI_v1.API_v1_Clear_Request.ClearLayer.API_v1_LayerType
            media: NetworkAPI_v1.API_v1_Clear_Request.ClearLayer.API_v1_LayerType
            video_input: NetworkAPI_v1.API_v1_Clear_Request.ClearLayer.API_v1_LayerType
            LAYER_FIELD_NUMBER: _ClassVar[int]
            layer: NetworkAPI_v1.API_v1_Clear_Request.ClearLayer.API_v1_LayerType
            def __init__(self, layer: _Optional[_Union[NetworkAPI_v1.API_v1_Clear_Request.ClearLayer.API_v1_LayerType, str]] = ...) -> None: ...
        class CreateGroup(_message.Message):
            __slots__ = ("group",)
            GROUP_FIELD_NUMBER: _ClassVar[int]
            group: _proApiV1BasicTypes_pb2.API_v1_ClearGroup
            def __init__(self, group: _Optional[_Union[_proApiV1BasicTypes_pb2.API_v1_ClearGroup, _Mapping]] = ...) -> None: ...
        class GetGroup(_message.Message):
            __slots__ = ("id",)
            ID_FIELD_NUMBER: _ClassVar[int]
            id: str
            def __init__(self, id: _Optional[str] = ...) -> None: ...
        class PutGroup(_message.Message):
            __slots__ = ("id", "group")
            ID_FIELD_NUMBER: _ClassVar[int]
            GROUP_FIELD_NUMBER: _ClassVar[int]
            id: str
            group: _proApiV1BasicTypes_pb2.API_v1_ClearGroup
            def __init__(self, id: _Optional[str] = ..., group: _Optional[_Union[_proApiV1BasicTypes_pb2.API_v1_ClearGroup, _Mapping]] = ...) -> None: ...
        class GetGroupIcon(_message.Message):
            __slots__ = ("id",)
            ID_FIELD_NUMBER: _ClassVar[int]
            id: str
            def __init__(self, id: _Optional[str] = ...) -> None: ...
        class PutGroupIcon(_message.Message):
            __slots__ = ("id", "content_type", "icon")
            ID_FIELD_NUMBER: _ClassVar[int]
            CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
            ICON_FIELD_NUMBER: _ClassVar[int]
            id: str
            content_type: str
            icon: bytes
            def __init__(self, id: _Optional[str] = ..., content_type: _Optional[str] = ..., icon: _Optional[bytes] = ...) -> None: ...
        class DeleteGroup(_message.Message):
            __slots__ = ("id",)
            ID_FIELD_NUMBER: _ClassVar[int]
            id: str
            def __init__(self, id: _Optional[str] = ...) -> None: ...
        class TriggerGroup(_message.Message):
            __slots__ = ("id",)
            ID_FIELD_NUMBER: _ClassVar[int]
            id: str
            def __init__(self, id: _Optional[str] = ...) -> None: ...
        class GetGroups(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        CLEAR_LAYER_FIELD_NUMBER: _ClassVar[int]
        CREATE_GROUP_FIELD_NUMBER: _ClassVar[int]
        GET_GROUP_FIELD_NUMBER: _ClassVar[int]
        PUT_GROUP_FIELD_NUMBER: _ClassVar[int]
        GET_GROUP_ICON_FIELD_NUMBER: _ClassVar[int]
        PUT_GROUP_ICON_FIELD_NUMBER: _ClassVar[int]
        DELETE_GROUP_FIELD_NUMBER: _ClassVar[int]
        TRIGGER_GROUP_FIELD_NUMBER: _ClassVar[int]
        GET_GROUPS_FIELD_NUMBER: _ClassVar[int]
        clear_layer: NetworkAPI_v1.API_v1_Clear_Request.ClearLayer
        create_group: NetworkAPI_v1.API_v1_Clear_Request.CreateGroup
        get_group: NetworkAPI_v1.API_v1_Clear_Request.GetGroup
        put_group: NetworkAPI_v1.API_v1_Clear_Request.PutGroup
        get_group_icon: NetworkAPI_v1.API_v1_Clear_Request.GetGroupIcon
        put_group_icon: NetworkAPI_v1.API_v1_Clear_Request.PutGroupIcon
        delete_group: NetworkAPI_v1.API_v1_Clear_Request.DeleteGroup
        trigger_group: NetworkAPI_v1.API_v1_Clear_Request.TriggerGroup
        get_groups: NetworkAPI_v1.API_v1_Clear_Request.GetGroups
        def __init__(self, clear_layer: _Optional[_Union[NetworkAPI_v1.API_v1_Clear_Request.ClearLayer, _Mapping]] = ..., create_group: _Optional[_Union[NetworkAPI_v1.API_v1_Clear_Request.CreateGroup, _Mapping]] = ..., get_group: _Optional[_Union[NetworkAPI_v1.API_v1_Clear_Request.GetGroup, _Mapping]] = ..., put_group: _Optional[_Union[NetworkAPI_v1.API_v1_Clear_Request.PutGroup, _Mapping]] = ..., get_group_icon: _Optional[_Union[NetworkAPI_v1.API_v1_Clear_Request.GetGroupIcon, _Mapping]] = ..., put_group_icon: _Optional[_Union[NetworkAPI_v1.API_v1_Clear_Request.PutGroupIcon, _Mapping]] = ..., delete_group: _Optional[_Union[NetworkAPI_v1.API_v1_Clear_Request.DeleteGroup, _Mapping]] = ..., trigger_group: _Optional[_Union[NetworkAPI_v1.API_v1_Clear_Request.TriggerGroup, _Mapping]] = ..., get_groups: _Optional[_Union[NetworkAPI_v1.API_v1_Clear_Request.GetGroups, _Mapping]] = ...) -> None: ...
    class API_v1_Groups_Request(_message.Message):
        __slots__ = ("groups_request", "trigger_group")
        class GroupsRequest(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class TriggerGroup(_message.Message):
            __slots__ = ("id",)
            ID_FIELD_NUMBER: _ClassVar[int]
            id: str
            def __init__(self, id: _Optional[str] = ...) -> None: ...
        GROUPS_REQUEST_FIELD_NUMBER: _ClassVar[int]
        TRIGGER_GROUP_FIELD_NUMBER: _ClassVar[int]
        groups_request: NetworkAPI_v1.API_v1_Groups_Request.GroupsRequest
        trigger_group: NetworkAPI_v1.API_v1_Groups_Request.TriggerGroup
        def __init__(self, groups_request: _Optional[_Union[NetworkAPI_v1.API_v1_Groups_Request.GroupsRequest, _Mapping]] = ..., trigger_group: _Optional[_Union[NetworkAPI_v1.API_v1_Groups_Request.TriggerGroup, _Mapping]] = ...) -> None: ...
    class API_v1_Link_Request(_message.Message):
        __slots__ = ("heartbeat", "status", "add_member", "remove_member")
        class Heartbeat(_message.Message):
            __slots__ = ("port", "if_modified_since")
            PORT_FIELD_NUMBER: _ClassVar[int]
            IF_MODIFIED_SINCE_FIELD_NUMBER: _ClassVar[int]
            port: int
            if_modified_since: str
            def __init__(self, port: _Optional[int] = ..., if_modified_since: _Optional[str] = ...) -> None: ...
        class Status(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class AddMember(_message.Message):
            __slots__ = ("group_definition", "member_details")
            GROUP_DEFINITION_FIELD_NUMBER: _ClassVar[int]
            MEMBER_DETAILS_FIELD_NUMBER: _ClassVar[int]
            group_definition: _proApiV1BasicTypes_pb2.API_v1_GroupDefinition
            member_details: _proApiV1BasicTypes_pb2.API_v1_GroupMember
            def __init__(self, group_definition: _Optional[_Union[_proApiV1BasicTypes_pb2.API_v1_GroupDefinition, _Mapping]] = ..., member_details: _Optional[_Union[_proApiV1BasicTypes_pb2.API_v1_GroupMember, _Mapping]] = ...) -> None: ...
        class RemoveMember(_message.Message):
            __slots__ = ("member_details",)
            MEMBER_DETAILS_FIELD_NUMBER: _ClassVar[int]
            member_details: _proApiV1BasicTypes_pb2.API_v1_GroupMember
            def __init__(self, member_details: _Optional[_Union[_proApiV1BasicTypes_pb2.API_v1_GroupMember, _Mapping]] = ...) -> None: ...
        HEARTBEAT_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        ADD_MEMBER_FIELD_NUMBER: _ClassVar[int]
        REMOVE_MEMBER_FIELD_NUMBER: _ClassVar[int]
        heartbeat: NetworkAPI_v1.API_v1_Link_Request.Heartbeat
        status: NetworkAPI_v1.API_v1_Link_Request.Status
        add_member: NetworkAPI_v1.API_v1_Link_Request.AddMember
        remove_member: NetworkAPI_v1.API_v1_Link_Request.RemoveMember
        def __init__(self, heartbeat: _Optional[_Union[NetworkAPI_v1.API_v1_Link_Request.Heartbeat, _Mapping]] = ..., status: _Optional[_Union[NetworkAPI_v1.API_v1_Link_Request.Status, _Mapping]] = ..., add_member: _Optional[_Union[NetworkAPI_v1.API_v1_Link_Request.AddMember, _Mapping]] = ..., remove_member: _Optional[_Union[NetworkAPI_v1.API_v1_Link_Request.RemoveMember, _Mapping]] = ...) -> None: ...
    class API_v1_Library_Request(_message.Message):
        __slots__ = ("libraries", "library", "trigger")
        class Libraries(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class Library(_message.Message):
            __slots__ = ("id",)
            ID_FIELD_NUMBER: _ClassVar[int]
            id: str
            def __init__(self, id: _Optional[str] = ...) -> None: ...
        class Trigger(_message.Message):
            __slots__ = ("library_id", "presentation_id", "index")
            LIBRARY_ID_FIELD_NUMBER: _ClassVar[int]
            PRESENTATION_ID_FIELD_NUMBER: _ClassVar[int]
            INDEX_FIELD_NUMBER: _ClassVar[int]
            library_id: str
            presentation_id: str
            index: int
            def __init__(self, library_id: _Optional[str] = ..., presentation_id: _Optional[str] = ..., index: _Optional[int] = ...) -> None: ...
        LIBRARIES_FIELD_NUMBER: _ClassVar[int]
        LIBRARY_FIELD_NUMBER: _ClassVar[int]
        TRIGGER_FIELD_NUMBER: _ClassVar[int]
        libraries: NetworkAPI_v1.API_v1_Library_Request.Libraries
        library: NetworkAPI_v1.API_v1_Library_Request.Library
        trigger: NetworkAPI_v1.API_v1_Library_Request.Trigger
        def __init__(self, libraries: _Optional[_Union[NetworkAPI_v1.API_v1_Library_Request.Libraries, _Mapping]] = ..., library: _Optional[_Union[NetworkAPI_v1.API_v1_Library_Request.Library, _Mapping]] = ..., trigger: _Optional[_Union[NetworkAPI_v1.API_v1_Library_Request.Trigger, _Mapping]] = ...) -> None: ...
    class API_v1_Looks_Request(_message.Message):
        __slots__ = ("looks", "create_look", "get_current_look", "put_current_look", "get_look", "put_look", "delete_look", "trigger_look")
        class Looks(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class CreateLook(_message.Message):
            __slots__ = ("look",)
            LOOK_FIELD_NUMBER: _ClassVar[int]
            look: _proApiV1BasicTypes_pb2.API_v1_Look
            def __init__(self, look: _Optional[_Union[_proApiV1BasicTypes_pb2.API_v1_Look, _Mapping]] = ...) -> None: ...
        class GetCurrentLook(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class PutCurrentLook(_message.Message):
            __slots__ = ("look",)
            LOOK_FIELD_NUMBER: _ClassVar[int]
            look: _proApiV1BasicTypes_pb2.API_v1_Look
            def __init__(self, look: _Optional[_Union[_proApiV1BasicTypes_pb2.API_v1_Look, _Mapping]] = ...) -> None: ...
        class GetLook(_message.Message):
            __slots__ = ("id",)
            ID_FIELD_NUMBER: _ClassVar[int]
            id: str
            def __init__(self, id: _Optional[str] = ...) -> None: ...
        class PutLook(_message.Message):
            __slots__ = ("id", "look")
            ID_FIELD_NUMBER: _ClassVar[int]
            LOOK_FIELD_NUMBER: _ClassVar[int]
            id: str
            look: _proApiV1BasicTypes_pb2.API_v1_Look
            def __init__(self, id: _Optional[str] = ..., look: _Optional[_Union[_proApiV1BasicTypes_pb2.API_v1_Look, _Mapping]] = ...) -> None: ...
        class DeleteLook(_message.Message):
            __slots__ = ("id",)
            ID_FIELD_NUMBER: _ClassVar[int]
            id: str
            def __init__(self, id: _Optional[str] = ...) -> None: ...
        class TriggerLook(_message.Message):
            __slots__ = ("id",)
            ID_FIELD_NUMBER: _ClassVar[int]
            id: str
            def __init__(self, id: _Optional[str] = ...) -> None: ...
        LOOKS_FIELD_NUMBER: _ClassVar[int]
        CREATE_LOOK_FIELD_NUMBER: _ClassVar[int]
        GET_CURRENT_LOOK_FIELD_NUMBER: _ClassVar[int]
        PUT_CURRENT_LOOK_FIELD_NUMBER: _ClassVar[int]
        GET_LOOK_FIELD_NUMBER: _ClassVar[int]
        PUT_LOOK_FIELD_NUMBER: _ClassVar[int]
        DELETE_LOOK_FIELD_NUMBER: _ClassVar[int]
        TRIGGER_LOOK_FIELD_NUMBER: _ClassVar[int]
        looks: NetworkAPI_v1.API_v1_Looks_Request.Looks
        create_look: NetworkAPI_v1.API_v1_Looks_Request.CreateLook
        get_current_look: NetworkAPI_v1.API_v1_Looks_Request.GetCurrentLook
        put_current_look: NetworkAPI_v1.API_v1_Looks_Request.PutCurrentLook
        get_look: NetworkAPI_v1.API_v1_Looks_Request.GetLook
        put_look: NetworkAPI_v1.API_v1_Looks_Request.PutLook
        delete_look: NetworkAPI_v1.API_v1_Looks_Request.DeleteLook
        trigger_look: NetworkAPI_v1.API_v1_Looks_Request.TriggerLook
        def __init__(self, looks: _Optional[_Union[NetworkAPI_v1.API_v1_Looks_Request.Looks, _Mapping]] = ..., create_look: _Optional[_Union[NetworkAPI_v1.API_v1_Looks_Request.CreateLook, _Mapping]] = ..., get_current_look: _Optional[_Union[NetworkAPI_v1.API_v1_Looks_Request.GetCurrentLook, _Mapping]] = ..., put_current_look: _Optional[_Union[NetworkAPI_v1.API_v1_Looks_Request.PutCurrentLook, _Mapping]] = ..., get_look: _Optional[_Union[NetworkAPI_v1.API_v1_Looks_Request.GetLook, _Mapping]] = ..., put_look: _Optional[_Union[NetworkAPI_v1.API_v1_Looks_Request.PutLook, _Mapping]] = ..., delete_look: _Optional[_Union[NetworkAPI_v1.API_v1_Looks_Request.DeleteLook, _Mapping]] = ..., trigger_look: _Optional[_Union[NetworkAPI_v1.API_v1_Looks_Request.TriggerLook, _Mapping]] = ...) -> None: ...
    class API_v1_Macro_Request(_message.Message):
        __slots__ = ("macros", "get_macro", "put_macro", "delete_macro", "trigger_macro")
        class Macros(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class GetMacro(_message.Message):
            __slots__ = ("id",)
            ID_FIELD_NUMBER: _ClassVar[int]
            id: str
            def __init__(self, id: _Optional[str] = ...) -> None: ...
        class PutMacro(_message.Message):
            __slots__ = ("id", "name_change", "color_change")
            ID_FIELD_NUMBER: _ClassVar[int]
            NAME_CHANGE_FIELD_NUMBER: _ClassVar[int]
            COLOR_CHANGE_FIELD_NUMBER: _ClassVar[int]
            id: str
            name_change: str
            color_change: _proApiV1BasicTypes_pb2.API_v1_Color
            def __init__(self, id: _Optional[str] = ..., name_change: _Optional[str] = ..., color_change: _Optional[_Union[_proApiV1BasicTypes_pb2.API_v1_Color, _Mapping]] = ...) -> None: ...
        class DeleteMacro(_message.Message):
            __slots__ = ("id",)
            ID_FIELD_NUMBER: _ClassVar[int]
            id: str
            def __init__(self, id: _Optional[str] = ...) -> None: ...
        class TriggerMacro(_message.Message):
            __slots__ = ("id",)
            ID_FIELD_NUMBER: _ClassVar[int]
            id: str
            def __init__(self, id: _Optional[str] = ...) -> None: ...
        MACROS_FIELD_NUMBER: _ClassVar[int]
        GET_MACRO_FIELD_NUMBER: _ClassVar[int]
        PUT_MACRO_FIELD_NUMBER: _ClassVar[int]
        DELETE_MACRO_FIELD_NUMBER: _ClassVar[int]
        TRIGGER_MACRO_FIELD_NUMBER: _ClassVar[int]
        macros: NetworkAPI_v1.API_v1_Macro_Request.Macros
        get_macro: NetworkAPI_v1.API_v1_Macro_Request.GetMacro
        put_macro: NetworkAPI_v1.API_v1_Macro_Request.PutMacro
        delete_macro: NetworkAPI_v1.API_v1_Macro_Request.DeleteMacro
        trigger_macro: NetworkAPI_v1.API_v1_Macro_Request.TriggerMacro
        def __init__(self, macros: _Optional[_Union[NetworkAPI_v1.API_v1_Macro_Request.Macros, _Mapping]] = ..., get_macro: _Optional[_Union[NetworkAPI_v1.API_v1_Macro_Request.GetMacro, _Mapping]] = ..., put_macro: _Optional[_Union[NetworkAPI_v1.API_v1_Macro_Request.PutMacro, _Mapping]] = ..., delete_macro: _Optional[_Union[NetworkAPI_v1.API_v1_Macro_Request.DeleteMacro, _Mapping]] = ..., trigger_macro: _Optional[_Union[NetworkAPI_v1.API_v1_Macro_Request.TriggerMacro, _Mapping]] = ...) -> None: ...
    class API_v1_Masks_Request(_message.Message):
        __slots__ = ("masks", "get_mask", "get_thumbnail")
        class Masks(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class GetMask(_message.Message):
            __slots__ = ("id",)
            ID_FIELD_NUMBER: _ClassVar[int]
            id: str
            def __init__(self, id: _Optional[str] = ...) -> None: ...
        class GetThumbnail(_message.Message):
            __slots__ = ("id", "quality")
            ID_FIELD_NUMBER: _ClassVar[int]
            QUALITY_FIELD_NUMBER: _ClassVar[int]
            id: str
            quality: int
            def __init__(self, id: _Optional[str] = ..., quality: _Optional[int] = ...) -> None: ...
        MASKS_FIELD_NUMBER: _ClassVar[int]
        GET_MASK_FIELD_NUMBER: _ClassVar[int]
        GET_THUMBNAIL_FIELD_NUMBER: _ClassVar[int]
        masks: NetworkAPI_v1.API_v1_Masks_Request.Masks
        get_mask: NetworkAPI_v1.API_v1_Masks_Request.GetMask
        get_thumbnail: NetworkAPI_v1.API_v1_Masks_Request.GetThumbnail
        def __init__(self, masks: _Optional[_Union[NetworkAPI_v1.API_v1_Masks_Request.Masks, _Mapping]] = ..., get_mask: _Optional[_Union[NetworkAPI_v1.API_v1_Masks_Request.GetMask, _Mapping]] = ..., get_thumbnail: _Optional[_Union[NetworkAPI_v1.API_v1_Masks_Request.GetThumbnail, _Mapping]] = ...) -> None: ...
    class API_v1_Media_Request(_message.Message):
        __slots__ = ("playlists", "get_playlist", "get_playlist_updates", "get_thumbnail", "playlist_focused", "playlist_active", "focus", "trigger")
        class Playlists(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class GetPlaylist(_message.Message):
            __slots__ = ("id", "start")
            ID_FIELD_NUMBER: _ClassVar[int]
            START_FIELD_NUMBER: _ClassVar[int]
            id: str
            start: int
            def __init__(self, id: _Optional[str] = ..., start: _Optional[int] = ...) -> None: ...
        class GetPlaylistUpdates(_message.Message):
            __slots__ = ("id",)
            ID_FIELD_NUMBER: _ClassVar[int]
            id: str
            def __init__(self, id: _Optional[str] = ...) -> None: ...
        class GetThumbnail(_message.Message):
            __slots__ = ("uuid", "quality")
            UUID_FIELD_NUMBER: _ClassVar[int]
            QUALITY_FIELD_NUMBER: _ClassVar[int]
            uuid: _basicTypes_pb2.UUID
            quality: int
            def __init__(self, uuid: _Optional[_Union[_basicTypes_pb2.UUID, _Mapping]] = ..., quality: _Optional[int] = ...) -> None: ...
        class EmptyMessage(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class FocusMessage(_message.Message):
            __slots__ = ("next", "previous", "active", "id")
            NEXT_FIELD_NUMBER: _ClassVar[int]
            PREVIOUS_FIELD_NUMBER: _ClassVar[int]
            ACTIVE_FIELD_NUMBER: _ClassVar[int]
            ID_FIELD_NUMBER: _ClassVar[int]
            next: NetworkAPI_v1.API_v1_Media_Request.EmptyMessage
            previous: NetworkAPI_v1.API_v1_Media_Request.EmptyMessage
            active: NetworkAPI_v1.API_v1_Media_Request.EmptyMessage
            id: _wrappers_pb2.StringValue
            def __init__(self, next: _Optional[_Union[NetworkAPI_v1.API_v1_Media_Request.EmptyMessage, _Mapping]] = ..., previous: _Optional[_Union[NetworkAPI_v1.API_v1_Media_Request.EmptyMessage, _Mapping]] = ..., active: _Optional[_Union[NetworkAPI_v1.API_v1_Media_Request.EmptyMessage, _Mapping]] = ..., id: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...) -> None: ...
        class TriggerMessage(_message.Message):
            __slots__ = ("focused", "active", "playlist_id", "start", "next", "previous", "media_id")
            FOCUSED_FIELD_NUMBER: _ClassVar[int]
            ACTIVE_FIELD_NUMBER: _ClassVar[int]
            PLAYLIST_ID_FIELD_NUMBER: _ClassVar[int]
            START_FIELD_NUMBER: _ClassVar[int]
            NEXT_FIELD_NUMBER: _ClassVar[int]
            PREVIOUS_FIELD_NUMBER: _ClassVar[int]
            MEDIA_ID_FIELD_NUMBER: _ClassVar[int]
            focused: NetworkAPI_v1.API_v1_Media_Request.EmptyMessage
            active: NetworkAPI_v1.API_v1_Media_Request.EmptyMessage
            playlist_id: _wrappers_pb2.StringValue
            start: NetworkAPI_v1.API_v1_Media_Request.EmptyMessage
            next: NetworkAPI_v1.API_v1_Media_Request.EmptyMessage
            previous: NetworkAPI_v1.API_v1_Media_Request.EmptyMessage
            media_id: _wrappers_pb2.StringValue
            def __init__(self, focused: _Optional[_Union[NetworkAPI_v1.API_v1_Media_Request.EmptyMessage, _Mapping]] = ..., active: _Optional[_Union[NetworkAPI_v1.API_v1_Media_Request.EmptyMessage, _Mapping]] = ..., playlist_id: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., start: _Optional[_Union[NetworkAPI_v1.API_v1_Media_Request.EmptyMessage, _Mapping]] = ..., next: _Optional[_Union[NetworkAPI_v1.API_v1_Media_Request.EmptyMessage, _Mapping]] = ..., previous: _Optional[_Union[NetworkAPI_v1.API_v1_Media_Request.EmptyMessage, _Mapping]] = ..., media_id: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...) -> None: ...
        PLAYLISTS_FIELD_NUMBER: _ClassVar[int]
        GET_PLAYLIST_FIELD_NUMBER: _ClassVar[int]
        GET_PLAYLIST_UPDATES_FIELD_NUMBER: _ClassVar[int]
        GET_THUMBNAIL_FIELD_NUMBER: _ClassVar[int]
        PLAYLIST_FOCUSED_FIELD_NUMBER: _ClassVar[int]
        PLAYLIST_ACTIVE_FIELD_NUMBER: _ClassVar[int]
        FOCUS_FIELD_NUMBER: _ClassVar[int]
        TRIGGER_FIELD_NUMBER: _ClassVar[int]
        playlists: NetworkAPI_v1.API_v1_Media_Request.Playlists
        get_playlist: NetworkAPI_v1.API_v1_Media_Request.GetPlaylist
        get_playlist_updates: NetworkAPI_v1.API_v1_Media_Request.GetPlaylistUpdates
        get_thumbnail: NetworkAPI_v1.API_v1_Media_Request.GetThumbnail
        playlist_focused: NetworkAPI_v1.API_v1_Media_Request.EmptyMessage
        playlist_active: NetworkAPI_v1.API_v1_Media_Request.EmptyMessage
        focus: NetworkAPI_v1.API_v1_Media_Request.FocusMessage
        trigger: NetworkAPI_v1.API_v1_Media_Request.TriggerMessage
        def __init__(self, playlists: _Optional[_Union[NetworkAPI_v1.API_v1_Media_Request.Playlists, _Mapping]] = ..., get_playlist: _Optional[_Union[NetworkAPI_v1.API_v1_Media_Request.GetPlaylist, _Mapping]] = ..., get_playlist_updates: _Optional[_Union[NetworkAPI_v1.API_v1_Media_Request.GetPlaylistUpdates, _Mapping]] = ..., get_thumbnail: _Optional[_Union[NetworkAPI_v1.API_v1_Media_Request.GetThumbnail, _Mapping]] = ..., playlist_focused: _Optional[_Union[NetworkAPI_v1.API_v1_Media_Request.EmptyMessage, _Mapping]] = ..., playlist_active: _Optional[_Union[NetworkAPI_v1.API_v1_Media_Request.EmptyMessage, _Mapping]] = ..., focus: _Optional[_Union[NetworkAPI_v1.API_v1_Media_Request.FocusMessage, _Mapping]] = ..., trigger: _Optional[_Union[NetworkAPI_v1.API_v1_Media_Request.TriggerMessage, _Mapping]] = ...) -> None: ...
    class API_v1_Message_Request(_message.Message):
        __slots__ = ("messages", "create_message", "get_message", "put_message", "delete_message", "trigger_message", "clear_message")
        class Messages(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class CreateMessage(_message.Message):
            __slots__ = ("message",)
            MESSAGE_FIELD_NUMBER: _ClassVar[int]
            message: _proApiV1BasicTypes_pb2.API_v1_Message
            def __init__(self, message: _Optional[_Union[_proApiV1BasicTypes_pb2.API_v1_Message, _Mapping]] = ...) -> None: ...
        class GetMessage(_message.Message):
            __slots__ = ("id",)
            ID_FIELD_NUMBER: _ClassVar[int]
            id: str
            def __init__(self, id: _Optional[str] = ...) -> None: ...
        class PutMessage(_message.Message):
            __slots__ = ("id", "message")
            ID_FIELD_NUMBER: _ClassVar[int]
            MESSAGE_FIELD_NUMBER: _ClassVar[int]
            id: str
            message: _proApiV1BasicTypes_pb2.API_v1_Message
            def __init__(self, id: _Optional[str] = ..., message: _Optional[_Union[_proApiV1BasicTypes_pb2.API_v1_Message, _Mapping]] = ...) -> None: ...
        class DeleteMessage(_message.Message):
            __slots__ = ("id",)
            ID_FIELD_NUMBER: _ClassVar[int]
            id: str
            def __init__(self, id: _Optional[str] = ...) -> None: ...
        class TriggerMessage(_message.Message):
            __slots__ = ("id", "tokens")
            ID_FIELD_NUMBER: _ClassVar[int]
            TOKENS_FIELD_NUMBER: _ClassVar[int]
            id: str
            tokens: _containers.RepeatedCompositeFieldContainer[_proApiV1BasicTypes_pb2.API_v1_Message.API_v1_MessageToken]
            def __init__(self, id: _Optional[str] = ..., tokens: _Optional[_Iterable[_Union[_proApiV1BasicTypes_pb2.API_v1_Message.API_v1_MessageToken, _Mapping]]] = ...) -> None: ...
        class ClearMessage(_message.Message):
            __slots__ = ("id",)
            ID_FIELD_NUMBER: _ClassVar[int]
            id: str
            def __init__(self, id: _Optional[str] = ...) -> None: ...
        MESSAGES_FIELD_NUMBER: _ClassVar[int]
        CREATE_MESSAGE_FIELD_NUMBER: _ClassVar[int]
        GET_MESSAGE_FIELD_NUMBER: _ClassVar[int]
        PUT_MESSAGE_FIELD_NUMBER: _ClassVar[int]
        DELETE_MESSAGE_FIELD_NUMBER: _ClassVar[int]
        TRIGGER_MESSAGE_FIELD_NUMBER: _ClassVar[int]
        CLEAR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
        messages: NetworkAPI_v1.API_v1_Message_Request.Messages
        create_message: NetworkAPI_v1.API_v1_Message_Request.CreateMessage
        get_message: NetworkAPI_v1.API_v1_Message_Request.GetMessage
        put_message: NetworkAPI_v1.API_v1_Message_Request.PutMessage
        delete_message: NetworkAPI_v1.API_v1_Message_Request.DeleteMessage
        trigger_message: NetworkAPI_v1.API_v1_Message_Request.TriggerMessage
        clear_message: NetworkAPI_v1.API_v1_Message_Request.ClearMessage
        def __init__(self, messages: _Optional[_Union[NetworkAPI_v1.API_v1_Message_Request.Messages, _Mapping]] = ..., create_message: _Optional[_Union[NetworkAPI_v1.API_v1_Message_Request.CreateMessage, _Mapping]] = ..., get_message: _Optional[_Union[NetworkAPI_v1.API_v1_Message_Request.GetMessage, _Mapping]] = ..., put_message: _Optional[_Union[NetworkAPI_v1.API_v1_Message_Request.PutMessage, _Mapping]] = ..., delete_message: _Optional[_Union[NetworkAPI_v1.API_v1_Message_Request.DeleteMessage, _Mapping]] = ..., trigger_message: _Optional[_Union[NetworkAPI_v1.API_v1_Message_Request.TriggerMessage, _Mapping]] = ..., clear_message: _Optional[_Union[NetworkAPI_v1.API_v1_Message_Request.ClearMessage, _Mapping]] = ...) -> None: ...
    class API_v1_Miscellaneous_Request(_message.Message):
        __slots__ = ("find_my_mouse",)
        class FindMyMouse(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        FIND_MY_MOUSE_FIELD_NUMBER: _ClassVar[int]
        find_my_mouse: NetworkAPI_v1.API_v1_Miscellaneous_Request.FindMyMouse
        def __init__(self, find_my_mouse: _Optional[_Union[NetworkAPI_v1.API_v1_Miscellaneous_Request.FindMyMouse, _Mapping]] = ...) -> None: ...
    class API_v1_Playlist_Request(_message.Message):
        __slots__ = ("playlists", "create_playlist", "get_playlist", "put_playlist", "post_playlist", "get_active_playlist", "focused", "next_focus", "previous_focus", "active_presentation_focus", "active_announcement_focus", "focused_trigger", "active_presentation_trigger", "active_announcement_trigger", "focused_next_trigger", "focused_previous_trigger", "active_presentation_next_trigger", "active_announcement_next_trigger", "active_presentation_previous_trigger", "active_announcement_previous_trigger", "id_focus", "id_trigger", "id_next_trigger", "id_previous_trigger", "focused_index_trigger", "active_presentation_index_trigger", "active_announcement_index_trigger", "id_updates")
        class Playlists(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class CreatePlaylist(_message.Message):
            __slots__ = ("name", "type")
            class API_v1_PlaylistType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                group: _ClassVar[NetworkAPI_v1.API_v1_Playlist_Request.CreatePlaylist.API_v1_PlaylistType]
                playlist: _ClassVar[NetworkAPI_v1.API_v1_Playlist_Request.CreatePlaylist.API_v1_PlaylistType]
            group: NetworkAPI_v1.API_v1_Playlist_Request.CreatePlaylist.API_v1_PlaylistType
            playlist: NetworkAPI_v1.API_v1_Playlist_Request.CreatePlaylist.API_v1_PlaylistType
            NAME_FIELD_NUMBER: _ClassVar[int]
            TYPE_FIELD_NUMBER: _ClassVar[int]
            name: str
            type: NetworkAPI_v1.API_v1_Playlist_Request.CreatePlaylist.API_v1_PlaylistType
            def __init__(self, name: _Optional[str] = ..., type: _Optional[_Union[NetworkAPI_v1.API_v1_Playlist_Request.CreatePlaylist.API_v1_PlaylistType, str]] = ...) -> None: ...
        class GetActivePlaylist(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class GetPlaylist(_message.Message):
            __slots__ = ("id",)
            ID_FIELD_NUMBER: _ClassVar[int]
            id: str
            def __init__(self, id: _Optional[str] = ...) -> None: ...
        class PutPlaylist(_message.Message):
            __slots__ = ("id", "items")
            ID_FIELD_NUMBER: _ClassVar[int]
            ITEMS_FIELD_NUMBER: _ClassVar[int]
            id: str
            items: _containers.RepeatedCompositeFieldContainer[_proApiV1BasicTypes_pb2.API_v1_PlaylistItem]
            def __init__(self, id: _Optional[str] = ..., items: _Optional[_Iterable[_Union[_proApiV1BasicTypes_pb2.API_v1_PlaylistItem, _Mapping]]] = ...) -> None: ...
        class PostPlaylist(_message.Message):
            __slots__ = ("id", "name", "type")
            class API_v1_PlaylistType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                group: _ClassVar[NetworkAPI_v1.API_v1_Playlist_Request.PostPlaylist.API_v1_PlaylistType]
                playlist: _ClassVar[NetworkAPI_v1.API_v1_Playlist_Request.PostPlaylist.API_v1_PlaylistType]
            group: NetworkAPI_v1.API_v1_Playlist_Request.PostPlaylist.API_v1_PlaylistType
            playlist: NetworkAPI_v1.API_v1_Playlist_Request.PostPlaylist.API_v1_PlaylistType
            ID_FIELD_NUMBER: _ClassVar[int]
            NAME_FIELD_NUMBER: _ClassVar[int]
            TYPE_FIELD_NUMBER: _ClassVar[int]
            id: str
            name: str
            type: NetworkAPI_v1.API_v1_Playlist_Request.PostPlaylist.API_v1_PlaylistType
            def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., type: _Optional[_Union[NetworkAPI_v1.API_v1_Playlist_Request.PostPlaylist.API_v1_PlaylistType, str]] = ...) -> None: ...
        class EmptyMessage(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class IdMessage(_message.Message):
            __slots__ = ("id",)
            ID_FIELD_NUMBER: _ClassVar[int]
            id: str
            def __init__(self, id: _Optional[str] = ...) -> None: ...
        class IndexMessage(_message.Message):
            __slots__ = ("index",)
            INDEX_FIELD_NUMBER: _ClassVar[int]
            index: int
            def __init__(self, index: _Optional[int] = ...) -> None: ...
        PLAYLISTS_FIELD_NUMBER: _ClassVar[int]
        CREATE_PLAYLIST_FIELD_NUMBER: _ClassVar[int]
        GET_PLAYLIST_FIELD_NUMBER: _ClassVar[int]
        PUT_PLAYLIST_FIELD_NUMBER: _ClassVar[int]
        POST_PLAYLIST_FIELD_NUMBER: _ClassVar[int]
        GET_ACTIVE_PLAYLIST_FIELD_NUMBER: _ClassVar[int]
        FOCUSED_FIELD_NUMBER: _ClassVar[int]
        NEXT_FOCUS_FIELD_NUMBER: _ClassVar[int]
        PREVIOUS_FOCUS_FIELD_NUMBER: _ClassVar[int]
        ACTIVE_PRESENTATION_FOCUS_FIELD_NUMBER: _ClassVar[int]
        ACTIVE_ANNOUNCEMENT_FOCUS_FIELD_NUMBER: _ClassVar[int]
        FOCUSED_TRIGGER_FIELD_NUMBER: _ClassVar[int]
        ACTIVE_PRESENTATION_TRIGGER_FIELD_NUMBER: _ClassVar[int]
        ACTIVE_ANNOUNCEMENT_TRIGGER_FIELD_NUMBER: _ClassVar[int]
        FOCUSED_NEXT_TRIGGER_FIELD_NUMBER: _ClassVar[int]
        FOCUSED_PREVIOUS_TRIGGER_FIELD_NUMBER: _ClassVar[int]
        ACTIVE_PRESENTATION_NEXT_TRIGGER_FIELD_NUMBER: _ClassVar[int]
        ACTIVE_ANNOUNCEMENT_NEXT_TRIGGER_FIELD_NUMBER: _ClassVar[int]
        ACTIVE_PRESENTATION_PREVIOUS_TRIGGER_FIELD_NUMBER: _ClassVar[int]
        ACTIVE_ANNOUNCEMENT_PREVIOUS_TRIGGER_FIELD_NUMBER: _ClassVar[int]
        ID_FOCUS_FIELD_NUMBER: _ClassVar[int]
        ID_TRIGGER_FIELD_NUMBER: _ClassVar[int]
        ID_NEXT_TRIGGER_FIELD_NUMBER: _ClassVar[int]
        ID_PREVIOUS_TRIGGER_FIELD_NUMBER: _ClassVar[int]
        FOCUSED_INDEX_TRIGGER_FIELD_NUMBER: _ClassVar[int]
        ACTIVE_PRESENTATION_INDEX_TRIGGER_FIELD_NUMBER: _ClassVar[int]
        ACTIVE_ANNOUNCEMENT_INDEX_TRIGGER_FIELD_NUMBER: _ClassVar[int]
        ID_UPDATES_FIELD_NUMBER: _ClassVar[int]
        playlists: NetworkAPI_v1.API_v1_Playlist_Request.Playlists
        create_playlist: NetworkAPI_v1.API_v1_Playlist_Request.CreatePlaylist
        get_playlist: NetworkAPI_v1.API_v1_Playlist_Request.GetPlaylist
        put_playlist: NetworkAPI_v1.API_v1_Playlist_Request.PutPlaylist
        post_playlist: NetworkAPI_v1.API_v1_Playlist_Request.PostPlaylist
        get_active_playlist: NetworkAPI_v1.API_v1_Playlist_Request.GetActivePlaylist
        focused: NetworkAPI_v1.API_v1_Playlist_Request.GetActivePlaylist
        next_focus: NetworkAPI_v1.API_v1_Playlist_Request.EmptyMessage
        previous_focus: NetworkAPI_v1.API_v1_Playlist_Request.EmptyMessage
        active_presentation_focus: NetworkAPI_v1.API_v1_Playlist_Request.EmptyMessage
        active_announcement_focus: NetworkAPI_v1.API_v1_Playlist_Request.EmptyMessage
        focused_trigger: NetworkAPI_v1.API_v1_Playlist_Request.EmptyMessage
        active_presentation_trigger: NetworkAPI_v1.API_v1_Playlist_Request.EmptyMessage
        active_announcement_trigger: NetworkAPI_v1.API_v1_Playlist_Request.EmptyMessage
        focused_next_trigger: NetworkAPI_v1.API_v1_Playlist_Request.EmptyMessage
        focused_previous_trigger: NetworkAPI_v1.API_v1_Playlist_Request.EmptyMessage
        active_presentation_next_trigger: NetworkAPI_v1.API_v1_Playlist_Request.EmptyMessage
        active_announcement_next_trigger: NetworkAPI_v1.API_v1_Playlist_Request.EmptyMessage
        active_presentation_previous_trigger: NetworkAPI_v1.API_v1_Playlist_Request.EmptyMessage
        active_announcement_previous_trigger: NetworkAPI_v1.API_v1_Playlist_Request.EmptyMessage
        id_focus: NetworkAPI_v1.API_v1_Playlist_Request.IdMessage
        id_trigger: NetworkAPI_v1.API_v1_Playlist_Request.IdMessage
        id_next_trigger: NetworkAPI_v1.API_v1_Playlist_Request.IdMessage
        id_previous_trigger: NetworkAPI_v1.API_v1_Playlist_Request.IdMessage
        focused_index_trigger: NetworkAPI_v1.API_v1_Playlist_Request.IndexMessage
        active_presentation_index_trigger: NetworkAPI_v1.API_v1_Playlist_Request.IndexMessage
        active_announcement_index_trigger: NetworkAPI_v1.API_v1_Playlist_Request.IndexMessage
        id_updates: NetworkAPI_v1.API_v1_Playlist_Request.IdMessage
        def __init__(self, playlists: _Optional[_Union[NetworkAPI_v1.API_v1_Playlist_Request.Playlists, _Mapping]] = ..., create_playlist: _Optional[_Union[NetworkAPI_v1.API_v1_Playlist_Request.CreatePlaylist, _Mapping]] = ..., get_playlist: _Optional[_Union[NetworkAPI_v1.API_v1_Playlist_Request.GetPlaylist, _Mapping]] = ..., put_playlist: _Optional[_Union[NetworkAPI_v1.API_v1_Playlist_Request.PutPlaylist, _Mapping]] = ..., post_playlist: _Optional[_Union[NetworkAPI_v1.API_v1_Playlist_Request.PostPlaylist, _Mapping]] = ..., get_active_playlist: _Optional[_Union[NetworkAPI_v1.API_v1_Playlist_Request.GetActivePlaylist, _Mapping]] = ..., focused: _Optional[_Union[NetworkAPI_v1.API_v1_Playlist_Request.GetActivePlaylist, _Mapping]] = ..., next_focus: _Optional[_Union[NetworkAPI_v1.API_v1_Playlist_Request.EmptyMessage, _Mapping]] = ..., previous_focus: _Optional[_Union[NetworkAPI_v1.API_v1_Playlist_Request.EmptyMessage, _Mapping]] = ..., active_presentation_focus: _Optional[_Union[NetworkAPI_v1.API_v1_Playlist_Request.EmptyMessage, _Mapping]] = ..., active_announcement_focus: _Optional[_Union[NetworkAPI_v1.API_v1_Playlist_Request.EmptyMessage, _Mapping]] = ..., focused_trigger: _Optional[_Union[NetworkAPI_v1.API_v1_Playlist_Request.EmptyMessage, _Mapping]] = ..., active_presentation_trigger: _Optional[_Union[NetworkAPI_v1.API_v1_Playlist_Request.EmptyMessage, _Mapping]] = ..., active_announcement_trigger: _Optional[_Union[NetworkAPI_v1.API_v1_Playlist_Request.EmptyMessage, _Mapping]] = ..., focused_next_trigger: _Optional[_Union[NetworkAPI_v1.API_v1_Playlist_Request.EmptyMessage, _Mapping]] = ..., focused_previous_trigger: _Optional[_Union[NetworkAPI_v1.API_v1_Playlist_Request.EmptyMessage, _Mapping]] = ..., active_presentation_next_trigger: _Optional[_Union[NetworkAPI_v1.API_v1_Playlist_Request.EmptyMessage, _Mapping]] = ..., active_announcement_next_trigger: _Optional[_Union[NetworkAPI_v1.API_v1_Playlist_Request.EmptyMessage, _Mapping]] = ..., active_presentation_previous_trigger: _Optional[_Union[NetworkAPI_v1.API_v1_Playlist_Request.EmptyMessage, _Mapping]] = ..., active_announcement_previous_trigger: _Optional[_Union[NetworkAPI_v1.API_v1_Playlist_Request.EmptyMessage, _Mapping]] = ..., id_focus: _Optional[_Union[NetworkAPI_v1.API_v1_Playlist_Request.IdMessage, _Mapping]] = ..., id_trigger: _Optional[_Union[NetworkAPI_v1.API_v1_Playlist_Request.IdMessage, _Mapping]] = ..., id_next_trigger: _Optional[_Union[NetworkAPI_v1.API_v1_Playlist_Request.IdMessage, _Mapping]] = ..., id_previous_trigger: _Optional[_Union[NetworkAPI_v1.API_v1_Playlist_Request.IdMessage, _Mapping]] = ..., focused_index_trigger: _Optional[_Union[NetworkAPI_v1.API_v1_Playlist_Request.IndexMessage, _Mapping]] = ..., active_presentation_index_trigger: _Optional[_Union[NetworkAPI_v1.API_v1_Playlist_Request.IndexMessage, _Mapping]] = ..., active_announcement_index_trigger: _Optional[_Union[NetworkAPI_v1.API_v1_Playlist_Request.IndexMessage, _Mapping]] = ..., id_updates: _Optional[_Union[NetworkAPI_v1.API_v1_Playlist_Request.IdMessage, _Mapping]] = ...) -> None: ...
    class API_v1_Preroll_Request(_message.Message):
        __slots__ = ("preroll_cue", "preroll_playlist_item", "preroll_media_item", "preroll_audio_item", "preroll_video_input", "preroll_library_item", "preroll_next", "preroll_previous", "activate_preroll_item", "cancel_preroll_item")
        class PrerollCue(_message.Message):
            __slots__ = ("index", "preroll_id")
            INDEX_FIELD_NUMBER: _ClassVar[int]
            PREROLL_ID_FIELD_NUMBER: _ClassVar[int]
            index: int
            preroll_id: int
            def __init__(self, index: _Optional[int] = ..., preroll_id: _Optional[int] = ...) -> None: ...
        class PrerollPlaylistItem(_message.Message):
            __slots__ = ("path", "preroll_id")
            PATH_FIELD_NUMBER: _ClassVar[int]
            PREROLL_ID_FIELD_NUMBER: _ClassVar[int]
            path: _containers.RepeatedCompositeFieldContainer[_proApiV1BasicTypes_pb2.API_v1_Identifier]
            preroll_id: int
            def __init__(self, path: _Optional[_Iterable[_Union[_proApiV1BasicTypes_pb2.API_v1_Identifier, _Mapping]]] = ..., preroll_id: _Optional[int] = ...) -> None: ...
        class PrerollMediaItem(_message.Message):
            __slots__ = ("path", "preroll_id")
            PATH_FIELD_NUMBER: _ClassVar[int]
            PREROLL_ID_FIELD_NUMBER: _ClassVar[int]
            path: _containers.RepeatedCompositeFieldContainer[_proApiV1BasicTypes_pb2.API_v1_Identifier]
            preroll_id: int
            def __init__(self, path: _Optional[_Iterable[_Union[_proApiV1BasicTypes_pb2.API_v1_Identifier, _Mapping]]] = ..., preroll_id: _Optional[int] = ...) -> None: ...
        class PrerollAudioItem(_message.Message):
            __slots__ = ("path", "preroll_id")
            PATH_FIELD_NUMBER: _ClassVar[int]
            PREROLL_ID_FIELD_NUMBER: _ClassVar[int]
            path: _containers.RepeatedCompositeFieldContainer[_proApiV1BasicTypes_pb2.API_v1_Identifier]
            preroll_id: int
            def __init__(self, path: _Optional[_Iterable[_Union[_proApiV1BasicTypes_pb2.API_v1_Identifier, _Mapping]]] = ..., preroll_id: _Optional[int] = ...) -> None: ...
        class PrerollVideoInput(_message.Message):
            __slots__ = ("id", "preroll_id")
            ID_FIELD_NUMBER: _ClassVar[int]
            PREROLL_ID_FIELD_NUMBER: _ClassVar[int]
            id: str
            preroll_id: int
            def __init__(self, id: _Optional[str] = ..., preroll_id: _Optional[int] = ...) -> None: ...
        class PrerollLibraryItem(_message.Message):
            __slots__ = ("path", "preroll_id")
            PATH_FIELD_NUMBER: _ClassVar[int]
            PREROLL_ID_FIELD_NUMBER: _ClassVar[int]
            path: _containers.RepeatedCompositeFieldContainer[_proApiV1BasicTypes_pb2.API_v1_Identifier]
            preroll_id: int
            def __init__(self, path: _Optional[_Iterable[_Union[_proApiV1BasicTypes_pb2.API_v1_Identifier, _Mapping]]] = ..., preroll_id: _Optional[int] = ...) -> None: ...
        class PrerollNext(_message.Message):
            __slots__ = ("preroll_id",)
            PREROLL_ID_FIELD_NUMBER: _ClassVar[int]
            preroll_id: int
            def __init__(self, preroll_id: _Optional[int] = ...) -> None: ...
        class PrerollPrevious(_message.Message):
            __slots__ = ("preroll_id",)
            PREROLL_ID_FIELD_NUMBER: _ClassVar[int]
            preroll_id: int
            def __init__(self, preroll_id: _Optional[int] = ...) -> None: ...
        class ActivatePrerollItem(_message.Message):
            __slots__ = ("id", "time")
            ID_FIELD_NUMBER: _ClassVar[int]
            TIME_FIELD_NUMBER: _ClassVar[int]
            id: int
            time: int
            def __init__(self, id: _Optional[int] = ..., time: _Optional[int] = ...) -> None: ...
        class CancelPrerollItem(_message.Message):
            __slots__ = ("id",)
            ID_FIELD_NUMBER: _ClassVar[int]
            id: int
            def __init__(self, id: _Optional[int] = ...) -> None: ...
        PREROLL_CUE_FIELD_NUMBER: _ClassVar[int]
        PREROLL_PLAYLIST_ITEM_FIELD_NUMBER: _ClassVar[int]
        PREROLL_MEDIA_ITEM_FIELD_NUMBER: _ClassVar[int]
        PREROLL_AUDIO_ITEM_FIELD_NUMBER: _ClassVar[int]
        PREROLL_VIDEO_INPUT_FIELD_NUMBER: _ClassVar[int]
        PREROLL_LIBRARY_ITEM_FIELD_NUMBER: _ClassVar[int]
        PREROLL_NEXT_FIELD_NUMBER: _ClassVar[int]
        PREROLL_PREVIOUS_FIELD_NUMBER: _ClassVar[int]
        ACTIVATE_PREROLL_ITEM_FIELD_NUMBER: _ClassVar[int]
        CANCEL_PREROLL_ITEM_FIELD_NUMBER: _ClassVar[int]
        preroll_cue: NetworkAPI_v1.API_v1_Preroll_Request.PrerollCue
        preroll_playlist_item: NetworkAPI_v1.API_v1_Preroll_Request.PrerollPlaylistItem
        preroll_media_item: NetworkAPI_v1.API_v1_Preroll_Request.PrerollMediaItem
        preroll_audio_item: NetworkAPI_v1.API_v1_Preroll_Request.PrerollAudioItem
        preroll_video_input: NetworkAPI_v1.API_v1_Preroll_Request.PrerollVideoInput
        preroll_library_item: NetworkAPI_v1.API_v1_Preroll_Request.PrerollLibraryItem
        preroll_next: NetworkAPI_v1.API_v1_Preroll_Request.PrerollNext
        preroll_previous: NetworkAPI_v1.API_v1_Preroll_Request.PrerollPrevious
        activate_preroll_item: NetworkAPI_v1.API_v1_Preroll_Request.ActivatePrerollItem
        cancel_preroll_item: NetworkAPI_v1.API_v1_Preroll_Request.CancelPrerollItem
        def __init__(self, preroll_cue: _Optional[_Union[NetworkAPI_v1.API_v1_Preroll_Request.PrerollCue, _Mapping]] = ..., preroll_playlist_item: _Optional[_Union[NetworkAPI_v1.API_v1_Preroll_Request.PrerollPlaylistItem, _Mapping]] = ..., preroll_media_item: _Optional[_Union[NetworkAPI_v1.API_v1_Preroll_Request.PrerollMediaItem, _Mapping]] = ..., preroll_audio_item: _Optional[_Union[NetworkAPI_v1.API_v1_Preroll_Request.PrerollAudioItem, _Mapping]] = ..., preroll_video_input: _Optional[_Union[NetworkAPI_v1.API_v1_Preroll_Request.PrerollVideoInput, _Mapping]] = ..., preroll_library_item: _Optional[_Union[NetworkAPI_v1.API_v1_Preroll_Request.PrerollLibraryItem, _Mapping]] = ..., preroll_next: _Optional[_Union[NetworkAPI_v1.API_v1_Preroll_Request.PrerollNext, _Mapping]] = ..., preroll_previous: _Optional[_Union[NetworkAPI_v1.API_v1_Preroll_Request.PrerollPrevious, _Mapping]] = ..., activate_preroll_item: _Optional[_Union[NetworkAPI_v1.API_v1_Preroll_Request.ActivatePrerollItem, _Mapping]] = ..., cancel_preroll_item: _Optional[_Union[NetworkAPI_v1.API_v1_Preroll_Request.CancelPrerollItem, _Mapping]] = ...) -> None: ...
    class API_v1_Presentation_Request(_message.Message):
        __slots__ = ("active", "focused", "slide_index", "chord_chart", "chord_chart_updates", "presentation", "delete_presentation", "timeline_operation", "active_presentation_timeline_operation", "focused_presentation_timeline_operation", "active_presentation_timeline_status", "focused_presentation_timeline_status", "thumbnail", "focus", "trigger")
        class Active(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class SlideIndex(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class ChordChart(_message.Message):
            __slots__ = ("quality",)
            QUALITY_FIELD_NUMBER: _ClassVar[int]
            quality: int
            def __init__(self, quality: _Optional[int] = ...) -> None: ...
        class ChordChartUpdates(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class Presentation(_message.Message):
            __slots__ = ("uuid",)
            UUID_FIELD_NUMBER: _ClassVar[int]
            uuid: _basicTypes_pb2.UUID
            def __init__(self, uuid: _Optional[_Union[_basicTypes_pb2.UUID, _Mapping]] = ...) -> None: ...
        class DeletePresentation(_message.Message):
            __slots__ = ("uuid",)
            UUID_FIELD_NUMBER: _ClassVar[int]
            uuid: _basicTypes_pb2.UUID
            def __init__(self, uuid: _Optional[_Union[_basicTypes_pb2.UUID, _Mapping]] = ...) -> None: ...
        class TimelineOperation(_message.Message):
            __slots__ = ("uuid", "operation")
            class API_v1_TimelineOperation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                play: _ClassVar[NetworkAPI_v1.API_v1_Presentation_Request.TimelineOperation.API_v1_TimelineOperation]
                pause: _ClassVar[NetworkAPI_v1.API_v1_Presentation_Request.TimelineOperation.API_v1_TimelineOperation]
                rewind: _ClassVar[NetworkAPI_v1.API_v1_Presentation_Request.TimelineOperation.API_v1_TimelineOperation]
            play: NetworkAPI_v1.API_v1_Presentation_Request.TimelineOperation.API_v1_TimelineOperation
            pause: NetworkAPI_v1.API_v1_Presentation_Request.TimelineOperation.API_v1_TimelineOperation
            rewind: NetworkAPI_v1.API_v1_Presentation_Request.TimelineOperation.API_v1_TimelineOperation
            UUID_FIELD_NUMBER: _ClassVar[int]
            OPERATION_FIELD_NUMBER: _ClassVar[int]
            uuid: _basicTypes_pb2.UUID
            operation: NetworkAPI_v1.API_v1_Presentation_Request.TimelineOperation.API_v1_TimelineOperation
            def __init__(self, uuid: _Optional[_Union[_basicTypes_pb2.UUID, _Mapping]] = ..., operation: _Optional[_Union[NetworkAPI_v1.API_v1_Presentation_Request.TimelineOperation.API_v1_TimelineOperation, str]] = ...) -> None: ...
        class ActivePresentationTimelineOperation(_message.Message):
            __slots__ = ("operation",)
            class API_v1_TimelineOperation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                play: _ClassVar[NetworkAPI_v1.API_v1_Presentation_Request.ActivePresentationTimelineOperation.API_v1_TimelineOperation]
                pause: _ClassVar[NetworkAPI_v1.API_v1_Presentation_Request.ActivePresentationTimelineOperation.API_v1_TimelineOperation]
                rewind: _ClassVar[NetworkAPI_v1.API_v1_Presentation_Request.ActivePresentationTimelineOperation.API_v1_TimelineOperation]
            play: NetworkAPI_v1.API_v1_Presentation_Request.ActivePresentationTimelineOperation.API_v1_TimelineOperation
            pause: NetworkAPI_v1.API_v1_Presentation_Request.ActivePresentationTimelineOperation.API_v1_TimelineOperation
            rewind: NetworkAPI_v1.API_v1_Presentation_Request.ActivePresentationTimelineOperation.API_v1_TimelineOperation
            OPERATION_FIELD_NUMBER: _ClassVar[int]
            operation: NetworkAPI_v1.API_v1_Presentation_Request.ActivePresentationTimelineOperation.API_v1_TimelineOperation
            def __init__(self, operation: _Optional[_Union[NetworkAPI_v1.API_v1_Presentation_Request.ActivePresentationTimelineOperation.API_v1_TimelineOperation, str]] = ...) -> None: ...
        class FocusedPresentationTimelineOperation(_message.Message):
            __slots__ = ("operation",)
            class API_v1_TimelineOperation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                play: _ClassVar[NetworkAPI_v1.API_v1_Presentation_Request.FocusedPresentationTimelineOperation.API_v1_TimelineOperation]
                pause: _ClassVar[NetworkAPI_v1.API_v1_Presentation_Request.FocusedPresentationTimelineOperation.API_v1_TimelineOperation]
                rewind: _ClassVar[NetworkAPI_v1.API_v1_Presentation_Request.FocusedPresentationTimelineOperation.API_v1_TimelineOperation]
            play: NetworkAPI_v1.API_v1_Presentation_Request.FocusedPresentationTimelineOperation.API_v1_TimelineOperation
            pause: NetworkAPI_v1.API_v1_Presentation_Request.FocusedPresentationTimelineOperation.API_v1_TimelineOperation
            rewind: NetworkAPI_v1.API_v1_Presentation_Request.FocusedPresentationTimelineOperation.API_v1_TimelineOperation
            OPERATION_FIELD_NUMBER: _ClassVar[int]
            operation: NetworkAPI_v1.API_v1_Presentation_Request.FocusedPresentationTimelineOperation.API_v1_TimelineOperation
            def __init__(self, operation: _Optional[_Union[NetworkAPI_v1.API_v1_Presentation_Request.FocusedPresentationTimelineOperation.API_v1_TimelineOperation, str]] = ...) -> None: ...
        class ActivePresentationTimelineStatus(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class FocusedPresentationTimelineStatus(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class Thumbnail(_message.Message):
            __slots__ = ("uuid", "cue_index", "quality", "content_type")
            class API_v1_ContentType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                PNG: _ClassVar[NetworkAPI_v1.API_v1_Presentation_Request.Thumbnail.API_v1_ContentType]
                JPEG: _ClassVar[NetworkAPI_v1.API_v1_Presentation_Request.Thumbnail.API_v1_ContentType]
            PNG: NetworkAPI_v1.API_v1_Presentation_Request.Thumbnail.API_v1_ContentType
            JPEG: NetworkAPI_v1.API_v1_Presentation_Request.Thumbnail.API_v1_ContentType
            UUID_FIELD_NUMBER: _ClassVar[int]
            CUE_INDEX_FIELD_NUMBER: _ClassVar[int]
            QUALITY_FIELD_NUMBER: _ClassVar[int]
            CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
            uuid: _basicTypes_pb2.UUID
            cue_index: int
            quality: int
            content_type: NetworkAPI_v1.API_v1_Presentation_Request.Thumbnail.API_v1_ContentType
            def __init__(self, uuid: _Optional[_Union[_basicTypes_pb2.UUID, _Mapping]] = ..., cue_index: _Optional[int] = ..., quality: _Optional[int] = ..., content_type: _Optional[_Union[NetworkAPI_v1.API_v1_Presentation_Request.Thumbnail.API_v1_ContentType, str]] = ...) -> None: ...
        class EmptyMessage(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class FocusMessage(_message.Message):
            __slots__ = ("next", "previous", "active", "uuid")
            NEXT_FIELD_NUMBER: _ClassVar[int]
            PREVIOUS_FIELD_NUMBER: _ClassVar[int]
            ACTIVE_FIELD_NUMBER: _ClassVar[int]
            UUID_FIELD_NUMBER: _ClassVar[int]
            next: NetworkAPI_v1.API_v1_Presentation_Request.EmptyMessage
            previous: NetworkAPI_v1.API_v1_Presentation_Request.EmptyMessage
            active: NetworkAPI_v1.API_v1_Presentation_Request.EmptyMessage
            uuid: str
            def __init__(self, next: _Optional[_Union[NetworkAPI_v1.API_v1_Presentation_Request.EmptyMessage, _Mapping]] = ..., previous: _Optional[_Union[NetworkAPI_v1.API_v1_Presentation_Request.EmptyMessage, _Mapping]] = ..., active: _Optional[_Union[NetworkAPI_v1.API_v1_Presentation_Request.EmptyMessage, _Mapping]] = ..., uuid: _Optional[str] = ...) -> None: ...
        class TriggerMessage(_message.Message):
            __slots__ = ("focused", "active", "uuid", "first", "next", "previous", "index", "group")
            FOCUSED_FIELD_NUMBER: _ClassVar[int]
            ACTIVE_FIELD_NUMBER: _ClassVar[int]
            UUID_FIELD_NUMBER: _ClassVar[int]
            FIRST_FIELD_NUMBER: _ClassVar[int]
            NEXT_FIELD_NUMBER: _ClassVar[int]
            PREVIOUS_FIELD_NUMBER: _ClassVar[int]
            INDEX_FIELD_NUMBER: _ClassVar[int]
            GROUP_FIELD_NUMBER: _ClassVar[int]
            focused: NetworkAPI_v1.API_v1_Presentation_Request.EmptyMessage
            active: NetworkAPI_v1.API_v1_Presentation_Request.EmptyMessage
            uuid: _wrappers_pb2.StringValue
            first: NetworkAPI_v1.API_v1_Presentation_Request.EmptyMessage
            next: NetworkAPI_v1.API_v1_Presentation_Request.EmptyMessage
            previous: NetworkAPI_v1.API_v1_Presentation_Request.EmptyMessage
            index: _wrappers_pb2.UInt32Value
            group: _wrappers_pb2.StringValue
            def __init__(self, focused: _Optional[_Union[NetworkAPI_v1.API_v1_Presentation_Request.EmptyMessage, _Mapping]] = ..., active: _Optional[_Union[NetworkAPI_v1.API_v1_Presentation_Request.EmptyMessage, _Mapping]] = ..., uuid: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., first: _Optional[_Union[NetworkAPI_v1.API_v1_Presentation_Request.EmptyMessage, _Mapping]] = ..., next: _Optional[_Union[NetworkAPI_v1.API_v1_Presentation_Request.EmptyMessage, _Mapping]] = ..., previous: _Optional[_Union[NetworkAPI_v1.API_v1_Presentation_Request.EmptyMessage, _Mapping]] = ..., index: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ..., group: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...) -> None: ...
        ACTIVE_FIELD_NUMBER: _ClassVar[int]
        FOCUSED_FIELD_NUMBER: _ClassVar[int]
        SLIDE_INDEX_FIELD_NUMBER: _ClassVar[int]
        CHORD_CHART_FIELD_NUMBER: _ClassVar[int]
        CHORD_CHART_UPDATES_FIELD_NUMBER: _ClassVar[int]
        PRESENTATION_FIELD_NUMBER: _ClassVar[int]
        DELETE_PRESENTATION_FIELD_NUMBER: _ClassVar[int]
        TIMELINE_OPERATION_FIELD_NUMBER: _ClassVar[int]
        ACTIVE_PRESENTATION_TIMELINE_OPERATION_FIELD_NUMBER: _ClassVar[int]
        FOCUSED_PRESENTATION_TIMELINE_OPERATION_FIELD_NUMBER: _ClassVar[int]
        ACTIVE_PRESENTATION_TIMELINE_STATUS_FIELD_NUMBER: _ClassVar[int]
        FOCUSED_PRESENTATION_TIMELINE_STATUS_FIELD_NUMBER: _ClassVar[int]
        THUMBNAIL_FIELD_NUMBER: _ClassVar[int]
        FOCUS_FIELD_NUMBER: _ClassVar[int]
        TRIGGER_FIELD_NUMBER: _ClassVar[int]
        active: NetworkAPI_v1.API_v1_Presentation_Request.Active
        focused: NetworkAPI_v1.API_v1_Presentation_Request.EmptyMessage
        slide_index: NetworkAPI_v1.API_v1_Presentation_Request.SlideIndex
        chord_chart: NetworkAPI_v1.API_v1_Presentation_Request.ChordChart
        chord_chart_updates: NetworkAPI_v1.API_v1_Presentation_Request.ChordChartUpdates
        presentation: NetworkAPI_v1.API_v1_Presentation_Request.Presentation
        delete_presentation: NetworkAPI_v1.API_v1_Presentation_Request.DeletePresentation
        timeline_operation: NetworkAPI_v1.API_v1_Presentation_Request.TimelineOperation
        active_presentation_timeline_operation: NetworkAPI_v1.API_v1_Presentation_Request.ActivePresentationTimelineOperation
        focused_presentation_timeline_operation: NetworkAPI_v1.API_v1_Presentation_Request.FocusedPresentationTimelineOperation
        active_presentation_timeline_status: NetworkAPI_v1.API_v1_Presentation_Request.ActivePresentationTimelineStatus
        focused_presentation_timeline_status: NetworkAPI_v1.API_v1_Presentation_Request.FocusedPresentationTimelineStatus
        thumbnail: NetworkAPI_v1.API_v1_Presentation_Request.Thumbnail
        focus: NetworkAPI_v1.API_v1_Presentation_Request.FocusMessage
        trigger: NetworkAPI_v1.API_v1_Presentation_Request.TriggerMessage
        def __init__(self, active: _Optional[_Union[NetworkAPI_v1.API_v1_Presentation_Request.Active, _Mapping]] = ..., focused: _Optional[_Union[NetworkAPI_v1.API_v1_Presentation_Request.EmptyMessage, _Mapping]] = ..., slide_index: _Optional[_Union[NetworkAPI_v1.API_v1_Presentation_Request.SlideIndex, _Mapping]] = ..., chord_chart: _Optional[_Union[NetworkAPI_v1.API_v1_Presentation_Request.ChordChart, _Mapping]] = ..., chord_chart_updates: _Optional[_Union[NetworkAPI_v1.API_v1_Presentation_Request.ChordChartUpdates, _Mapping]] = ..., presentation: _Optional[_Union[NetworkAPI_v1.API_v1_Presentation_Request.Presentation, _Mapping]] = ..., delete_presentation: _Optional[_Union[NetworkAPI_v1.API_v1_Presentation_Request.DeletePresentation, _Mapping]] = ..., timeline_operation: _Optional[_Union[NetworkAPI_v1.API_v1_Presentation_Request.TimelineOperation, _Mapping]] = ..., active_presentation_timeline_operation: _Optional[_Union[NetworkAPI_v1.API_v1_Presentation_Request.ActivePresentationTimelineOperation, _Mapping]] = ..., focused_presentation_timeline_operation: _Optional[_Union[NetworkAPI_v1.API_v1_Presentation_Request.FocusedPresentationTimelineOperation, _Mapping]] = ..., active_presentation_timeline_status: _Optional[_Union[NetworkAPI_v1.API_v1_Presentation_Request.ActivePresentationTimelineStatus, _Mapping]] = ..., focused_presentation_timeline_status: _Optional[_Union[NetworkAPI_v1.API_v1_Presentation_Request.FocusedPresentationTimelineStatus, _Mapping]] = ..., thumbnail: _Optional[_Union[NetworkAPI_v1.API_v1_Presentation_Request.Thumbnail, _Mapping]] = ..., focus: _Optional[_Union[NetworkAPI_v1.API_v1_Presentation_Request.FocusMessage, _Mapping]] = ..., trigger: _Optional[_Union[NetworkAPI_v1.API_v1_Presentation_Request.TriggerMessage, _Mapping]] = ...) -> None: ...
    class API_v1_Prop_Request(_message.Message):
        __slots__ = ("props", "get_prop", "delete_prop", "trigger_prop", "clear_prop", "get_thumbnail")
        class Props(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class GetProp(_message.Message):
            __slots__ = ("id",)
            ID_FIELD_NUMBER: _ClassVar[int]
            id: str
            def __init__(self, id: _Optional[str] = ...) -> None: ...
        class DeleteProp(_message.Message):
            __slots__ = ("id",)
            ID_FIELD_NUMBER: _ClassVar[int]
            id: str
            def __init__(self, id: _Optional[str] = ...) -> None: ...
        class TriggerProp(_message.Message):
            __slots__ = ("id",)
            ID_FIELD_NUMBER: _ClassVar[int]
            id: str
            def __init__(self, id: _Optional[str] = ...) -> None: ...
        class ClearProp(_message.Message):
            __slots__ = ("id",)
            ID_FIELD_NUMBER: _ClassVar[int]
            id: str
            def __init__(self, id: _Optional[str] = ...) -> None: ...
        class GetThumbnail(_message.Message):
            __slots__ = ("id", "quality")
            ID_FIELD_NUMBER: _ClassVar[int]
            QUALITY_FIELD_NUMBER: _ClassVar[int]
            id: str
            quality: int
            def __init__(self, id: _Optional[str] = ..., quality: _Optional[int] = ...) -> None: ...
        PROPS_FIELD_NUMBER: _ClassVar[int]
        GET_PROP_FIELD_NUMBER: _ClassVar[int]
        DELETE_PROP_FIELD_NUMBER: _ClassVar[int]
        TRIGGER_PROP_FIELD_NUMBER: _ClassVar[int]
        CLEAR_PROP_FIELD_NUMBER: _ClassVar[int]
        GET_THUMBNAIL_FIELD_NUMBER: _ClassVar[int]
        props: NetworkAPI_v1.API_v1_Prop_Request.Props
        get_prop: NetworkAPI_v1.API_v1_Prop_Request.GetProp
        delete_prop: NetworkAPI_v1.API_v1_Prop_Request.DeleteProp
        trigger_prop: NetworkAPI_v1.API_v1_Prop_Request.TriggerProp
        clear_prop: NetworkAPI_v1.API_v1_Prop_Request.ClearProp
        get_thumbnail: NetworkAPI_v1.API_v1_Prop_Request.GetThumbnail
        def __init__(self, props: _Optional[_Union[NetworkAPI_v1.API_v1_Prop_Request.Props, _Mapping]] = ..., get_prop: _Optional[_Union[NetworkAPI_v1.API_v1_Prop_Request.GetProp, _Mapping]] = ..., delete_prop: _Optional[_Union[NetworkAPI_v1.API_v1_Prop_Request.DeleteProp, _Mapping]] = ..., trigger_prop: _Optional[_Union[NetworkAPI_v1.API_v1_Prop_Request.TriggerProp, _Mapping]] = ..., clear_prop: _Optional[_Union[NetworkAPI_v1.API_v1_Prop_Request.ClearProp, _Mapping]] = ..., get_thumbnail: _Optional[_Union[NetworkAPI_v1.API_v1_Prop_Request.GetThumbnail, _Mapping]] = ...) -> None: ...
    class API_v1_Stage_Request(_message.Message):
        __slots__ = ("get_layout_map", "set_layout_map", "get_message", "put_message", "delete_message", "get_screens", "get_screen_layout", "set_screen_layout", "get_layouts", "delete_layout", "get_layout_thumbnail")
        class GetLayoutMap(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class SetLayoutMap(_message.Message):
            __slots__ = ("map",)
            MAP_FIELD_NUMBER: _ClassVar[int]
            map: _proApiV1BasicTypes_pb2.API_v1_StageLayoutMap
            def __init__(self, map: _Optional[_Union[_proApiV1BasicTypes_pb2.API_v1_StageLayoutMap, _Mapping]] = ...) -> None: ...
        class GetMessage(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class PutMessage(_message.Message):
            __slots__ = ("message",)
            MESSAGE_FIELD_NUMBER: _ClassVar[int]
            message: str
            def __init__(self, message: _Optional[str] = ...) -> None: ...
        class DeleteMessage(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class GetScreens(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class GetScreenLayout(_message.Message):
            __slots__ = ("id",)
            ID_FIELD_NUMBER: _ClassVar[int]
            id: str
            def __init__(self, id: _Optional[str] = ...) -> None: ...
        class SetScreenLayout(_message.Message):
            __slots__ = ("id", "layout")
            ID_FIELD_NUMBER: _ClassVar[int]
            LAYOUT_FIELD_NUMBER: _ClassVar[int]
            id: str
            layout: str
            def __init__(self, id: _Optional[str] = ..., layout: _Optional[str] = ...) -> None: ...
        class GetLayouts(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class DeleteLayout(_message.Message):
            __slots__ = ("id",)
            ID_FIELD_NUMBER: _ClassVar[int]
            id: str
            def __init__(self, id: _Optional[str] = ...) -> None: ...
        class GetLayoutThumbnail(_message.Message):
            __slots__ = ("id", "quality")
            ID_FIELD_NUMBER: _ClassVar[int]
            QUALITY_FIELD_NUMBER: _ClassVar[int]
            id: str
            quality: int
            def __init__(self, id: _Optional[str] = ..., quality: _Optional[int] = ...) -> None: ...
        GET_LAYOUT_MAP_FIELD_NUMBER: _ClassVar[int]
        SET_LAYOUT_MAP_FIELD_NUMBER: _ClassVar[int]
        GET_MESSAGE_FIELD_NUMBER: _ClassVar[int]
        PUT_MESSAGE_FIELD_NUMBER: _ClassVar[int]
        DELETE_MESSAGE_FIELD_NUMBER: _ClassVar[int]
        GET_SCREENS_FIELD_NUMBER: _ClassVar[int]
        GET_SCREEN_LAYOUT_FIELD_NUMBER: _ClassVar[int]
        SET_SCREEN_LAYOUT_FIELD_NUMBER: _ClassVar[int]
        GET_LAYOUTS_FIELD_NUMBER: _ClassVar[int]
        DELETE_LAYOUT_FIELD_NUMBER: _ClassVar[int]
        GET_LAYOUT_THUMBNAIL_FIELD_NUMBER: _ClassVar[int]
        get_layout_map: NetworkAPI_v1.API_v1_Stage_Request.GetLayoutMap
        set_layout_map: NetworkAPI_v1.API_v1_Stage_Request.SetLayoutMap
        get_message: NetworkAPI_v1.API_v1_Stage_Request.GetMessage
        put_message: NetworkAPI_v1.API_v1_Stage_Request.PutMessage
        delete_message: NetworkAPI_v1.API_v1_Stage_Request.DeleteMessage
        get_screens: NetworkAPI_v1.API_v1_Stage_Request.GetScreens
        get_screen_layout: NetworkAPI_v1.API_v1_Stage_Request.GetScreenLayout
        set_screen_layout: NetworkAPI_v1.API_v1_Stage_Request.SetScreenLayout
        get_layouts: NetworkAPI_v1.API_v1_Stage_Request.GetLayouts
        delete_layout: NetworkAPI_v1.API_v1_Stage_Request.DeleteLayout
        get_layout_thumbnail: NetworkAPI_v1.API_v1_Stage_Request.GetLayoutThumbnail
        def __init__(self, get_layout_map: _Optional[_Union[NetworkAPI_v1.API_v1_Stage_Request.GetLayoutMap, _Mapping]] = ..., set_layout_map: _Optional[_Union[NetworkAPI_v1.API_v1_Stage_Request.SetLayoutMap, _Mapping]] = ..., get_message: _Optional[_Union[NetworkAPI_v1.API_v1_Stage_Request.GetMessage, _Mapping]] = ..., put_message: _Optional[_Union[NetworkAPI_v1.API_v1_Stage_Request.PutMessage, _Mapping]] = ..., delete_message: _Optional[_Union[NetworkAPI_v1.API_v1_Stage_Request.DeleteMessage, _Mapping]] = ..., get_screens: _Optional[_Union[NetworkAPI_v1.API_v1_Stage_Request.GetScreens, _Mapping]] = ..., get_screen_layout: _Optional[_Union[NetworkAPI_v1.API_v1_Stage_Request.GetScreenLayout, _Mapping]] = ..., set_screen_layout: _Optional[_Union[NetworkAPI_v1.API_v1_Stage_Request.SetScreenLayout, _Mapping]] = ..., get_layouts: _Optional[_Union[NetworkAPI_v1.API_v1_Stage_Request.GetLayouts, _Mapping]] = ..., delete_layout: _Optional[_Union[NetworkAPI_v1.API_v1_Stage_Request.DeleteLayout, _Mapping]] = ..., get_layout_thumbnail: _Optional[_Union[NetworkAPI_v1.API_v1_Stage_Request.GetLayoutThumbnail, _Mapping]] = ...) -> None: ...
    class API_v1_Status_Request(_message.Message):
        __slots__ = ("get_layers", "get_stage_screens", "put_stage_screens", "get_audience_screens", "put_audience_screens", "get_screens", "get_slide")
        class GetLayers(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class GetStageScreens(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class PutStageScreens(_message.Message):
            __slots__ = ("enabled",)
            ENABLED_FIELD_NUMBER: _ClassVar[int]
            enabled: bool
            def __init__(self, enabled: bool = ...) -> None: ...
        class GetAudienceScreens(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class PutAudienceScreens(_message.Message):
            __slots__ = ("enabled",)
            ENABLED_FIELD_NUMBER: _ClassVar[int]
            enabled: bool
            def __init__(self, enabled: bool = ...) -> None: ...
        class GetScreens(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class GetSlide(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        GET_LAYERS_FIELD_NUMBER: _ClassVar[int]
        GET_STAGE_SCREENS_FIELD_NUMBER: _ClassVar[int]
        PUT_STAGE_SCREENS_FIELD_NUMBER: _ClassVar[int]
        GET_AUDIENCE_SCREENS_FIELD_NUMBER: _ClassVar[int]
        PUT_AUDIENCE_SCREENS_FIELD_NUMBER: _ClassVar[int]
        GET_SCREENS_FIELD_NUMBER: _ClassVar[int]
        GET_SLIDE_FIELD_NUMBER: _ClassVar[int]
        get_layers: NetworkAPI_v1.API_v1_Status_Request.GetLayers
        get_stage_screens: NetworkAPI_v1.API_v1_Status_Request.GetStageScreens
        put_stage_screens: NetworkAPI_v1.API_v1_Status_Request.PutStageScreens
        get_audience_screens: NetworkAPI_v1.API_v1_Status_Request.GetAudienceScreens
        put_audience_screens: NetworkAPI_v1.API_v1_Status_Request.PutAudienceScreens
        get_screens: NetworkAPI_v1.API_v1_Status_Request.GetScreens
        get_slide: NetworkAPI_v1.API_v1_Status_Request.GetSlide
        def __init__(self, get_layers: _Optional[_Union[NetworkAPI_v1.API_v1_Status_Request.GetLayers, _Mapping]] = ..., get_stage_screens: _Optional[_Union[NetworkAPI_v1.API_v1_Status_Request.GetStageScreens, _Mapping]] = ..., put_stage_screens: _Optional[_Union[NetworkAPI_v1.API_v1_Status_Request.PutStageScreens, _Mapping]] = ..., get_audience_screens: _Optional[_Union[NetworkAPI_v1.API_v1_Status_Request.GetAudienceScreens, _Mapping]] = ..., put_audience_screens: _Optional[_Union[NetworkAPI_v1.API_v1_Status_Request.PutAudienceScreens, _Mapping]] = ..., get_screens: _Optional[_Union[NetworkAPI_v1.API_v1_Status_Request.GetScreens, _Mapping]] = ..., get_slide: _Optional[_Union[NetworkAPI_v1.API_v1_Status_Request.GetSlide, _Mapping]] = ...) -> None: ...
    class API_v1_Theme_Request(_message.Message):
        __slots__ = ("get_all", "get_theme", "delete_theme", "get_theme_name", "put_theme_name", "get_theme_slide", "put_theme_slide", "delete_theme_slide", "get_theme_slide_thumbnail")
        class GetAll(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class GetTheme(_message.Message):
            __slots__ = ("id",)
            ID_FIELD_NUMBER: _ClassVar[int]
            id: str
            def __init__(self, id: _Optional[str] = ...) -> None: ...
        class DeleteTheme(_message.Message):
            __slots__ = ("id",)
            ID_FIELD_NUMBER: _ClassVar[int]
            id: str
            def __init__(self, id: _Optional[str] = ...) -> None: ...
        class GetThemeName(_message.Message):
            __slots__ = ("id",)
            ID_FIELD_NUMBER: _ClassVar[int]
            id: str
            def __init__(self, id: _Optional[str] = ...) -> None: ...
        class PutThemeName(_message.Message):
            __slots__ = ("id", "name")
            ID_FIELD_NUMBER: _ClassVar[int]
            NAME_FIELD_NUMBER: _ClassVar[int]
            id: str
            name: str
            def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...
        class GetThemeSlide(_message.Message):
            __slots__ = ("id", "theme_slide")
            ID_FIELD_NUMBER: _ClassVar[int]
            THEME_SLIDE_FIELD_NUMBER: _ClassVar[int]
            id: str
            theme_slide: str
            def __init__(self, id: _Optional[str] = ..., theme_slide: _Optional[str] = ...) -> None: ...
        class PutThemeSlide(_message.Message):
            __slots__ = ("id", "theme_slide", "slide")
            ID_FIELD_NUMBER: _ClassVar[int]
            THEME_SLIDE_FIELD_NUMBER: _ClassVar[int]
            SLIDE_FIELD_NUMBER: _ClassVar[int]
            id: str
            theme_slide: str
            slide: _proApiV1BasicTypes_pb2.API_v1_ThemeSlide
            def __init__(self, id: _Optional[str] = ..., theme_slide: _Optional[str] = ..., slide: _Optional[_Union[_proApiV1BasicTypes_pb2.API_v1_ThemeSlide, _Mapping]] = ...) -> None: ...
        class DeleteThemeSlide(_message.Message):
            __slots__ = ("id", "theme_slide")
            ID_FIELD_NUMBER: _ClassVar[int]
            THEME_SLIDE_FIELD_NUMBER: _ClassVar[int]
            id: str
            theme_slide: str
            def __init__(self, id: _Optional[str] = ..., theme_slide: _Optional[str] = ...) -> None: ...
        class GetThemeSlideThumbnail(_message.Message):
            __slots__ = ("id", "theme_slide", "quality")
            ID_FIELD_NUMBER: _ClassVar[int]
            THEME_SLIDE_FIELD_NUMBER: _ClassVar[int]
            QUALITY_FIELD_NUMBER: _ClassVar[int]
            id: str
            theme_slide: str
            quality: int
            def __init__(self, id: _Optional[str] = ..., theme_slide: _Optional[str] = ..., quality: _Optional[int] = ...) -> None: ...
        GET_ALL_FIELD_NUMBER: _ClassVar[int]
        GET_THEME_FIELD_NUMBER: _ClassVar[int]
        DELETE_THEME_FIELD_NUMBER: _ClassVar[int]
        GET_THEME_NAME_FIELD_NUMBER: _ClassVar[int]
        PUT_THEME_NAME_FIELD_NUMBER: _ClassVar[int]
        GET_THEME_SLIDE_FIELD_NUMBER: _ClassVar[int]
        PUT_THEME_SLIDE_FIELD_NUMBER: _ClassVar[int]
        DELETE_THEME_SLIDE_FIELD_NUMBER: _ClassVar[int]
        GET_THEME_SLIDE_THUMBNAIL_FIELD_NUMBER: _ClassVar[int]
        get_all: NetworkAPI_v1.API_v1_Theme_Request.GetAll
        get_theme: NetworkAPI_v1.API_v1_Theme_Request.GetTheme
        delete_theme: NetworkAPI_v1.API_v1_Theme_Request.DeleteTheme
        get_theme_name: NetworkAPI_v1.API_v1_Theme_Request.GetThemeName
        put_theme_name: NetworkAPI_v1.API_v1_Theme_Request.PutThemeName
        get_theme_slide: NetworkAPI_v1.API_v1_Theme_Request.GetThemeSlide
        put_theme_slide: NetworkAPI_v1.API_v1_Theme_Request.PutThemeSlide
        delete_theme_slide: NetworkAPI_v1.API_v1_Theme_Request.DeleteThemeSlide
        get_theme_slide_thumbnail: NetworkAPI_v1.API_v1_Theme_Request.GetThemeSlideThumbnail
        def __init__(self, get_all: _Optional[_Union[NetworkAPI_v1.API_v1_Theme_Request.GetAll, _Mapping]] = ..., get_theme: _Optional[_Union[NetworkAPI_v1.API_v1_Theme_Request.GetTheme, _Mapping]] = ..., delete_theme: _Optional[_Union[NetworkAPI_v1.API_v1_Theme_Request.DeleteTheme, _Mapping]] = ..., get_theme_name: _Optional[_Union[NetworkAPI_v1.API_v1_Theme_Request.GetThemeName, _Mapping]] = ..., put_theme_name: _Optional[_Union[NetworkAPI_v1.API_v1_Theme_Request.PutThemeName, _Mapping]] = ..., get_theme_slide: _Optional[_Union[NetworkAPI_v1.API_v1_Theme_Request.GetThemeSlide, _Mapping]] = ..., put_theme_slide: _Optional[_Union[NetworkAPI_v1.API_v1_Theme_Request.PutThemeSlide, _Mapping]] = ..., delete_theme_slide: _Optional[_Union[NetworkAPI_v1.API_v1_Theme_Request.DeleteThemeSlide, _Mapping]] = ..., get_theme_slide_thumbnail: _Optional[_Union[NetworkAPI_v1.API_v1_Theme_Request.GetThemeSlideThumbnail, _Mapping]] = ...) -> None: ...
    class API_v1_Timer_Request(_message.Message):
        __slots__ = ("timers", "create_timer", "current_times", "all_timers_operation", "get_timer", "put_timer", "delete_timer", "timer_operation", "system_time", "video_countdown")
        class Timers(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class CreateTimer(_message.Message):
            __slots__ = ("name", "allows_overrun", "countdown", "count_down_to_time", "elapsed")
            NAME_FIELD_NUMBER: _ClassVar[int]
            ALLOWS_OVERRUN_FIELD_NUMBER: _ClassVar[int]
            COUNTDOWN_FIELD_NUMBER: _ClassVar[int]
            COUNT_DOWN_TO_TIME_FIELD_NUMBER: _ClassVar[int]
            ELAPSED_FIELD_NUMBER: _ClassVar[int]
            name: str
            allows_overrun: bool
            countdown: _proApiV1BasicTypes_pb2.API_v1_Timer.API_v1_Timer_Countdown
            count_down_to_time: _proApiV1BasicTypes_pb2.API_v1_Timer.API_v1_Timer_CountdownToTime
            elapsed: _proApiV1BasicTypes_pb2.API_v1_Timer.API_v1_Timer_Elapsed
            def __init__(self, name: _Optional[str] = ..., allows_overrun: bool = ..., countdown: _Optional[_Union[_proApiV1BasicTypes_pb2.API_v1_Timer.API_v1_Timer_Countdown, _Mapping]] = ..., count_down_to_time: _Optional[_Union[_proApiV1BasicTypes_pb2.API_v1_Timer.API_v1_Timer_CountdownToTime, _Mapping]] = ..., elapsed: _Optional[_Union[_proApiV1BasicTypes_pb2.API_v1_Timer.API_v1_Timer_Elapsed, _Mapping]] = ...) -> None: ...
        class CurrentTimes(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class AllTimersOperation(_message.Message):
            __slots__ = ("operation",)
            class API_v1_TimerOperation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                start: _ClassVar[NetworkAPI_v1.API_v1_Timer_Request.AllTimersOperation.API_v1_TimerOperation]
                stop: _ClassVar[NetworkAPI_v1.API_v1_Timer_Request.AllTimersOperation.API_v1_TimerOperation]
                reset: _ClassVar[NetworkAPI_v1.API_v1_Timer_Request.AllTimersOperation.API_v1_TimerOperation]
            start: NetworkAPI_v1.API_v1_Timer_Request.AllTimersOperation.API_v1_TimerOperation
            stop: NetworkAPI_v1.API_v1_Timer_Request.AllTimersOperation.API_v1_TimerOperation
            reset: NetworkAPI_v1.API_v1_Timer_Request.AllTimersOperation.API_v1_TimerOperation
            OPERATION_FIELD_NUMBER: _ClassVar[int]
            operation: NetworkAPI_v1.API_v1_Timer_Request.AllTimersOperation.API_v1_TimerOperation
            def __init__(self, operation: _Optional[_Union[NetworkAPI_v1.API_v1_Timer_Request.AllTimersOperation.API_v1_TimerOperation, str]] = ...) -> None: ...
        class GetTimer(_message.Message):
            __slots__ = ("id",)
            ID_FIELD_NUMBER: _ClassVar[int]
            id: str
            def __init__(self, id: _Optional[str] = ...) -> None: ...
        class PutTimer(_message.Message):
            __slots__ = ("id", "timer")
            ID_FIELD_NUMBER: _ClassVar[int]
            TIMER_FIELD_NUMBER: _ClassVar[int]
            id: str
            timer: _proApiV1BasicTypes_pb2.API_v1_Timer
            def __init__(self, id: _Optional[str] = ..., timer: _Optional[_Union[_proApiV1BasicTypes_pb2.API_v1_Timer, _Mapping]] = ...) -> None: ...
        class DeleteTimer(_message.Message):
            __slots__ = ("id",)
            ID_FIELD_NUMBER: _ClassVar[int]
            id: str
            def __init__(self, id: _Optional[str] = ...) -> None: ...
        class TimerOperation(_message.Message):
            __slots__ = ("id", "operation")
            class API_v1_TimerOperation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                start: _ClassVar[NetworkAPI_v1.API_v1_Timer_Request.TimerOperation.API_v1_TimerOperation]
                stop: _ClassVar[NetworkAPI_v1.API_v1_Timer_Request.TimerOperation.API_v1_TimerOperation]
                reset: _ClassVar[NetworkAPI_v1.API_v1_Timer_Request.TimerOperation.API_v1_TimerOperation]
            start: NetworkAPI_v1.API_v1_Timer_Request.TimerOperation.API_v1_TimerOperation
            stop: NetworkAPI_v1.API_v1_Timer_Request.TimerOperation.API_v1_TimerOperation
            reset: NetworkAPI_v1.API_v1_Timer_Request.TimerOperation.API_v1_TimerOperation
            ID_FIELD_NUMBER: _ClassVar[int]
            OPERATION_FIELD_NUMBER: _ClassVar[int]
            id: str
            operation: NetworkAPI_v1.API_v1_Timer_Request.TimerOperation.API_v1_TimerOperation
            def __init__(self, id: _Optional[str] = ..., operation: _Optional[_Union[NetworkAPI_v1.API_v1_Timer_Request.TimerOperation.API_v1_TimerOperation, str]] = ...) -> None: ...
        class SystemTime(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class VideoCountdown(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        TIMERS_FIELD_NUMBER: _ClassVar[int]
        CREATE_TIMER_FIELD_NUMBER: _ClassVar[int]
        CURRENT_TIMES_FIELD_NUMBER: _ClassVar[int]
        ALL_TIMERS_OPERATION_FIELD_NUMBER: _ClassVar[int]
        GET_TIMER_FIELD_NUMBER: _ClassVar[int]
        PUT_TIMER_FIELD_NUMBER: _ClassVar[int]
        DELETE_TIMER_FIELD_NUMBER: _ClassVar[int]
        TIMER_OPERATION_FIELD_NUMBER: _ClassVar[int]
        SYSTEM_TIME_FIELD_NUMBER: _ClassVar[int]
        VIDEO_COUNTDOWN_FIELD_NUMBER: _ClassVar[int]
        timers: NetworkAPI_v1.API_v1_Timer_Request.Timers
        create_timer: NetworkAPI_v1.API_v1_Timer_Request.CreateTimer
        current_times: NetworkAPI_v1.API_v1_Timer_Request.CurrentTimes
        all_timers_operation: NetworkAPI_v1.API_v1_Timer_Request.AllTimersOperation
        get_timer: NetworkAPI_v1.API_v1_Timer_Request.GetTimer
        put_timer: NetworkAPI_v1.API_v1_Timer_Request.PutTimer
        delete_timer: NetworkAPI_v1.API_v1_Timer_Request.DeleteTimer
        timer_operation: NetworkAPI_v1.API_v1_Timer_Request.TimerOperation
        system_time: NetworkAPI_v1.API_v1_Timer_Request.SystemTime
        video_countdown: NetworkAPI_v1.API_v1_Timer_Request.VideoCountdown
        def __init__(self, timers: _Optional[_Union[NetworkAPI_v1.API_v1_Timer_Request.Timers, _Mapping]] = ..., create_timer: _Optional[_Union[NetworkAPI_v1.API_v1_Timer_Request.CreateTimer, _Mapping]] = ..., current_times: _Optional[_Union[NetworkAPI_v1.API_v1_Timer_Request.CurrentTimes, _Mapping]] = ..., all_timers_operation: _Optional[_Union[NetworkAPI_v1.API_v1_Timer_Request.AllTimersOperation, _Mapping]] = ..., get_timer: _Optional[_Union[NetworkAPI_v1.API_v1_Timer_Request.GetTimer, _Mapping]] = ..., put_timer: _Optional[_Union[NetworkAPI_v1.API_v1_Timer_Request.PutTimer, _Mapping]] = ..., delete_timer: _Optional[_Union[NetworkAPI_v1.API_v1_Timer_Request.DeleteTimer, _Mapping]] = ..., timer_operation: _Optional[_Union[NetworkAPI_v1.API_v1_Timer_Request.TimerOperation, _Mapping]] = ..., system_time: _Optional[_Union[NetworkAPI_v1.API_v1_Timer_Request.SystemTime, _Mapping]] = ..., video_countdown: _Optional[_Union[NetworkAPI_v1.API_v1_Timer_Request.VideoCountdown, _Mapping]] = ...) -> None: ...
    class API_v1_Transport_Request(_message.Message):
        __slots__ = ("play", "pause", "skip_backward", "skip_forward", "go_to_end", "get_time", "put_time", "get_auto_advance", "delete_auto_advance", "get_current_media")
        class Play(_message.Message):
            __slots__ = ("layer",)
            class API_v1_LayerType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                audio: _ClassVar[NetworkAPI_v1.API_v1_Transport_Request.Play.API_v1_LayerType]
                props: _ClassVar[NetworkAPI_v1.API_v1_Transport_Request.Play.API_v1_LayerType]
                messages: _ClassVar[NetworkAPI_v1.API_v1_Transport_Request.Play.API_v1_LayerType]
                announcements: _ClassVar[NetworkAPI_v1.API_v1_Transport_Request.Play.API_v1_LayerType]
                slide: _ClassVar[NetworkAPI_v1.API_v1_Transport_Request.Play.API_v1_LayerType]
                media: _ClassVar[NetworkAPI_v1.API_v1_Transport_Request.Play.API_v1_LayerType]
                video_input: _ClassVar[NetworkAPI_v1.API_v1_Transport_Request.Play.API_v1_LayerType]
            audio: NetworkAPI_v1.API_v1_Transport_Request.Play.API_v1_LayerType
            props: NetworkAPI_v1.API_v1_Transport_Request.Play.API_v1_LayerType
            messages: NetworkAPI_v1.API_v1_Transport_Request.Play.API_v1_LayerType
            announcements: NetworkAPI_v1.API_v1_Transport_Request.Play.API_v1_LayerType
            slide: NetworkAPI_v1.API_v1_Transport_Request.Play.API_v1_LayerType
            media: NetworkAPI_v1.API_v1_Transport_Request.Play.API_v1_LayerType
            video_input: NetworkAPI_v1.API_v1_Transport_Request.Play.API_v1_LayerType
            LAYER_FIELD_NUMBER: _ClassVar[int]
            layer: NetworkAPI_v1.API_v1_Transport_Request.Play.API_v1_LayerType
            def __init__(self, layer: _Optional[_Union[NetworkAPI_v1.API_v1_Transport_Request.Play.API_v1_LayerType, str]] = ...) -> None: ...
        class Pause(_message.Message):
            __slots__ = ("layer",)
            class API_v1_LayerType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                audio: _ClassVar[NetworkAPI_v1.API_v1_Transport_Request.Pause.API_v1_LayerType]
                props: _ClassVar[NetworkAPI_v1.API_v1_Transport_Request.Pause.API_v1_LayerType]
                messages: _ClassVar[NetworkAPI_v1.API_v1_Transport_Request.Pause.API_v1_LayerType]
                announcements: _ClassVar[NetworkAPI_v1.API_v1_Transport_Request.Pause.API_v1_LayerType]
                slide: _ClassVar[NetworkAPI_v1.API_v1_Transport_Request.Pause.API_v1_LayerType]
                media: _ClassVar[NetworkAPI_v1.API_v1_Transport_Request.Pause.API_v1_LayerType]
                video_input: _ClassVar[NetworkAPI_v1.API_v1_Transport_Request.Pause.API_v1_LayerType]
            audio: NetworkAPI_v1.API_v1_Transport_Request.Pause.API_v1_LayerType
            props: NetworkAPI_v1.API_v1_Transport_Request.Pause.API_v1_LayerType
            messages: NetworkAPI_v1.API_v1_Transport_Request.Pause.API_v1_LayerType
            announcements: NetworkAPI_v1.API_v1_Transport_Request.Pause.API_v1_LayerType
            slide: NetworkAPI_v1.API_v1_Transport_Request.Pause.API_v1_LayerType
            media: NetworkAPI_v1.API_v1_Transport_Request.Pause.API_v1_LayerType
            video_input: NetworkAPI_v1.API_v1_Transport_Request.Pause.API_v1_LayerType
            LAYER_FIELD_NUMBER: _ClassVar[int]
            layer: NetworkAPI_v1.API_v1_Transport_Request.Pause.API_v1_LayerType
            def __init__(self, layer: _Optional[_Union[NetworkAPI_v1.API_v1_Transport_Request.Pause.API_v1_LayerType, str]] = ...) -> None: ...
        class SkipBackward(_message.Message):
            __slots__ = ("layer", "seconds")
            class API_v1_LayerType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                audio: _ClassVar[NetworkAPI_v1.API_v1_Transport_Request.SkipBackward.API_v1_LayerType]
                props: _ClassVar[NetworkAPI_v1.API_v1_Transport_Request.SkipBackward.API_v1_LayerType]
                messages: _ClassVar[NetworkAPI_v1.API_v1_Transport_Request.SkipBackward.API_v1_LayerType]
                announcements: _ClassVar[NetworkAPI_v1.API_v1_Transport_Request.SkipBackward.API_v1_LayerType]
                slide: _ClassVar[NetworkAPI_v1.API_v1_Transport_Request.SkipBackward.API_v1_LayerType]
                media: _ClassVar[NetworkAPI_v1.API_v1_Transport_Request.SkipBackward.API_v1_LayerType]
                video_input: _ClassVar[NetworkAPI_v1.API_v1_Transport_Request.SkipBackward.API_v1_LayerType]
            audio: NetworkAPI_v1.API_v1_Transport_Request.SkipBackward.API_v1_LayerType
            props: NetworkAPI_v1.API_v1_Transport_Request.SkipBackward.API_v1_LayerType
            messages: NetworkAPI_v1.API_v1_Transport_Request.SkipBackward.API_v1_LayerType
            announcements: NetworkAPI_v1.API_v1_Transport_Request.SkipBackward.API_v1_LayerType
            slide: NetworkAPI_v1.API_v1_Transport_Request.SkipBackward.API_v1_LayerType
            media: NetworkAPI_v1.API_v1_Transport_Request.SkipBackward.API_v1_LayerType
            video_input: NetworkAPI_v1.API_v1_Transport_Request.SkipBackward.API_v1_LayerType
            LAYER_FIELD_NUMBER: _ClassVar[int]
            SECONDS_FIELD_NUMBER: _ClassVar[int]
            layer: NetworkAPI_v1.API_v1_Transport_Request.SkipBackward.API_v1_LayerType
            seconds: float
            def __init__(self, layer: _Optional[_Union[NetworkAPI_v1.API_v1_Transport_Request.SkipBackward.API_v1_LayerType, str]] = ..., seconds: _Optional[float] = ...) -> None: ...
        class SkipForward(_message.Message):
            __slots__ = ("layer", "seconds")
            class API_v1_LayerType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                audio: _ClassVar[NetworkAPI_v1.API_v1_Transport_Request.SkipForward.API_v1_LayerType]
                props: _ClassVar[NetworkAPI_v1.API_v1_Transport_Request.SkipForward.API_v1_LayerType]
                messages: _ClassVar[NetworkAPI_v1.API_v1_Transport_Request.SkipForward.API_v1_LayerType]
                announcements: _ClassVar[NetworkAPI_v1.API_v1_Transport_Request.SkipForward.API_v1_LayerType]
                slide: _ClassVar[NetworkAPI_v1.API_v1_Transport_Request.SkipForward.API_v1_LayerType]
                media: _ClassVar[NetworkAPI_v1.API_v1_Transport_Request.SkipForward.API_v1_LayerType]
                video_input: _ClassVar[NetworkAPI_v1.API_v1_Transport_Request.SkipForward.API_v1_LayerType]
            audio: NetworkAPI_v1.API_v1_Transport_Request.SkipForward.API_v1_LayerType
            props: NetworkAPI_v1.API_v1_Transport_Request.SkipForward.API_v1_LayerType
            messages: NetworkAPI_v1.API_v1_Transport_Request.SkipForward.API_v1_LayerType
            announcements: NetworkAPI_v1.API_v1_Transport_Request.SkipForward.API_v1_LayerType
            slide: NetworkAPI_v1.API_v1_Transport_Request.SkipForward.API_v1_LayerType
            media: NetworkAPI_v1.API_v1_Transport_Request.SkipForward.API_v1_LayerType
            video_input: NetworkAPI_v1.API_v1_Transport_Request.SkipForward.API_v1_LayerType
            LAYER_FIELD_NUMBER: _ClassVar[int]
            SECONDS_FIELD_NUMBER: _ClassVar[int]
            layer: NetworkAPI_v1.API_v1_Transport_Request.SkipForward.API_v1_LayerType
            seconds: float
            def __init__(self, layer: _Optional[_Union[NetworkAPI_v1.API_v1_Transport_Request.SkipForward.API_v1_LayerType, str]] = ..., seconds: _Optional[float] = ...) -> None: ...
        class GoToEnd(_message.Message):
            __slots__ = ("layer", "seconds")
            class API_v1_LayerType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                audio: _ClassVar[NetworkAPI_v1.API_v1_Transport_Request.GoToEnd.API_v1_LayerType]
                props: _ClassVar[NetworkAPI_v1.API_v1_Transport_Request.GoToEnd.API_v1_LayerType]
                messages: _ClassVar[NetworkAPI_v1.API_v1_Transport_Request.GoToEnd.API_v1_LayerType]
                announcements: _ClassVar[NetworkAPI_v1.API_v1_Transport_Request.GoToEnd.API_v1_LayerType]
                slide: _ClassVar[NetworkAPI_v1.API_v1_Transport_Request.GoToEnd.API_v1_LayerType]
                media: _ClassVar[NetworkAPI_v1.API_v1_Transport_Request.GoToEnd.API_v1_LayerType]
                video_input: _ClassVar[NetworkAPI_v1.API_v1_Transport_Request.GoToEnd.API_v1_LayerType]
            audio: NetworkAPI_v1.API_v1_Transport_Request.GoToEnd.API_v1_LayerType
            props: NetworkAPI_v1.API_v1_Transport_Request.GoToEnd.API_v1_LayerType
            messages: NetworkAPI_v1.API_v1_Transport_Request.GoToEnd.API_v1_LayerType
            announcements: NetworkAPI_v1.API_v1_Transport_Request.GoToEnd.API_v1_LayerType
            slide: NetworkAPI_v1.API_v1_Transport_Request.GoToEnd.API_v1_LayerType
            media: NetworkAPI_v1.API_v1_Transport_Request.GoToEnd.API_v1_LayerType
            video_input: NetworkAPI_v1.API_v1_Transport_Request.GoToEnd.API_v1_LayerType
            LAYER_FIELD_NUMBER: _ClassVar[int]
            SECONDS_FIELD_NUMBER: _ClassVar[int]
            layer: NetworkAPI_v1.API_v1_Transport_Request.GoToEnd.API_v1_LayerType
            seconds: float
            def __init__(self, layer: _Optional[_Union[NetworkAPI_v1.API_v1_Transport_Request.GoToEnd.API_v1_LayerType, str]] = ..., seconds: _Optional[float] = ...) -> None: ...
        class GetTime(_message.Message):
            __slots__ = ("layer",)
            class API_v1_LayerType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                audio: _ClassVar[NetworkAPI_v1.API_v1_Transport_Request.GetTime.API_v1_LayerType]
                props: _ClassVar[NetworkAPI_v1.API_v1_Transport_Request.GetTime.API_v1_LayerType]
                messages: _ClassVar[NetworkAPI_v1.API_v1_Transport_Request.GetTime.API_v1_LayerType]
                announcements: _ClassVar[NetworkAPI_v1.API_v1_Transport_Request.GetTime.API_v1_LayerType]
                slide: _ClassVar[NetworkAPI_v1.API_v1_Transport_Request.GetTime.API_v1_LayerType]
                media: _ClassVar[NetworkAPI_v1.API_v1_Transport_Request.GetTime.API_v1_LayerType]
                video_input: _ClassVar[NetworkAPI_v1.API_v1_Transport_Request.GetTime.API_v1_LayerType]
            audio: NetworkAPI_v1.API_v1_Transport_Request.GetTime.API_v1_LayerType
            props: NetworkAPI_v1.API_v1_Transport_Request.GetTime.API_v1_LayerType
            messages: NetworkAPI_v1.API_v1_Transport_Request.GetTime.API_v1_LayerType
            announcements: NetworkAPI_v1.API_v1_Transport_Request.GetTime.API_v1_LayerType
            slide: NetworkAPI_v1.API_v1_Transport_Request.GetTime.API_v1_LayerType
            media: NetworkAPI_v1.API_v1_Transport_Request.GetTime.API_v1_LayerType
            video_input: NetworkAPI_v1.API_v1_Transport_Request.GetTime.API_v1_LayerType
            LAYER_FIELD_NUMBER: _ClassVar[int]
            layer: NetworkAPI_v1.API_v1_Transport_Request.GetTime.API_v1_LayerType
            def __init__(self, layer: _Optional[_Union[NetworkAPI_v1.API_v1_Transport_Request.GetTime.API_v1_LayerType, str]] = ...) -> None: ...
        class PutTime(_message.Message):
            __slots__ = ("layer", "seconds")
            class API_v1_LayerType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                audio: _ClassVar[NetworkAPI_v1.API_v1_Transport_Request.PutTime.API_v1_LayerType]
                props: _ClassVar[NetworkAPI_v1.API_v1_Transport_Request.PutTime.API_v1_LayerType]
                messages: _ClassVar[NetworkAPI_v1.API_v1_Transport_Request.PutTime.API_v1_LayerType]
                announcements: _ClassVar[NetworkAPI_v1.API_v1_Transport_Request.PutTime.API_v1_LayerType]
                slide: _ClassVar[NetworkAPI_v1.API_v1_Transport_Request.PutTime.API_v1_LayerType]
                media: _ClassVar[NetworkAPI_v1.API_v1_Transport_Request.PutTime.API_v1_LayerType]
                video_input: _ClassVar[NetworkAPI_v1.API_v1_Transport_Request.PutTime.API_v1_LayerType]
            audio: NetworkAPI_v1.API_v1_Transport_Request.PutTime.API_v1_LayerType
            props: NetworkAPI_v1.API_v1_Transport_Request.PutTime.API_v1_LayerType
            messages: NetworkAPI_v1.API_v1_Transport_Request.PutTime.API_v1_LayerType
            announcements: NetworkAPI_v1.API_v1_Transport_Request.PutTime.API_v1_LayerType
            slide: NetworkAPI_v1.API_v1_Transport_Request.PutTime.API_v1_LayerType
            media: NetworkAPI_v1.API_v1_Transport_Request.PutTime.API_v1_LayerType
            video_input: NetworkAPI_v1.API_v1_Transport_Request.PutTime.API_v1_LayerType
            LAYER_FIELD_NUMBER: _ClassVar[int]
            SECONDS_FIELD_NUMBER: _ClassVar[int]
            layer: NetworkAPI_v1.API_v1_Transport_Request.PutTime.API_v1_LayerType
            seconds: float
            def __init__(self, layer: _Optional[_Union[NetworkAPI_v1.API_v1_Transport_Request.PutTime.API_v1_LayerType, str]] = ..., seconds: _Optional[float] = ...) -> None: ...
        class GetAutoAdvance(_message.Message):
            __slots__ = ("layer",)
            class API_v1_LayerType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                audio: _ClassVar[NetworkAPI_v1.API_v1_Transport_Request.GetAutoAdvance.API_v1_LayerType]
                props: _ClassVar[NetworkAPI_v1.API_v1_Transport_Request.GetAutoAdvance.API_v1_LayerType]
                messages: _ClassVar[NetworkAPI_v1.API_v1_Transport_Request.GetAutoAdvance.API_v1_LayerType]
                announcements: _ClassVar[NetworkAPI_v1.API_v1_Transport_Request.GetAutoAdvance.API_v1_LayerType]
                slide: _ClassVar[NetworkAPI_v1.API_v1_Transport_Request.GetAutoAdvance.API_v1_LayerType]
                media: _ClassVar[NetworkAPI_v1.API_v1_Transport_Request.GetAutoAdvance.API_v1_LayerType]
                video_input: _ClassVar[NetworkAPI_v1.API_v1_Transport_Request.GetAutoAdvance.API_v1_LayerType]
            audio: NetworkAPI_v1.API_v1_Transport_Request.GetAutoAdvance.API_v1_LayerType
            props: NetworkAPI_v1.API_v1_Transport_Request.GetAutoAdvance.API_v1_LayerType
            messages: NetworkAPI_v1.API_v1_Transport_Request.GetAutoAdvance.API_v1_LayerType
            announcements: NetworkAPI_v1.API_v1_Transport_Request.GetAutoAdvance.API_v1_LayerType
            slide: NetworkAPI_v1.API_v1_Transport_Request.GetAutoAdvance.API_v1_LayerType
            media: NetworkAPI_v1.API_v1_Transport_Request.GetAutoAdvance.API_v1_LayerType
            video_input: NetworkAPI_v1.API_v1_Transport_Request.GetAutoAdvance.API_v1_LayerType
            LAYER_FIELD_NUMBER: _ClassVar[int]
            layer: NetworkAPI_v1.API_v1_Transport_Request.GetAutoAdvance.API_v1_LayerType
            def __init__(self, layer: _Optional[_Union[NetworkAPI_v1.API_v1_Transport_Request.GetAutoAdvance.API_v1_LayerType, str]] = ...) -> None: ...
        class DeleteAutoAdvance(_message.Message):
            __slots__ = ("layer",)
            class API_v1_LayerType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                audio: _ClassVar[NetworkAPI_v1.API_v1_Transport_Request.DeleteAutoAdvance.API_v1_LayerType]
                props: _ClassVar[NetworkAPI_v1.API_v1_Transport_Request.DeleteAutoAdvance.API_v1_LayerType]
                messages: _ClassVar[NetworkAPI_v1.API_v1_Transport_Request.DeleteAutoAdvance.API_v1_LayerType]
                announcements: _ClassVar[NetworkAPI_v1.API_v1_Transport_Request.DeleteAutoAdvance.API_v1_LayerType]
                slide: _ClassVar[NetworkAPI_v1.API_v1_Transport_Request.DeleteAutoAdvance.API_v1_LayerType]
                media: _ClassVar[NetworkAPI_v1.API_v1_Transport_Request.DeleteAutoAdvance.API_v1_LayerType]
                video_input: _ClassVar[NetworkAPI_v1.API_v1_Transport_Request.DeleteAutoAdvance.API_v1_LayerType]
            audio: NetworkAPI_v1.API_v1_Transport_Request.DeleteAutoAdvance.API_v1_LayerType
            props: NetworkAPI_v1.API_v1_Transport_Request.DeleteAutoAdvance.API_v1_LayerType
            messages: NetworkAPI_v1.API_v1_Transport_Request.DeleteAutoAdvance.API_v1_LayerType
            announcements: NetworkAPI_v1.API_v1_Transport_Request.DeleteAutoAdvance.API_v1_LayerType
            slide: NetworkAPI_v1.API_v1_Transport_Request.DeleteAutoAdvance.API_v1_LayerType
            media: NetworkAPI_v1.API_v1_Transport_Request.DeleteAutoAdvance.API_v1_LayerType
            video_input: NetworkAPI_v1.API_v1_Transport_Request.DeleteAutoAdvance.API_v1_LayerType
            LAYER_FIELD_NUMBER: _ClassVar[int]
            layer: NetworkAPI_v1.API_v1_Transport_Request.DeleteAutoAdvance.API_v1_LayerType
            def __init__(self, layer: _Optional[_Union[NetworkAPI_v1.API_v1_Transport_Request.DeleteAutoAdvance.API_v1_LayerType, str]] = ...) -> None: ...
        class GetCurrentMedia(_message.Message):
            __slots__ = ("layer",)
            class API_v1_LayerType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                audio: _ClassVar[NetworkAPI_v1.API_v1_Transport_Request.GetCurrentMedia.API_v1_LayerType]
                props: _ClassVar[NetworkAPI_v1.API_v1_Transport_Request.GetCurrentMedia.API_v1_LayerType]
                messages: _ClassVar[NetworkAPI_v1.API_v1_Transport_Request.GetCurrentMedia.API_v1_LayerType]
                announcements: _ClassVar[NetworkAPI_v1.API_v1_Transport_Request.GetCurrentMedia.API_v1_LayerType]
                slide: _ClassVar[NetworkAPI_v1.API_v1_Transport_Request.GetCurrentMedia.API_v1_LayerType]
                media: _ClassVar[NetworkAPI_v1.API_v1_Transport_Request.GetCurrentMedia.API_v1_LayerType]
                video_input: _ClassVar[NetworkAPI_v1.API_v1_Transport_Request.GetCurrentMedia.API_v1_LayerType]
            audio: NetworkAPI_v1.API_v1_Transport_Request.GetCurrentMedia.API_v1_LayerType
            props: NetworkAPI_v1.API_v1_Transport_Request.GetCurrentMedia.API_v1_LayerType
            messages: NetworkAPI_v1.API_v1_Transport_Request.GetCurrentMedia.API_v1_LayerType
            announcements: NetworkAPI_v1.API_v1_Transport_Request.GetCurrentMedia.API_v1_LayerType
            slide: NetworkAPI_v1.API_v1_Transport_Request.GetCurrentMedia.API_v1_LayerType
            media: NetworkAPI_v1.API_v1_Transport_Request.GetCurrentMedia.API_v1_LayerType
            video_input: NetworkAPI_v1.API_v1_Transport_Request.GetCurrentMedia.API_v1_LayerType
            LAYER_FIELD_NUMBER: _ClassVar[int]
            layer: NetworkAPI_v1.API_v1_Transport_Request.GetCurrentMedia.API_v1_LayerType
            def __init__(self, layer: _Optional[_Union[NetworkAPI_v1.API_v1_Transport_Request.GetCurrentMedia.API_v1_LayerType, str]] = ...) -> None: ...
        PLAY_FIELD_NUMBER: _ClassVar[int]
        PAUSE_FIELD_NUMBER: _ClassVar[int]
        SKIP_BACKWARD_FIELD_NUMBER: _ClassVar[int]
        SKIP_FORWARD_FIELD_NUMBER: _ClassVar[int]
        GO_TO_END_FIELD_NUMBER: _ClassVar[int]
        GET_TIME_FIELD_NUMBER: _ClassVar[int]
        PUT_TIME_FIELD_NUMBER: _ClassVar[int]
        GET_AUTO_ADVANCE_FIELD_NUMBER: _ClassVar[int]
        DELETE_AUTO_ADVANCE_FIELD_NUMBER: _ClassVar[int]
        GET_CURRENT_MEDIA_FIELD_NUMBER: _ClassVar[int]
        play: NetworkAPI_v1.API_v1_Transport_Request.Play
        pause: NetworkAPI_v1.API_v1_Transport_Request.Pause
        skip_backward: NetworkAPI_v1.API_v1_Transport_Request.SkipBackward
        skip_forward: NetworkAPI_v1.API_v1_Transport_Request.SkipForward
        go_to_end: NetworkAPI_v1.API_v1_Transport_Request.GoToEnd
        get_time: NetworkAPI_v1.API_v1_Transport_Request.GetTime
        put_time: NetworkAPI_v1.API_v1_Transport_Request.PutTime
        get_auto_advance: NetworkAPI_v1.API_v1_Transport_Request.GetAutoAdvance
        delete_auto_advance: NetworkAPI_v1.API_v1_Transport_Request.DeleteAutoAdvance
        get_current_media: NetworkAPI_v1.API_v1_Transport_Request.GetCurrentMedia
        def __init__(self, play: _Optional[_Union[NetworkAPI_v1.API_v1_Transport_Request.Play, _Mapping]] = ..., pause: _Optional[_Union[NetworkAPI_v1.API_v1_Transport_Request.Pause, _Mapping]] = ..., skip_backward: _Optional[_Union[NetworkAPI_v1.API_v1_Transport_Request.SkipBackward, _Mapping]] = ..., skip_forward: _Optional[_Union[NetworkAPI_v1.API_v1_Transport_Request.SkipForward, _Mapping]] = ..., go_to_end: _Optional[_Union[NetworkAPI_v1.API_v1_Transport_Request.GoToEnd, _Mapping]] = ..., get_time: _Optional[_Union[NetworkAPI_v1.API_v1_Transport_Request.GetTime, _Mapping]] = ..., put_time: _Optional[_Union[NetworkAPI_v1.API_v1_Transport_Request.PutTime, _Mapping]] = ..., get_auto_advance: _Optional[_Union[NetworkAPI_v1.API_v1_Transport_Request.GetAutoAdvance, _Mapping]] = ..., delete_auto_advance: _Optional[_Union[NetworkAPI_v1.API_v1_Transport_Request.DeleteAutoAdvance, _Mapping]] = ..., get_current_media: _Optional[_Union[NetworkAPI_v1.API_v1_Transport_Request.GetCurrentMedia, _Mapping]] = ...) -> None: ...
    class API_v1_Trigger_Request(_message.Message):
        __slots__ = ("cue", "playlist", "media", "audio", "video_input", "library", "next", "previous", "media_next", "media_previous", "audio_next", "audio_previous")
        class Cue(_message.Message):
            __slots__ = ("index",)
            INDEX_FIELD_NUMBER: _ClassVar[int]
            index: int
            def __init__(self, index: _Optional[int] = ...) -> None: ...
        class Playlist(_message.Message):
            __slots__ = ("id",)
            ID_FIELD_NUMBER: _ClassVar[int]
            id: str
            def __init__(self, id: _Optional[str] = ...) -> None: ...
        class Media(_message.Message):
            __slots__ = ("id",)
            ID_FIELD_NUMBER: _ClassVar[int]
            id: str
            def __init__(self, id: _Optional[str] = ...) -> None: ...
        class MediaNext(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class MediaPrevious(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class Audio(_message.Message):
            __slots__ = ("id",)
            ID_FIELD_NUMBER: _ClassVar[int]
            id: str
            def __init__(self, id: _Optional[str] = ...) -> None: ...
        class AudioNext(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class AudioPrevious(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class VideoInput(_message.Message):
            __slots__ = ("id",)
            ID_FIELD_NUMBER: _ClassVar[int]
            id: str
            def __init__(self, id: _Optional[str] = ...) -> None: ...
        class Library(_message.Message):
            __slots__ = ("id",)
            ID_FIELD_NUMBER: _ClassVar[int]
            id: str
            def __init__(self, id: _Optional[str] = ...) -> None: ...
        class Next(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class Previous(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        CUE_FIELD_NUMBER: _ClassVar[int]
        PLAYLIST_FIELD_NUMBER: _ClassVar[int]
        MEDIA_FIELD_NUMBER: _ClassVar[int]
        AUDIO_FIELD_NUMBER: _ClassVar[int]
        VIDEO_INPUT_FIELD_NUMBER: _ClassVar[int]
        LIBRARY_FIELD_NUMBER: _ClassVar[int]
        NEXT_FIELD_NUMBER: _ClassVar[int]
        PREVIOUS_FIELD_NUMBER: _ClassVar[int]
        MEDIA_NEXT_FIELD_NUMBER: _ClassVar[int]
        MEDIA_PREVIOUS_FIELD_NUMBER: _ClassVar[int]
        AUDIO_NEXT_FIELD_NUMBER: _ClassVar[int]
        AUDIO_PREVIOUS_FIELD_NUMBER: _ClassVar[int]
        cue: NetworkAPI_v1.API_v1_Trigger_Request.Cue
        playlist: NetworkAPI_v1.API_v1_Trigger_Request.Playlist
        media: NetworkAPI_v1.API_v1_Trigger_Request.Media
        audio: NetworkAPI_v1.API_v1_Trigger_Request.Audio
        video_input: NetworkAPI_v1.API_v1_Trigger_Request.VideoInput
        library: NetworkAPI_v1.API_v1_Trigger_Request.Library
        next: NetworkAPI_v1.API_v1_Trigger_Request.Next
        previous: NetworkAPI_v1.API_v1_Trigger_Request.Previous
        media_next: NetworkAPI_v1.API_v1_Trigger_Request.MediaNext
        media_previous: NetworkAPI_v1.API_v1_Trigger_Request.MediaPrevious
        audio_next: NetworkAPI_v1.API_v1_Trigger_Request.AudioNext
        audio_previous: NetworkAPI_v1.API_v1_Trigger_Request.AudioPrevious
        def __init__(self, cue: _Optional[_Union[NetworkAPI_v1.API_v1_Trigger_Request.Cue, _Mapping]] = ..., playlist: _Optional[_Union[NetworkAPI_v1.API_v1_Trigger_Request.Playlist, _Mapping]] = ..., media: _Optional[_Union[NetworkAPI_v1.API_v1_Trigger_Request.Media, _Mapping]] = ..., audio: _Optional[_Union[NetworkAPI_v1.API_v1_Trigger_Request.Audio, _Mapping]] = ..., video_input: _Optional[_Union[NetworkAPI_v1.API_v1_Trigger_Request.VideoInput, _Mapping]] = ..., library: _Optional[_Union[NetworkAPI_v1.API_v1_Trigger_Request.Library, _Mapping]] = ..., next: _Optional[_Union[NetworkAPI_v1.API_v1_Trigger_Request.Next, _Mapping]] = ..., previous: _Optional[_Union[NetworkAPI_v1.API_v1_Trigger_Request.Previous, _Mapping]] = ..., media_next: _Optional[_Union[NetworkAPI_v1.API_v1_Trigger_Request.MediaNext, _Mapping]] = ..., media_previous: _Optional[_Union[NetworkAPI_v1.API_v1_Trigger_Request.MediaPrevious, _Mapping]] = ..., audio_next: _Optional[_Union[NetworkAPI_v1.API_v1_Trigger_Request.AudioNext, _Mapping]] = ..., audio_previous: _Optional[_Union[NetworkAPI_v1.API_v1_Trigger_Request.AudioPrevious, _Mapping]] = ...) -> None: ...
    class API_v1_Video_Inputs_Request(_message.Message):
        __slots__ = ("get_all", "trigger")
        class GetAll(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class Trigger(_message.Message):
            __slots__ = ("id",)
            ID_FIELD_NUMBER: _ClassVar[int]
            id: str
            def __init__(self, id: _Optional[str] = ...) -> None: ...
        GET_ALL_FIELD_NUMBER: _ClassVar[int]
        TRIGGER_FIELD_NUMBER: _ClassVar[int]
        get_all: NetworkAPI_v1.API_v1_Video_Inputs_Request.GetAll
        trigger: NetworkAPI_v1.API_v1_Video_Inputs_Request.Trigger
        def __init__(self, get_all: _Optional[_Union[NetworkAPI_v1.API_v1_Video_Inputs_Request.GetAll, _Mapping]] = ..., trigger: _Optional[_Union[NetworkAPI_v1.API_v1_Video_Inputs_Request.Trigger, _Mapping]] = ...) -> None: ...
    class API_v1_Announcement_Response(_message.Message):
        __slots__ = ("active_timeline_operation", "active_timeline_status", "active", "slide_index", "active_focus", "active_trigger", "active_next_trigger", "active_previous_trigger", "active_index_trigger")
        class ActiveTimelineOperation(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class ActiveTimelineStatus(_message.Message):
            __slots__ = ("is_running", "current_time")
            IS_RUNNING_FIELD_NUMBER: _ClassVar[int]
            CURRENT_TIME_FIELD_NUMBER: _ClassVar[int]
            is_running: bool
            current_time: float
            def __init__(self, is_running: bool = ..., current_time: _Optional[float] = ...) -> None: ...
        class Active(_message.Message):
            __slots__ = ("announcement",)
            ANNOUNCEMENT_FIELD_NUMBER: _ClassVar[int]
            announcement: _proApiV1BasicTypes_pb2.API_v1_Presentation
            def __init__(self, announcement: _Optional[_Union[_proApiV1BasicTypes_pb2.API_v1_Presentation, _Mapping]] = ...) -> None: ...
        class SlideIndex(_message.Message):
            __slots__ = ("announcement_index",)
            ANNOUNCEMENT_INDEX_FIELD_NUMBER: _ClassVar[int]
            announcement_index: _proApiV1BasicTypes_pb2.API_v1_SlideIndex
            def __init__(self, announcement_index: _Optional[_Union[_proApiV1BasicTypes_pb2.API_v1_SlideIndex, _Mapping]] = ...) -> None: ...
        class ActiveFocus(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class ActiveTrigger(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class ActiveNextTrigger(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class ActivePreviousTrigger(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class ActiveIndexTrigger(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        ACTIVE_TIMELINE_OPERATION_FIELD_NUMBER: _ClassVar[int]
        ACTIVE_TIMELINE_STATUS_FIELD_NUMBER: _ClassVar[int]
        ACTIVE_FIELD_NUMBER: _ClassVar[int]
        SLIDE_INDEX_FIELD_NUMBER: _ClassVar[int]
        ACTIVE_FOCUS_FIELD_NUMBER: _ClassVar[int]
        ACTIVE_TRIGGER_FIELD_NUMBER: _ClassVar[int]
        ACTIVE_NEXT_TRIGGER_FIELD_NUMBER: _ClassVar[int]
        ACTIVE_PREVIOUS_TRIGGER_FIELD_NUMBER: _ClassVar[int]
        ACTIVE_INDEX_TRIGGER_FIELD_NUMBER: _ClassVar[int]
        active_timeline_operation: NetworkAPI_v1.API_v1_Announcement_Response.ActiveTimelineOperation
        active_timeline_status: NetworkAPI_v1.API_v1_Announcement_Response.ActiveTimelineStatus
        active: NetworkAPI_v1.API_v1_Announcement_Response.Active
        slide_index: NetworkAPI_v1.API_v1_Announcement_Response.SlideIndex
        active_focus: NetworkAPI_v1.API_v1_Announcement_Response.ActiveFocus
        active_trigger: NetworkAPI_v1.API_v1_Announcement_Response.ActiveTrigger
        active_next_trigger: NetworkAPI_v1.API_v1_Announcement_Response.ActiveNextTrigger
        active_previous_trigger: NetworkAPI_v1.API_v1_Announcement_Response.ActivePreviousTrigger
        active_index_trigger: NetworkAPI_v1.API_v1_Announcement_Response.ActiveIndexTrigger
        def __init__(self, active_timeline_operation: _Optional[_Union[NetworkAPI_v1.API_v1_Announcement_Response.ActiveTimelineOperation, _Mapping]] = ..., active_timeline_status: _Optional[_Union[NetworkAPI_v1.API_v1_Announcement_Response.ActiveTimelineStatus, _Mapping]] = ..., active: _Optional[_Union[NetworkAPI_v1.API_v1_Announcement_Response.Active, _Mapping]] = ..., slide_index: _Optional[_Union[NetworkAPI_v1.API_v1_Announcement_Response.SlideIndex, _Mapping]] = ..., active_focus: _Optional[_Union[NetworkAPI_v1.API_v1_Announcement_Response.ActiveFocus, _Mapping]] = ..., active_trigger: _Optional[_Union[NetworkAPI_v1.API_v1_Announcement_Response.ActiveTrigger, _Mapping]] = ..., active_next_trigger: _Optional[_Union[NetworkAPI_v1.API_v1_Announcement_Response.ActiveNextTrigger, _Mapping]] = ..., active_previous_trigger: _Optional[_Union[NetworkAPI_v1.API_v1_Announcement_Response.ActivePreviousTrigger, _Mapping]] = ..., active_index_trigger: _Optional[_Union[NetworkAPI_v1.API_v1_Announcement_Response.ActiveIndexTrigger, _Mapping]] = ...) -> None: ...
    class API_v1_Audio_Response(_message.Message):
        __slots__ = ("playlists", "playlist", "update", "playlist_focused", "playlist_active", "playlist_next_focus", "playlist_previous_focus", "playlist_active_focus", "playlist_id_focus", "playlist_focused_trigger", "playlist_active_trigger", "playlist_id_trigger", "playlist_focused_next_trigger", "playlist_focused_previous_trigger", "playlist_focused_id_trigger", "playlist_active_next_trigger", "playlist_active_previous_trigger", "playlist_active_id_trigger", "playlist_id_next_trigger", "playlist_id_previous_trigger")
        class Playlists(_message.Message):
            __slots__ = ("playlists",)
            PLAYLISTS_FIELD_NUMBER: _ClassVar[int]
            playlists: _containers.RepeatedCompositeFieldContainer[_proApiV1BasicTypes_pb2.API_v1_Playlist]
            def __init__(self, playlists: _Optional[_Iterable[_Union[_proApiV1BasicTypes_pb2.API_v1_Playlist, _Mapping]]] = ...) -> None: ...
        class Playlist(_message.Message):
            __slots__ = ("id", "items")
            ID_FIELD_NUMBER: _ClassVar[int]
            ITEMS_FIELD_NUMBER: _ClassVar[int]
            id: _proApiV1BasicTypes_pb2.API_v1_Identifier
            items: _containers.RepeatedCompositeFieldContainer[_proApiV1BasicTypes_pb2.API_v1_MediaPlaylistItem]
            def __init__(self, id: _Optional[_Union[_proApiV1BasicTypes_pb2.API_v1_Identifier, _Mapping]] = ..., items: _Optional[_Iterable[_Union[_proApiV1BasicTypes_pb2.API_v1_MediaPlaylistItem, _Mapping]]] = ...) -> None: ...
        class PlaylistUpdate(_message.Message):
            __slots__ = ("id",)
            ID_FIELD_NUMBER: _ClassVar[int]
            id: _proApiV1BasicTypes_pb2.API_v1_Identifier
            def __init__(self, id: _Optional[_Union[_proApiV1BasicTypes_pb2.API_v1_Identifier, _Mapping]] = ...) -> None: ...
        class EmptyMessage(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class FocusedPlaylist(_message.Message):
            __slots__ = ("id",)
            ID_FIELD_NUMBER: _ClassVar[int]
            id: _proApiV1BasicTypes_pb2.API_v1_Identifier
            def __init__(self, id: _Optional[_Union[_proApiV1BasicTypes_pb2.API_v1_Identifier, _Mapping]] = ...) -> None: ...
        class ActivePlaylist(_message.Message):
            __slots__ = ("playlist", "item")
            PLAYLIST_FIELD_NUMBER: _ClassVar[int]
            ITEM_FIELD_NUMBER: _ClassVar[int]
            playlist: _proApiV1BasicTypes_pb2.API_v1_Identifier
            item: _proApiV1BasicTypes_pb2.API_v1_Identifier
            def __init__(self, playlist: _Optional[_Union[_proApiV1BasicTypes_pb2.API_v1_Identifier, _Mapping]] = ..., item: _Optional[_Union[_proApiV1BasicTypes_pb2.API_v1_Identifier, _Mapping]] = ...) -> None: ...
        PLAYLISTS_FIELD_NUMBER: _ClassVar[int]
        PLAYLIST_FIELD_NUMBER: _ClassVar[int]
        UPDATE_FIELD_NUMBER: _ClassVar[int]
        PLAYLIST_FOCUSED_FIELD_NUMBER: _ClassVar[int]
        PLAYLIST_ACTIVE_FIELD_NUMBER: _ClassVar[int]
        PLAYLIST_NEXT_FOCUS_FIELD_NUMBER: _ClassVar[int]
        PLAYLIST_PREVIOUS_FOCUS_FIELD_NUMBER: _ClassVar[int]
        PLAYLIST_ACTIVE_FOCUS_FIELD_NUMBER: _ClassVar[int]
        PLAYLIST_ID_FOCUS_FIELD_NUMBER: _ClassVar[int]
        PLAYLIST_FOCUSED_TRIGGER_FIELD_NUMBER: _ClassVar[int]
        PLAYLIST_ACTIVE_TRIGGER_FIELD_NUMBER: _ClassVar[int]
        PLAYLIST_ID_TRIGGER_FIELD_NUMBER: _ClassVar[int]
        PLAYLIST_FOCUSED_NEXT_TRIGGER_FIELD_NUMBER: _ClassVar[int]
        PLAYLIST_FOCUSED_PREVIOUS_TRIGGER_FIELD_NUMBER: _ClassVar[int]
        PLAYLIST_FOCUSED_ID_TRIGGER_FIELD_NUMBER: _ClassVar[int]
        PLAYLIST_ACTIVE_NEXT_TRIGGER_FIELD_NUMBER: _ClassVar[int]
        PLAYLIST_ACTIVE_PREVIOUS_TRIGGER_FIELD_NUMBER: _ClassVar[int]
        PLAYLIST_ACTIVE_ID_TRIGGER_FIELD_NUMBER: _ClassVar[int]
        PLAYLIST_ID_NEXT_TRIGGER_FIELD_NUMBER: _ClassVar[int]
        PLAYLIST_ID_PREVIOUS_TRIGGER_FIELD_NUMBER: _ClassVar[int]
        playlists: NetworkAPI_v1.API_v1_Audio_Response.Playlists
        playlist: NetworkAPI_v1.API_v1_Audio_Response.Playlist
        update: NetworkAPI_v1.API_v1_Audio_Response.PlaylistUpdate
        playlist_focused: NetworkAPI_v1.API_v1_Audio_Response.FocusedPlaylist
        playlist_active: NetworkAPI_v1.API_v1_Audio_Response.ActivePlaylist
        playlist_next_focus: NetworkAPI_v1.API_v1_Audio_Response.EmptyMessage
        playlist_previous_focus: NetworkAPI_v1.API_v1_Audio_Response.EmptyMessage
        playlist_active_focus: NetworkAPI_v1.API_v1_Audio_Response.EmptyMessage
        playlist_id_focus: NetworkAPI_v1.API_v1_Audio_Response.EmptyMessage
        playlist_focused_trigger: NetworkAPI_v1.API_v1_Audio_Response.EmptyMessage
        playlist_active_trigger: NetworkAPI_v1.API_v1_Audio_Response.EmptyMessage
        playlist_id_trigger: NetworkAPI_v1.API_v1_Audio_Response.EmptyMessage
        playlist_focused_next_trigger: NetworkAPI_v1.API_v1_Audio_Response.EmptyMessage
        playlist_focused_previous_trigger: NetworkAPI_v1.API_v1_Audio_Response.EmptyMessage
        playlist_focused_id_trigger: NetworkAPI_v1.API_v1_Audio_Response.EmptyMessage
        playlist_active_next_trigger: NetworkAPI_v1.API_v1_Audio_Response.EmptyMessage
        playlist_active_previous_trigger: NetworkAPI_v1.API_v1_Audio_Response.EmptyMessage
        playlist_active_id_trigger: NetworkAPI_v1.API_v1_Audio_Response.EmptyMessage
        playlist_id_next_trigger: NetworkAPI_v1.API_v1_Audio_Response.EmptyMessage
        playlist_id_previous_trigger: NetworkAPI_v1.API_v1_Audio_Response.EmptyMessage
        def __init__(self, playlists: _Optional[_Union[NetworkAPI_v1.API_v1_Audio_Response.Playlists, _Mapping]] = ..., playlist: _Optional[_Union[NetworkAPI_v1.API_v1_Audio_Response.Playlist, _Mapping]] = ..., update: _Optional[_Union[NetworkAPI_v1.API_v1_Audio_Response.PlaylistUpdate, _Mapping]] = ..., playlist_focused: _Optional[_Union[NetworkAPI_v1.API_v1_Audio_Response.FocusedPlaylist, _Mapping]] = ..., playlist_active: _Optional[_Union[NetworkAPI_v1.API_v1_Audio_Response.ActivePlaylist, _Mapping]] = ..., playlist_next_focus: _Optional[_Union[NetworkAPI_v1.API_v1_Audio_Response.EmptyMessage, _Mapping]] = ..., playlist_previous_focus: _Optional[_Union[NetworkAPI_v1.API_v1_Audio_Response.EmptyMessage, _Mapping]] = ..., playlist_active_focus: _Optional[_Union[NetworkAPI_v1.API_v1_Audio_Response.EmptyMessage, _Mapping]] = ..., playlist_id_focus: _Optional[_Union[NetworkAPI_v1.API_v1_Audio_Response.EmptyMessage, _Mapping]] = ..., playlist_focused_trigger: _Optional[_Union[NetworkAPI_v1.API_v1_Audio_Response.EmptyMessage, _Mapping]] = ..., playlist_active_trigger: _Optional[_Union[NetworkAPI_v1.API_v1_Audio_Response.EmptyMessage, _Mapping]] = ..., playlist_id_trigger: _Optional[_Union[NetworkAPI_v1.API_v1_Audio_Response.EmptyMessage, _Mapping]] = ..., playlist_focused_next_trigger: _Optional[_Union[NetworkAPI_v1.API_v1_Audio_Response.EmptyMessage, _Mapping]] = ..., playlist_focused_previous_trigger: _Optional[_Union[NetworkAPI_v1.API_v1_Audio_Response.EmptyMessage, _Mapping]] = ..., playlist_focused_id_trigger: _Optional[_Union[NetworkAPI_v1.API_v1_Audio_Response.EmptyMessage, _Mapping]] = ..., playlist_active_next_trigger: _Optional[_Union[NetworkAPI_v1.API_v1_Audio_Response.EmptyMessage, _Mapping]] = ..., playlist_active_previous_trigger: _Optional[_Union[NetworkAPI_v1.API_v1_Audio_Response.EmptyMessage, _Mapping]] = ..., playlist_active_id_trigger: _Optional[_Union[NetworkAPI_v1.API_v1_Audio_Response.EmptyMessage, _Mapping]] = ..., playlist_id_next_trigger: _Optional[_Union[NetworkAPI_v1.API_v1_Audio_Response.EmptyMessage, _Mapping]] = ..., playlist_id_previous_trigger: _Optional[_Union[NetworkAPI_v1.API_v1_Audio_Response.EmptyMessage, _Mapping]] = ...) -> None: ...
    class API_v1_Capture_Response(_message.Message):
        __slots__ = ("get_status", "operation", "get_settings", "set_settings", "get_encodings")
        class GetStatus(_message.Message):
            __slots__ = ("status", "capture_time", "status_text")
            class API_v1_CaptureStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                active: _ClassVar[NetworkAPI_v1.API_v1_Capture_Response.GetStatus.API_v1_CaptureStatus]
                inactive: _ClassVar[NetworkAPI_v1.API_v1_Capture_Response.GetStatus.API_v1_CaptureStatus]
                caution: _ClassVar[NetworkAPI_v1.API_v1_Capture_Response.GetStatus.API_v1_CaptureStatus]
                error: _ClassVar[NetworkAPI_v1.API_v1_Capture_Response.GetStatus.API_v1_CaptureStatus]
            active: NetworkAPI_v1.API_v1_Capture_Response.GetStatus.API_v1_CaptureStatus
            inactive: NetworkAPI_v1.API_v1_Capture_Response.GetStatus.API_v1_CaptureStatus
            caution: NetworkAPI_v1.API_v1_Capture_Response.GetStatus.API_v1_CaptureStatus
            error: NetworkAPI_v1.API_v1_Capture_Response.GetStatus.API_v1_CaptureStatus
            STATUS_FIELD_NUMBER: _ClassVar[int]
            CAPTURE_TIME_FIELD_NUMBER: _ClassVar[int]
            STATUS_TEXT_FIELD_NUMBER: _ClassVar[int]
            status: NetworkAPI_v1.API_v1_Capture_Response.GetStatus.API_v1_CaptureStatus
            capture_time: str
            status_text: str
            def __init__(self, status: _Optional[_Union[NetworkAPI_v1.API_v1_Capture_Response.GetStatus.API_v1_CaptureStatus, str]] = ..., capture_time: _Optional[str] = ..., status_text: _Optional[str] = ...) -> None: ...
        class Operation(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class GetSettings(_message.Message):
            __slots__ = ("settings",)
            SETTINGS_FIELD_NUMBER: _ClassVar[int]
            settings: _proApiV1BasicTypes_pb2.API_v1_CaptureSettings
            def __init__(self, settings: _Optional[_Union[_proApiV1BasicTypes_pb2.API_v1_CaptureSettings, _Mapping]] = ...) -> None: ...
        class SetSettings(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class Encodings(_message.Message):
            __slots__ = ("encodings",)
            ENCODINGS_FIELD_NUMBER: _ClassVar[int]
            encodings: _containers.RepeatedScalarFieldContainer[str]
            def __init__(self, encodings: _Optional[_Iterable[str]] = ...) -> None: ...
        GET_STATUS_FIELD_NUMBER: _ClassVar[int]
        OPERATION_FIELD_NUMBER: _ClassVar[int]
        GET_SETTINGS_FIELD_NUMBER: _ClassVar[int]
        SET_SETTINGS_FIELD_NUMBER: _ClassVar[int]
        GET_ENCODINGS_FIELD_NUMBER: _ClassVar[int]
        get_status: NetworkAPI_v1.API_v1_Capture_Response.GetStatus
        operation: NetworkAPI_v1.API_v1_Capture_Response.Operation
        get_settings: NetworkAPI_v1.API_v1_Capture_Response.GetSettings
        set_settings: NetworkAPI_v1.API_v1_Capture_Response.SetSettings
        get_encodings: NetworkAPI_v1.API_v1_Capture_Response.Encodings
        def __init__(self, get_status: _Optional[_Union[NetworkAPI_v1.API_v1_Capture_Response.GetStatus, _Mapping]] = ..., operation: _Optional[_Union[NetworkAPI_v1.API_v1_Capture_Response.Operation, _Mapping]] = ..., get_settings: _Optional[_Union[NetworkAPI_v1.API_v1_Capture_Response.GetSettings, _Mapping]] = ..., set_settings: _Optional[_Union[NetworkAPI_v1.API_v1_Capture_Response.SetSettings, _Mapping]] = ..., get_encodings: _Optional[_Union[NetworkAPI_v1.API_v1_Capture_Response.Encodings, _Mapping]] = ...) -> None: ...
    class API_v1_Clear_Response(_message.Message):
        __slots__ = ("clear_layer", "create_group", "get_group", "put_group", "delete_group", "trigger_group", "get_groups", "get_group_icon", "put_group_icon")
        class ClearLayer(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class PutGroup(_message.Message):
            __slots__ = ("group",)
            GROUP_FIELD_NUMBER: _ClassVar[int]
            group: _proApiV1BasicTypes_pb2.API_v1_ClearGroup
            def __init__(self, group: _Optional[_Union[_proApiV1BasicTypes_pb2.API_v1_ClearGroup, _Mapping]] = ...) -> None: ...
        class DeleteGroup(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class TriggerGroup(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class CreateGroup(_message.Message):
            __slots__ = ("group",)
            GROUP_FIELD_NUMBER: _ClassVar[int]
            group: _proApiV1BasicTypes_pb2.API_v1_ClearGroup
            def __init__(self, group: _Optional[_Union[_proApiV1BasicTypes_pb2.API_v1_ClearGroup, _Mapping]] = ...) -> None: ...
        class GetGroup(_message.Message):
            __slots__ = ("group",)
            GROUP_FIELD_NUMBER: _ClassVar[int]
            group: _proApiV1BasicTypes_pb2.API_v1_ClearGroup
            def __init__(self, group: _Optional[_Union[_proApiV1BasicTypes_pb2.API_v1_ClearGroup, _Mapping]] = ...) -> None: ...
        class GetGroups(_message.Message):
            __slots__ = ("groups",)
            GROUPS_FIELD_NUMBER: _ClassVar[int]
            groups: _containers.RepeatedCompositeFieldContainer[_proApiV1BasicTypes_pb2.API_v1_ClearGroup]
            def __init__(self, groups: _Optional[_Iterable[_Union[_proApiV1BasicTypes_pb2.API_v1_ClearGroup, _Mapping]]] = ...) -> None: ...
        class GetGroupIcon(_message.Message):
            __slots__ = ("content_type", "icon")
            CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
            ICON_FIELD_NUMBER: _ClassVar[int]
            content_type: str
            icon: bytes
            def __init__(self, content_type: _Optional[str] = ..., icon: _Optional[bytes] = ...) -> None: ...
        class PutGroupIcon(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        CLEAR_LAYER_FIELD_NUMBER: _ClassVar[int]
        CREATE_GROUP_FIELD_NUMBER: _ClassVar[int]
        GET_GROUP_FIELD_NUMBER: _ClassVar[int]
        PUT_GROUP_FIELD_NUMBER: _ClassVar[int]
        DELETE_GROUP_FIELD_NUMBER: _ClassVar[int]
        TRIGGER_GROUP_FIELD_NUMBER: _ClassVar[int]
        GET_GROUPS_FIELD_NUMBER: _ClassVar[int]
        GET_GROUP_ICON_FIELD_NUMBER: _ClassVar[int]
        PUT_GROUP_ICON_FIELD_NUMBER: _ClassVar[int]
        clear_layer: NetworkAPI_v1.API_v1_Clear_Response.ClearLayer
        create_group: NetworkAPI_v1.API_v1_Clear_Response.CreateGroup
        get_group: NetworkAPI_v1.API_v1_Clear_Response.GetGroup
        put_group: NetworkAPI_v1.API_v1_Clear_Response.PutGroup
        delete_group: NetworkAPI_v1.API_v1_Clear_Response.DeleteGroup
        trigger_group: NetworkAPI_v1.API_v1_Clear_Response.TriggerGroup
        get_groups: NetworkAPI_v1.API_v1_Clear_Response.GetGroups
        get_group_icon: NetworkAPI_v1.API_v1_Clear_Response.GetGroupIcon
        put_group_icon: NetworkAPI_v1.API_v1_Clear_Response.PutGroupIcon
        def __init__(self, clear_layer: _Optional[_Union[NetworkAPI_v1.API_v1_Clear_Response.ClearLayer, _Mapping]] = ..., create_group: _Optional[_Union[NetworkAPI_v1.API_v1_Clear_Response.CreateGroup, _Mapping]] = ..., get_group: _Optional[_Union[NetworkAPI_v1.API_v1_Clear_Response.GetGroup, _Mapping]] = ..., put_group: _Optional[_Union[NetworkAPI_v1.API_v1_Clear_Response.PutGroup, _Mapping]] = ..., delete_group: _Optional[_Union[NetworkAPI_v1.API_v1_Clear_Response.DeleteGroup, _Mapping]] = ..., trigger_group: _Optional[_Union[NetworkAPI_v1.API_v1_Clear_Response.TriggerGroup, _Mapping]] = ..., get_groups: _Optional[_Union[NetworkAPI_v1.API_v1_Clear_Response.GetGroups, _Mapping]] = ..., get_group_icon: _Optional[_Union[NetworkAPI_v1.API_v1_Clear_Response.GetGroupIcon, _Mapping]] = ..., put_group_icon: _Optional[_Union[NetworkAPI_v1.API_v1_Clear_Response.PutGroupIcon, _Mapping]] = ...) -> None: ...
    class API_v1_Groups_Response(_message.Message):
        __slots__ = ("groups", "trigger_group")
        class GroupsRequest(_message.Message):
            __slots__ = ("groups",)
            class Group(_message.Message):
                __slots__ = ("id", "color")
                ID_FIELD_NUMBER: _ClassVar[int]
                COLOR_FIELD_NUMBER: _ClassVar[int]
                id: _proApiV1BasicTypes_pb2.API_v1_Identifier
                color: _proApiV1BasicTypes_pb2.API_v1_Color
                def __init__(self, id: _Optional[_Union[_proApiV1BasicTypes_pb2.API_v1_Identifier, _Mapping]] = ..., color: _Optional[_Union[_proApiV1BasicTypes_pb2.API_v1_Color, _Mapping]] = ...) -> None: ...
            GROUPS_FIELD_NUMBER: _ClassVar[int]
            groups: _containers.RepeatedCompositeFieldContainer[NetworkAPI_v1.API_v1_Groups_Response.GroupsRequest.Group]
            def __init__(self, groups: _Optional[_Iterable[_Union[NetworkAPI_v1.API_v1_Groups_Response.GroupsRequest.Group, _Mapping]]] = ...) -> None: ...
        class TriggerGroup(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        GROUPS_FIELD_NUMBER: _ClassVar[int]
        TRIGGER_GROUP_FIELD_NUMBER: _ClassVar[int]
        groups: NetworkAPI_v1.API_v1_Groups_Response.GroupsRequest
        trigger_group: NetworkAPI_v1.API_v1_Groups_Response.TriggerGroup
        def __init__(self, groups: _Optional[_Union[NetworkAPI_v1.API_v1_Groups_Response.GroupsRequest, _Mapping]] = ..., trigger_group: _Optional[_Union[NetworkAPI_v1.API_v1_Groups_Response.TriggerGroup, _Mapping]] = ...) -> None: ...
    class API_v1_Link_Response(_message.Message):
        __slots__ = ("heartbeat", "status", "add_member", "remove_member")
        class Heartbeat(_message.Message):
            __slots__ = ("group_definition", "status")
            GROUP_DEFINITION_FIELD_NUMBER: _ClassVar[int]
            STATUS_FIELD_NUMBER: _ClassVar[int]
            group_definition: _proApiV1BasicTypes_pb2.API_v1_GroupDefinition
            status: _proApiV1BasicTypes_pb2.API_v1_GroupMemberStatus
            def __init__(self, group_definition: _Optional[_Union[_proApiV1BasicTypes_pb2.API_v1_GroupDefinition, _Mapping]] = ..., status: _Optional[_Union[_proApiV1BasicTypes_pb2.API_v1_GroupMemberStatus, _Mapping]] = ...) -> None: ...
        class Status(_message.Message):
            __slots__ = ("group_definition", "member_name")
            GROUP_DEFINITION_FIELD_NUMBER: _ClassVar[int]
            MEMBER_NAME_FIELD_NUMBER: _ClassVar[int]
            group_definition: _proApiV1BasicTypes_pb2.API_v1_GroupDefinition
            member_name: str
            def __init__(self, group_definition: _Optional[_Union[_proApiV1BasicTypes_pb2.API_v1_GroupDefinition, _Mapping]] = ..., member_name: _Optional[str] = ...) -> None: ...
        class AddMember(_message.Message):
            __slots__ = ("group_definition", "accept", "decline")
            class RemoteMachineAccepts(_message.Message):
                __slots__ = ()
                def __init__(self) -> None: ...
            class RemoteMachineDecline(_message.Message):
                __slots__ = ("reason",)
                class DeclineReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                    __slots__ = ()
                    ALREADY_IN_GROUP: _ClassVar[NetworkAPI_v1.API_v1_Link_Response.AddMember.RemoteMachineDecline.DeclineReason]
                    USER_DECLINED: _ClassVar[NetworkAPI_v1.API_v1_Link_Response.AddMember.RemoteMachineDecline.DeclineReason]
                ALREADY_IN_GROUP: NetworkAPI_v1.API_v1_Link_Response.AddMember.RemoteMachineDecline.DeclineReason
                USER_DECLINED: NetworkAPI_v1.API_v1_Link_Response.AddMember.RemoteMachineDecline.DeclineReason
                REASON_FIELD_NUMBER: _ClassVar[int]
                reason: NetworkAPI_v1.API_v1_Link_Response.AddMember.RemoteMachineDecline.DeclineReason
                def __init__(self, reason: _Optional[_Union[NetworkAPI_v1.API_v1_Link_Response.AddMember.RemoteMachineDecline.DeclineReason, str]] = ...) -> None: ...
            GROUP_DEFINITION_FIELD_NUMBER: _ClassVar[int]
            ACCEPT_FIELD_NUMBER: _ClassVar[int]
            DECLINE_FIELD_NUMBER: _ClassVar[int]
            group_definition: _proApiV1BasicTypes_pb2.API_v1_GroupDefinition
            accept: NetworkAPI_v1.API_v1_Link_Response.AddMember.RemoteMachineAccepts
            decline: NetworkAPI_v1.API_v1_Link_Response.AddMember.RemoteMachineDecline
            def __init__(self, group_definition: _Optional[_Union[_proApiV1BasicTypes_pb2.API_v1_GroupDefinition, _Mapping]] = ..., accept: _Optional[_Union[NetworkAPI_v1.API_v1_Link_Response.AddMember.RemoteMachineAccepts, _Mapping]] = ..., decline: _Optional[_Union[NetworkAPI_v1.API_v1_Link_Response.AddMember.RemoteMachineDecline, _Mapping]] = ...) -> None: ...
        class RemoveMember(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        HEARTBEAT_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        ADD_MEMBER_FIELD_NUMBER: _ClassVar[int]
        REMOVE_MEMBER_FIELD_NUMBER: _ClassVar[int]
        heartbeat: NetworkAPI_v1.API_v1_Link_Response.Heartbeat
        status: NetworkAPI_v1.API_v1_Link_Response.Status
        add_member: NetworkAPI_v1.API_v1_Link_Response.AddMember
        remove_member: NetworkAPI_v1.API_v1_Link_Response.RemoveMember
        def __init__(self, heartbeat: _Optional[_Union[NetworkAPI_v1.API_v1_Link_Response.Heartbeat, _Mapping]] = ..., status: _Optional[_Union[NetworkAPI_v1.API_v1_Link_Response.Status, _Mapping]] = ..., add_member: _Optional[_Union[NetworkAPI_v1.API_v1_Link_Response.AddMember, _Mapping]] = ..., remove_member: _Optional[_Union[NetworkAPI_v1.API_v1_Link_Response.RemoveMember, _Mapping]] = ...) -> None: ...
    class API_v1_Library_Response(_message.Message):
        __slots__ = ("libraries", "library", "triggger")
        class Libraries(_message.Message):
            __slots__ = ("libraries",)
            LIBRARIES_FIELD_NUMBER: _ClassVar[int]
            libraries: _containers.RepeatedCompositeFieldContainer[_proApiV1BasicTypes_pb2.API_v1_Identifier]
            def __init__(self, libraries: _Optional[_Iterable[_Union[_proApiV1BasicTypes_pb2.API_v1_Identifier, _Mapping]]] = ...) -> None: ...
        class Library(_message.Message):
            __slots__ = ("update_type", "items")
            class UpdateType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                all: _ClassVar[NetworkAPI_v1.API_v1_Library_Response.Library.UpdateType]
                add: _ClassVar[NetworkAPI_v1.API_v1_Library_Response.Library.UpdateType]
                remove: _ClassVar[NetworkAPI_v1.API_v1_Library_Response.Library.UpdateType]
            all: NetworkAPI_v1.API_v1_Library_Response.Library.UpdateType
            add: NetworkAPI_v1.API_v1_Library_Response.Library.UpdateType
            remove: NetworkAPI_v1.API_v1_Library_Response.Library.UpdateType
            UPDATE_TYPE_FIELD_NUMBER: _ClassVar[int]
            ITEMS_FIELD_NUMBER: _ClassVar[int]
            update_type: NetworkAPI_v1.API_v1_Library_Response.Library.UpdateType
            items: _containers.RepeatedCompositeFieldContainer[_proApiV1BasicTypes_pb2.API_v1_Identifier]
            def __init__(self, update_type: _Optional[_Union[NetworkAPI_v1.API_v1_Library_Response.Library.UpdateType, str]] = ..., items: _Optional[_Iterable[_Union[_proApiV1BasicTypes_pb2.API_v1_Identifier, _Mapping]]] = ...) -> None: ...
        class Trigger(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        LIBRARIES_FIELD_NUMBER: _ClassVar[int]
        LIBRARY_FIELD_NUMBER: _ClassVar[int]
        TRIGGGER_FIELD_NUMBER: _ClassVar[int]
        libraries: NetworkAPI_v1.API_v1_Library_Response.Libraries
        library: NetworkAPI_v1.API_v1_Library_Response.Library
        triggger: NetworkAPI_v1.API_v1_Library_Response.Trigger
        def __init__(self, libraries: _Optional[_Union[NetworkAPI_v1.API_v1_Library_Response.Libraries, _Mapping]] = ..., library: _Optional[_Union[NetworkAPI_v1.API_v1_Library_Response.Library, _Mapping]] = ..., triggger: _Optional[_Union[NetworkAPI_v1.API_v1_Library_Response.Trigger, _Mapping]] = ...) -> None: ...
    class API_v1_Looks_Response(_message.Message):
        __slots__ = ("looks", "create_look", "get_current_look", "put_current_look", "get_look", "put_look", "delete_look", "trigger_look")
        class Looks(_message.Message):
            __slots__ = ("looks",)
            LOOKS_FIELD_NUMBER: _ClassVar[int]
            looks: _containers.RepeatedCompositeFieldContainer[_proApiV1BasicTypes_pb2.API_v1_Look]
            def __init__(self, looks: _Optional[_Iterable[_Union[_proApiV1BasicTypes_pb2.API_v1_Look, _Mapping]]] = ...) -> None: ...
        class CreateLook(_message.Message):
            __slots__ = ("look",)
            LOOK_FIELD_NUMBER: _ClassVar[int]
            look: _proApiV1BasicTypes_pb2.API_v1_Look
            def __init__(self, look: _Optional[_Union[_proApiV1BasicTypes_pb2.API_v1_Look, _Mapping]] = ...) -> None: ...
        class GetCurrentLook(_message.Message):
            __slots__ = ("look",)
            LOOK_FIELD_NUMBER: _ClassVar[int]
            look: _proApiV1BasicTypes_pb2.API_v1_Look
            def __init__(self, look: _Optional[_Union[_proApiV1BasicTypes_pb2.API_v1_Look, _Mapping]] = ...) -> None: ...
        class PutCurrentLook(_message.Message):
            __slots__ = ("look",)
            LOOK_FIELD_NUMBER: _ClassVar[int]
            look: _proApiV1BasicTypes_pb2.API_v1_Look
            def __init__(self, look: _Optional[_Union[_proApiV1BasicTypes_pb2.API_v1_Look, _Mapping]] = ...) -> None: ...
        class GetLook(_message.Message):
            __slots__ = ("look",)
            LOOK_FIELD_NUMBER: _ClassVar[int]
            look: _proApiV1BasicTypes_pb2.API_v1_Look
            def __init__(self, look: _Optional[_Union[_proApiV1BasicTypes_pb2.API_v1_Look, _Mapping]] = ...) -> None: ...
        class PutLook(_message.Message):
            __slots__ = ("look",)
            LOOK_FIELD_NUMBER: _ClassVar[int]
            look: _proApiV1BasicTypes_pb2.API_v1_Look
            def __init__(self, look: _Optional[_Union[_proApiV1BasicTypes_pb2.API_v1_Look, _Mapping]] = ...) -> None: ...
        class DeleteLook(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class TriggerLook(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        LOOKS_FIELD_NUMBER: _ClassVar[int]
        CREATE_LOOK_FIELD_NUMBER: _ClassVar[int]
        GET_CURRENT_LOOK_FIELD_NUMBER: _ClassVar[int]
        PUT_CURRENT_LOOK_FIELD_NUMBER: _ClassVar[int]
        GET_LOOK_FIELD_NUMBER: _ClassVar[int]
        PUT_LOOK_FIELD_NUMBER: _ClassVar[int]
        DELETE_LOOK_FIELD_NUMBER: _ClassVar[int]
        TRIGGER_LOOK_FIELD_NUMBER: _ClassVar[int]
        looks: NetworkAPI_v1.API_v1_Looks_Response.Looks
        create_look: NetworkAPI_v1.API_v1_Looks_Response.CreateLook
        get_current_look: NetworkAPI_v1.API_v1_Looks_Response.GetCurrentLook
        put_current_look: NetworkAPI_v1.API_v1_Looks_Response.PutCurrentLook
        get_look: NetworkAPI_v1.API_v1_Looks_Response.GetLook
        put_look: NetworkAPI_v1.API_v1_Looks_Response.PutLook
        delete_look: NetworkAPI_v1.API_v1_Looks_Response.DeleteLook
        trigger_look: NetworkAPI_v1.API_v1_Looks_Response.TriggerLook
        def __init__(self, looks: _Optional[_Union[NetworkAPI_v1.API_v1_Looks_Response.Looks, _Mapping]] = ..., create_look: _Optional[_Union[NetworkAPI_v1.API_v1_Looks_Response.CreateLook, _Mapping]] = ..., get_current_look: _Optional[_Union[NetworkAPI_v1.API_v1_Looks_Response.GetCurrentLook, _Mapping]] = ..., put_current_look: _Optional[_Union[NetworkAPI_v1.API_v1_Looks_Response.PutCurrentLook, _Mapping]] = ..., get_look: _Optional[_Union[NetworkAPI_v1.API_v1_Looks_Response.GetLook, _Mapping]] = ..., put_look: _Optional[_Union[NetworkAPI_v1.API_v1_Looks_Response.PutLook, _Mapping]] = ..., delete_look: _Optional[_Union[NetworkAPI_v1.API_v1_Looks_Response.DeleteLook, _Mapping]] = ..., trigger_look: _Optional[_Union[NetworkAPI_v1.API_v1_Looks_Response.TriggerLook, _Mapping]] = ...) -> None: ...
    class API_v1_Macro_Response(_message.Message):
        __slots__ = ("macros", "get_macro", "put_macro", "delete_macro", "trigger_macro")
        class Macros(_message.Message):
            __slots__ = ("macros",)
            MACROS_FIELD_NUMBER: _ClassVar[int]
            macros: _containers.RepeatedCompositeFieldContainer[_proApiV1BasicTypes_pb2.API_v1_Macro]
            def __init__(self, macros: _Optional[_Iterable[_Union[_proApiV1BasicTypes_pb2.API_v1_Macro, _Mapping]]] = ...) -> None: ...
        class GetMacro(_message.Message):
            __slots__ = ("macro",)
            MACRO_FIELD_NUMBER: _ClassVar[int]
            macro: _proApiV1BasicTypes_pb2.API_v1_Macro
            def __init__(self, macro: _Optional[_Union[_proApiV1BasicTypes_pb2.API_v1_Macro, _Mapping]] = ...) -> None: ...
        class PutMacro(_message.Message):
            __slots__ = ("macro",)
            MACRO_FIELD_NUMBER: _ClassVar[int]
            macro: _proApiV1BasicTypes_pb2.API_v1_Macro
            def __init__(self, macro: _Optional[_Union[_proApiV1BasicTypes_pb2.API_v1_Macro, _Mapping]] = ...) -> None: ...
        class DeleteMacro(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class TriggerMacro(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        MACROS_FIELD_NUMBER: _ClassVar[int]
        GET_MACRO_FIELD_NUMBER: _ClassVar[int]
        PUT_MACRO_FIELD_NUMBER: _ClassVar[int]
        DELETE_MACRO_FIELD_NUMBER: _ClassVar[int]
        TRIGGER_MACRO_FIELD_NUMBER: _ClassVar[int]
        macros: NetworkAPI_v1.API_v1_Macro_Response.Macros
        get_macro: NetworkAPI_v1.API_v1_Macro_Response.GetMacro
        put_macro: NetworkAPI_v1.API_v1_Macro_Response.PutMacro
        delete_macro: NetworkAPI_v1.API_v1_Macro_Response.DeleteMacro
        trigger_macro: NetworkAPI_v1.API_v1_Macro_Response.TriggerMacro
        def __init__(self, macros: _Optional[_Union[NetworkAPI_v1.API_v1_Macro_Response.Macros, _Mapping]] = ..., get_macro: _Optional[_Union[NetworkAPI_v1.API_v1_Macro_Response.GetMacro, _Mapping]] = ..., put_macro: _Optional[_Union[NetworkAPI_v1.API_v1_Macro_Response.PutMacro, _Mapping]] = ..., delete_macro: _Optional[_Union[NetworkAPI_v1.API_v1_Macro_Response.DeleteMacro, _Mapping]] = ..., trigger_macro: _Optional[_Union[NetworkAPI_v1.API_v1_Macro_Response.TriggerMacro, _Mapping]] = ...) -> None: ...
    class API_v1_Masks_Response(_message.Message):
        __slots__ = ("masks", "get_mask", "get_thumbnail")
        class Masks(_message.Message):
            __slots__ = ("masks",)
            MASKS_FIELD_NUMBER: _ClassVar[int]
            masks: _containers.RepeatedCompositeFieldContainer[_proApiV1BasicTypes_pb2.API_v1_Identifier]
            def __init__(self, masks: _Optional[_Iterable[_Union[_proApiV1BasicTypes_pb2.API_v1_Identifier, _Mapping]]] = ...) -> None: ...
        class GetMask(_message.Message):
            __slots__ = ("id",)
            ID_FIELD_NUMBER: _ClassVar[int]
            id: _proApiV1BasicTypes_pb2.API_v1_Identifier
            def __init__(self, id: _Optional[_Union[_proApiV1BasicTypes_pb2.API_v1_Identifier, _Mapping]] = ...) -> None: ...
        class GetThumbnail(_message.Message):
            __slots__ = ("data",)
            DATA_FIELD_NUMBER: _ClassVar[int]
            data: bytes
            def __init__(self, data: _Optional[bytes] = ...) -> None: ...
        MASKS_FIELD_NUMBER: _ClassVar[int]
        GET_MASK_FIELD_NUMBER: _ClassVar[int]
        GET_THUMBNAIL_FIELD_NUMBER: _ClassVar[int]
        masks: NetworkAPI_v1.API_v1_Masks_Response.Masks
        get_mask: NetworkAPI_v1.API_v1_Masks_Response.GetMask
        get_thumbnail: NetworkAPI_v1.API_v1_Masks_Response.GetThumbnail
        def __init__(self, masks: _Optional[_Union[NetworkAPI_v1.API_v1_Masks_Response.Masks, _Mapping]] = ..., get_mask: _Optional[_Union[NetworkAPI_v1.API_v1_Masks_Response.GetMask, _Mapping]] = ..., get_thumbnail: _Optional[_Union[NetworkAPI_v1.API_v1_Masks_Response.GetThumbnail, _Mapping]] = ...) -> None: ...
    class API_v1_Media_Response(_message.Message):
        __slots__ = ("playlists", "get_playlist", "get_playlist_updates", "get_thumbnail", "playlist_focused", "playlist_active", "focus", "trigger")
        class Playlists(_message.Message):
            __slots__ = ("playlists",)
            PLAYLISTS_FIELD_NUMBER: _ClassVar[int]
            playlists: _containers.RepeatedCompositeFieldContainer[_proApiV1BasicTypes_pb2.API_v1_Playlist]
            def __init__(self, playlists: _Optional[_Iterable[_Union[_proApiV1BasicTypes_pb2.API_v1_Playlist, _Mapping]]] = ...) -> None: ...
        class GetPlaylist(_message.Message):
            __slots__ = ("id", "items")
            ID_FIELD_NUMBER: _ClassVar[int]
            ITEMS_FIELD_NUMBER: _ClassVar[int]
            id: _proApiV1BasicTypes_pb2.API_v1_Identifier
            items: _containers.RepeatedCompositeFieldContainer[_proApiV1BasicTypes_pb2.API_v1_MediaPlaylistItem]
            def __init__(self, id: _Optional[_Union[_proApiV1BasicTypes_pb2.API_v1_Identifier, _Mapping]] = ..., items: _Optional[_Iterable[_Union[_proApiV1BasicTypes_pb2.API_v1_MediaPlaylistItem, _Mapping]]] = ...) -> None: ...
        class GetPlaylistUpdates(_message.Message):
            __slots__ = ("id",)
            ID_FIELD_NUMBER: _ClassVar[int]
            id: _proApiV1BasicTypes_pb2.API_v1_Identifier
            def __init__(self, id: _Optional[_Union[_proApiV1BasicTypes_pb2.API_v1_Identifier, _Mapping]] = ...) -> None: ...
        class GetThumbnail(_message.Message):
            __slots__ = ("uuid", "thumbnail_data")
            UUID_FIELD_NUMBER: _ClassVar[int]
            THUMBNAIL_DATA_FIELD_NUMBER: _ClassVar[int]
            uuid: _basicTypes_pb2.UUID
            thumbnail_data: bytes
            def __init__(self, uuid: _Optional[_Union[_basicTypes_pb2.UUID, _Mapping]] = ..., thumbnail_data: _Optional[bytes] = ...) -> None: ...
        class GetFocusedPlaylist(_message.Message):
            __slots__ = ("id",)
            ID_FIELD_NUMBER: _ClassVar[int]
            id: _proApiV1BasicTypes_pb2.API_v1_Identifier
            def __init__(self, id: _Optional[_Union[_proApiV1BasicTypes_pb2.API_v1_Identifier, _Mapping]] = ...) -> None: ...
        class GetActivePlaylist(_message.Message):
            __slots__ = ("playlist", "item")
            PLAYLIST_FIELD_NUMBER: _ClassVar[int]
            ITEM_FIELD_NUMBER: _ClassVar[int]
            playlist: _proApiV1BasicTypes_pb2.API_v1_Identifier
            item: _proApiV1BasicTypes_pb2.API_v1_Identifier
            def __init__(self, playlist: _Optional[_Union[_proApiV1BasicTypes_pb2.API_v1_Identifier, _Mapping]] = ..., item: _Optional[_Union[_proApiV1BasicTypes_pb2.API_v1_Identifier, _Mapping]] = ...) -> None: ...
        class EmptyMessage(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        PLAYLISTS_FIELD_NUMBER: _ClassVar[int]
        GET_PLAYLIST_FIELD_NUMBER: _ClassVar[int]
        GET_PLAYLIST_UPDATES_FIELD_NUMBER: _ClassVar[int]
        GET_THUMBNAIL_FIELD_NUMBER: _ClassVar[int]
        PLAYLIST_FOCUSED_FIELD_NUMBER: _ClassVar[int]
        PLAYLIST_ACTIVE_FIELD_NUMBER: _ClassVar[int]
        FOCUS_FIELD_NUMBER: _ClassVar[int]
        TRIGGER_FIELD_NUMBER: _ClassVar[int]
        playlists: NetworkAPI_v1.API_v1_Media_Response.Playlists
        get_playlist: NetworkAPI_v1.API_v1_Media_Response.GetPlaylist
        get_playlist_updates: NetworkAPI_v1.API_v1_Media_Response.GetPlaylistUpdates
        get_thumbnail: NetworkAPI_v1.API_v1_Media_Response.GetThumbnail
        playlist_focused: NetworkAPI_v1.API_v1_Media_Response.GetFocusedPlaylist
        playlist_active: NetworkAPI_v1.API_v1_Media_Response.GetActivePlaylist
        focus: NetworkAPI_v1.API_v1_Media_Response.EmptyMessage
        trigger: NetworkAPI_v1.API_v1_Media_Response.EmptyMessage
        def __init__(self, playlists: _Optional[_Union[NetworkAPI_v1.API_v1_Media_Response.Playlists, _Mapping]] = ..., get_playlist: _Optional[_Union[NetworkAPI_v1.API_v1_Media_Response.GetPlaylist, _Mapping]] = ..., get_playlist_updates: _Optional[_Union[NetworkAPI_v1.API_v1_Media_Response.GetPlaylistUpdates, _Mapping]] = ..., get_thumbnail: _Optional[_Union[NetworkAPI_v1.API_v1_Media_Response.GetThumbnail, _Mapping]] = ..., playlist_focused: _Optional[_Union[NetworkAPI_v1.API_v1_Media_Response.GetFocusedPlaylist, _Mapping]] = ..., playlist_active: _Optional[_Union[NetworkAPI_v1.API_v1_Media_Response.GetActivePlaylist, _Mapping]] = ..., focus: _Optional[_Union[NetworkAPI_v1.API_v1_Media_Response.EmptyMessage, _Mapping]] = ..., trigger: _Optional[_Union[NetworkAPI_v1.API_v1_Media_Response.EmptyMessage, _Mapping]] = ...) -> None: ...
    class API_v1_Message_Response(_message.Message):
        __slots__ = ("messages", "create_message", "get_message", "put_message", "delete_message", "trigger_message", "clear_message")
        class Messages(_message.Message):
            __slots__ = ("messages",)
            MESSAGES_FIELD_NUMBER: _ClassVar[int]
            messages: _containers.RepeatedCompositeFieldContainer[_proApiV1BasicTypes_pb2.API_v1_Message]
            def __init__(self, messages: _Optional[_Iterable[_Union[_proApiV1BasicTypes_pb2.API_v1_Message, _Mapping]]] = ...) -> None: ...
        class CreateMessage(_message.Message):
            __slots__ = ("message",)
            MESSAGE_FIELD_NUMBER: _ClassVar[int]
            message: _proApiV1BasicTypes_pb2.API_v1_Message
            def __init__(self, message: _Optional[_Union[_proApiV1BasicTypes_pb2.API_v1_Message, _Mapping]] = ...) -> None: ...
        class GetMessage(_message.Message):
            __slots__ = ("message",)
            MESSAGE_FIELD_NUMBER: _ClassVar[int]
            message: _proApiV1BasicTypes_pb2.API_v1_Message
            def __init__(self, message: _Optional[_Union[_proApiV1BasicTypes_pb2.API_v1_Message, _Mapping]] = ...) -> None: ...
        class PutMessage(_message.Message):
            __slots__ = ("message",)
            MESSAGE_FIELD_NUMBER: _ClassVar[int]
            message: _proApiV1BasicTypes_pb2.API_v1_Message
            def __init__(self, message: _Optional[_Union[_proApiV1BasicTypes_pb2.API_v1_Message, _Mapping]] = ...) -> None: ...
        class DeleteMessage(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class TriggerMessage(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class ClearMessage(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        MESSAGES_FIELD_NUMBER: _ClassVar[int]
        CREATE_MESSAGE_FIELD_NUMBER: _ClassVar[int]
        GET_MESSAGE_FIELD_NUMBER: _ClassVar[int]
        PUT_MESSAGE_FIELD_NUMBER: _ClassVar[int]
        DELETE_MESSAGE_FIELD_NUMBER: _ClassVar[int]
        TRIGGER_MESSAGE_FIELD_NUMBER: _ClassVar[int]
        CLEAR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
        messages: NetworkAPI_v1.API_v1_Message_Response.Messages
        create_message: NetworkAPI_v1.API_v1_Message_Response.CreateMessage
        get_message: NetworkAPI_v1.API_v1_Message_Response.GetMessage
        put_message: NetworkAPI_v1.API_v1_Message_Response.PutMessage
        delete_message: NetworkAPI_v1.API_v1_Message_Response.DeleteMessage
        trigger_message: NetworkAPI_v1.API_v1_Message_Response.TriggerMessage
        clear_message: NetworkAPI_v1.API_v1_Message_Response.ClearMessage
        def __init__(self, messages: _Optional[_Union[NetworkAPI_v1.API_v1_Message_Response.Messages, _Mapping]] = ..., create_message: _Optional[_Union[NetworkAPI_v1.API_v1_Message_Response.CreateMessage, _Mapping]] = ..., get_message: _Optional[_Union[NetworkAPI_v1.API_v1_Message_Response.GetMessage, _Mapping]] = ..., put_message: _Optional[_Union[NetworkAPI_v1.API_v1_Message_Response.PutMessage, _Mapping]] = ..., delete_message: _Optional[_Union[NetworkAPI_v1.API_v1_Message_Response.DeleteMessage, _Mapping]] = ..., trigger_message: _Optional[_Union[NetworkAPI_v1.API_v1_Message_Response.TriggerMessage, _Mapping]] = ..., clear_message: _Optional[_Union[NetworkAPI_v1.API_v1_Message_Response.ClearMessage, _Mapping]] = ...) -> None: ...
    class API_v1_Miscellaneous_Response(_message.Message):
        __slots__ = ("find_my_mouse",)
        class FindMyMouse(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        FIND_MY_MOUSE_FIELD_NUMBER: _ClassVar[int]
        find_my_mouse: NetworkAPI_v1.API_v1_Miscellaneous_Response.FindMyMouse
        def __init__(self, find_my_mouse: _Optional[_Union[NetworkAPI_v1.API_v1_Miscellaneous_Response.FindMyMouse, _Mapping]] = ...) -> None: ...
    class API_v1_Playlist_Response(_message.Message):
        __slots__ = ("playlists", "create_playlist", "get_playlist", "put_playlist", "post_playlist", "get_active_playlist", "focused", "next_focus", "previous_focus", "active_presentation_focus", "active_announcement_focus", "focused_trigger", "active_presentation_trigger", "active_announcement_trigger", "focused_next_trigger", "focused_previous_trigger", "active_presentation_next_trigger", "active_announcement_next_trigger", "active_presentation_previous_trigger", "active_announcement_previous_trigger", "id_focus", "id_trigger", "id_next_trigger", "id_previous_trigger", "focused_index_trigger", "active_presentation_index_trigger", "active_announcement_index_trigger", "id_updates")
        class Playlists(_message.Message):
            __slots__ = ("playlists",)
            PLAYLISTS_FIELD_NUMBER: _ClassVar[int]
            playlists: _containers.RepeatedCompositeFieldContainer[_proApiV1BasicTypes_pb2.API_v1_Playlist]
            def __init__(self, playlists: _Optional[_Iterable[_Union[_proApiV1BasicTypes_pb2.API_v1_Playlist, _Mapping]]] = ...) -> None: ...
        class CreatePlaylist(_message.Message):
            __slots__ = ("playlist",)
            PLAYLIST_FIELD_NUMBER: _ClassVar[int]
            playlist: _proApiV1BasicTypes_pb2.API_v1_Playlist
            def __init__(self, playlist: _Optional[_Union[_proApiV1BasicTypes_pb2.API_v1_Playlist, _Mapping]] = ...) -> None: ...
        class GetActivePlaylist(_message.Message):
            __slots__ = ("presentation", "announcements")
            PRESENTATION_FIELD_NUMBER: _ClassVar[int]
            ANNOUNCEMENTS_FIELD_NUMBER: _ClassVar[int]
            presentation: _proApiV1BasicTypes_pb2.API_v1_PlaylistAndItem
            announcements: _proApiV1BasicTypes_pb2.API_v1_PlaylistAndItem
            def __init__(self, presentation: _Optional[_Union[_proApiV1BasicTypes_pb2.API_v1_PlaylistAndItem, _Mapping]] = ..., announcements: _Optional[_Union[_proApiV1BasicTypes_pb2.API_v1_PlaylistAndItem, _Mapping]] = ...) -> None: ...
        class GetPlaylist(_message.Message):
            __slots__ = ("id", "items")
            ID_FIELD_NUMBER: _ClassVar[int]
            ITEMS_FIELD_NUMBER: _ClassVar[int]
            id: _proApiV1BasicTypes_pb2.API_v1_Identifier
            items: _containers.RepeatedCompositeFieldContainer[_proApiV1BasicTypes_pb2.API_v1_PlaylistItem]
            def __init__(self, id: _Optional[_Union[_proApiV1BasicTypes_pb2.API_v1_Identifier, _Mapping]] = ..., items: _Optional[_Iterable[_Union[_proApiV1BasicTypes_pb2.API_v1_PlaylistItem, _Mapping]]] = ...) -> None: ...
        class PutPlaylist(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class PostPlaylist(_message.Message):
            __slots__ = ("playlist",)
            PLAYLIST_FIELD_NUMBER: _ClassVar[int]
            playlist: _proApiV1BasicTypes_pb2.API_v1_Playlist
            def __init__(self, playlist: _Optional[_Union[_proApiV1BasicTypes_pb2.API_v1_Playlist, _Mapping]] = ...) -> None: ...
        class GetFocusedPlaylist(_message.Message):
            __slots__ = ("playlist",)
            PLAYLIST_FIELD_NUMBER: _ClassVar[int]
            playlist: _proApiV1BasicTypes_pb2.API_v1_PlaylistAndItem
            def __init__(self, playlist: _Optional[_Union[_proApiV1BasicTypes_pb2.API_v1_PlaylistAndItem, _Mapping]] = ...) -> None: ...
        class EmptyMessage(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        PLAYLISTS_FIELD_NUMBER: _ClassVar[int]
        CREATE_PLAYLIST_FIELD_NUMBER: _ClassVar[int]
        GET_PLAYLIST_FIELD_NUMBER: _ClassVar[int]
        PUT_PLAYLIST_FIELD_NUMBER: _ClassVar[int]
        POST_PLAYLIST_FIELD_NUMBER: _ClassVar[int]
        GET_ACTIVE_PLAYLIST_FIELD_NUMBER: _ClassVar[int]
        FOCUSED_FIELD_NUMBER: _ClassVar[int]
        NEXT_FOCUS_FIELD_NUMBER: _ClassVar[int]
        PREVIOUS_FOCUS_FIELD_NUMBER: _ClassVar[int]
        ACTIVE_PRESENTATION_FOCUS_FIELD_NUMBER: _ClassVar[int]
        ACTIVE_ANNOUNCEMENT_FOCUS_FIELD_NUMBER: _ClassVar[int]
        FOCUSED_TRIGGER_FIELD_NUMBER: _ClassVar[int]
        ACTIVE_PRESENTATION_TRIGGER_FIELD_NUMBER: _ClassVar[int]
        ACTIVE_ANNOUNCEMENT_TRIGGER_FIELD_NUMBER: _ClassVar[int]
        FOCUSED_NEXT_TRIGGER_FIELD_NUMBER: _ClassVar[int]
        FOCUSED_PREVIOUS_TRIGGER_FIELD_NUMBER: _ClassVar[int]
        ACTIVE_PRESENTATION_NEXT_TRIGGER_FIELD_NUMBER: _ClassVar[int]
        ACTIVE_ANNOUNCEMENT_NEXT_TRIGGER_FIELD_NUMBER: _ClassVar[int]
        ACTIVE_PRESENTATION_PREVIOUS_TRIGGER_FIELD_NUMBER: _ClassVar[int]
        ACTIVE_ANNOUNCEMENT_PREVIOUS_TRIGGER_FIELD_NUMBER: _ClassVar[int]
        ID_FOCUS_FIELD_NUMBER: _ClassVar[int]
        ID_TRIGGER_FIELD_NUMBER: _ClassVar[int]
        ID_NEXT_TRIGGER_FIELD_NUMBER: _ClassVar[int]
        ID_PREVIOUS_TRIGGER_FIELD_NUMBER: _ClassVar[int]
        FOCUSED_INDEX_TRIGGER_FIELD_NUMBER: _ClassVar[int]
        ACTIVE_PRESENTATION_INDEX_TRIGGER_FIELD_NUMBER: _ClassVar[int]
        ACTIVE_ANNOUNCEMENT_INDEX_TRIGGER_FIELD_NUMBER: _ClassVar[int]
        ID_UPDATES_FIELD_NUMBER: _ClassVar[int]
        playlists: NetworkAPI_v1.API_v1_Playlist_Response.Playlists
        create_playlist: NetworkAPI_v1.API_v1_Playlist_Response.CreatePlaylist
        get_playlist: NetworkAPI_v1.API_v1_Playlist_Response.GetPlaylist
        put_playlist: NetworkAPI_v1.API_v1_Playlist_Response.PutPlaylist
        post_playlist: NetworkAPI_v1.API_v1_Playlist_Response.PostPlaylist
        get_active_playlist: NetworkAPI_v1.API_v1_Playlist_Response.GetActivePlaylist
        focused: NetworkAPI_v1.API_v1_Playlist_Response.GetFocusedPlaylist
        next_focus: NetworkAPI_v1.API_v1_Playlist_Response.EmptyMessage
        previous_focus: NetworkAPI_v1.API_v1_Playlist_Response.EmptyMessage
        active_presentation_focus: NetworkAPI_v1.API_v1_Playlist_Response.EmptyMessage
        active_announcement_focus: NetworkAPI_v1.API_v1_Playlist_Response.EmptyMessage
        focused_trigger: NetworkAPI_v1.API_v1_Playlist_Response.EmptyMessage
        active_presentation_trigger: NetworkAPI_v1.API_v1_Playlist_Response.EmptyMessage
        active_announcement_trigger: NetworkAPI_v1.API_v1_Playlist_Response.EmptyMessage
        focused_next_trigger: NetworkAPI_v1.API_v1_Playlist_Response.EmptyMessage
        focused_previous_trigger: NetworkAPI_v1.API_v1_Playlist_Response.EmptyMessage
        active_presentation_next_trigger: NetworkAPI_v1.API_v1_Playlist_Response.EmptyMessage
        active_announcement_next_trigger: NetworkAPI_v1.API_v1_Playlist_Response.EmptyMessage
        active_presentation_previous_trigger: NetworkAPI_v1.API_v1_Playlist_Response.EmptyMessage
        active_announcement_previous_trigger: NetworkAPI_v1.API_v1_Playlist_Response.EmptyMessage
        id_focus: NetworkAPI_v1.API_v1_Playlist_Response.EmptyMessage
        id_trigger: NetworkAPI_v1.API_v1_Playlist_Response.EmptyMessage
        id_next_trigger: NetworkAPI_v1.API_v1_Playlist_Response.EmptyMessage
        id_previous_trigger: NetworkAPI_v1.API_v1_Playlist_Response.EmptyMessage
        focused_index_trigger: NetworkAPI_v1.API_v1_Playlist_Response.EmptyMessage
        active_presentation_index_trigger: NetworkAPI_v1.API_v1_Playlist_Response.EmptyMessage
        active_announcement_index_trigger: NetworkAPI_v1.API_v1_Playlist_Response.EmptyMessage
        id_updates: NetworkAPI_v1.API_v1_Playlist_Response.EmptyMessage
        def __init__(self, playlists: _Optional[_Union[NetworkAPI_v1.API_v1_Playlist_Response.Playlists, _Mapping]] = ..., create_playlist: _Optional[_Union[NetworkAPI_v1.API_v1_Playlist_Response.CreatePlaylist, _Mapping]] = ..., get_playlist: _Optional[_Union[NetworkAPI_v1.API_v1_Playlist_Response.GetPlaylist, _Mapping]] = ..., put_playlist: _Optional[_Union[NetworkAPI_v1.API_v1_Playlist_Response.PutPlaylist, _Mapping]] = ..., post_playlist: _Optional[_Union[NetworkAPI_v1.API_v1_Playlist_Response.PostPlaylist, _Mapping]] = ..., get_active_playlist: _Optional[_Union[NetworkAPI_v1.API_v1_Playlist_Response.GetActivePlaylist, _Mapping]] = ..., focused: _Optional[_Union[NetworkAPI_v1.API_v1_Playlist_Response.GetFocusedPlaylist, _Mapping]] = ..., next_focus: _Optional[_Union[NetworkAPI_v1.API_v1_Playlist_Response.EmptyMessage, _Mapping]] = ..., previous_focus: _Optional[_Union[NetworkAPI_v1.API_v1_Playlist_Response.EmptyMessage, _Mapping]] = ..., active_presentation_focus: _Optional[_Union[NetworkAPI_v1.API_v1_Playlist_Response.EmptyMessage, _Mapping]] = ..., active_announcement_focus: _Optional[_Union[NetworkAPI_v1.API_v1_Playlist_Response.EmptyMessage, _Mapping]] = ..., focused_trigger: _Optional[_Union[NetworkAPI_v1.API_v1_Playlist_Response.EmptyMessage, _Mapping]] = ..., active_presentation_trigger: _Optional[_Union[NetworkAPI_v1.API_v1_Playlist_Response.EmptyMessage, _Mapping]] = ..., active_announcement_trigger: _Optional[_Union[NetworkAPI_v1.API_v1_Playlist_Response.EmptyMessage, _Mapping]] = ..., focused_next_trigger: _Optional[_Union[NetworkAPI_v1.API_v1_Playlist_Response.EmptyMessage, _Mapping]] = ..., focused_previous_trigger: _Optional[_Union[NetworkAPI_v1.API_v1_Playlist_Response.EmptyMessage, _Mapping]] = ..., active_presentation_next_trigger: _Optional[_Union[NetworkAPI_v1.API_v1_Playlist_Response.EmptyMessage, _Mapping]] = ..., active_announcement_next_trigger: _Optional[_Union[NetworkAPI_v1.API_v1_Playlist_Response.EmptyMessage, _Mapping]] = ..., active_presentation_previous_trigger: _Optional[_Union[NetworkAPI_v1.API_v1_Playlist_Response.EmptyMessage, _Mapping]] = ..., active_announcement_previous_trigger: _Optional[_Union[NetworkAPI_v1.API_v1_Playlist_Response.EmptyMessage, _Mapping]] = ..., id_focus: _Optional[_Union[NetworkAPI_v1.API_v1_Playlist_Response.EmptyMessage, _Mapping]] = ..., id_trigger: _Optional[_Union[NetworkAPI_v1.API_v1_Playlist_Response.EmptyMessage, _Mapping]] = ..., id_next_trigger: _Optional[_Union[NetworkAPI_v1.API_v1_Playlist_Response.EmptyMessage, _Mapping]] = ..., id_previous_trigger: _Optional[_Union[NetworkAPI_v1.API_v1_Playlist_Response.EmptyMessage, _Mapping]] = ..., focused_index_trigger: _Optional[_Union[NetworkAPI_v1.API_v1_Playlist_Response.EmptyMessage, _Mapping]] = ..., active_presentation_index_trigger: _Optional[_Union[NetworkAPI_v1.API_v1_Playlist_Response.EmptyMessage, _Mapping]] = ..., active_announcement_index_trigger: _Optional[_Union[NetworkAPI_v1.API_v1_Playlist_Response.EmptyMessage, _Mapping]] = ..., id_updates: _Optional[_Union[NetworkAPI_v1.API_v1_Playlist_Response.EmptyMessage, _Mapping]] = ...) -> None: ...
    class API_v1_Preroll_Response(_message.Message):
        __slots__ = ("preroll_ready", "activate_preroll_item", "cancel_preroll_item")
        class PrerollReady(_message.Message):
            __slots__ = ("id", "latency", "time")
            ID_FIELD_NUMBER: _ClassVar[int]
            LATENCY_FIELD_NUMBER: _ClassVar[int]
            TIME_FIELD_NUMBER: _ClassVar[int]
            id: int
            latency: int
            time: int
            def __init__(self, id: _Optional[int] = ..., latency: _Optional[int] = ..., time: _Optional[int] = ...) -> None: ...
        class ActivatePrerollItem(_message.Message):
            __slots__ = ("success",)
            SUCCESS_FIELD_NUMBER: _ClassVar[int]
            success: bool
            def __init__(self, success: bool = ...) -> None: ...
        class CancelPrerollItem(_message.Message):
            __slots__ = ("success",)
            SUCCESS_FIELD_NUMBER: _ClassVar[int]
            success: bool
            def __init__(self, success: bool = ...) -> None: ...
        PREROLL_READY_FIELD_NUMBER: _ClassVar[int]
        ACTIVATE_PREROLL_ITEM_FIELD_NUMBER: _ClassVar[int]
        CANCEL_PREROLL_ITEM_FIELD_NUMBER: _ClassVar[int]
        preroll_ready: NetworkAPI_v1.API_v1_Preroll_Response.PrerollReady
        activate_preroll_item: NetworkAPI_v1.API_v1_Preroll_Response.ActivatePrerollItem
        cancel_preroll_item: NetworkAPI_v1.API_v1_Preroll_Response.CancelPrerollItem
        def __init__(self, preroll_ready: _Optional[_Union[NetworkAPI_v1.API_v1_Preroll_Response.PrerollReady, _Mapping]] = ..., activate_preroll_item: _Optional[_Union[NetworkAPI_v1.API_v1_Preroll_Response.ActivatePrerollItem, _Mapping]] = ..., cancel_preroll_item: _Optional[_Union[NetworkAPI_v1.API_v1_Preroll_Response.CancelPrerollItem, _Mapping]] = ...) -> None: ...
    class API_v1_Presentation_Response(_message.Message):
        __slots__ = ("active", "slide_index", "chord_chart", "chord_chart_update", "presentation", "delete_presentation", "trigger_presentation", "trigger_cue", "timeline_operation", "active_presentation_timeline_operation", "focused_presentation_timeline_operation", "active_presentation_timeline_status", "focused_presentation_timeline_status", "thumbnail", "focused", "focus", "trigger")
        class Active(_message.Message):
            __slots__ = ("presentation",)
            PRESENTATION_FIELD_NUMBER: _ClassVar[int]
            presentation: _proApiV1BasicTypes_pb2.API_v1_Presentation
            def __init__(self, presentation: _Optional[_Union[_proApiV1BasicTypes_pb2.API_v1_Presentation, _Mapping]] = ...) -> None: ...
        class SlideIndex(_message.Message):
            __slots__ = ("presentation_index",)
            PRESENTATION_INDEX_FIELD_NUMBER: _ClassVar[int]
            presentation_index: _proApiV1BasicTypes_pb2.API_v1_SlideIndex
            def __init__(self, presentation_index: _Optional[_Union[_proApiV1BasicTypes_pb2.API_v1_SlideIndex, _Mapping]] = ...) -> None: ...
        class ChordChart(_message.Message):
            __slots__ = ("chord_chart",)
            CHORD_CHART_FIELD_NUMBER: _ClassVar[int]
            chord_chart: bytes
            def __init__(self, chord_chart: _Optional[bytes] = ...) -> None: ...
        class ChordChartUpdates(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class Presentation(_message.Message):
            __slots__ = ("presentation",)
            PRESENTATION_FIELD_NUMBER: _ClassVar[int]
            presentation: _proApiV1BasicTypes_pb2.API_v1_Presentation
            def __init__(self, presentation: _Optional[_Union[_proApiV1BasicTypes_pb2.API_v1_Presentation, _Mapping]] = ...) -> None: ...
        class DeletePresentation(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class TriggerPresentation(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class TriggerCue(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class TimelineOperation(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class ActivePresentationTimelineOperation(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class FocusedPresentationTimelineOperation(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class ActivePresentationTimelineStatus(_message.Message):
            __slots__ = ("is_running", "current_time")
            IS_RUNNING_FIELD_NUMBER: _ClassVar[int]
            CURRENT_TIME_FIELD_NUMBER: _ClassVar[int]
            is_running: bool
            current_time: float
            def __init__(self, is_running: bool = ..., current_time: _Optional[float] = ...) -> None: ...
        class FocusedPresentationTimelineStatus(_message.Message):
            __slots__ = ("is_running", "current_time")
            IS_RUNNING_FIELD_NUMBER: _ClassVar[int]
            CURRENT_TIME_FIELD_NUMBER: _ClassVar[int]
            is_running: bool
            current_time: float
            def __init__(self, is_running: bool = ..., current_time: _Optional[float] = ...) -> None: ...
        class Thumbnail(_message.Message):
            __slots__ = ("data", "content_type")
            class API_v1_ContentType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                PNG: _ClassVar[NetworkAPI_v1.API_v1_Presentation_Response.Thumbnail.API_v1_ContentType]
                JPEG: _ClassVar[NetworkAPI_v1.API_v1_Presentation_Response.Thumbnail.API_v1_ContentType]
            PNG: NetworkAPI_v1.API_v1_Presentation_Response.Thumbnail.API_v1_ContentType
            JPEG: NetworkAPI_v1.API_v1_Presentation_Response.Thumbnail.API_v1_ContentType
            DATA_FIELD_NUMBER: _ClassVar[int]
            CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
            data: bytes
            content_type: NetworkAPI_v1.API_v1_Presentation_Response.Thumbnail.API_v1_ContentType
            def __init__(self, data: _Optional[bytes] = ..., content_type: _Optional[_Union[NetworkAPI_v1.API_v1_Presentation_Response.Thumbnail.API_v1_ContentType, str]] = ...) -> None: ...
        class Focused(_message.Message):
            __slots__ = ("id",)
            ID_FIELD_NUMBER: _ClassVar[int]
            id: _proApiV1BasicTypes_pb2.API_v1_Identifier
            def __init__(self, id: _Optional[_Union[_proApiV1BasicTypes_pb2.API_v1_Identifier, _Mapping]] = ...) -> None: ...
        class EmptyMessage(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        ACTIVE_FIELD_NUMBER: _ClassVar[int]
        SLIDE_INDEX_FIELD_NUMBER: _ClassVar[int]
        CHORD_CHART_FIELD_NUMBER: _ClassVar[int]
        CHORD_CHART_UPDATE_FIELD_NUMBER: _ClassVar[int]
        PRESENTATION_FIELD_NUMBER: _ClassVar[int]
        DELETE_PRESENTATION_FIELD_NUMBER: _ClassVar[int]
        TRIGGER_PRESENTATION_FIELD_NUMBER: _ClassVar[int]
        TRIGGER_CUE_FIELD_NUMBER: _ClassVar[int]
        TIMELINE_OPERATION_FIELD_NUMBER: _ClassVar[int]
        ACTIVE_PRESENTATION_TIMELINE_OPERATION_FIELD_NUMBER: _ClassVar[int]
        FOCUSED_PRESENTATION_TIMELINE_OPERATION_FIELD_NUMBER: _ClassVar[int]
        ACTIVE_PRESENTATION_TIMELINE_STATUS_FIELD_NUMBER: _ClassVar[int]
        FOCUSED_PRESENTATION_TIMELINE_STATUS_FIELD_NUMBER: _ClassVar[int]
        THUMBNAIL_FIELD_NUMBER: _ClassVar[int]
        FOCUSED_FIELD_NUMBER: _ClassVar[int]
        FOCUS_FIELD_NUMBER: _ClassVar[int]
        TRIGGER_FIELD_NUMBER: _ClassVar[int]
        active: NetworkAPI_v1.API_v1_Presentation_Response.Active
        slide_index: NetworkAPI_v1.API_v1_Presentation_Response.SlideIndex
        chord_chart: NetworkAPI_v1.API_v1_Presentation_Response.ChordChart
        chord_chart_update: NetworkAPI_v1.API_v1_Presentation_Response.ChordChartUpdates
        presentation: NetworkAPI_v1.API_v1_Presentation_Response.Presentation
        delete_presentation: NetworkAPI_v1.API_v1_Presentation_Response.DeletePresentation
        trigger_presentation: NetworkAPI_v1.API_v1_Presentation_Response.TriggerPresentation
        trigger_cue: NetworkAPI_v1.API_v1_Presentation_Response.TriggerCue
        timeline_operation: NetworkAPI_v1.API_v1_Presentation_Response.TimelineOperation
        active_presentation_timeline_operation: NetworkAPI_v1.API_v1_Presentation_Response.ActivePresentationTimelineOperation
        focused_presentation_timeline_operation: NetworkAPI_v1.API_v1_Presentation_Response.FocusedPresentationTimelineOperation
        active_presentation_timeline_status: NetworkAPI_v1.API_v1_Presentation_Response.ActivePresentationTimelineStatus
        focused_presentation_timeline_status: NetworkAPI_v1.API_v1_Presentation_Response.FocusedPresentationTimelineStatus
        thumbnail: NetworkAPI_v1.API_v1_Presentation_Response.Thumbnail
        focused: NetworkAPI_v1.API_v1_Presentation_Response.Focused
        focus: NetworkAPI_v1.API_v1_Presentation_Response.EmptyMessage
        trigger: NetworkAPI_v1.API_v1_Presentation_Response.EmptyMessage
        def __init__(self, active: _Optional[_Union[NetworkAPI_v1.API_v1_Presentation_Response.Active, _Mapping]] = ..., slide_index: _Optional[_Union[NetworkAPI_v1.API_v1_Presentation_Response.SlideIndex, _Mapping]] = ..., chord_chart: _Optional[_Union[NetworkAPI_v1.API_v1_Presentation_Response.ChordChart, _Mapping]] = ..., chord_chart_update: _Optional[_Union[NetworkAPI_v1.API_v1_Presentation_Response.ChordChartUpdates, _Mapping]] = ..., presentation: _Optional[_Union[NetworkAPI_v1.API_v1_Presentation_Response.Presentation, _Mapping]] = ..., delete_presentation: _Optional[_Union[NetworkAPI_v1.API_v1_Presentation_Response.DeletePresentation, _Mapping]] = ..., trigger_presentation: _Optional[_Union[NetworkAPI_v1.API_v1_Presentation_Response.TriggerPresentation, _Mapping]] = ..., trigger_cue: _Optional[_Union[NetworkAPI_v1.API_v1_Presentation_Response.TriggerCue, _Mapping]] = ..., timeline_operation: _Optional[_Union[NetworkAPI_v1.API_v1_Presentation_Response.TimelineOperation, _Mapping]] = ..., active_presentation_timeline_operation: _Optional[_Union[NetworkAPI_v1.API_v1_Presentation_Response.ActivePresentationTimelineOperation, _Mapping]] = ..., focused_presentation_timeline_operation: _Optional[_Union[NetworkAPI_v1.API_v1_Presentation_Response.FocusedPresentationTimelineOperation, _Mapping]] = ..., active_presentation_timeline_status: _Optional[_Union[NetworkAPI_v1.API_v1_Presentation_Response.ActivePresentationTimelineStatus, _Mapping]] = ..., focused_presentation_timeline_status: _Optional[_Union[NetworkAPI_v1.API_v1_Presentation_Response.FocusedPresentationTimelineStatus, _Mapping]] = ..., thumbnail: _Optional[_Union[NetworkAPI_v1.API_v1_Presentation_Response.Thumbnail, _Mapping]] = ..., focused: _Optional[_Union[NetworkAPI_v1.API_v1_Presentation_Response.Focused, _Mapping]] = ..., focus: _Optional[_Union[NetworkAPI_v1.API_v1_Presentation_Response.EmptyMessage, _Mapping]] = ..., trigger: _Optional[_Union[NetworkAPI_v1.API_v1_Presentation_Response.EmptyMessage, _Mapping]] = ...) -> None: ...
    class API_v1_Prop_Response(_message.Message):
        __slots__ = ("props", "get_prop", "delete_prop", "trigger_prop", "clear_prop", "get_thumbnail")
        class Props(_message.Message):
            __slots__ = ("props",)
            PROPS_FIELD_NUMBER: _ClassVar[int]
            props: _containers.RepeatedCompositeFieldContainer[_proApiV1BasicTypes_pb2.API_v1_PropData]
            def __init__(self, props: _Optional[_Iterable[_Union[_proApiV1BasicTypes_pb2.API_v1_PropData, _Mapping]]] = ...) -> None: ...
        class GetProp(_message.Message):
            __slots__ = ("prop",)
            PROP_FIELD_NUMBER: _ClassVar[int]
            prop: _proApiV1BasicTypes_pb2.API_v1_PropData
            def __init__(self, prop: _Optional[_Union[_proApiV1BasicTypes_pb2.API_v1_PropData, _Mapping]] = ...) -> None: ...
        class DeleteProp(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class TriggerProp(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class ClearProp(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class GetThumbnail(_message.Message):
            __slots__ = ("data",)
            DATA_FIELD_NUMBER: _ClassVar[int]
            data: bytes
            def __init__(self, data: _Optional[bytes] = ...) -> None: ...
        PROPS_FIELD_NUMBER: _ClassVar[int]
        GET_PROP_FIELD_NUMBER: _ClassVar[int]
        DELETE_PROP_FIELD_NUMBER: _ClassVar[int]
        TRIGGER_PROP_FIELD_NUMBER: _ClassVar[int]
        CLEAR_PROP_FIELD_NUMBER: _ClassVar[int]
        GET_THUMBNAIL_FIELD_NUMBER: _ClassVar[int]
        props: NetworkAPI_v1.API_v1_Prop_Response.Props
        get_prop: NetworkAPI_v1.API_v1_Prop_Response.GetProp
        delete_prop: NetworkAPI_v1.API_v1_Prop_Response.DeleteProp
        trigger_prop: NetworkAPI_v1.API_v1_Prop_Response.TriggerProp
        clear_prop: NetworkAPI_v1.API_v1_Prop_Response.ClearProp
        get_thumbnail: NetworkAPI_v1.API_v1_Prop_Response.GetThumbnail
        def __init__(self, props: _Optional[_Union[NetworkAPI_v1.API_v1_Prop_Response.Props, _Mapping]] = ..., get_prop: _Optional[_Union[NetworkAPI_v1.API_v1_Prop_Response.GetProp, _Mapping]] = ..., delete_prop: _Optional[_Union[NetworkAPI_v1.API_v1_Prop_Response.DeleteProp, _Mapping]] = ..., trigger_prop: _Optional[_Union[NetworkAPI_v1.API_v1_Prop_Response.TriggerProp, _Mapping]] = ..., clear_prop: _Optional[_Union[NetworkAPI_v1.API_v1_Prop_Response.ClearProp, _Mapping]] = ..., get_thumbnail: _Optional[_Union[NetworkAPI_v1.API_v1_Prop_Response.GetThumbnail, _Mapping]] = ...) -> None: ...
    class API_v1_Stage_Response(_message.Message):
        __slots__ = ("get_layout_map", "set_layout_map", "get_message", "put_message", "delete_message", "get_screens", "get_screen_layout", "set_screen_layout", "get_layouts", "delete_layout", "get_layout_thumbnail")
        class GetLayoutMap(_message.Message):
            __slots__ = ("map",)
            MAP_FIELD_NUMBER: _ClassVar[int]
            map: _proApiV1BasicTypes_pb2.API_v1_StageLayoutMap
            def __init__(self, map: _Optional[_Union[_proApiV1BasicTypes_pb2.API_v1_StageLayoutMap, _Mapping]] = ...) -> None: ...
        class SetLayoutMap(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class GetMessage(_message.Message):
            __slots__ = ("message",)
            MESSAGE_FIELD_NUMBER: _ClassVar[int]
            message: str
            def __init__(self, message: _Optional[str] = ...) -> None: ...
        class PutMessage(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class DeleteMessage(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class GetScreens(_message.Message):
            __slots__ = ("screens",)
            SCREENS_FIELD_NUMBER: _ClassVar[int]
            screens: _containers.RepeatedCompositeFieldContainer[_proApiV1BasicTypes_pb2.API_v1_Identifier]
            def __init__(self, screens: _Optional[_Iterable[_Union[_proApiV1BasicTypes_pb2.API_v1_Identifier, _Mapping]]] = ...) -> None: ...
        class GetScreenLayout(_message.Message):
            __slots__ = ("id",)
            ID_FIELD_NUMBER: _ClassVar[int]
            id: _proApiV1BasicTypes_pb2.API_v1_Identifier
            def __init__(self, id: _Optional[_Union[_proApiV1BasicTypes_pb2.API_v1_Identifier, _Mapping]] = ...) -> None: ...
        class SetScreenLayout(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class GetLayouts(_message.Message):
            __slots__ = ("layouts",)
            class Layout(_message.Message):
                __slots__ = ("id",)
                ID_FIELD_NUMBER: _ClassVar[int]
                id: _proApiV1BasicTypes_pb2.API_v1_Identifier
                def __init__(self, id: _Optional[_Union[_proApiV1BasicTypes_pb2.API_v1_Identifier, _Mapping]] = ...) -> None: ...
            LAYOUTS_FIELD_NUMBER: _ClassVar[int]
            layouts: _containers.RepeatedCompositeFieldContainer[NetworkAPI_v1.API_v1_Stage_Response.GetLayouts.Layout]
            def __init__(self, layouts: _Optional[_Iterable[_Union[NetworkAPI_v1.API_v1_Stage_Response.GetLayouts.Layout, _Mapping]]] = ...) -> None: ...
        class DeleteLayout(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class GetLayoutThumbnail(_message.Message):
            __slots__ = ("data",)
            DATA_FIELD_NUMBER: _ClassVar[int]
            data: bytes
            def __init__(self, data: _Optional[bytes] = ...) -> None: ...
        GET_LAYOUT_MAP_FIELD_NUMBER: _ClassVar[int]
        SET_LAYOUT_MAP_FIELD_NUMBER: _ClassVar[int]
        GET_MESSAGE_FIELD_NUMBER: _ClassVar[int]
        PUT_MESSAGE_FIELD_NUMBER: _ClassVar[int]
        DELETE_MESSAGE_FIELD_NUMBER: _ClassVar[int]
        GET_SCREENS_FIELD_NUMBER: _ClassVar[int]
        GET_SCREEN_LAYOUT_FIELD_NUMBER: _ClassVar[int]
        SET_SCREEN_LAYOUT_FIELD_NUMBER: _ClassVar[int]
        GET_LAYOUTS_FIELD_NUMBER: _ClassVar[int]
        DELETE_LAYOUT_FIELD_NUMBER: _ClassVar[int]
        GET_LAYOUT_THUMBNAIL_FIELD_NUMBER: _ClassVar[int]
        get_layout_map: NetworkAPI_v1.API_v1_Stage_Response.GetLayoutMap
        set_layout_map: NetworkAPI_v1.API_v1_Stage_Response.SetLayoutMap
        get_message: NetworkAPI_v1.API_v1_Stage_Response.GetMessage
        put_message: NetworkAPI_v1.API_v1_Stage_Response.PutMessage
        delete_message: NetworkAPI_v1.API_v1_Stage_Response.DeleteMessage
        get_screens: NetworkAPI_v1.API_v1_Stage_Response.GetScreens
        get_screen_layout: NetworkAPI_v1.API_v1_Stage_Response.GetScreenLayout
        set_screen_layout: NetworkAPI_v1.API_v1_Stage_Response.SetScreenLayout
        get_layouts: NetworkAPI_v1.API_v1_Stage_Response.GetLayouts
        delete_layout: NetworkAPI_v1.API_v1_Stage_Response.DeleteLayout
        get_layout_thumbnail: NetworkAPI_v1.API_v1_Stage_Response.GetLayoutThumbnail
        def __init__(self, get_layout_map: _Optional[_Union[NetworkAPI_v1.API_v1_Stage_Response.GetLayoutMap, _Mapping]] = ..., set_layout_map: _Optional[_Union[NetworkAPI_v1.API_v1_Stage_Response.SetLayoutMap, _Mapping]] = ..., get_message: _Optional[_Union[NetworkAPI_v1.API_v1_Stage_Response.GetMessage, _Mapping]] = ..., put_message: _Optional[_Union[NetworkAPI_v1.API_v1_Stage_Response.PutMessage, _Mapping]] = ..., delete_message: _Optional[_Union[NetworkAPI_v1.API_v1_Stage_Response.DeleteMessage, _Mapping]] = ..., get_screens: _Optional[_Union[NetworkAPI_v1.API_v1_Stage_Response.GetScreens, _Mapping]] = ..., get_screen_layout: _Optional[_Union[NetworkAPI_v1.API_v1_Stage_Response.GetScreenLayout, _Mapping]] = ..., set_screen_layout: _Optional[_Union[NetworkAPI_v1.API_v1_Stage_Response.SetScreenLayout, _Mapping]] = ..., get_layouts: _Optional[_Union[NetworkAPI_v1.API_v1_Stage_Response.GetLayouts, _Mapping]] = ..., delete_layout: _Optional[_Union[NetworkAPI_v1.API_v1_Stage_Response.DeleteLayout, _Mapping]] = ..., get_layout_thumbnail: _Optional[_Union[NetworkAPI_v1.API_v1_Stage_Response.GetLayoutThumbnail, _Mapping]] = ...) -> None: ...
    class API_v1_Status_Response(_message.Message):
        __slots__ = ("get_layers", "get_stage_screens", "put_stage_screens", "get_audience_screens", "put_audience_screens", "get_screens", "get_slide")
        class GetLayers(_message.Message):
            __slots__ = ("video_input", "media", "slide", "announcements", "props", "messages", "audio")
            VIDEO_INPUT_FIELD_NUMBER: _ClassVar[int]
            MEDIA_FIELD_NUMBER: _ClassVar[int]
            SLIDE_FIELD_NUMBER: _ClassVar[int]
            ANNOUNCEMENTS_FIELD_NUMBER: _ClassVar[int]
            PROPS_FIELD_NUMBER: _ClassVar[int]
            MESSAGES_FIELD_NUMBER: _ClassVar[int]
            AUDIO_FIELD_NUMBER: _ClassVar[int]
            video_input: bool
            media: bool
            slide: bool
            announcements: bool
            props: bool
            messages: bool
            audio: bool
            def __init__(self, video_input: bool = ..., media: bool = ..., slide: bool = ..., announcements: bool = ..., props: bool = ..., messages: bool = ..., audio: bool = ...) -> None: ...
        class GetStageScreens(_message.Message):
            __slots__ = ("enabled",)
            ENABLED_FIELD_NUMBER: _ClassVar[int]
            enabled: bool
            def __init__(self, enabled: bool = ...) -> None: ...
        class PutStageScreens(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class GetAudienceScreens(_message.Message):
            __slots__ = ("enabled",)
            ENABLED_FIELD_NUMBER: _ClassVar[int]
            enabled: bool
            def __init__(self, enabled: bool = ...) -> None: ...
        class PutAudienceScreens(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class GetScreens(_message.Message):
            __slots__ = ("screens",)
            SCREENS_FIELD_NUMBER: _ClassVar[int]
            screens: _containers.RepeatedCompositeFieldContainer[_proApiV1BasicTypes_pb2.API_v1_ScreenConfig]
            def __init__(self, screens: _Optional[_Iterable[_Union[_proApiV1BasicTypes_pb2.API_v1_ScreenConfig, _Mapping]]] = ...) -> None: ...
        class GetSlide(_message.Message):
            __slots__ = ("current", "next")
            CURRENT_FIELD_NUMBER: _ClassVar[int]
            NEXT_FIELD_NUMBER: _ClassVar[int]
            current: _proApiV1BasicTypes_pb2.API_v1_SlideDisplayDetails
            next: _proApiV1BasicTypes_pb2.API_v1_SlideDisplayDetails
            def __init__(self, current: _Optional[_Union[_proApiV1BasicTypes_pb2.API_v1_SlideDisplayDetails, _Mapping]] = ..., next: _Optional[_Union[_proApiV1BasicTypes_pb2.API_v1_SlideDisplayDetails, _Mapping]] = ...) -> None: ...
        GET_LAYERS_FIELD_NUMBER: _ClassVar[int]
        GET_STAGE_SCREENS_FIELD_NUMBER: _ClassVar[int]
        PUT_STAGE_SCREENS_FIELD_NUMBER: _ClassVar[int]
        GET_AUDIENCE_SCREENS_FIELD_NUMBER: _ClassVar[int]
        PUT_AUDIENCE_SCREENS_FIELD_NUMBER: _ClassVar[int]
        GET_SCREENS_FIELD_NUMBER: _ClassVar[int]
        GET_SLIDE_FIELD_NUMBER: _ClassVar[int]
        get_layers: NetworkAPI_v1.API_v1_Status_Response.GetLayers
        get_stage_screens: NetworkAPI_v1.API_v1_Status_Response.GetStageScreens
        put_stage_screens: NetworkAPI_v1.API_v1_Status_Response.PutStageScreens
        get_audience_screens: NetworkAPI_v1.API_v1_Status_Response.GetAudienceScreens
        put_audience_screens: NetworkAPI_v1.API_v1_Status_Response.PutAudienceScreens
        get_screens: NetworkAPI_v1.API_v1_Status_Response.GetScreens
        get_slide: NetworkAPI_v1.API_v1_Status_Response.GetSlide
        def __init__(self, get_layers: _Optional[_Union[NetworkAPI_v1.API_v1_Status_Response.GetLayers, _Mapping]] = ..., get_stage_screens: _Optional[_Union[NetworkAPI_v1.API_v1_Status_Response.GetStageScreens, _Mapping]] = ..., put_stage_screens: _Optional[_Union[NetworkAPI_v1.API_v1_Status_Response.PutStageScreens, _Mapping]] = ..., get_audience_screens: _Optional[_Union[NetworkAPI_v1.API_v1_Status_Response.GetAudienceScreens, _Mapping]] = ..., put_audience_screens: _Optional[_Union[NetworkAPI_v1.API_v1_Status_Response.PutAudienceScreens, _Mapping]] = ..., get_screens: _Optional[_Union[NetworkAPI_v1.API_v1_Status_Response.GetScreens, _Mapping]] = ..., get_slide: _Optional[_Union[NetworkAPI_v1.API_v1_Status_Response.GetSlide, _Mapping]] = ...) -> None: ...
    class API_v1_Theme_Response(_message.Message):
        __slots__ = ("get_all", "get_theme", "delete_theme", "get_theme_name", "put_theme_name", "get_theme_slide", "put_theme_slide", "delete_theme_slide", "get_theme_slide_thumbnail")
        class GetAll(_message.Message):
            __slots__ = ("groups", "themes")
            GROUPS_FIELD_NUMBER: _ClassVar[int]
            THEMES_FIELD_NUMBER: _ClassVar[int]
            groups: _containers.RepeatedCompositeFieldContainer[_proApiV1BasicTypes_pb2.API_v1_ThemeGroup]
            themes: _containers.RepeatedCompositeFieldContainer[_proApiV1BasicTypes_pb2.API_v1_Theme]
            def __init__(self, groups: _Optional[_Iterable[_Union[_proApiV1BasicTypes_pb2.API_v1_ThemeGroup, _Mapping]]] = ..., themes: _Optional[_Iterable[_Union[_proApiV1BasicTypes_pb2.API_v1_Theme, _Mapping]]] = ...) -> None: ...
        class GetTheme(_message.Message):
            __slots__ = ("theme", "group")
            THEME_FIELD_NUMBER: _ClassVar[int]
            GROUP_FIELD_NUMBER: _ClassVar[int]
            theme: _proApiV1BasicTypes_pb2.API_v1_Theme
            group: _proApiV1BasicTypes_pb2.API_v1_ThemeGroup
            def __init__(self, theme: _Optional[_Union[_proApiV1BasicTypes_pb2.API_v1_Theme, _Mapping]] = ..., group: _Optional[_Union[_proApiV1BasicTypes_pb2.API_v1_ThemeGroup, _Mapping]] = ...) -> None: ...
        class DeleteTheme(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class GetThemeName(_message.Message):
            __slots__ = ("name",)
            NAME_FIELD_NUMBER: _ClassVar[int]
            name: str
            def __init__(self, name: _Optional[str] = ...) -> None: ...
        class PutThemeName(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class GetThemeSlide(_message.Message):
            __slots__ = ("theme_slide",)
            THEME_SLIDE_FIELD_NUMBER: _ClassVar[int]
            theme_slide: _proApiV1BasicTypes_pb2.API_v1_ThemeSlide
            def __init__(self, theme_slide: _Optional[_Union[_proApiV1BasicTypes_pb2.API_v1_ThemeSlide, _Mapping]] = ...) -> None: ...
        class PutThemeSlide(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class DeleteThemeSlide(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class GetThemeSlideThumbnail(_message.Message):
            __slots__ = ("data",)
            DATA_FIELD_NUMBER: _ClassVar[int]
            data: bytes
            def __init__(self, data: _Optional[bytes] = ...) -> None: ...
        GET_ALL_FIELD_NUMBER: _ClassVar[int]
        GET_THEME_FIELD_NUMBER: _ClassVar[int]
        DELETE_THEME_FIELD_NUMBER: _ClassVar[int]
        GET_THEME_NAME_FIELD_NUMBER: _ClassVar[int]
        PUT_THEME_NAME_FIELD_NUMBER: _ClassVar[int]
        GET_THEME_SLIDE_FIELD_NUMBER: _ClassVar[int]
        PUT_THEME_SLIDE_FIELD_NUMBER: _ClassVar[int]
        DELETE_THEME_SLIDE_FIELD_NUMBER: _ClassVar[int]
        GET_THEME_SLIDE_THUMBNAIL_FIELD_NUMBER: _ClassVar[int]
        get_all: NetworkAPI_v1.API_v1_Theme_Response.GetAll
        get_theme: NetworkAPI_v1.API_v1_Theme_Response.GetTheme
        delete_theme: NetworkAPI_v1.API_v1_Theme_Response.DeleteTheme
        get_theme_name: NetworkAPI_v1.API_v1_Theme_Response.GetThemeName
        put_theme_name: NetworkAPI_v1.API_v1_Theme_Response.PutThemeName
        get_theme_slide: NetworkAPI_v1.API_v1_Theme_Response.GetThemeSlide
        put_theme_slide: NetworkAPI_v1.API_v1_Theme_Response.PutThemeSlide
        delete_theme_slide: NetworkAPI_v1.API_v1_Theme_Response.DeleteThemeSlide
        get_theme_slide_thumbnail: NetworkAPI_v1.API_v1_Theme_Response.GetThemeSlideThumbnail
        def __init__(self, get_all: _Optional[_Union[NetworkAPI_v1.API_v1_Theme_Response.GetAll, _Mapping]] = ..., get_theme: _Optional[_Union[NetworkAPI_v1.API_v1_Theme_Response.GetTheme, _Mapping]] = ..., delete_theme: _Optional[_Union[NetworkAPI_v1.API_v1_Theme_Response.DeleteTheme, _Mapping]] = ..., get_theme_name: _Optional[_Union[NetworkAPI_v1.API_v1_Theme_Response.GetThemeName, _Mapping]] = ..., put_theme_name: _Optional[_Union[NetworkAPI_v1.API_v1_Theme_Response.PutThemeName, _Mapping]] = ..., get_theme_slide: _Optional[_Union[NetworkAPI_v1.API_v1_Theme_Response.GetThemeSlide, _Mapping]] = ..., put_theme_slide: _Optional[_Union[NetworkAPI_v1.API_v1_Theme_Response.PutThemeSlide, _Mapping]] = ..., delete_theme_slide: _Optional[_Union[NetworkAPI_v1.API_v1_Theme_Response.DeleteThemeSlide, _Mapping]] = ..., get_theme_slide_thumbnail: _Optional[_Union[NetworkAPI_v1.API_v1_Theme_Response.GetThemeSlideThumbnail, _Mapping]] = ...) -> None: ...
    class API_v1_Timer_Response(_message.Message):
        __slots__ = ("timers", "create_timer", "current_times", "all_timers_operation", "get_timer", "put_timer", "delete_timer", "timer_operation", "system_time", "video_countdown")
        class Timers(_message.Message):
            __slots__ = ("timers",)
            TIMERS_FIELD_NUMBER: _ClassVar[int]
            timers: _containers.RepeatedCompositeFieldContainer[_proApiV1BasicTypes_pb2.API_v1_Timer]
            def __init__(self, timers: _Optional[_Iterable[_Union[_proApiV1BasicTypes_pb2.API_v1_Timer, _Mapping]]] = ...) -> None: ...
        class CreateTimer(_message.Message):
            __slots__ = ("timer",)
            TIMER_FIELD_NUMBER: _ClassVar[int]
            timer: _proApiV1BasicTypes_pb2.API_v1_Timer
            def __init__(self, timer: _Optional[_Union[_proApiV1BasicTypes_pb2.API_v1_Timer, _Mapping]] = ...) -> None: ...
        class CurrentTimes(_message.Message):
            __slots__ = ("timers",)
            TIMERS_FIELD_NUMBER: _ClassVar[int]
            timers: _containers.RepeatedCompositeFieldContainer[_proApiV1BasicTypes_pb2.API_v1_TimerValue]
            def __init__(self, timers: _Optional[_Iterable[_Union[_proApiV1BasicTypes_pb2.API_v1_TimerValue, _Mapping]]] = ...) -> None: ...
        class AllTimersOperation(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class GetTimer(_message.Message):
            __slots__ = ("timer",)
            TIMER_FIELD_NUMBER: _ClassVar[int]
            timer: _proApiV1BasicTypes_pb2.API_v1_Timer
            def __init__(self, timer: _Optional[_Union[_proApiV1BasicTypes_pb2.API_v1_Timer, _Mapping]] = ...) -> None: ...
        class PutTimer(_message.Message):
            __slots__ = ("timer",)
            TIMER_FIELD_NUMBER: _ClassVar[int]
            timer: _proApiV1BasicTypes_pb2.API_v1_Timer
            def __init__(self, timer: _Optional[_Union[_proApiV1BasicTypes_pb2.API_v1_Timer, _Mapping]] = ...) -> None: ...
        class DeleteTimer(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class TimerOperation(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class SystemTime(_message.Message):
            __slots__ = ("time",)
            TIME_FIELD_NUMBER: _ClassVar[int]
            time: int
            def __init__(self, time: _Optional[int] = ...) -> None: ...
        class VideoCountdown(_message.Message):
            __slots__ = ("time",)
            TIME_FIELD_NUMBER: _ClassVar[int]
            time: str
            def __init__(self, time: _Optional[str] = ...) -> None: ...
        TIMERS_FIELD_NUMBER: _ClassVar[int]
        CREATE_TIMER_FIELD_NUMBER: _ClassVar[int]
        CURRENT_TIMES_FIELD_NUMBER: _ClassVar[int]
        ALL_TIMERS_OPERATION_FIELD_NUMBER: _ClassVar[int]
        GET_TIMER_FIELD_NUMBER: _ClassVar[int]
        PUT_TIMER_FIELD_NUMBER: _ClassVar[int]
        DELETE_TIMER_FIELD_NUMBER: _ClassVar[int]
        TIMER_OPERATION_FIELD_NUMBER: _ClassVar[int]
        SYSTEM_TIME_FIELD_NUMBER: _ClassVar[int]
        VIDEO_COUNTDOWN_FIELD_NUMBER: _ClassVar[int]
        timers: NetworkAPI_v1.API_v1_Timer_Response.Timers
        create_timer: NetworkAPI_v1.API_v1_Timer_Response.CreateTimer
        current_times: NetworkAPI_v1.API_v1_Timer_Response.CurrentTimes
        all_timers_operation: NetworkAPI_v1.API_v1_Timer_Response.AllTimersOperation
        get_timer: NetworkAPI_v1.API_v1_Timer_Response.GetTimer
        put_timer: NetworkAPI_v1.API_v1_Timer_Response.PutTimer
        delete_timer: NetworkAPI_v1.API_v1_Timer_Response.DeleteTimer
        timer_operation: NetworkAPI_v1.API_v1_Timer_Response.TimerOperation
        system_time: NetworkAPI_v1.API_v1_Timer_Response.SystemTime
        video_countdown: NetworkAPI_v1.API_v1_Timer_Response.VideoCountdown
        def __init__(self, timers: _Optional[_Union[NetworkAPI_v1.API_v1_Timer_Response.Timers, _Mapping]] = ..., create_timer: _Optional[_Union[NetworkAPI_v1.API_v1_Timer_Response.CreateTimer, _Mapping]] = ..., current_times: _Optional[_Union[NetworkAPI_v1.API_v1_Timer_Response.CurrentTimes, _Mapping]] = ..., all_timers_operation: _Optional[_Union[NetworkAPI_v1.API_v1_Timer_Response.AllTimersOperation, _Mapping]] = ..., get_timer: _Optional[_Union[NetworkAPI_v1.API_v1_Timer_Response.GetTimer, _Mapping]] = ..., put_timer: _Optional[_Union[NetworkAPI_v1.API_v1_Timer_Response.PutTimer, _Mapping]] = ..., delete_timer: _Optional[_Union[NetworkAPI_v1.API_v1_Timer_Response.DeleteTimer, _Mapping]] = ..., timer_operation: _Optional[_Union[NetworkAPI_v1.API_v1_Timer_Response.TimerOperation, _Mapping]] = ..., system_time: _Optional[_Union[NetworkAPI_v1.API_v1_Timer_Response.SystemTime, _Mapping]] = ..., video_countdown: _Optional[_Union[NetworkAPI_v1.API_v1_Timer_Response.VideoCountdown, _Mapping]] = ...) -> None: ...
    class API_v1_Transport_Response(_message.Message):
        __slots__ = ("play", "pause", "skip_backward", "skip_forward", "go_to_end", "get_time", "put_time", "get_auto_advance", "delete_auto_advance", "get_current_media")
        class Play(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class Pause(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class SkipBackward(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class SkipForward(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class GoToEnd(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class GetTime(_message.Message):
            __slots__ = ("seconds",)
            SECONDS_FIELD_NUMBER: _ClassVar[int]
            seconds: float
            def __init__(self, seconds: _Optional[float] = ...) -> None: ...
        class PutTime(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class GetAutoAdvance(_message.Message):
            __slots__ = ("auto_advance",)
            AUTO_ADVANCE_FIELD_NUMBER: _ClassVar[int]
            auto_advance: bool
            def __init__(self, auto_advance: bool = ...) -> None: ...
        class DeleteAutoAdvance(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class GetCurrentMedia(_message.Message):
            __slots__ = ("is_playing", "uuid", "name", "artist", "audio_only", "duration")
            IS_PLAYING_FIELD_NUMBER: _ClassVar[int]
            UUID_FIELD_NUMBER: _ClassVar[int]
            NAME_FIELD_NUMBER: _ClassVar[int]
            ARTIST_FIELD_NUMBER: _ClassVar[int]
            AUDIO_ONLY_FIELD_NUMBER: _ClassVar[int]
            DURATION_FIELD_NUMBER: _ClassVar[int]
            is_playing: bool
            uuid: _basicTypes_pb2.UUID
            name: str
            artist: str
            audio_only: bool
            duration: float
            def __init__(self, is_playing: bool = ..., uuid: _Optional[_Union[_basicTypes_pb2.UUID, _Mapping]] = ..., name: _Optional[str] = ..., artist: _Optional[str] = ..., audio_only: bool = ..., duration: _Optional[float] = ...) -> None: ...
        PLAY_FIELD_NUMBER: _ClassVar[int]
        PAUSE_FIELD_NUMBER: _ClassVar[int]
        SKIP_BACKWARD_FIELD_NUMBER: _ClassVar[int]
        SKIP_FORWARD_FIELD_NUMBER: _ClassVar[int]
        GO_TO_END_FIELD_NUMBER: _ClassVar[int]
        GET_TIME_FIELD_NUMBER: _ClassVar[int]
        PUT_TIME_FIELD_NUMBER: _ClassVar[int]
        GET_AUTO_ADVANCE_FIELD_NUMBER: _ClassVar[int]
        DELETE_AUTO_ADVANCE_FIELD_NUMBER: _ClassVar[int]
        GET_CURRENT_MEDIA_FIELD_NUMBER: _ClassVar[int]
        play: NetworkAPI_v1.API_v1_Transport_Response.Play
        pause: NetworkAPI_v1.API_v1_Transport_Response.Pause
        skip_backward: NetworkAPI_v1.API_v1_Transport_Response.SkipBackward
        skip_forward: NetworkAPI_v1.API_v1_Transport_Response.SkipForward
        go_to_end: NetworkAPI_v1.API_v1_Transport_Response.GoToEnd
        get_time: NetworkAPI_v1.API_v1_Transport_Response.GetTime
        put_time: NetworkAPI_v1.API_v1_Transport_Response.PutTime
        get_auto_advance: NetworkAPI_v1.API_v1_Transport_Response.GetAutoAdvance
        delete_auto_advance: NetworkAPI_v1.API_v1_Transport_Response.DeleteAutoAdvance
        get_current_media: NetworkAPI_v1.API_v1_Transport_Response.GetCurrentMedia
        def __init__(self, play: _Optional[_Union[NetworkAPI_v1.API_v1_Transport_Response.Play, _Mapping]] = ..., pause: _Optional[_Union[NetworkAPI_v1.API_v1_Transport_Response.Pause, _Mapping]] = ..., skip_backward: _Optional[_Union[NetworkAPI_v1.API_v1_Transport_Response.SkipBackward, _Mapping]] = ..., skip_forward: _Optional[_Union[NetworkAPI_v1.API_v1_Transport_Response.SkipForward, _Mapping]] = ..., go_to_end: _Optional[_Union[NetworkAPI_v1.API_v1_Transport_Response.GoToEnd, _Mapping]] = ..., get_time: _Optional[_Union[NetworkAPI_v1.API_v1_Transport_Response.GetTime, _Mapping]] = ..., put_time: _Optional[_Union[NetworkAPI_v1.API_v1_Transport_Response.PutTime, _Mapping]] = ..., get_auto_advance: _Optional[_Union[NetworkAPI_v1.API_v1_Transport_Response.GetAutoAdvance, _Mapping]] = ..., delete_auto_advance: _Optional[_Union[NetworkAPI_v1.API_v1_Transport_Response.DeleteAutoAdvance, _Mapping]] = ..., get_current_media: _Optional[_Union[NetworkAPI_v1.API_v1_Transport_Response.GetCurrentMedia, _Mapping]] = ...) -> None: ...
    class API_v1_Trigger_Response(_message.Message):
        __slots__ = ("cue", "playlist", "media", "audio", "video_input", "library", "next", "previous", "media_next", "media_previous", "audio_next", "audio_previous")
        class Cue(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class Playlist(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class Media(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class MediaNext(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class MediaPrevious(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class Audio(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class AudioNext(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class AudioPrevious(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class VideoInput(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class Library(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class Next(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class Previous(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        CUE_FIELD_NUMBER: _ClassVar[int]
        PLAYLIST_FIELD_NUMBER: _ClassVar[int]
        MEDIA_FIELD_NUMBER: _ClassVar[int]
        AUDIO_FIELD_NUMBER: _ClassVar[int]
        VIDEO_INPUT_FIELD_NUMBER: _ClassVar[int]
        LIBRARY_FIELD_NUMBER: _ClassVar[int]
        NEXT_FIELD_NUMBER: _ClassVar[int]
        PREVIOUS_FIELD_NUMBER: _ClassVar[int]
        MEDIA_NEXT_FIELD_NUMBER: _ClassVar[int]
        MEDIA_PREVIOUS_FIELD_NUMBER: _ClassVar[int]
        AUDIO_NEXT_FIELD_NUMBER: _ClassVar[int]
        AUDIO_PREVIOUS_FIELD_NUMBER: _ClassVar[int]
        cue: NetworkAPI_v1.API_v1_Trigger_Response.Cue
        playlist: NetworkAPI_v1.API_v1_Trigger_Response.Playlist
        media: NetworkAPI_v1.API_v1_Trigger_Response.Media
        audio: NetworkAPI_v1.API_v1_Trigger_Response.Audio
        video_input: NetworkAPI_v1.API_v1_Trigger_Response.VideoInput
        library: NetworkAPI_v1.API_v1_Trigger_Response.Library
        next: NetworkAPI_v1.API_v1_Trigger_Response.Next
        previous: NetworkAPI_v1.API_v1_Trigger_Response.Previous
        media_next: NetworkAPI_v1.API_v1_Trigger_Response.MediaNext
        media_previous: NetworkAPI_v1.API_v1_Trigger_Response.MediaPrevious
        audio_next: NetworkAPI_v1.API_v1_Trigger_Response.AudioNext
        audio_previous: NetworkAPI_v1.API_v1_Trigger_Response.AudioPrevious
        def __init__(self, cue: _Optional[_Union[NetworkAPI_v1.API_v1_Trigger_Response.Cue, _Mapping]] = ..., playlist: _Optional[_Union[NetworkAPI_v1.API_v1_Trigger_Response.Playlist, _Mapping]] = ..., media: _Optional[_Union[NetworkAPI_v1.API_v1_Trigger_Response.Media, _Mapping]] = ..., audio: _Optional[_Union[NetworkAPI_v1.API_v1_Trigger_Response.Audio, _Mapping]] = ..., video_input: _Optional[_Union[NetworkAPI_v1.API_v1_Trigger_Response.VideoInput, _Mapping]] = ..., library: _Optional[_Union[NetworkAPI_v1.API_v1_Trigger_Response.Library, _Mapping]] = ..., next: _Optional[_Union[NetworkAPI_v1.API_v1_Trigger_Response.Next, _Mapping]] = ..., previous: _Optional[_Union[NetworkAPI_v1.API_v1_Trigger_Response.Previous, _Mapping]] = ..., media_next: _Optional[_Union[NetworkAPI_v1.API_v1_Trigger_Response.MediaNext, _Mapping]] = ..., media_previous: _Optional[_Union[NetworkAPI_v1.API_v1_Trigger_Response.MediaPrevious, _Mapping]] = ..., audio_next: _Optional[_Union[NetworkAPI_v1.API_v1_Trigger_Response.AudioNext, _Mapping]] = ..., audio_previous: _Optional[_Union[NetworkAPI_v1.API_v1_Trigger_Response.AudioPrevious, _Mapping]] = ...) -> None: ...
    class API_v1_Video_Inputs_Response(_message.Message):
        __slots__ = ("get_all", "trigger")
        class GetAll(_message.Message):
            __slots__ = ("inputs",)
            INPUTS_FIELD_NUMBER: _ClassVar[int]
            inputs: _containers.RepeatedCompositeFieldContainer[_proApiV1BasicTypes_pb2.API_v1_Identifier]
            def __init__(self, inputs: _Optional[_Iterable[_Union[_proApiV1BasicTypes_pb2.API_v1_Identifier, _Mapping]]] = ...) -> None: ...
        class Trigger(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        GET_ALL_FIELD_NUMBER: _ClassVar[int]
        TRIGGER_FIELD_NUMBER: _ClassVar[int]
        get_all: NetworkAPI_v1.API_v1_Video_Inputs_Response.GetAll
        trigger: NetworkAPI_v1.API_v1_Video_Inputs_Response.Trigger
        def __init__(self, get_all: _Optional[_Union[NetworkAPI_v1.API_v1_Video_Inputs_Response.GetAll, _Mapping]] = ..., trigger: _Optional[_Union[NetworkAPI_v1.API_v1_Video_Inputs_Response.Trigger, _Mapping]] = ...) -> None: ...
    ACTION_FIELD_NUMBER: _ClassVar[int]
    action: NetworkAPI_v1.Action
    def __init__(self, action: _Optional[_Union[NetworkAPI_v1.Action, _Mapping]] = ...) -> None: ...
